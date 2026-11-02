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
COMODATO = 'Aparelho fornecido em comodato ou aluguel, mediante contrato — sem preço de tabela. Peça uma proposta que combinamos as condições, o fornecimento dos reagentes e a instalação.'

CATS = {
 'eqbioq': ('Equipamentos de bioquímica', 'equipamentos-de-bioquimica', '🧪',
            'Analisadores automáticos de bioquímica e analisador de eletrólitos (íons) para laboratório clínico, em comodato ou aluguel mediante contrato.'),
 'eqhemat': ('Equipamentos de hematologia', 'equipamentos-de-hematologia', '🩸',
            'Analisadores hematológicos de 5 partes (hemograma completo com diferencial) para laboratório clínico, em comodato ou aluguel mediante contrato.'),
 'eqvet': ('Equipamentos veterinários', 'equipamentos-veterinarios', '🐾',
            'Analisador de hematologia veterinário para clínicas e laboratórios veterinários, em comodato ou aluguel mediante contrato.'),
}
ITENS = [
 {'cod': 'EXC400', 'k': 'eqbioq', 'm': 'Zybio', 'foto': 'equip_EXC400b.png',
  'nome': 'Analisador automático de bioquímica EXC 400 — 400 testes/h, Zybio',
  'slug': 'analisador-automatico-de-bioquimica-exc-400-zybio-exc400',
  'ficha': ['Analisador químico automatizado de chão para rotina de médio e grande porte',
            'Rendimento constante de 400 testes por hora, com prioridade para amostras STAT durante a rotina',
            '80 posições de reagente com refrigeração ininterrupta 24 h; 100 posições de amostra, incluindo 5 de emergência',
            'Volume de reação de 90 a 450 µL; consumo de água de até 20 L/h',
            '12 comprimentos de onda (340 a 800 nm); lâmpada halógena de tungstênio com cerca de 2.000 h de uso',
            'Metodologias: ponto final, tempo fixo e cinética; calibração de um ponto, dois pontos e multipontos',
            'Pré-aquecimento e limpeza automáticos; cubeta de quartzo opcional para uso prolongado',
            'Interface LIS bidirecional; impressão automática dos resultados; sistema Windows 10',
            'Marca: Zybio · Modelo: EXC 400'],
  'kw': 'analisador automatico bioquimica exc 400 exc400 zybio equipamento aparelho 400 testes hora comodato aluguel bioquimico',
  'sobre': 'O EXC 400 é um analisador químico automatizado de chão que executa 400 testes por hora e combina funções avançadas e versáteis para testes de alta qualidade, com tempo de resposta menor e custo operacional reduzido. Tem 80 posições de reagente refrigeradas, volume de aspiração reduzido para reagente e amostra, economia de água e interface LIS bidirecional. Indicado para laboratórios de médio e grande porte.'},
 {'cod': 'EXC200', 'k': 'eqbioq', 'm': 'Zybio', 'foto': 'equip_EXC200.png',
  'nome': 'Analisador automático de bioquímica EXC 200 — até 240 testes/h, Zybio',
  'slug': 'analisador-automatico-de-bioquimica-exc-200-zybio-exc200',
  'ficha': ['Analisador automático de bioquímica compacto para laboratórios de pequeno e médio porte',
            'Rendimento de até 240 testes por hora; bioquímica e turbidimetria',
            'Tela sensível ao toque colorida, com menu de navegação intuitivo e sistema operacional integrado',
            'Volume de reação de 90 µL; consumo de água inferior a 5 L/h; absorção de reagente com passo de 0,5 µL',
            'Cubeta de quartzo permanente e semipermanente; lavagem das cubetas em 6 etapas',
            'Resfriamento ininterrupto de 24 h dos reagentes; carry-over de 0,005%',
            'Sonda com detecção de nível de líquido, ajuste automático de profundidade e proteção contra colisão',
            'Leitura de absorbância com linearidade de 0 a 4,0 Abs; interface LIS bidirecional',
            'Marca: Zybio · Modelo: EXC 200'],
  'kw': 'analisador automatico bioquimica exc 200 exc200 zybio equipamento aparelho 240 testes hora compacto comodato aluguel bioquimico turbidimetria',
  'sobre': 'O EXC 200 é um analisador automático de bioquímica pequeno no tamanho e grande na eficiência: rende até 240 testes por hora, com tela sensível ao toque e interface LIS bidirecional. Volume de reação baixo (90 µL) e menor consumo de água resultam em economia. Resfriamento de 24 horas mantém os reagentes em boas condições. Ideal para pequenos e médios laboratórios.'},
 {'cod': 'EHC120', 'k': 'eqbioq', 'm': 'Equip Bio', 'foto': 'equip_EHC120.png',
  'nome': 'Analisador automático de bioquímica EHC-120 — até 130 testes/h, Equip Bio',
  'slug': 'analisador-automatico-de-bioquimica-ehc-120-equip-bio-ehc120',
  'ficha': ['Analisador automático de bioquímica compacto, para pequenos e médios laboratórios',
            'Capacidade de até 130 testes por hora',
            'Compartimento refrigerado para reagentes, com 20 a 40 posições; amostras e reagentes com posições adaptáveis',
            'Cubeta de reação com função especial de transmissão ultravioleta; 60 cubetas',
            '8 comprimentos de onda; lâmpada halógena de tungstênio',
            'Ajuste automático da profundidade da sonda e proteção contra colisão da sonda de detecção de nível',
            'Sistema espectrométrico de matriz totalmente selado; tela sensível ao toque integrada',
            'Interface Bi-LIS; leitor de código de barras opcional',
            'Marca: Equip Bio · Modelo: EHC-120'],
  'kw': 'analisador automatico bioquimica ehc 120 ehc120 equip bio equipamento aparelho 130 testes hora compacto comodato aluguel bioquimico',
  'sobre': 'O EHC-120 é um analisador automático de bioquímica preciso, compacto e estável, com capacidade de até 130 testes por hora. Compartimento refrigerado para reagentes, posições de amostra e reagente adaptáveis, sistema espectrométrico totalmente selado e tela sensível ao toque com interface Bi-LIS. Indicado para pequenos e médios laboratórios.'},
 {'cod': 'XI921', 'k': 'eqbioq', 'm': 'Equip Ion', 'foto': 'equip_XI921.png',
  'nome': 'Analisador eletrolítico XI-921 — Na, K, Cl, Ca e pH, Equip Ion',
  'slug': 'analisador-eletrolitico-xi-921-equip-ion-xi921',
  'ficha': ['Analisador eletrolítico por eletrodo íon seletivo (medição direta)',
            'Mede sódio (Na⁺), potássio (K⁺), cloreto (Cl⁻), cálcio (Ca²⁺) e pH',
            'Amostras: soro, plasma, sangue total e urina diluída',
            'Calibração, pipetagem de amostra e limpeza da agulha automáticas',
            'Ampla tela sensível ao toque; impressora térmica interna; porta serial RS-232',
            'Carregador automático de amostras opcional, com 26 posições (2 de emergência)',
            'Leitor de código de barras opcional para identificação das amostras',
            'Disponível com e sem carregador automático',
            'Marca: Equip Ion · Modelo: XI-921'],
  'kw': 'analisador eletrolitico xi 921 xi921 equip ion eletrólitos ions sodio potassio cloreto calcio ph eletrodo seletivo comodato aluguel',
  'sobre': 'O XI-921 é um analisador eletrolítico compacto, eficiente e fácil de usar, com excelente precisão e confiabilidade, alta performance, baixo custo de manutenção e eletrodos altamente duráveis. A calibração, a pipetagem da amostra e a limpeza da agulha são automáticas. Pode ser equipado com carregador automático de amostras e leitor de código de barras.'},
 {'cod': 'Z50', 'k': 'eqhemat', 'm': 'Zybio', 'foto': 'equip_Z50_ok.png',
  'nome': 'Analisador hematológico Z50 — 5 partes (5-diff), Zybio',
  'slug': 'analisador-hematologico-z50-5-partes-zybio-z50',
  'ficha': ['Analisador hematológico automático de 5 partes (hemograma completo com diferencial de 5 partes)',
            'CBC + 5 DIFF com 25 parâmetros relatáveis e 4 parâmetros de pesquisa',
            '2 histogramas (RBC e PLT), 1 diagrama de dispersão 2D (WBC/BASO) e 1 diagrama 3D para diferenciação dos leucócitos',
            'Dispersão a laser em 3 ângulos e citometria de fluxo; impedância para contagem de WBC/BASO, RBC e PLT',
            'Apenas 18 µL de sangue total venoso ou capilar por exame',
            'Três reagentes no modo CBC + DIFF; 2 lises embutidos; sistema hidráulico otimizado',
            'Mais de 20 sinalizadores inteligentes para alterações e morfologia anormal das células',
            'Tela sensível ao toque de alta definição; design compacto',
            'Marca: Zybio · Modelo: Z50'],
  'kw': 'analisador hematologico z50 zybio hemograma 5 partes 5 diff contador hematologico equipamento aparelho hematologia comodato aluguel',
  'sobre': 'O Z50 é um analisador de hematologia de 5 partes de design compacto, que usa dispersão a laser em três ângulos e citometria de fluxo para a diferenciação dos leucócitos, mesmo em amostras com eosinofilia alta. Com apenas 18 µL de sangue e três reagentes no modo CBC + DIFF, oferece bom desempenho para laboratórios de pequeno e médio porte.'},
 {'cod': 'EXZ6000', 'k': 'eqhemat', 'm': 'Zybio', 'foto': 'equip_EXZ6000.png',
  'nome': 'Analisador hematológico EXZ 6000 com carregador automático, Zybio',
  'slug': 'analisador-hematologico-exz-6000-carregador-automatico-zybio-exz6000',
  'ficha': ['Analisador hematológico automatizado de 5 partes, com carregador automático de até 50 tubos de amostra',
            '29 parâmetros, 5 diagramas de dispersão e 3 histogramas',
            'Citometria de fluxo com tecnologia de dispersão a laser',
            'Apenas 20 µL de sangue total, inclusive em tubo fechado com o carregador automático',
            'Rendimento de até 90 amostras por hora no modo CBC',
            'Linearidade de WBC de 500,00 ×10⁹/L e de PLT de 5000 ×10⁹/L',
            'Tela sensível ao toque de 12,1 polegadas; valores-alvo de CQ importados via pendrive (USB)',
            'Informações do reagente carregadas automaticamente por radiofrequência (RF)',
            'Marca: Zybio · Modelo: EXZ 6000'],
  'kw': 'analisador hematologico exz 6000 exz6000 zybio hemograma carregador automatico 5 partes contador hematologico equipamento hematologia comodato aluguel',
  'sobre': 'O EXZ 6000 é um analisador hematológico automatizado com carregador automático que processa até 50 tubos por vez, consumindo apenas 20 µL de sangue total em tubo fechado. Mede 29 parâmetros com citometria de fluxo e dispersão a laser. Ideal para laboratórios de médio e grande porte e aplicável ao atendimento pediátrico.'},
 {'cod': 'Z4VET', 'k': 'eqvet', 'm': 'Zybio', 'foto': 'equip_Z4VET.png',
  'nome': 'Analisador de hematologia veterinário Z4 VET — 4 diff, Zybio',
  'slug': 'analisador-de-hematologia-veterinario-z4-vet-4-diff-zybio-z4vet',
  'ficha': ['Analisador de hematologia veterinário compacto de 4 partes (4 diff)',
            '23 parâmetros e 4 histogramas (RBC, PLT, WBC e EOS)',
            'Princípio de impedância (Coulter) com algoritmo para medição de eosinófilos, sem reagente extra',
            'Até 60 amostras por hora; apenas 10 µL de sangue total',
            'Cães, gatos, hamster, porquinho-da-índia, vaca, ovelha, coelho, vison, porco e alpaca',
            'Tela sensível ao toque colorida de 10,4 polegadas; impressora térmica integrada ou externa opcional',
            'Armazenamento de mais de 100.000 resultados; portas USB e rede',
            'Lise integrado; manutenção simples, com limpeza de sonda e desentupimento automáticos',
            'Marca: Zybio · Modelo: Z4 VET'],
  'kw': 'analisador hematologia veterinario z4 vet z4vet zybio hemograma animais cao gato clinica veterinaria 4 diff contador equipamento comodato aluguel',
  'sobre': 'O Z4 VET é um analisador de hematologia compacto e poderoso, com 4 diff, 23 parâmetros e 4 histogramas, adaptado para pequenos laboratórios e clínicas veterinárias e como máquina de backup para hospitais veterinários de médio e grande porte. Banco de dados com limites de referência de diversas espécies e alertas para resultados anormais.'},
]
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
    kw[it['cod']] = it['kw']; ft[it['cod']] = ' · '.join(x.rstrip('.') + '.' for x in it['ficha'])
json.dump(kw, open(R + 'kw.json', 'w', encoding='utf-8'), ensure_ascii=False, separators=(',', ':'))
json.dump(ft, open(R + 'ft.json', 'w', encoding='utf-8'), ensure_ascii=False, separators=(',', ':'))
info = {p['c']: p for p in seed}

# ---- páginas de produto
tpl = open(R + 'p/escalpe-para-coleta-de-sangue-a-vacuo-21g-com-tubo-de-7-ev21.html', encoding='utf-8').read()
STYLE = tpl[tpl.find('<style>'):tpl.find('</head>')].replace("item_id:'EV21'", "item_id:'%COD%'")
FOOT = tpl[tpl.find('<footer class="siteftr">'):]
RETURN = {"@type": "MerchantReturnPolicy", "applicableCountry": "BR", "returnPolicyCategory": "https://schema.org/MerchantReturnFiniteReturnWindow",
          "merchantReturnDays": 7, "returnMethod": "https://schema.org/ReturnByMail", "returnFees": "https://schema.org/FreeReturn",
          "refundType": "https://schema.org/FullRefund", "merchantReturnLink": SITE + "/trocas-e-devolucoes.html"}
def card(o):
    n = html.escape(o['nome'])
    return f'<a class="rc" href="{o["url"]}"><img src="{o["img"]}" alt="{n}" loading="lazy" width="160" height="160"><span class="rn">{n}</span><b class="rp sc">Sob consulta</b><span class="rv">Ver produto</span></a>'
def pagina(it):
    cod, n = it['cod'], it['nome']; ne = html.escape(n)
    catn, cats = it['cat'][0], it['cat'][1]
    titulo = f'{n} | SULLAB'
    desc = f'{n}. {COMODATO}'
    de = html.escape(desc)
    fdesc = ' · '.join(x.rstrip('.') + '.' for x in it['ficha'])
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
    ficha = '<br>'.join(html.escape(x.rstrip('.') + '.') for x in it['ficha'])
    preco_html = f'<div class="preco">{html.escape(COMODATO)}</div>'
    botoes = f'<a class="btn-whats" href="{SITE}/?orcar={cod}" target="_blank" rel="noopener">📄 Pedir orçamento</a>'
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
{STYLE.replace('%COD%', cod)}</head><body>
<div class="wrap">
<div class="top"><img src="{SITE}/img/sullab-topo.webp" alt="SULLAB" width="65" height="34"><a href="{SITE}/">SULLAB</a></div>
<div class="crumb"><a href="{SITE}/">Início</a> › <a href="{SITE}/categoria/{cats}.html">{catn}</a> › {ne}</div>
<div class="card">
{gal}
<div>
<h1>{ne}</h1>
<div class="brand"><b>Marca:</b> {html.escape(it['m'])} · <b>Código:</b> {cod}</div>{preco_html}<div class="tb"><span>📄 Comodato ou aluguel</span><span>🔧 Assistência técnica</span></div><div class="ficha">🔬 <b>Ficha técnica</b><br>{ficha}</div>
{botoes}
<div>
<a class="btn2" href="{SITE}/categoria/{cats}.html">Ver {catn}</a>
</div>

</div></div>
<h2>Sobre o produto</h2><p class="lead">{html.escape(it['sobre'])}</p>
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
    grid = '\n'.join(f'<a href="{it["url"]}"><span class="nm">{html.escape(it["nome"][:80])}</span><span class="prc">Sob consulta →</span><span class="cs">cód. {it["cod"]}</span></a>' for it in lista)
    faq = [("Esses aparelhos são vendidos?", "Trabalhamos com os analisadores em comodato ou aluguel, mediante contrato. Não há preço de tabela: as condições são combinadas com o laboratório, junto com o fornecimento dos reagentes."),
           ("Vocês fornecem os reagentes e a assistência técnica?", "Sim. A SULLAB fornece os reagentes e soluções e conta com equipe técnica de manutenção de analisadores de bioquímica e hematologia."),
           ("Como peço uma proposta?", "Abra o aparelho desejado e clique em Pedir orçamento. A equipe responde pelo WhatsApp.")]
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
