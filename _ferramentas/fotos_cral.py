#!/usr/bin/env python3
"""30/10/2026 — Baixa as fotos oficiais da CRAL usadas no site (links storage.googleapis),
deixa quadradas 1000x1000 com fundo branco no padrão do site (img/p/<COD>.jpg/.webp)
e troca os links externos pelos arquivos locais. Roda no GitHub Actions (fotos-cral.yml)."""
import io, os, re, sys, urllib.request
from PIL import Image

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PAD = re.compile(r'https://storage\.googleapis\.com/cv-pub-cloud/cral/imagens/produtos/([A-Za-z0-9._-]+?)\.jpg')
EXT = ('.html', '.json', '.xml', '.js', '.csv')

arquivos = []
for d, _, fs in os.walk(RAIZ):
    if '/.git' in d:
        continue
    for f in fs:
        if f.endswith(EXT):
            arquivos.append(os.path.join(d, f))

codigos = set()
for a in arquivos:
    try:
        codigos.update(PAD.findall(open(a, encoding='utf-8').read()))
    except Exception:
        pass
print('fotos CRAL referenciadas:', len(codigos))

ok = {}
for cod in sorted(codigos):
    url = f'https://storage.googleapis.com/cv-pub-cloud/cral/imagens/produtos/{cod}.jpg'
    try:
        raw = urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'}), timeout=30).read()
        im = Image.open(io.BytesIO(raw)).convert('RGB')
    except Exception as e:
        print('FALHOU', cod, e)
        continue
    im.thumbnail((920, 920), Image.LANCZOS)
    tela = Image.new('RGB', (1000, 1000), 'white')
    tela.paste(im, ((1000 - im.width) // 2, (1000 - im.height) // 2))
    dst = os.path.join(RAIZ, 'img', 'p', cod)
    tela.save(dst + '.jpg', 'JPEG', quality=86, optimize=True, progressive=True)
    tela.save(dst + '.webp', 'WEBP', quality=82, method=6)
    ok[cod] = True

def troca(m):
    cod = m.group(1)
    return f'https://lojasullabrj.com.br/img/p/{cod}.jpg' if cod in ok else m.group(0)

mud = 0
for a in arquivos:
    try:
        s = open(a, encoding='utf-8').read()
    except Exception:
        continue
    n = PAD.sub(troca, s)
    if n != s:
        open(a, 'w', encoding='utf-8').write(n)
        mud += 1
print(f'fotos salvas: {len(ok)} | arquivos com link trocado: {mud}')
if not ok:
    sys.exit(1)
