# -*- coding: utf-8 -*-
"""Cadastra no site os ANALISADORES (02/11/2026): bioquímica/eletrólitos, hematologia e veterinário.

Aparelhos em comodato ou aluguel, mediante contrato: sem preço no site, botão "Pedir orçamento".
Fotos e textos: site do fabricante/representante (fichas oficiais) + folhetos. Fotos em /mnt/user-data/uploads/Claude/tmp/equip_img/.
Gera: img/p/<cód>.jpg|webp, img/cat/<k>*.jpg|webp (cartões da página inicial), data/catalogo.json, kw.json, ft.json,
p/*.html, categoria/*.html, sitemaps. Depois rodar: python3 _ferramentas/miniaturas.py e dados_site.py
Uso: python3 _ferramentas/adiciona_equipamentos.py
"""
import html, json, os, re, sys
from PIL import Image
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import dados_site as ds

R = ds.R
SITE = 'https://lojasullabrj.com.br'
HOJE = '2026-11-02'
FONTE = '/mnt/user-data/uploads/Claude/tmp/equip_img/'
COMODATO = 'Equipamento disponível em comodato ou aluguel, mediante contrato. Solicite uma proposta.'

CATS = {
 'eqbioq': ('Equipamentos de bioquímica', 'equipamentos-de-bioquimica', '🧪',
            'Analisadores automáticos de bioquímica e analisador de eletrólitos (íons) para laboratório clínico, em comodato ou aluguel mediante contrato.'),
 'eqhemat': ('Equipamentos de hematologia', 'equipamentos-de-hematologia', '🩸',
            'Analisadores hematológicos de 5 partes (hemograma completo com diferencial) para laboratório clínico, em comodato ou aluguel mediante contrato.'),
 'eqvet': ('Equipamentos veterinários', 'equipamentos-veterinarios', '🐾',
            'Analisador de hematologia veterinário para clínicas e laboratórios veterinários, em comodato ou aluguel mediante contrato.'),
}
from dados_equipamentos import ITENS as _D
ITENS = []
for d in _D:
    it = dict(d); it['ficha'] = [t + ': ' + v for t, v in d['spec'][:6]]; it['sobre'] = ' '.join(d['desc']); ITENS.append(it)
for it in ITENS:
    it['url'] = f'{SITE}/p/{it["slug"]}.html'
    it['img'] = f'{SITE}/img/p/{it["cod"]}.jpg'
    it['imgw'] = f'{SITE}/img/p/{it["cod"]}.webp'
    it['cat'] = CATS[it['k']]

# ---- fotos
def carrega(f):
    im = Image.open(FONTE + f).convert('RGBA')
    bg = Image.new('RGBA', im.size, (255, 255, 255, 255)); bg.alpha_composite(im)
    box = im.split()[3].getbbox() or (0, 0) + im.size
    return bg.convert('RGB').crop(box)

for it in ITENS:
    im = carrega(it['foto'])
    lado = int(max(im.size) * 1.12)
    f = Image.new('RGB', (lado, lado), 'white'); f.paste(im, ((lado - im.width) // 2, (lado - im.height) // 2))
    f = f.resize((1240, 1240), Image.LANCZOS)
    f.save(R + f'img/p/{it["cod"]}.jpg', 'JPEG', quality=86, optimize=True, progressive=True)
    f.save(R + f'img/p/{it["cod"]}.webp', 'WEBP', quality=82, method=6)

# ---- cartões da página inicial (800x600, fundo claro como os demais)
def fundo():
    t = Image.new('RGB', (800, 600))
    for y in range(600):
        v = 230 + int(10 * y / 600); t.paste((v, v + 5, v + 11), (0, y, 800, y + 1))
    return t
def tile(k, lista):
    t = fundo(); n = len(lista); larg = 800 // n
    for i, f in enumerate(lista):
        im = carrega(f); im.thumbnail((larg - 40, 380))
        # remove o branco para não ficar um retângulo: máscara por proximidade de branco
        m = Image.eval(im.convert('L'), lambda p: 0 if p > 250 else 255).filter(__import__('PIL.ImageFilter', fromlist=['x']).MedianFilter(3))
        t.paste(im, (i * larg + (larg - im.width) // 2, 300 - im.height // 2 + 20), m)
    t.save(R + f'img/cat/{k}.jpg', 'JPEG', quality=84); t.save(R + f'img/cat/{k}.webp', 'WEBP', quality=80)
    s = t.resize((400, 300), Image.LANCZOS); s.save(R + f'img/cat/{k}-400.jpg', 'JPEG', quality=82); s.save(R + f'img/cat/{k}-400.webp', 'WEBP', quality=78)
tile('eqbioq', ['equip_EXC400b.png', 'equip_EHC120.png', 'equip_XI921.png'])
tile('eqhemat', ['equip_Z50_ok.png', 'equip_EXZ6000.png'])
tile('eqvet', ['equip_Z4VET.png'])

# ---- catálogo, kw, ft
seed = ds.ler_catalogo(); cods = {p['c'] for p in seed}
for it in ITENS:
    if it['cod'] not in cods:
        seed.append({'c': it['cod'], 'n': it['nome'], 'm': it['m'], 'k': it['k'], 'img': f'img/p/{it["cod"]}.webp'})
ds.gravar_catalogo(seed)
kw = json.load(open(R + 'kw.json', encoding='utf-8')); ft = json.load(open(R + 'ft.json', encoding='utf-8'))
for it in ITENS:
    kw[it['cod']] = it['kw']; ft[it['cod']] = ' · '.join(t + ': ' + v for t, v in it['spec'][:8])
json.dump(kw, open(R + 'kw.json', 'w', encoding='utf-8'), ensure_ascii=False, separators=(',', ':'))
json.dump(ft, open(R + 'ft.json', 'w', encoding='utf-8'), ensure_ascii=False, separators=(',', ':'))
fj = json.load(open(R + 'data/ficha.json', encoding='utf-8'))
for it in ITENS:
    fj[it['cod']] = {'rows': [[t, v] for t, v in it['spec']], 'why': it['dif'], 'desc': it['desc']}
json.dump(fj, open(R + 'data/ficha.json', 'w', encoding='utf-8'), ensure_ascii=False, separators=(',', ':'))
info = {p['c']: p for p in seed}

# ---- páginas de produto
tpl = open(R + 'p/escalpe-para-coleta-de-sangue-a-vacuo-21g-com-tubo-de-7-ev21.html', encoding='utf-8').read()
STYLE = tpl[tpl.find('<style>'):tpl.find('</head>')].replace("item_id:'EV21'", "item_id:'%COD%'")
FOOT = tpl[tpl.find('<footer class="siteftr">'):]
RETURN = {"@type": "MerchantReturnPolicy", "applicableCountry": "BR", "returnPolicyCategory": "https://schema.org/MerchantReturnFiniteReturnWindow",
          "merchantReturnDays": 7, "returnMethod": "https://schema.org/ReturnByMail", "returnFees": "https://schema.org/FreeReturn",
          "refundType": "https://schema.org/FullRefund", "merchantReturnLink": SITE + "/trocas-e-devolucoes.html"}
EXTRA = '.ft{width:100%;border-collapse:collapse;font-size:14px;margin:6px 0 18px}.ft th{text-align:left;width:34%;background:#f1f6fa;color:#24455e;font-weight:600;vertical-align:top}.ft th,.ft td{padding:8px 10px;border-bottom:1px solid #e1e8ee}.dif{padding-left:20px;line-height:1.55}.dif li{margin:4px 0}.tipo{color:#4a5a68;margin:6px 0 10px;font-weight:600}'
def card(o):
    n = html.escape(o['nome'])
    return f'<a class="rc" href="{o["url"]}"><img src="{o["img"]}" alt="{n}" loading="lazy" width="160" height="160"><span class="rn">{n}</span><b class="rp sc">Comodato / aluguel</b><span class="rv">Ver aparelho</span></a>'
def pagina(it):
    cod, n = it['cod'], it['nome']; ne = html.escape(n)
    catn, cats = it['cat'][0], it['cat'][1]
    titulo = f'{n} | SULLAB'
    desc = f'{n}. ' + it['desc'][0] + ' ' + COMODATO
    de = html.escape(desc)
    fdesc = ' '.join(it['desc'])
    prod = {"@context": "https://schema.org/", "@type": "Product", "name": n, "sku": cod, "category": catn, "description": fdesc,
            "brand": {"@type": "Brand", "name": it['m']}, "image": it['img'], "mpn": cod,
            "offers": {"@type": "Offer", "priceCurrency": "BRL", "availability": "https://schema.org/InStock", "url": it['url'],
                       "itemCondition": "https://schema.org/NewCondition", "seller": {"@type": "Organization", "name": "SULLAB"}, "hasMerchantReturnPolicy": RETURN}}
    bc = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Início", "item": SITE + "/"},
        {"@type": "ListItem", "position": 2, "name": catn, "item": f'{SITE}/categoria/{cats}.html'},
        {"@type": "ListItem", "position": 3, "name": n, "item": it['url']}]}
    img, imgw = it['img'], it['imgw']
    gal = (f'<div class="gal"><div class="ph" id="ph" style="background-image:url(\'{img}\');background-image:image-set(url(\'{imgw}\') type(\'image/webp\'),url(\'{img}\') type(\'image/jpeg\'))"></div>'
           f'<div class="th"><button type="button" class="on" aria-label="Foto do produto" '
           f'onclick="var p=document.getElementById(\'ph\');p.style.backgroundImage=&quot;url(\'{img}\')&quot;;var b=this.parentNode.children;for(var i=0;i<b.length;i++)b[i].className=\'\';this.className=\'on\'">'
           f'<img decoding="async" src="{imgw}" alt="Foto do produto" loading="lazy" width="1240" height="1240"></button></div></div>')
    tabela = '<table class="ft">' + ''.join(f'<tr><th>{html.escape(t)}</th><td>{html.escape(v)}</td></tr>' for t, v in it['spec']) + '</table>'
    difs = '<ul class="dif">' + ''.join(f'<li>{html.escape(x)}</li>' for x in it['dif']) + '</ul>'
    descs = ''.join(f'<p class="lead">{html.escape(x)}</p>' for x in it['desc'])
    preco_html = f'<div class="preco">{html.escape(COMODATO)}</div>'
    botoes = f'<a class="btn-whats" href="{SITE}/?proposta={cod}" target="_blank" rel="noopener">📄 Solicitar proposta</a>'
    rel = ''.join(card(o) for o in ITENS if o is not it)
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
{STYLE.replace('%COD%', cod).replace('</style>', EXTRA + '</style>')}</head><body>
<div class="wrap">
<div class="top"><img src="{SITE}/img/sullab-topo.webp" alt="SULLAB" width="65" height="34"><a href="{SITE}/">SULLAB</a></div>
<div class="crumb"><a href="{SITE}/">Início</a> › <a href="{SITE}/categoria/{cats}.html">{catn}</a> › {ne}</div>
<div class="card">
{gal}
<div>
<h1>{ne}</h1>
<div class="brand"><b>Marca:</b> {html.escape(it['m'])} · <b>Código:</b> {cod}</div>{preco_html}<div class="tb"><span>📄 Comodato ou aluguel</span><span>🔧 Assistência técnica</span></div><p class="tipo">{html.escape(it['tipo'])}</p>
{botoes}
<div>
<a class="btn2" href="{SITE}/categoria/{cats}.html">Ver {catn}</a>
</div>

</div></div>
<h2>Descrição</h2>{descs}<h2>Diferenciais</h2>{difs}<h2>Ficha técnica completa</h2>{tabela}
<h2>Outros equipamentos</h2><div class="rel rcards">
{rel}
</div>
{FOOT}'''
for it in ITENS:
    open(R + 'p/' + it['slug'] + '.html', 'w', encoding='utf-8').write(pagina(it))

# ---- páginas de categoria (modelo: agulhas.html)
ag = open(R + 'categoria/agulhas.html', encoding='utf-8').read()
head_style = ag[ag.find('<style>'):ag.find('</head>')]
foot = ag[ag.find('<footer class="siteftr">'):]
for k, (nome, slug, ic, lead) in CATS.items():
    lista = [it for it in ITENS if it['k'] == k]
    URLC = f'{SITE}/categoria/{slug}.html'
    grid = '\n'.join(f'<a href="{it["url"]}"><span class="nm">{html.escape(it["nome"][:80])}</span><span class="prc">Comodato / aluguel →</span><span class="cs">cód. {it["cod"]}</span></a>' for it in lista)
    faq = [("Como é o fornecimento desses aparelhos?", "Os analisadores são fornecidos em comodato ou aluguel, mediante contrato, com as condições combinadas junto com o fornecimento dos reagentes."),
           ("Vocês fornecem os reagentes e a assistência técnica?", "Sim. A SULLAB fornece os reagentes e soluções e conta com equipe técnica de manutenção de analisadores de bioquímica e hematologia."),
           ("Como peço uma proposta?", "Abra o aparelho desejado e clique em Solicitar proposta. A equipe responde pelo WhatsApp.")]
    faq_ld = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faq]}
    bc_ld = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [{"@type": "ListItem", "position": 1, "name": "Início", "item": SITE + "/"}, {"@type": "ListItem", "position": 2, "name": nome, "item": URLC}]}
    il_ld = {"@context": "https://schema.org", "@type": "ItemList", "itemListElement": [{"@type": "ListItem", "position": i + 1, "url": it['url'], "name": it['nome']} for i, it in enumerate(lista)]}
    TIT = f'{nome}: comodato e aluguel | SULLAB'
    corpo = f'''<!DOCTYPE html><html lang="pt-BR"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(TIT)}</title>
<meta name="description" content="{html.escape(lead)}">
<link rel="canonical" href="{URLC}">
<meta name="robots" content="index,follow">
<meta property="og:type" content="website"><meta property="og:title" content="{html.escape(TIT)}">
<meta property="og:description" content="{html.escape(lead)}">
<meta property="og:url" content="{URLC}">
<script type="application/ld+json">{json.dumps(bc_ld, ensure_ascii=False)}</script>
<script type="application/ld+json">{json.dumps(faq_ld, ensure_ascii=False)}</script>
<script type="application/ld+json">{json.dumps(il_ld, ensure_ascii=False)}</script>
{head_style}</head><body>
<div class="wrap">
<div class="top"><img src="{SITE}/img/sullab-topo.webp" alt="SULLAB" width="65" height="34"><a href="{SITE}/">SULLAB</a></div>
<div class="crumb"><a href="{SITE}/">Início</a> › {nome}</div>
<h1>{nome}</h1>
<p class="lead">{html.escape(lead)} A SULLAB é distribuidora de produtos para laboratório e diagnóstico clínico, com assistência técnica e fornecimento de reagentes.</p>
<a class="btn" href="{SITE}/?cat={k}">Ver na loja →</a><div class="tb"><span>📄 Comodato ou aluguel</span><span>🔧 Assistência técnica</span><span>🧪 Reagentes e soluções</span></div>
<h2>{nome} ({len(lista)})</h2>
<div class="grid">
{grid}
</div>
<h2>Perguntas frequentes</h2><div class="faq">{''.join(f'<details><summary>{html.escape(q)}</summary><p>{html.escape(a)}</p></details>' for q, a in faq)}</div>
{foot}'''
    open(R + f'categoria/{slug}.html', 'w', encoding='utf-8').write(corpo)

# ---- sitemaps
sp = R + 'sitemap-produtos.xml'; s = open(sp, encoding='utf-8').read()
s = s.replace('</urlset>', ''.join(f'<url><loc>{it["url"]}</loc><lastmod>{HOJE}</lastmod><changefreq>weekly</changefreq></url>\n' for it in ITENS if it['url'] not in s) + '</urlset>', 1)
open(sp, 'w', encoding='utf-8').write(s)
sc = R + 'sitemap-categorias.xml'; s = open(sc, encoding='utf-8').read()
add = ''.join(f'<url><loc>{SITE}/categoria/{v[1]}.html</loc><lastmod>{HOJE}</lastmod><changefreq>weekly</changefreq></url>\n' for v in CATS.values() if f'/categoria/{v[1]}.html' not in s)
open(sc, 'w', encoding='utf-8').write(s.replace('</urlset>', add + '</urlset>', 1))
print('ok:', ', '.join(it['cod'] for it in ITENS))
