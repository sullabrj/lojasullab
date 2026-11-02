# -*- coding: utf-8 -*-
"""02/11/2026 — Categorias MICROSCÓPIOS e CENTRÍFUGAS (CRAL) + preços novos (estudo de mercado de 02/11/2026).

1) Microscópios: preços novos em todos os arquivos (páginas, categorias, feed, catálogo, precos.json); saem de "Equipamentos e acessórios"
   (k 'equip' -> 'microsc') e ganham a categoria /categoria/microscopios.html.
2) Centrífugas CRALTECH: cadastro (catálogo, preços, ficha, kw, ft, páginas /p/, categoria /categoria/centrifugas.html, feed, sitemaps).
   Sem preço (sob consulta): CT-4000-220V, CT-16000, CT-16000-220V.
3) Fotos das centrífugas: link do portal da CRAL; o workflow fotos-cral.yml baixa, quadra e troca pelo arquivo local.
Idempotente. Depois: fotos (workflow), miniaturas.py, dados_site.py e o tile da home (tiles_micro_centrifugas.py).
Uso: python3 _ferramentas/adiciona_micro_centrifugas.py"""
import glob, html, json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import dados_site as ds
from dados_centrifugas import ITENS as RAW

R = ds.R
SITE = 'https://lojasullabrj.com.br'
HOJE = '2026-11-02'
IMG_CRAL = 'https://storage.googleapis.com/cv-pub-cloud/cral/imagens/produtos/%s.jpg'

# código: (custo do portal, venda nova)
MICROS = {'MICB-10': (1479.35, 2390.00), 'MICBTRI10': (2435.77, 3990.00), 'MICB100-INF': (2651.89, 4790.00), 'MICB200-INF': (3646.72, 5470.00),
          'MICBTRI100-INF': (3716.65, 6190.00), 'MICB-20': (6651.99, 13900.00), 'MIBEST': (983.35, 2090.00)}
CATS = {
 'microsc': ('Microscópios', 'microscopios', '🔬', 'Microscópios biológicos binoculares e trinoculares (óptica finita e infinita, com contraste de fase) e lupa estereoscópica para laboratório clínico, patologia, veterinária e ensino.'),
 'centrif': ('Centrífugas', 'centrifugas', '🌀', 'Centrífugas de bancada, microcentrífugas e centrífuga para microhematócrito para laboratório de análises clínicas, bancos de sangue e biologia molecular.'),
}


def brl(v):
    return 'R$ ' + f'{v:,.2f}'.replace(',', 'X').replace('.', ',').replace('X', '.')


def ponto(v):
    return f'{v:.2f}'


# ---------------------------------------------------------------- dados
ITENS = []
base = {d['cod']: d for d in RAW if 'espelho' not in d}
for d in RAW:
    it = dict(d)
    if 'espelho' in d:
        b = base[d['espelho']]
        for k in ('desc', 'dif', 'spec', 'kw'):
            it[k] = b[k]
        it['kw'] = b['kw'] + ' ' + d['cod'].lower()
    volt = it.get('volt')
    it['spec'] = [(t, v.replace('%V%', 'AC ' + volt) if volt else v) for t, v in it['spec']]
    it['m'] = 'CRAL'
    it['k'] = 'centrif'
    it['url'] = f'{SITE}/p/{it["slug"]}.html'
    it['img'] = IMG_CRAL % it['cod']
    ITENS.append(it)

# ---------------------------------------------------------------- 1) preços dos microscópios (todos os arquivos)
pre = ds.ler_precos()
trocas = []
for cod, (custo, novo) in MICROS.items():
    velho = pre[cod][0]
    if abs(velho - novo) > 0.001:
        trocas.append((brl(velho)[3:], brl(novo)[3:], ponto(velho), ponto(novo)))
        pre[cod] = [novo, novo, None]
arquivos = []
for d, _, fs in os.walk(R):
    if '/.git' in d or '/node_modules' in d or '/docs' in d:
        continue
    for f in fs:
        if f.endswith(('.html', '.xml', '.csv', '.js', '.json')) and f not in ('precos.json',):
            arquivos.append(os.path.join(d, f))
mudou = 0
for a in arquivos:
    try:
        t = open(a, encoding='utf-8').read()
    except Exception:
        continue
    o = t
    for vb, nb, vp, np_ in trocas:
        t = t.replace('R$ ' + vb, 'R$ ' + nb).replace(vb, nb) if vb in t else t
        t = t.replace(vp + ' BRL', np_ + ' BRL').replace('"price": "' + vp + '"', '"price": "' + np_ + '"')
    if t != o:
        open(a, 'w', encoding='utf-8').write(t)
        mudou += 1
print('arquivos com preço de microscópio trocado:', mudou)
for it in ITENS:
    if it['venda'] is not None:
        pre[it['cod']] = [it['venda'], it['venda'], None]
ds.gravar_precos(pre)

# ---------------------------------------------------------------- 2) catálogo
seed = ds.ler_catalogo()
cods = {p['c'] for p in seed}
for p in seed:
    if p['c'] in MICROS:
        p['k'] = 'microsc'
for it in ITENS:
    if it['cod'] not in cods:
        seed.append({'c': it['cod'], 'n': it['nome'], 'm': 'CRAL', 'k': 'centrif', 'img': it['img']})
ds.gravar_catalogo(seed)
kw = json.load(open(R + 'kw.json', encoding='utf-8'))
ft = json.load(open(R + 'ft.json', encoding='utf-8'))
fj = json.load(open(R + 'data/ficha.json', encoding='utf-8'))
for it in ITENS:
    kw[it['cod']] = it['kw']
    ft[it['cod']] = ' · '.join(t + ': ' + v for t, v in it['spec'][:8])
    fj[it['cod']] = {'rows': [[t, v] for t, v in it['spec']], 'why': it['dif'], 'desc': it['desc']}
json.dump(kw, open(R + 'kw.json', 'w', encoding='utf-8'), ensure_ascii=False, separators=(',', ':'))
json.dump(ft, open(R + 'ft.json', 'w', encoding='utf-8'), ensure_ascii=False, separators=(',', ':'))
json.dump(fj, open(R + 'data/ficha.json', 'w', encoding='utf-8'), ensure_ascii=False, separators=(',', ':'))

# ---------------------------------------------------------------- 3) páginas dos microscópios: nova categoria
ARQ_MIC = {}
for a in glob.glob(R + 'p/microscopio-*.html'):
    s = open(a, encoding='utf-8').read()
    m = re.search(r'"sku": "([^"]+)"', s)
    if m and m.group(1) in MICROS:
        ARQ_MIC[m.group(1)] = a
        i = s.find('<footer class="siteftr">')
        n = s[:i].replace('categoria/equipamentos-e-acessorios.html', 'categoria/microscopios.html').replace('Equipamentos e acessórios', 'Microscópios') + s[i:]
        if n != s:
            open(a, 'w', encoding='utf-8').write(n)
feed = open(R + 'feed-google.xml', encoding='utf-8').read()
def _feed(m):
    b = m.group(0)
    if any(f'<g:id>{c}</g:id>' in b for c in MICROS):
        b = b.replace('<g:product_type>Equipamentos e acessórios</g:product_type>', '<g:product_type>Microscópios</g:product_type>')
    return b
feed = re.sub(r'<item>.*?</item>', _feed, feed, flags=re.S)

# ---------------------------------------------------------------- 4) página de produto das centrífugas
tpl = open(ARQ_MIC['MICB-10'], encoding='utf-8').read()
STYLE = re.sub(r"item_id:'MICB-10'", "item_id:'%COD%'", tpl[tpl.find('<style>'):tpl.find('</head>')])
FOOT = tpl[tpl.find('<footer class="siteftr">'):]
EXTRA = '.ft{width:100%;border-collapse:collapse;font-size:14px;margin:6px 0 18px}.ft th{text-align:left;width:34%;background:#f1f6fa;color:#24455e;font-weight:600;vertical-align:top}.ft th,.ft td{padding:8px 10px;border-bottom:1px solid #e1e8ee}.dif{padding-left:20px;line-height:1.55}.dif li{margin:4px 0}.tipo{color:#4a5a68;margin:6px 0 10px;font-weight:600}'
RETURN = {"@type": "MerchantReturnPolicy", "applicableCountry": "BR", "returnPolicyCategory": "https://schema.org/MerchantReturnFiniteReturnWindow",
          "merchantReturnDays": 7, "returnMethod": "https://schema.org/ReturnByMail", "returnFees": "https://schema.org/FreeReturn",
          "refundType": "https://schema.org/FullRefund", "merchantReturnLink": SITE + "/trocas-e-devolucoes.html"}
FAQ = [("O preço é o mesmo para empresa e pessoa física?", "Sim. O preço do site é único para empresa (CNPJ) e pessoa física (CPF), sem cadastro: coloque no carrinho, informe o CEP para o frete e finalize. Todo pedido sai com NF-e."),
       ("Como pago e recebo a nota fiscal?", "Pix com 5% de desconto ou cartão de crédito; boleto a partir de R$ 400. O frete é calculado pelo CEP no carrinho e todo pedido sai com NF-e. Pix somente na chave CNPJ 32.198.434/0001-34 — nunca pedimos pagamento em outra conta.")]
FAQ_SC = [("Como peço o orçamento?", "Clique em Pedir orçamento: o item vai para o seu pedido e a equipe responde com o valor, o prazo e o frete pelo WhatsApp."),
          ("Todo pedido sai com nota fiscal?", "Sim. Todo pedido sai com NF-e e o frete é calculado pelo CEP.")]


def card_rel(o):
    n = html.escape(o['nome'])
    pr = f'<b class="rp">{brl(o["venda"])}</b>' if o['venda'] else '<b class="rp sc">Sob consulta</b>'
    return f'<a class="rc" href="{o["url"]}"><img src="{o["img"]}" alt="{n}" loading="lazy" width="160" height="160"><span class="rn">{n}</span>{pr}<span class="rv">Ver produto</span></a>'


def pagina(it):
    cod, n = it['cod'], it['nome']
    ne = html.escape(n)
    catn, cats = CATS['centrif'][0], CATS['centrif'][1]
    preco = it['venda']
    titulo = f'{n} | SULLAB'
    if preco:
        desc = f'{n}. {it["desc"][0][:150].rstrip()}… {brl(preco)} · Compre direto no site · Pix 5% · NF-e · frete por CEP.'
    else:
        desc = f'{n}. {it["desc"][0][:170].rstrip()}… Preço sob consulta · NF-e · frete por CEP.'
    de = html.escape(desc)
    prod = {"@context": "https://schema.org/", "@type": "Product", "name": n, "sku": cod, "category": catn, "description": ' '.join(it['desc']),
            "brand": {"@type": "Brand", "name": "CRAL"}, "image": it['img'], "mpn": cod}
    if preco:
        prod["offers"] = {"@type": "Offer", "priceCurrency": "BRL", "price": ponto(preco), "availability": "https://schema.org/InStock", "url": it['url'],
                          "itemCondition": "https://schema.org/NewCondition", "seller": {"@type": "Organization", "name": "SULLAB"}, "hasMerchantReturnPolicy": RETURN}
    bc = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Início", "item": SITE + "/"},
        {"@type": "ListItem", "position": 2, "name": catn, "item": f'{SITE}/categoria/{cats}.html'},
        {"@type": "ListItem", "position": 3, "name": n, "item": it['url']}]}
    faq = FAQ if preco else FAQ_SC
    faq_ld = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faq]}
    img = it['img']
    gal = f'<div class="gal"><div class="ph" id="ph" style="background-image:url(\'{img}\')"></div></div>'
    if preco:
        preco_html = (f'<div class="preco" style="margin:10px 0;padding:10px 12px;background:#f4f7fb;border-radius:8px;font-size:15px">💰 <b>{brl(preco)}</b> '
                      f'<span class="pfx" style="color:#5a6472;font-weight:400;font-size:13px">por unidade · empresas (CNPJ) e pessoa física, com NF-e</span><br>'
                      f'<span class="pfx" style="color:#5a6472;font-weight:400;font-size:13px">Pix com 5% de desconto. Frete calculado pelo CEP na loja.</span></div>'
                      f'<div class="tb"><span>🧾 NF-e em todo pedido</span><span>🚚 Envio em 24h</span></div>'
                      f'<a class="trocaslk" href="{SITE}/trocas-e-devolucoes.html">Ver política de trocas e devoluções</a>')
        botoes = f'<a class="btn-whats" style="background:#2f9e63" href="{SITE}/?carrinho={cod}:1&amp;add=1">🛒 Comprar agora</a><a class="btn" href="{SITE}/?q={cod}">Ver na loja →</a>'
    else:
        preco_html = ('<div class="preco" style="margin:10px 0;padding:10px 12px;background:#f4f7fb;border-radius:8px;font-size:15px">💬 <b>Preço sob consulta</b> '
                      '<span class="pfx" style="color:#5a6472;font-weight:400;font-size:13px">· peça o orçamento e a equipe responde pelo WhatsApp</span></div>'
                      '<div class="tb"><span>🧾 NF-e em todo pedido</span><span>🚚 Frete calculado pelo CEP</span></div>')
        botoes = f'<a class="btn-whats" href="{SITE}/?orcar={cod}" target="_blank" rel="noopener">📄 Pedir orçamento</a>'
    tabela = '<table class="ft">' + ''.join(f'<tr><th>{html.escape(t)}</th><td>{html.escape(v)}</td></tr>' for t, v in it['spec']) + '</table>'
    difs = '<ul class="dif">' + ''.join(f'<li>{html.escape(x)}</li>' for x in it['dif']) + '</ul>'
    descs = ''.join(f'<p class="lead">{html.escape(x)}</p>' for x in it['desc'])
    rel = ''.join(card_rel(o) for o in ITENS if o is not it and o['cod'] != it.get('espelho'))[:20000]
    faq_html = ''.join(f'<details><summary>{html.escape(q)}</summary><p>{html.escape(a)}</p></details>' for q, a in faq)
    return f'''<!DOCTYPE html><html lang="pt-BR"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(titulo)}</title>
<meta name="description" content="{de}">
<link rel="canonical" href="{it['url']}">
<meta name="robots" content="index,follow">
<meta property="og:type" content="product"><meta property="og:title" content="{html.escape(titulo)}">
<meta property="og:description" content="{de}">
<meta property="og:image" content="{img}"><meta name="twitter:card" content="summary">
<meta property="og:url" content="{it['url']}">

<script type="application/ld+json">{json.dumps(prod, ensure_ascii=False)}</script>
<script type="application/ld+json">{json.dumps(bc, ensure_ascii=False)}</script>
<script type="application/ld+json">{json.dumps(faq_ld, ensure_ascii=False)}</script>
{STYLE.replace('%COD%', cod).replace('</style>', EXTRA + '</style>', 1)}</head><body>
<div class="wrap">
<div class="top"><img src="{SITE}/img/sullab-topo.webp" alt="SULLAB" width="65" height="34"><a href="{SITE}/">SULLAB</a></div>
<div class="crumb"><a href="{SITE}/">Início</a> › <a href="{SITE}/categoria/{cats}.html">{catn}</a> › {ne}</div>
<div class="card">
{gal}
<div>
<h1>{ne}</h1>
<div class="brand"><b>Marca:</b> CRAL · <b>Código:</b> {cod}</div><p class="tipo">{html.escape(it['tipo'])}</p>{preco_html}
{botoes}
<div>
<a class="btn2" href="{SITE}/categoria/{cats}.html">Ver {catn}</a>
<a class="btn2" href="{SITE}/marca/cral.html">Ver produtos CRAL</a>
</div>

</div></div>
<h2>Descrição</h2>{descs}<h2>Diferenciais</h2>{difs}<h2>Ficha técnica completa</h2>{tabela}
<h2>Perguntas frequentes</h2><div class="faq">{faq_html}</div>
<h2>Outras centrífugas</h2><div class="rel rcards">
{rel}
</div>
{FOOT}'''


for it in ITENS:
    open(R + 'p/' + it['slug'] + '.html', 'w', encoding='utf-8').write(pagina(it))

# ---------------------------------------------------------------- 5) categorias
eq = open(R + 'categoria/equipamentos-e-acessorios.html', encoding='utf-8').read()
# 5a) tira os microscópios de "Equipamentos e acessórios"
urls_mic = [m for m in re.findall(r'https://lojasullabrj\.com\.br/p/microscopio-[a-z0-9-]+\.html', eq)]
urls_mic = sorted(set(urls_mic))
if urls_mic:
    eq = re.sub(r'<div class="it">(?:(?!</div>).)*?cód\. (?:MICB[A-Z0-9-]*|MIBEST)</span>.*?</div>\n?', '', eq, flags=re.S)
    eq = re.sub(r'<tr><td><b>Microscópio[^<]*</b></td>.*?</tr>', '', eq, flags=re.S)
    eq = eq.replace('de microscópios biológicos e estereoscópios à câmara de Neubauer', 'da câmara de Neubauer')
    for u in urls_mic:
        eq = re.sub(r', \{"@type": "ListItem", "position": \d+, "url": "' + re.escape(u) + r'", "name": "[^"]*"\}', '', eq)
        eq = re.sub(r'\{"@type": "ListItem", "position": \d+, "url": "' + re.escape(u) + r'", "name": "[^"]*"\}, ', '', eq)
    n_it = len(re.findall(r'<div class="it">', eq))
    eq = re.sub(r'(Produtos de Equipamentos e acessórios) \(\d+\)', rf'\1 ({n_it})', eq)
    open(R + 'categoria/equipamentos-e-acessorios.html', 'w', encoding='utf-8').write(eq)
    print('Equipamentos e acessórios: restam', n_it, 'itens')

eq = open(R + 'categoria/equipamentos-e-acessorios.html', encoding='utf-8').read()
HEAD_STYLE = eq[eq.find('<style>'):eq.find('</head>')]
FOOT_C = eq[eq.find('<footer class="siteftr">'):]
fx_html = '<div class="fxwrap"><input id="fx" type="search" aria-label="Filtrar itens desta categoria" placeholder="🔍 Digite para filtrar os itens..."><p id="fxn"></p></div>'

LEAD = {
 'microsc': 'Microscópios biológicos binoculares e trinoculares, de óptica finita e infinita, com versão de contraste de fase, e lupa estereoscópica 20X a 80X, todos com iluminação LED e alimentação bivolt.',
 'centrif': 'Centrífugas de bancada, microcentrífugas e centrífuga para microhematócrito, com microprocessador, motor sem escovas e travas de segurança, para laboratórios de análises clínicas e bancos de sangue.'}
FAQ_CAT = {
 'microsc': [("Qual a diferença entre óptica finita e infinita?", "Na óptica finita o tubo tem comprimento fixo e as objetivas formam a imagem direto na ocular; na infinita há uma lente de tubo, o que permite acrescentar acessórios (contraste de fase, câmera) sem perder qualidade de imagem."),
             ("Quando escolher o modelo trinocular?", "O trinocular tem uma saída extra para câmera, útil para fotografar, projetar ou gravar a lâmina; o binocular atende a rotina de bancada."),
             ("Os microscópios acompanham óleo de imersão e filtros?", "A ficha técnica de cada modelo lista o conjunto óptico; consulte a página do item e, em caso de dúvida, fale com a equipe pelo WhatsApp.")],
 'centrif': [("Qual centrífuga serve para tubos de coleta de sangue?", "As centrífugas de bancada CT-4000Y (8 tubos) e CT-4000Y12 (12 tubos) trabalham com tubos de 10 a 15 mL; para volumes maiores, o CT-4000 leva 24 tubos."),
             ("Qual a diferença entre microcentrífuga e centrífuga de bancada?", "A microcentrífuga gira microtubos de 0,2 a 2,2 mL em alta rotação (PCR, proteínas, biologia molecular); a de bancada gira tubos de 10 a 15 mL em menor rotação (soro e plasma)."),
             ("Para que serve a centrífuga de microhematócrito?", "Ela gira tubos capilares a 12.000 rpm para medir o hematócrito, a proporção de glóbulos vermelhos no sangue.")]}
FAQ_COMUM = ("O preço é o mesmo para empresa e pessoa física?", "Sim. O preço do site é único para empresa (CNPJ) e pessoa física (CPF), sem cadastro: coloque no carrinho, informe o CEP para o frete e finalize. Todo pedido sai com NF-e.")


def itens_cat(k):
    out = []
    if k == 'microsc':
        for cod, a in ARQ_MIC.items():
            s = open(a, encoding='utf-8').read()
            nome = re.search(r'<h1>(.*?)</h1>', s).group(1)
            out.append({'cod': cod, 'nome': html.unescape(nome), 'url': SITE + '/p/' + os.path.basename(a), 'venda': MICROS[cod][1]})
        out.sort(key=lambda x: x['venda'])
    else:
        out = [dict(cod=i['cod'], nome=i['nome'], url=i['url'], venda=i['venda']) for i in ITENS]
    return out


for k, (nome, slug, ic, lead0) in CATS.items():
    lista = itens_cat(k)
    URLC = f'{SITE}/categoria/{slug}.html'
    grid = []
    for o in lista:
        if o['venda']:
            grid.append(f'<div class="it"><a class="nm" href="{o["url"]}">{html.escape(o["nome"])}</a><span class="pr">{brl(o["venda"])} <small>· Pix 5% off</small></span><span class="cs">cód. {o["cod"]}</span>'
                        f'<a class="cpr" href="{SITE}/?carrinho={o["cod"]}:1&amp;add=1" rel="nofollow">🛒 Comprar agora</a></div>')
        else:
            grid.append(f'<div class="it"><a class="nm" href="{o["url"]}">{html.escape(o["nome"])}</a><span class="pr">Preço sob consulta</span><span class="cs">cód. {o["cod"]}</span>'
                        f'<a class="cpr" href="{SITE}/?orcar={o["cod"]}" rel="nofollow">📄 Pedir orçamento</a></div>')
    faq = [FAQ_COMUM] + FAQ_CAT[k]
    faq_ld = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faq]}
    bc_ld = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [{"@type": "ListItem", "position": 1, "name": "Início", "item": SITE + "/"}, {"@type": "ListItem", "position": 2, "name": nome, "item": URLC}]}
    il_ld = {"@context": "https://schema.org", "@type": "ItemList", "itemListElement": [{"@type": "ListItem", "position": i + 1, "url": o['url'], "name": o['nome']} for i, o in enumerate(lista)]}
    TIT = f'{nome}: preço CNPJ e NF-e | SULLAB'
    DESC = f'{LEAD[k]} Preço para CNPJ, NF-e e entrega para todo o Brasil.'
    corpo = f'''<!DOCTYPE html><html lang="pt-BR"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(TIT)}</title>
<meta name="description" content="{html.escape(DESC)}">
<link rel="canonical" href="{URLC}">
<meta name="robots" content="index,follow">
<meta property="og:type" content="website"><meta property="og:title" content="{html.escape(TIT)}">
<meta property="og:description" content="{html.escape(DESC)}">
<meta property="og:url" content="{URLC}">
<script type="application/ld+json">{json.dumps(bc_ld, ensure_ascii=False)}</script>
<script type="application/ld+json">{json.dumps(faq_ld, ensure_ascii=False)}</script>
<script type="application/ld+json">{json.dumps(il_ld, ensure_ascii=False)}</script>
{HEAD_STYLE}
<div class="wrap">
<div class="top"><img src="{SITE}/img/sullab-topo.webp" alt="SULLAB" width="65" height="34"><a href="{SITE}/">SULLAB</a></div>
<div class="crumb"><a href="{SITE}/">Início</a> › {nome}</div>
<h1>{nome}</h1>
<p class="lead">{html.escape(LEAD[k])} A SULLAB é distribuidora de produtos para laboratório e diagnóstico clínico, com preço para CNPJ, nota fiscal (NF-e) e entrega para todo o Brasil.</p>
<a class="btn" href="{SITE}/?cat={k}">Comprar no site →</a><div class="tb"><span>🧾 NF-e</span><span>💚 Pix com desconto</span><span>🚚 Envio 24h</span><span>🏭 Sem taxa de marketplace</span></div>
<h2>{nome} ({len(lista)})</h2>
{fx_html}
<div class="grid">
{chr(10).join(grid)}
</div>
<h2>Perguntas frequentes</h2><div class="faq">{''.join(f'<details><summary>{html.escape(q)}</summary><p>{html.escape(a)}</p></details>' for q, a in faq)}</div>
{FOOT_C}'''
    open(R + f'categoria/{slug}.html', 'w', encoding='utf-8').write(corpo)

# ---------------------------------------------------------------- 6) feed do Google, sitemaps
def item_feed(it):
    n = html.escape(it['nome'])
    return (f'<item>\n<g:id>{it["cod"]}</g:id>\n<g:title>{n} — CRAL</g:title>\n<g:description>{n}. Marca CRAL. Código {it["cod"]}. {html.escape(" ".join(it["desc"]))} Produto para laboratório. Venda para empresas (CNPJ) com NF-e e entrega para todo o Brasil.</g:description>\n'
            f'<g:link>{it["url"]}</g:link>\n<g:image_link>{SITE}/img/p/{it["cod"]}.jpg</g:image_link>\n<g:condition>new</g:condition>\n<g:availability>in_stock</g:availability>\n'
            f'<g:price>{ponto(it["venda"])} BRL</g:price>\n<g:brand>CRAL</g:brand>\n<g:mpn>{it["cod"]}</g:mpn>\n<g:identifier_exists>no</g:identifier_exists>\n'
            f'<g:google_product_category>Business &amp; Industrial &gt; Science &amp; Laboratory &gt; Laboratory Equipment &gt; Centrifuges</g:google_product_category>\n<g:product_type>Centrífugas</g:product_type>\n</item>\n')
novos = ''.join(item_feed(it) for it in ITENS if it['venda'] and f'<g:id>{it["cod"]}</g:id>' not in feed)
if novos:
    feed = feed.replace('</channel>', novos + '</channel>', 1)
open(R + 'feed-google.xml', 'w', encoding='utf-8').write(feed)
sp = R + 'sitemap-produtos.xml'
s = open(sp, encoding='utf-8').read()
s = s.replace('</urlset>', ''.join(f'<url><loc>{it["url"]}</loc><lastmod>{HOJE}</lastmod><changefreq>weekly</changefreq></url>\n' for it in ITENS if it['url'] not in s) + '</urlset>', 1)
open(sp, 'w', encoding='utf-8').write(s)
sc = R + 'sitemap-categorias.xml'
s = open(sc, encoding='utf-8').read()
add = ''.join(f'<url><loc>{SITE}/categoria/{v[1]}.html</loc><lastmod>{HOJE}</lastmod><changefreq>weekly</changefreq></url>\n' for v in CATS.values() if f'/categoria/{v[1]}.html' not in s)
open(sc, 'w', encoding='utf-8').write(s.replace('</urlset>', add + '</urlset>', 1))

# ---------------------------------------------------------------- 7) Worker: frete e lucro (lucro líquido = preço x 0,8512 - custo)
wp = R + '_ferramentas/workers/sullab-api.js'
w = open(wp, encoding='utf-8').read()
if '02/11/2026 microscopios' not in w:
    frete = {it['cod']: it['frete'] for it in ITENS}
    prod = {}
    for cod, (custo, novo) in MICROS.items():
        prod[cod] = [novo, round(novo * 0.8512 - custo, 3)]
    for it in ITENS:
        if it['venda']:
            prod[it['cod']] = [it['venda'], round(it['venda'] * 0.8512 - it['custo'], 3)]
    linha = ('// 02/11/2026 microscopios (preços novos do estudo de mercado) e centrífugas CRAL: FRETE_TAB [kg,alt,larg,comp] com folga; PROD [preço, lucro líquido = preço x 0,8512 - custo]\n'
             'Object.assign(FRETE_TAB, ' + json.dumps(frete, separators=(',', ':')) + ');\n'
             'Object.assign(PROD, ' + json.dumps(prod, separators=(',', ':')) + ');\n')
    ancora = '// 31/10/2026 (estudo robô do carrinho)'
    assert ancora in w
    w = w.replace(ancora, linha + ancora, 1)
    open(wp, 'w', encoding='utf-8').write(w)
print('ok:', ', '.join(i['cod'] for i in ITENS))
