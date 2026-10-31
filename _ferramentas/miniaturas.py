#!/usr/bin/env python3
"""Miniaturas WebP das fotos de produto (30/10/2026) — PageSpeed celular: "imagens 939 KiB a economizar".

Os cartões (home, produtos relacionados, catálogo, miniaturas da galeria) mostram a foto com ~130–160 px,
mas baixavam o arquivo de 800–1240 px. Este script cria uma cópia pequena (320 px, WebP) de cada foto local
usada em cartão e troca o src dos cartões por ela, com srcset apontando para a foto original em telas de alta
densidade. Nada é apagado: as fotos originais continuam no lugar e o modal/galeria grande continua usando elas.

Nome da miniatura = hash do conteúdo da foto original (img/t/<hash>.webp): se a foto original mudar, a
miniatura muda de nome sozinha — o cache de 1 ano da Cloudflare nunca serve foto velha.

O que o script faz (pode rodar quantas vezes quiser; só grava o que mudou):
  1. data/catalogo.json: campo "t" (miniatura) em cada produto com foto local;
  2. p/*.html: cartões "Produtos relacionados" e botões da galeria usam a miniatura; a foto grande (fundo do
     quadro) passa a vir em WebP quando existe a versão .webp ao lado do .jpg; logo do topo em versão pequena;
  3. catalogo.html e catalogo/index.html: fotos locais dos cartões com miniatura + srcset;
  4. categoria/, marca/, guia/, blog/ e demais páginas: logo do topo e selo MOVA em versão pequena.
Uso: python3 _ferramentas/miniaturas.py [--dry]
Rodar depois de cadastrar produto/foto nova (adiciona_*.py, fotos_cral.py). Dependência: Pillow.
"""
import glob
import hashlib
import json
import os
import re
import sys

from PIL import Image

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import dados_site as ds  # noqa: E402

R = ds.R
DRY = '--dry' in sys.argv
LADO = 320
SITE = 'https://lojasullabrj.com.br'
RX_LOCAL = re.compile(r'^(?:https?://(?:www\.)?lojasullabrj\.com\.br)?/?((?:img/)?[^?#"\']+\.(?:webp|jpe?g|png))(?:\?[^"\']*)?$', re.I)
_cache = {}
criadas = 0


def local(src):
    """'https://lojasullabrj.com.br/img/b/X.webp?v=1' -> 'img/b/X.webp' se o arquivo existe no site."""
    m = RX_LOCAL.match(src or '')
    if not m:
        return None
    rel = m.group(1).lstrip('/')
    return rel if os.path.isfile(R + rel) and not rel.startswith('img/t/') else None


def miniatura(src):
    """Caminho relativo da miniatura (img/t/<hash>.webp), criando o arquivo se precisar. None = sem miniatura."""
    global criadas
    rel = local(src)
    if not rel:
        return None
    if rel in _cache:
        return _cache[rel]
    h = hashlib.sha1(open(R + rel, 'rb').read()).hexdigest()[:12]
    dst = f'img/t/{h}.webp'
    if not os.path.exists(R + dst):
        try:
            im = Image.open(R + rel)
            im.load()
        except Exception as e:  # foto corrompida: segue com a original
            print('não abriu', rel, e)
            _cache[rel] = None
            return None
        if max(im.size) <= LADO * 1.15 and rel.endswith('.webp'):
            _cache[rel] = None  # já é pequena: não vale a cópia
            return None
        if im.mode in ('P', 'LA', 'RGBA'):
            fundo = Image.new('RGB', im.size, 'white')
            fundo.paste(im.convert('RGBA'), mask=im.convert('RGBA').split()[-1])
            im = fundo
        else:
            im = im.convert('RGB')
        im.thumbnail((LADO, LADO), Image.LANCZOS)
        if not DRY:
            os.makedirs(R + 'img/t', exist_ok=True)
            im.save(R + dst, 'WEBP', quality=78, method=6)
        criadas += 1
    _cache[rel] = dst
    return dst


def grava(path, novo, velho):
    if novo != velho:
        if not DRY:
            open(path, 'w', encoding='utf-8').write(novo)
        return 1
    return 0


# ---------------------------------------------------------------- 1. catálogo da home
seed = ds.ler_catalogo()
n_t = 0
for p in seed:
    t = miniatura(p.get('img', ''))
    if t:
        if p.get('t') != t:
            p['t'] = t
        n_t += 1
    elif 'img' in p and 't' in p:
        del p['t']
if not DRY:
    ds.gravar_catalogo(seed)
print('catálogo: produtos com miniatura', n_t, 'de', len(seed))


# ---------------------------------------------------------------- 2/3/4. páginas estáticas
def abs_(rel):
    return SITE + '/' + rel


TOPO_PNG = 'og-sullab.png'
TOPO_MINI = 'img/sullab-topo.webp'
MOVA_PNG = '/img/mova-logo-2026.png'
MOVA_MINI = '/img/mova-logo-2026-340.webp'


def logos():
    if DRY:
        return
    if not os.path.exists(R + TOPO_MINI):
        im = Image.open(R + TOPO_PNG).convert('RGB')
        im.thumbnail((130, 130 * im.height // im.width), Image.LANCZOS)
        im.save(R + TOPO_MINI, 'WEBP', quality=86, method=6)
    if not os.path.exists(R + MOVA_MINI.lstrip('/')):
        im = Image.open(R + MOVA_PNG.lstrip('/')).convert('RGBA')
        im.thumbnail((340, 340 * im.height // im.width), Image.LANCZOS)
        im.save(R + MOVA_MINI.lstrip('/'), 'WEBP', quality=88, method=6)


logos()

RX_IMG = re.compile(r'<img\b[^>]*>')


def troca_img(tag, largura_original='1000w', sizes='(max-width:700px) 45vw, 160px'):
    """<img src=foto grande> -> src=miniatura + srcset (miniatura 320w, original) — mantém width/height/alt/lazy."""
    if 'srcset=' in tag:
        return tag
    m = re.search(r'\ssrc="([^"]+)"', tag)
    if not m:
        return tag
    src = m.group(1)
    t = miniatura(src)
    if not t:
        return tag
    pref = SITE + '/' if src.startswith('http') else '/'
    novo = tag.replace(m.group(0), f' src="{pref}{t}" srcset="{pref}{t} {LADO}w, {src} {largura_original}" sizes="{sizes}"', 1)
    if 'decoding=' not in novo:
        novo = novo.replace('<img ', '<img decoding="async" ', 1)
    return novo


def troca_logos(t):
    t = re.sub(r'<img src="(https://lojasullabrj\.com\.br/)og-sullab\.png" alt="SULLAB" width="65" height="34">',
               r'<img src="\1' + TOPO_MINI + '" alt="SULLAB" width="65" height="34">', t)
    t = t.replace('src="' + MOVA_PNG + '"', 'src="' + MOVA_MINI + '"')
    return t


def bg_webp(t):
    """fundo do quadro da foto: url('X.jpg') -> image-set(webp, jpg) quando existe X.webp ao lado."""
    def f(m):
        url = m.group(1)
        rel = local(url)
        if not rel or not rel.lower().endswith(('.jpg', '.jpeg')):
            return m.group(0)
        w = re.sub(r'\.jpe?g$', '.webp', rel, flags=re.I)
        if not os.path.isfile(R + w):
            return m.group(0)
        wurl = url[:len(url) - len(rel)] + w if url.endswith(rel) else url.rsplit('.', 1)[0] + '.webp'
        return (f"background-image:url('{url}');background-image:image-set(url('{wurl}') type('image/webp'),"
                f"url('{url}') type('image/jpeg'))")
    return re.sub(r"background-image:url\('([^']+)'\)(?!;background-image:image-set)", f, t, count=1)


mud = {'p': 0, 'catalogo': 0, 'outras': 0}
for f in sorted(glob.glob(R + 'p/*.html')):
    o = open(f, encoding='utf-8').read()
    t = troca_logos(o)
    # cartões "Produtos relacionados"
    t = re.sub(r'(<a class="rc"[^>]*>)(<img\b[^>]*>)', lambda m: m.group(1) + troca_img(m.group(2), sizes='(max-width:700px) 40vw, 170px'), t)
    # botões da galeria (64 px): só a miniatura; o clique continua trocando o fundo pela foto grande
    t = re.sub(r'(<button type="button"[^>]*>)(<img\b[^>]*>)',
               lambda m: m.group(1) + troca_img(m.group(2), sizes='64px'), t)
    t = bg_webp(t)
    mud['p'] += grava(f, t, o)

for f in (R + 'catalogo.html', R + 'catalogo/index.html'):
    o = open(f, encoding='utf-8').read()
    t = re.sub(r'(<div class="ph">)(<img\b[^>]*>)', lambda m: m.group(1) + troca_img(m.group(2), sizes='(max-width:700px) 40vw, 186px'), o)
    t = troca_logos(t)
    mud['catalogo'] += grava(f, t, o)

outras = [f for f in glob.glob(R + '**/*.html', recursive=True)
          if '/p/' not in f and '/_ferramentas/' not in f and '/.git/' not in f
          and not f.endswith(('/catalogo.html', '/catalogo/index.html'))]
for f in outras:
    o = open(f, encoding='utf-8').read()
    t = troca_logos(o)
    mud['outras'] += grava(f, t, o)

print('miniaturas novas:', criadas, '| páginas alteradas:', mud, '(dry)' if DRY else '')
