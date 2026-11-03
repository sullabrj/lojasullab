# -*- coding: utf-8 -*-
"""Cadastra no site o tubo VACUETTE 454321 — coagulação citrato de sódio 3,2% 2 mL 13x75 (03/11/2026).

Pedido do dono (cliente Laboratório Fontana, 7.200 tubos). Mesmo custo do 454327 (tabela Greiner MG/RJ/ES/Sul
de 01/04/2026: R$ 0,6039 por tubo + 5,2% de IPI), portanto o mesmo preço do site (R$ 43,20 o rack c/ 50).
Foto: shop.gbo.com (454321_001.jpg) — tampa azul clara, anel branco (tubo "sandwich", PREMIUM).

Clona o 454327 em: data/catalogo.json, data/precos.json, data/ficha.json, js/loja.js (QTD, GREINER_DE,
GREINER_ORDEM, PIX3), pm.js (PIX3), kw.json, ft.json, p/<slug>.html, categoria/tubos-a-vacuo.html,
marca/vacuette.html, catalogo.html, catalogo/index.html, sitemap-produtos.xml, feed-google.xml,
feeds/catalogo_whatsapp.csv, _ferramentas/pedido_minimo_itens.json, _ferramentas/gerar_pdfs.py e o Worker
(_ferramentas/workers/sullab-api.js: FRETE_TAB, GREINER, PROD).
Depois: python3 _ferramentas/miniaturas.py
Uso: python3 _ferramentas/adiciona_citrato_2ml.py <foto_gbo.jpg>
"""
import json
import os
import re
import sys

from PIL import Image

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import dados_site as ds  # noqa: E402

R = ds.R
HOJE = '2026-11-03'
VELHO, NOVO = '454327', '454321'
NOME_V = 'Tubo coagulação (citrato de sódio 3,2%) 3,5 mL 13×75 — rack c/ 50 un'
NOME_N = 'Tubo coagulação (citrato de sódio 3,2%) 2 mL 13×75 — rack c/ 50 un'
SLUG_V = 'tubo-coagulacao-citrato-de-sodio-3-2-3-5-ml-1375-rack-c-50-un-454327'
SLUG_N = 'tubo-coagulacao-citrato-de-sodio-3-2-2-ml-1375-rack-c-50-un-454321'


def ler(p):
    return open(R + p, encoding='utf-8').read()


def grava(p, t):
    open(R + p, 'w', encoding='utf-8').write(t)


def troca_nomes(s):
    """Texto de um bloco clonado do 454327 -> 454321."""
    s = s.replace(SLUG_V, SLUG_N).replace(NOME_V, NOME_N)
    s = s.replace(NOME_V.replace(' — ', ' - '), NOME_N.replace(' — ', ' - '))
    s = s.replace('Tubo coagulação 3,5 mL', 'Tubo coagulação 2 mL')
    s = s.replace('Volume: 3,5 mL', 'Volume: 2 mL').replace('<td>3,5 mL</td>', '<td>2 mL</td>')
    s = s.replace('uso único com 3,5 mL', 'uso único com 2 mL').replace('anel preto', 'anel branco')
    return s.replace(VELHO, NOVO)


def clona_bloco(path, rx, flags=re.S):
    """Acha o 1º bloco do 454327 (regex) e insere a cópia trocada logo depois."""
    t = ler(path)
    if NOVO in t:
        print('já tem', path)
        return
    m = re.search(rx, t, flags)
    if not m:
        raise SystemExit('bloco não achado em ' + path)
    b = m.group(0)
    t = t[:m.end()] + troca_nomes(b) + t[m.end():]
    grava(path, t)
    print('ok', path)


# ---------------------------------------------------------------- foto (1000x1000 fundo branco, como o 454327)
src = sys.argv[1]
im = Image.open(src).convert('RGB')
lado = int(max(im.size) * 1.12)
fundo = Image.new('RGB', (lado, lado), (255, 255, 255))
fundo.paste(im, ((lado - im.width) // 2, (lado - im.height) // 2))
f1000 = fundo.resize((1000, 1000), Image.LANCZOS)
f1000.save(R + NOVO + '.jpg', 'JPEG', quality=88, optimize=True, progressive=True)
fundo.resize((800, 800), Image.LANCZOS).save(R + 'img/wa/cat/' + NOVO + '.jpg', 'JPEG', quality=86, optimize=True)

# ---------------------------------------------------------------- dados
seed = ds.ler_catalogo()
if not any(p['c'] == NOVO for p in seed):
    i = next(k for k, p in enumerate(seed) if p['c'] == VELHO)
    novo = {'c': NOVO, 'n': NOME_N, 'm': 'Vacuette', 'k': 'tubo', 'img': 'https://lojasullabrj.com.br/' + NOVO + '.jpg'}
    seed.insert(i + 1, novo)
    ds.gravar_catalogo(seed)
pre = ds.ler_precos()
if NOVO not in pre:
    novo_pre = {}
    for k, v in pre.items():
        novo_pre[k] = v
        if k == VELHO:
            novo_pre[NOVO] = list(v)
    ds.gravar_precos(novo_pre)

fi = json.load(open(R + 'data/ficha.json', encoding='utf-8'))
if NOVO not in fi:
    d = json.loads(troca_nomes(json.dumps(fi[VELHO], ensure_ascii=False)))
    for r in d['rows']:
        if r[0] == 'Volume':
            r[1] = '2 mL'
    d['why'] = ['Citrato de sódio 3,2% para coagulação', 'Rack com 50 unidades', 'Tubo de uso único com 2 mL (baixo volume)']
    novo_fi = {}
    for k, v in fi.items():
        novo_fi[k] = v
        if k == VELHO:
            novo_fi[NOVO] = d
    t = json.dumps(novo_fi, ensure_ascii=False, separators=(',', ':'))
    antigo = open(R + 'data/ficha.json', encoding='utf-8').read()
    if antigo.endswith('\n'):
        t += '\n'
    open(R + 'data/ficha.json', 'w', encoding='utf-8').write(t)
    ds.atualizar_versoes()

for js in ['kw.json', 'ft.json']:
    t = ler(js)
    if '"' + NOVO + '"' not in t:
        m = re.search(r'"' + VELHO + r'":"(?:[^"\\]|\\.)*"', t)
        b = m.group(0)
        nb = '"' + NOVO + '"' + b[len(VELHO) + 2:]
        if js == 'ft.json':
            nb = nb.replace('Volume: 3,5 mL', 'Volume: 2 mL')
        else:
            nb = nb.replace('"' + NOVO + '":"', '"' + NOVO + '":"2ml 454321 ')
        t = t[:m.end()] + ',' + nb + t[m.end():]
        grava(js, t)

# ---------------------------------------------------------------- loja.js / pm.js
loja = ds.ler_loja_js()
if '"' + NOVO + '"' not in loja:
    loja = loja.replace('"454327":[50,"unidade","rack"]', '"454327":[50,"unidade","rack"],"454321":[50,"unidade","rack"]', 1)
    loja = loja.replace('"454327": 44.69,', '"454327": 44.69, "454321": 44.69,', 1)
    loja = loja.replace('"456071", "454327",', '"456071", "454327", "454321",', 1)
    loja = loja.replace('"454327":1,', '"454327":1,"454321":1,', 1)
    assert loja.count('"454321"') == 4, loja.count('"454321"')
    ds.gravar_loja_js(loja)
pm = ler('pm.js')
if '"454321"' not in pm:
    pm = pm.replace('"454327":1,', '"454327":1,"454321":1,', 1)
    grava('pm.js', pm)

mi = json.load(open(R + '_ferramentas/pedido_minimo_itens.json', encoding='utf-8'))
if NOVO not in mi['pix3']:
    mi['pix3'] = sorted(mi['pix3'] + [NOVO])
    open(R + '_ferramentas/pedido_minimo_itens.json', 'w', encoding='utf-8').write(json.dumps(mi, ensure_ascii=False, indent=0) + '\n')

# ---------------------------------------------------------------- página do produto
pv = R + 'p/' + SLUG_V + '.html'
pn = R + 'p/' + SLUG_N + '.html'
if not os.path.exists(pn):
    t = open(pv, encoding='utf-8').read()
    # o título/descrição curtos não levam o nome completo
    t = t.replace('(citrato de sódio 3,2%) 3,5 mL 13×75 Vacuette', '(citrato de sódio 3,2%) 2 mL 13×75 Vacuette')
    t = troca_nomes(t)
    open(pn, 'w', encoding='utf-8').write(t)

# ---------------------------------------------------------------- listas e páginas
clona_bloco('categoria/tubos-a-vacuo.html',
            r'\{"@type": "ListItem", "position": \d+, "url": "https://lojasullabrj\.com\.br/p/' + SLUG_V + r'\.html", "name": "[^"]*"\}, ')
t = ler('categoria/tubos-a-vacuo.html')
n = [0]


def pos(m):
    n[0] += 1
    return '"position": %d' % n[0]


t = re.sub(r'"position": \d+', pos, t)
if NOVO not in t.split('<div class="grid">', 1)[1]:
    m = re.search(r'<div class="it"><a class="nm" href="https://lojasullabrj\.com\.br/p/' + SLUG_V + r'\.html">.*?</div>\n', t, re.S)
    t = t[:m.end()] + troca_nomes(m.group(0)) + t[m.end():]
    t = re.sub(r'<h2>Produtos de Tubos a vácuo \((\d+)\)</h2>', lambda x: '<h2>Produtos de Tubos a vácuo (%d)</h2>' % (int(x.group(1)) + 1), t)
grava('categoria/tubos-a-vacuo.html', t)

clona_bloco('marca/vacuette.html', r'<a href="https://lojasullabrj\.com\.br/p/' + SLUG_V + r'\.html">[^<]*</a>\n')
for cat in ['catalogo.html', 'catalogo/index.html']:
    t = ler(cat)
    if NOVO not in t:
        m = re.search(r'<a class="item" target="_blank" rel="noopener" href="https://lojasullabrj\.com\.br/(?:p/' + SLUG_V + r'\.html|\?q=' + VELHO + r')">.*?</a>', t, re.S)
        nb = re.sub(r'src="[^"]*img/t/[0-9a-f]+\.webp" srcset="[^"]*"', 'src="https://lojasullabrj.com.br/' + NOVO + '.jpg"', troca_nomes(m.group(0)))
        t = t[:m.end()] + nb + t[m.end():]
        t = t.replace('<b>20 itens</b> neste catálogo · linha completa com <b>20 itens</b> no site',
                      '<b>21 itens</b> neste catálogo · linha completa com <b>21 itens</b> no site')
        grava(cat, t)

t = ler('sitemap-produtos.xml')
if NOVO not in t:
    m = re.search(r'<url><loc>https://lojasullabrj\.com\.br/p/' + SLUG_V + r'\.html</loc>.*?</url>\n', t, re.S)
    nb = re.sub(r'<lastmod>[^<]*</lastmod>', '<lastmod>' + HOJE + '</lastmod>', troca_nomes(m.group(0)))
    grava('sitemap-produtos.xml', t[:m.end()] + nb + t[m.end():])

clona_bloco('feed-google.xml', r'<item>\n<g:id>' + VELHO + r'</g:id>.*?</item>\n')
t = ler('feeds/catalogo_whatsapp.csv')
if '\n' + NOVO + ',' not in t:
    m = re.search(r'\n' + VELHO + r',.*?\n', t)
    grava('feeds/catalogo_whatsapp.csv', t[:m.end()] + troca_nomes(m.group(0)[1:]) + t[m.end():])

t = ler('_ferramentas/gerar_pdfs.py')
if "'" + NOVO + "'" not in t:
    t = t.replace("    '454327': ('Azul clara, anel preto', 'Citrato de sódio 3,2% (9NC)', 'TP/INR, TTPA, fibrinogênio, D-dímero', '4x', '10290310032'),\n",
                  "    '454327': ('Azul clara, anel preto', 'Citrato de sódio 3,2% (9NC)', 'TP/INR, TTPA, fibrinogênio, D-dímero', '4x', '10290310032'),\n"
                  "    '454321': ('Azul clara, anel branco', 'Citrato de sódio 3,2% (9NC)', 'TP/INR, TTPA, fibrinogênio, D-dímero', '4x', '10290310032'),\n", 1)
    t = t.replace("ORDEM_COLETA = ['454327', ", "ORDEM_COLETA = ['454327', '454321', ", 1)
    grava('_ferramentas/gerar_pdfs.py', t)

# ---------------------------------------------------------------- Worker sullab-api (frete, Greiner, PROD)
w = ler('_ferramentas/workers/sullab-api.js')
if '"454321"' not in w:
    w = re.sub(r'"454327":(\[[^\]]*\])', lambda m: m.group(0) + ',"454321":' + m.group(1), w)
    w = w.replace('"454327",', '"454321","454327",', 1)
    grava('_ferramentas/workers/sullab-api.js', w)
print('fim; agora: python3 _ferramentas/miniaturas.py')
