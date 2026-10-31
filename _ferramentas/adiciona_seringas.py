# -*- coding: utf-8 -*-
"""Cadastra no site as SERINGAS (31/10/2026) — aprovadas pelo dono, com estoque e NF de compra.

Itens: SR 10 mL Luer Slip c/ 500 (3469), Neolab gasometria 2,5 mL c/ 100 (SG25SA-1) e SR 5 mL c/ 500 (564).
Foto: só entra no site o item que tem foto boa do produto real (FOTOS abaixo). Item sem foto fica em PENDENTE_FOTO.

Frete: o peso/caixa de cada código fica no Worker sullab-api (api.lojasullabrj.com.br/frete2), fora deste repositório.
Enquanto o Worker não tiver o peso, os itens entram como "sob consulta" (sem preço em data/precos.json), para o
checkout nunca calcular frete errado. Depois de cadastrar o peso no Worker:
    python3 _ferramentas/adiciona_seringas.py --ativar-precos
grava os preços, a quantidade por caixa (QTD) e o feed do Google, e refaz as páginas com o preço.

Gera/atualiza: img/p/<cód>.jpg/.webp, data/catalogo.json, kw.json, ft.json, p/*.html,
categoria/seringas-e-agulhas.html (nova), categoria/agulhas.html (link), sitemap-produtos.xml, sitemap-categorias.xml.
Depois rodar: python3 _ferramentas/miniaturas.py   (miniatura dos cartões)
Uso: python3 _ferramentas/adiciona_seringas.py [--ativar-precos]
"""
import html
import json
import os
import re
import sys

from PIL import Image

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import dados_site as ds  # noqa: E402

R = ds.R
SITE = 'https://lojasullabrj.com.br'
HOJE = '2026-10-31'
ATIVAR = '--ativar-precos' in sys.argv
CAT = ('seringa', 'Seringas e agulhas', 'seringas-e-agulhas')
FONTE_FOTOS = '/mnt/user-data/uploads/Claude/Fotos_Produtos_16-10-2026/_principal_1240/'

ITENS = [
    {'cod': '3469', 'm': 'SR', 'qtd': 500, 'venda': 345.00,
     'nome': 'Seringa descartável 10 mL sem agulha, bico Luer Slip SR — caixa c/ 500 un',
     'slug': 'seringa-descartavel-10-ml-sem-agulha-luer-slip-sr-3469',
     'foto': FONTE_FOTOS + 'SR/SERINGA-10ML - Seringa 10 mL - principal 1240.jpg',
     'frete': [4.5, 30, 35, 45],
     'ficha': ['Seringa hipodérmica estéril de uso único, para uso manual, sem agulha',
               'Capacidade: 10 mL, com escala de graduação em mL',
               'Bico Luer Slip (encaixe por pressão)',
               'Atóxica, apirogênica e livre de látex',
               'Esterilizada por óxido de etileno; embalagem individual com abertura em pétala',
               'Embalagem: caixa com 500 unidades',
               'Registro Anvisa: 81391540016',
               'Marca: SR'],
     'kw': 'seringa seringas hipodermica descartavel 10ml 10 ml luer slip bico sem agulha sr injecao medicacao coleta esteril uso unico 3469',
     'sobre': 'Seringa descartável SR de 10 mL com bico Luer Slip, estéril e de uso único, para aspiração e administração de '
              'medicamentos, coleta e preparo de amostras. Vem sem agulha: combine com a agulha hipodérmica do calibre adequado ao procedimento. '
              'Corpo transparente com graduação nítida e êmbolo de deslizamento suave. Venda por caixa com 500 unidades, com NF-e para CNPJ.'},
    {'cod': 'SG25SA-1', 'm': 'Neolab', 'qtd': 100, 'venda': 185.00,
     'nome': 'Seringa para gasometria 2,5 mL com heparina de lítio, Luer Lock, sem agulha Neolab — caixa c/ 100 un',
     'slug': 'seringa-para-gasometria-2-5-ml-heparina-de-litio-luer-lock-sem-agulha-neolab-sg25sa-1',
     'foto': FONTE_FOTOS + 'Neolab/450 - Seringa Litio Gasometria 2,5 mL ref SG25SA-1 - principal 1240.jpg',
     'frete': [0.6, 10, 15, 20],
     'ficha': ['Seringa para coleta de sangue arterial para gasometria (análise de gases sanguíneos)',
               'Capacidade: 2,5 mL',
               'Anticoagulante: heparina de lítio',
               'Conexão Luer Lock, sem agulha',
               'Estéril (óxido de etileno), uso único, para diagnóstico in vitro (IVD)',
               'Armazenamento: 4 °C a 25 °C, em local seco e protegido da luz',
               'Embalagem: caixa com 100 unidades',
               'Referência: SG25SA-1 · Registro Anvisa: 81140320022',
               'Marca: Neolab'],
     'kw': 'seringa seringas gasometria gasometrica gases sanguineos arterial heparina litio litica heparinizada 2,5ml 2.5ml 25 luer lock sem agulha neolab sg25sa sg25sa1 sg25sa-1 coleta',
     'sobre': 'Seringa Neolab de 2,5 mL para gasometria, com heparina de lítio, para coleta de sangue arterial destinado à análise de gases '
              'sanguíneos, pH e eletrólitos. A conexão Luer Lock permite acoplar a agulha de punção e vedar a seringa após a coleta. '
              'Estéril e de uso único. Versão sem agulha. Venda por caixa com 100 unidades, com NF-e para CNPJ.'},
    {'cod': '564', 'm': 'SR', 'qtd': 500, 'venda': 225.00,
     'nome': 'Seringa descartável 5 mL sem agulha, bico Luer Slip SR — caixa c/ 500 un',
     'slug': 'seringa-descartavel-5-ml-sem-agulha-luer-slip-sr-564',
     'foto': None,  # sem foto do produto: não entra no site até ter foto
     'frete': [3.2, 25, 30, 40],
     'ficha': [], 'kw': '', 'sobre': ''},
]
PENDENTE_FOTO = [it for it in ITENS if not it['foto']]
ITENS = [it for it in ITENS if it['foto']]


def brl(v):
    return 'R$ ' + f'{v:,.2f}'.replace(',', 'X').replace('.', ',').replace('X', '.')


for it in ITENS:
    it['url'] = f'{SITE}/p/{it["slug"]}.html'
    it['img'] = f'{SITE}/img/p/{it["cod"]}.jpg'
    it['imgw'] = f'{SITE}/img/p/{it["cod"]}.webp'

# ---------------------------------------------------------------- fotos 1240x1240 fundo branco
for it in ITENS:
    dst = R + f'img/p/{it["cod"]}.jpg'
    if os.path.exists(dst) and not os.path.exists(it['foto']):
        continue
    im = Image.open(it['foto']).convert('RGB')
    lado = max(im.size)
    fundo = Image.new('RGB', (lado, lado), (255, 255, 255))
    fundo.paste(im, ((lado - im.width) // 2, (lado - im.height) // 2))
    fundo = fundo.resize((1240, 1240), Image.LANCZOS)
    fundo.save(dst, 'JPEG', quality=84, optimize=True, progressive=True)
    fundo.save(R + f'img/p/{it["cod"]}.webp', 'WEBP', quality=80, method=6)

# ---------------------------------------------------------------- catálogo, preços, kw, ft
seed = ds.ler_catalogo()
cods = {p['c'] for p in seed}
for it in ITENS:
    if it['cod'] not in cods:
        seed.append({'c': it['cod'], 'n': it['nome'], 'm': it['m'], 'k': CAT[0], 'img': f'img/p/{it["cod"]}.webp'})
ds.gravar_catalogo(seed)
if ATIVAR:
    pre = ds.ler_precos()
    for it in ITENS:
        pre[it['cod']] = [it['venda'], it['venda'], None]
    ds.gravar_precos(pre)
    loja = open(ds.LOJA_JS, encoding='utf-8').read()
    q0 = loja.find('window.QTD=') + len('window.QTD=')
    qd, qfim = json.JSONDecoder().raw_decode(loja[q0:])
    novos = {it['cod']: [it['qtd'], 'unidade', 'caixa'] for it in ITENS if it['cod'] not in qd}
    if novos:
        txt = loja[q0:q0 + qfim]
        add = ','.join(f'{json.dumps(c)}:{json.dumps(v, ensure_ascii=False)}' for c, v in novos.items())
        loja = loja[:q0] + txt[:-1] + ',' + add + '}' + loja[q0 + qfim:]
        open(ds.LOJA_JS, 'w', encoding='utf-8').write(loja)
        ds.atualizar_versoes()

kw = json.load(open(R + 'kw.json', encoding='utf-8'))
ft = json.load(open(R + 'ft.json', encoding='utf-8'))
for it in ITENS:
    kw[it['cod']] = it['kw']
    ft[it['cod']] = ' · '.join(x.rstrip('.') + '.' for x in it['ficha'])
json.dump(kw, open(R + 'kw.json', 'w', encoding='utf-8'), ensure_ascii=False, separators=(',', ':'))
json.dump(ft, open(R + 'ft.json', 'w', encoding='utf-8'), ensure_ascii=False, separators=(',', ':'))

# ---------------------------------------------------------------- páginas de produto (modelo: página do EV21)
tpl = open(R + 'p/escalpe-para-coleta-de-sangue-a-vacuo-21g-com-tubo-de-7-ev21.html', encoding='utf-8').read()
STYLE = tpl[tpl.find('<style>'):tpl.find('</head>')].replace("item_id:'EV21'", "item_id:'%COD%'")
FOOT = tpl[tpl.find('<footer class="siteftr">'):]
RETURN = {"@type": "MerchantReturnPolicy", "applicableCountry": "BR", "returnPolicyCategory": "https://schema.org/MerchantReturnFiniteReturnWindow",
          "merchantReturnDays": 7, "returnMethod": "https://schema.org/ReturnByMail", "returnFees": "https://schema.org/FreeReturn",
          "refundType": "https://schema.org/FullRefund", "merchantReturnLink": SITE + "/trocas-e-devolucoes.html"}
AGULHAS = [('https://lojasullabrj.com.br/p/agulha-multipla-p-coleta-a-vacuo-250-8-mm-21g-caixa-c-100-trifacetada-siliconada-450072.html', '450072'),
           ('https://lojasullabrj.com.br/p/agulha-multipla-p-coleta-a-vacuo-250-7-mm-22g-caixa-c-100-trifacetada-siliconada-450071.html', '450071'),
           ('https://lojasullabrj.com.br/p/escalpe-para-coleta-de-sangue-a-vacuo-21g-com-tubo-de-7-ev21.html', 'EV21')]
info = {p['c']: p for p in seed}
precos = ds.ler_precos()


def preco_de(c):
    v = precos.get(c)
    return v[1] if v and v[1] else 0


def img_de(c):
    p = info[c]
    t = p.get('img') or ''
    return t if t.startswith('http') else SITE + '/' + t.lstrip('/')


def card(url, c):
    n = html.escape(info[c]['n'])
    v = preco_de(c)
    ptxt = f'<b class="rp">{brl(v)}</b>' if v else '<b class="rp sc">Sob consulta</b>'
    return f'<a class="rc" href="{url}"><img src="{img_de(c)}" alt="{n}" loading="lazy" width="160" height="160"><span class="rn">{n}</span>{ptxt}<span class="rv">Ver produto</span></a>'


def pagina(it):
    cod, n = it['cod'], it['nome']
    ne = html.escape(n)
    curto = re.split(r' — caixa c/', n)[0]
    titulo = f'{curto} | SULLAB'
    catk, catn, cats = CAT
    v = it['venda'] if ATIVAR else 0
    emb = f'caixa c/ {it["qtd"]} un'
    if v:
        un = brl(v / it['qtd'])
        desc = f'{n}: {emb} por {brl(v)} ({un} por unidade) no CNPJ, com NF-e e entrega para todo o Brasil. Compre no site com desconto no Pix.'
        preco_html = (f'<div class="preco" style="margin:10px 0;padding:10px 12px;background:#f4f7fb;border-radius:8px;font-size:15px">💰 <b>{brl(v)}</b> '
                      f'<span class="pfx" style="color:#5a6472;font-weight:400;font-size:13px">por {emb}. · <b>{un} por unidade</b> · empresas (CNPJ), com NF-e</span><br>'
                      '<span class="pfx" style="color:#5a6472;font-weight:400;font-size:13px">Frete calculado pelo CEP na loja; grátis automático em pedidos que atingem o valor mínimo.</span></div>')
        botoes = f'<a class="btn-whats" style="background:#2f9e63" href="{SITE}/?carrinho={cod}:1">🛒 Comprar agora</a><a class="btn" href="{SITE}/?q={cod}">Ver na loja →</a>'
        oferta = {"@type": "Offer", "priceCurrency": "BRL", "price": f'{v:.2f}', "availability": "https://schema.org/InStock", "url": it['url'],
                  "itemCondition": "https://schema.org/NewCondition", "seller": {"@type": "Organization", "name": "SULLAB"}, "hasMerchantReturnPolicy": RETURN}
    else:
        desc = f'{n}: {emb}, com registro Anvisa. Preço CNPJ sob consulta, com NF-e e entrega para todo o Brasil. Peça o orçamento.'
        preco_html = '<div class="preco">Preço sob consulta — peça o orçamento e respondemos com valor atualizado, frete e NF-e.</div>'
        botoes = f'<a class="btn-whats" href="{SITE}/?orcar={cod}" target="_blank" rel="noopener">📄 Pedir orçamento</a><a class="btn" href="{SITE}/?q={cod}">Comprar na loja →</a>'
        oferta = {"@type": "Offer", "priceCurrency": "BRL", "availability": "https://schema.org/InStock", "url": it['url'],
                  "itemCondition": "https://schema.org/NewCondition", "seller": {"@type": "Organization", "name": "SULLAB"}, "hasMerchantReturnPolicy": RETURN}
    de = html.escape(desc)
    fdesc = ' · '.join(x.rstrip('.') + '.' for x in it['ficha'])
    prod = {"@context": "https://schema.org/", "@type": "Product", "name": n, "sku": cod, "category": catn, "description": fdesc,
            "brand": {"@type": "Brand", "name": it['m']}, "offers": oferta, "image": it['img'], "mpn": cod}
    bc = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Início", "item": SITE + "/"},
        {"@type": "ListItem", "position": 2, "name": catn, "item": f'{SITE}/categoria/{cats}.html'},
        {"@type": "ListItem", "position": 3, "name": n, "item": it['url']}]}
    img, imgw = it['img'], it['imgw']
    gal = (f'<div class="gal"><div class="ph" id="ph" style="background-image:url(\'{img}\');background-image:image-set(url(\'{imgw}\') type(\'image/webp\'),url(\'{img}\') type(\'image/jpeg\'))"></div>'
           f'<div class="th"><button type="button" class="on" aria-label="Foto do produto" '
           f'onclick="var p=document.getElementById(\'ph\');p.style.backgroundImage=&quot;url(\'{img}\')&quot;;var b=this.parentNode.children;for(var i=0;i<b.length;i++)b[i].className=\'\';this.className=\'on\'">'
           f'<img decoding="async" src="{imgw}" alt="Foto do produto" loading="lazy" width="1240" height="1240"></button></div></div>')
    ficha = '<br>'.join(html.escape(x.rstrip('.') + '.') for x in it['ficha'])
    rel = [card(o['url'], o['cod']) for o in ITENS if o is not it] + [card(u, c) for u, c in AGULHAS if c in info]
    return f'''<!DOCTYPE html><html lang="pt-BR"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(titulo)}</title>
<meta name="description" content="{de}">
<link rel="canonical" href="{it['url']}">
<meta name="robots" content="index,follow">
<meta property="og:type" content="product"><meta property="og:title" content="{html.escape(titulo)}">
<meta property="og:description" content="{de}">
<meta property="og:image" content="{img}">
<meta property="og:url" content="{it['url']}">

<script type="application/ld+json">{json.dumps(prod, ensure_ascii=False)}</script>
<script type="application/ld+json">{json.dumps(bc, ensure_ascii=False)}</script>
{STYLE.replace('%COD%', cod)}</head><body>
<div class="wrap">
<div class="top"><img src="{SITE}/img/sullab-topo.webp" alt="SULLAB" width="65" height="34"><a href="{SITE}/">SULLAB</a></div>
<div class="crumb"><a href="{SITE}/">Início</a> › <a href="{SITE}/categoria/{cats}.html">{catn}</a> › {ne}</div>
<div class="card">
{gal}
<div>
<h1>{ne}</h1>
<div class="brand"><b>Marca:</b> {html.escape(it['m'])} · <b>Código:</b> {cod}</div>{preco_html}<div class="tb"><span>🧾 NF-e em todo pedido</span><span>🚚 Envio em 24h</span></div><a class="trocaslk" href="{SITE}/trocas-e-devolucoes.html">Ver política de trocas e devoluções</a><div class="ficha">🔬 <b>Ficha técnica</b><br>{ficha}</div>
{botoes}
<div>
<a class="btn2" href="{SITE}/categoria/{cats}.html">Ver {catn}</a>
</div>

</div></div>
<h2>Sobre o produto</h2><p class="lead">{html.escape(it['sobre'])}</p>
<h2>Produtos relacionados</h2><div class="rel rcards">
{chr(10).join(rel)}
</div>
{FOOT}'''


for it in ITENS:
    open(R + 'p/' + it['slug'] + '.html', 'w', encoding='utf-8').write(pagina(it))

# ---------------------------------------------------------------- categoria nova: Seringas e agulhas (modelo: agulhas.html)
ag = open(R + 'categoria/agulhas.html', encoding='utf-8').read()
URLC = f'{SITE}/categoria/{CAT[2]}.html'
gi = ag.find('<div class="grid">\n') + len('<div class="grid">\n')
ge = ag.find('</div>', gi)
linhas_ag = ag[gi:ge].strip('\n').split('\n')
ld_ag = json.loads(re.search(r'"@type": "ItemList", "itemListElement": (\[.*?\])\}', ag).group(1))


def grid_a(it):
    v = it['venda'] if ATIVAR else 0
    pr = f'<span class="pr">{brl(v)} <small>CNPJ</small></span>' if v else '<span class="prc">Sob consulta →</span>'
    return f'<a href="{it["url"]}"><span class="nm">{html.escape(it["nome"][:70].rstrip())}</span>{pr}<span class="cs">cód. {it["cod"]}</span></a>'


n_tot = len(ITENS) + len(linhas_ag)
DESC_C = f'Seringas descartáveis (Luer Slip), seringas para gasometria com heparina de lítio e agulhas para coleta a vácuo. Preço CNPJ, NF-e e entrega para todo o Brasil. {n_tot} itens.'
faq = [("Qual a diferença entre bico Luer Slip e Luer Lock?", "No Luer Slip a agulha encaixa por pressão no bico da seringa; no Luer Lock ela é rosqueada, o que dá mais firmeza à conexão e evita que se solte em procedimentos sob pressão, como a coleta para gasometria."),
       ("As seringas vêm com agulha?", "As seringas desta página são vendidas sem agulha. Escolha a agulha no calibre (gauge) adequado ao procedimento e combine com a seringa."),
       ("Para que serve a seringa com heparina de lítio?", "É usada na coleta de sangue arterial para gasometria. A heparina de lítio evita a coagulação da amostra sem interferir na medição de gases, pH e eletrólitos."),
       ("As caixas vêm com quantas unidades?", "As seringas descartáveis SR vêm em caixas com 500 unidades e as seringas de gasometria Neolab em caixas com 100 unidades. Confira a embalagem na ficha de cada produto.")]
faq_ld = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faq]}
bc_ld = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [{"@type": "ListItem", "position": 1, "name": "Início", "item": SITE + "/"}, {"@type": "ListItem", "position": 2, "name": CAT[1], "item": URLC}]}
il = [{"@type": "ListItem", "position": i + 1, "url": it['url'], "name": it['nome']} for i, it in enumerate(ITENS)]
il += [{"@type": "ListItem", "position": len(il) + i + 1, "url": x['url'], "name": x['name']} for i, x in enumerate(ld_ag)]
il_ld = {"@context": "https://schema.org", "@type": "ItemList", "itemListElement": il}
head_style = ag[ag.find('<style>'):ag.find('</head>')]
foot = ag[ag.find('<footer class="siteftr">'):]
TIT = 'Seringas e agulhas: preço CNPJ e NF-e | SULLAB'
corpo = f'''<!DOCTYPE html><html lang="pt-BR"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{TIT}</title>
<meta name="description" content="{html.escape(DESC_C)}">
<link rel="canonical" href="{URLC}">
<meta name="robots" content="index,follow">
<meta property="og:type" content="website"><meta property="og:title" content="{TIT}">
<meta property="og:description" content="{html.escape(DESC_C)}">
<meta property="og:url" content="{URLC}">
<script type="application/ld+json">{json.dumps(bc_ld, ensure_ascii=False)}</script>
<script type="application/ld+json">{json.dumps(faq_ld, ensure_ascii=False)}</script>
<script type="application/ld+json">{json.dumps(il_ld, ensure_ascii=False)}</script>
{head_style}</head><body>
<div class="wrap">
<div class="top"><img src="{SITE}/img/sullab-topo.webp" alt="SULLAB" width="65" height="34"><a href="{SITE}/">SULLAB</a></div>
<div class="crumb"><a href="{SITE}/">Início</a> › {CAT[1]}</div>
<h1>{CAT[1]}</h1>
<p class="lead">Seringas descartáveis estéreis com bico Luer Slip, seringas para gasometria com heparina de lítio (Luer Lock) e agulhas para coleta de sangue a vácuo. A SULLAB é distribuidora de produtos para laboratório e diagnóstico clínico, com preço para CNPJ, nota fiscal (NF-e) e entrega para todo o Brasil. Veja abaixo as <b>seringas e agulhas</b> disponíveis.</p>
<a class="btn" href="{SITE}/?cat=agulha">Ver na loja e montar orçamento →</a><div class="tb"><span>🧾 NF-e</span><span>💰 Preço CNPJ</span><span>🚚 Envio 24h</span><span>🏭 Sem taxa de marketplace</span></div>
<h2>Seringas e agulhas ({n_tot})</h2>
<div class="grid">
{chr(10).join(grid_a(it) for it in ITENS)}
{chr(10).join(linhas_ag)}
</div>
<h2>Perguntas frequentes</h2><div class="faq">{''.join(f'<details><summary>{html.escape(q)}</summary><p>{html.escape(a)}</p></details>' for q, a in faq)}</div>
{foot}'''
open(R + f'categoria/{CAT[2]}.html', 'w', encoding='utf-8').write(corpo)

# agulhas.html: link para a categoria nova (uma vez)
LNK = f'<p class="lead">Procurando seringas? Veja <a href="{URLC}">Seringas e agulhas</a>.</p>'
if LNK not in ag:
    k = ag.find('<h2>Perguntas frequentes</h2>')
    ag = ag[:k] + LNK + '\n' + ag[k:]
    open(R + 'categoria/agulhas.html', 'w', encoding='utf-8').write(ag)

# ---------------------------------------------------------------- sitemaps
sp = R + 'sitemap-produtos.xml'
s = open(sp, encoding='utf-8').read()
add = ''.join(f'<url><loc>{it["url"]}</loc><lastmod>{HOJE}</lastmod><changefreq>weekly</changefreq></url>\n' for it in ITENS if it['url'] not in s)
s = s.replace('</urlset>', add + '</urlset>', 1)
open(sp, 'w', encoding='utf-8').write(s)
sc = R + 'sitemap-categorias.xml'
s = open(sc, encoding='utf-8').read()
if URLC not in s:
    ant = '<url><loc>https://lojasullabrj.com.br/categoria/agulhas.html</loc>'
    k = s.find('</url>', s.find(ant)) + len('</url>\n')
    s = s[:k] + f'<url><loc>{URLC}</loc><lastmod>{HOJE}</lastmod><changefreq>weekly</changefreq></url>\n' + s[k:]
    open(sc, 'w', encoding='utf-8').write(s)

# ---------------------------------------------------------------- feed Google (só com preço)
if ATIVAR:
    fp = R + 'feed-google.xml'
    s = open(fp, encoding='utf-8').read()
    x = html.escape
    for it in ITENS:
        if f'<g:id>{x(it["cod"])}</g:id>' in s:
            continue
        d = f'{it["nome"]}. Marca {it["m"]}. ' + ' '.join(y.rstrip('.') + '.' for y in it['ficha'][:-1]) + ' Venda para empresas (CNPJ) com NF-e e entrega para todo o Brasil.'
        s = s.replace('</channel>', f'''<item>
<g:id>{x(it["cod"])}</g:id>
<g:title>{x(it["nome"])}</g:title>
<g:description>{x(d)}</g:description>
<g:link>{it["url"]}</g:link>
<g:image_link>{it["img"]}</g:image_link>
<g:condition>new</g:condition>
<g:availability>in_stock</g:availability>
<g:price>{it["venda"]:.2f} BRL</g:price>
<g:brand>{x(it["m"])}</g:brand>
<g:mpn>{x(it["cod"])}</g:mpn>
<g:identifier_exists>no</g:identifier_exists>
<g:google_product_category>Health &amp; Beauty &gt; Health Care &gt; Medical Supplies</g:google_product_category>
<g:product_type>{x(CAT[1])}</g:product_type>
</item>
</channel>''', 1)
    open(fp, 'w', encoding='utf-8').write(s)

print('no site:', ', '.join(it['cod'] for it in ITENS), '| sem foto (fora):', ', '.join(it['cod'] for it in PENDENTE_FOTO) or '-',
      '| preços:', 'ativos' if ATIVAR else 'sob consulta (aguardando peso no Worker)')
print('Peso/caixa para o Worker (kg, alt, larg, comp):')
for it in ITENS + PENDENTE_FOTO:
    print(' ', it['cod'], it['frete'], brl(it['venda']))
