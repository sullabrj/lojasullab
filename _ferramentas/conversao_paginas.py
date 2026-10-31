#!/usr/bin/env python3
"""Rodada de conversão (31/10/2026) nas páginas estáticas /p/ e /categoria/.

Idempotente: pode rodar de novo depois de qualquer outro script que regere as páginas.
  python3 _ferramentas/conversao_paginas.py

O que faz:
  /p/  · "Comprar agora" soma ao carrinho (&add=1) e troca "Pedir orçamento" por "Comprar agora" quando o item tem preço;
       · selo de pedido mínimo (R$ 250 tubos/agulhas Vacuette; R$ 150 testes rápidos e refrigerados);
       · meta description pró-compra ("Compre direto no site · Pix 5% · NF-e · frete por CEP");
       · FAQ curta (preço único, pedido mínimo, pagamento) · rodapé com contato e aviso do Pix · faixa da MOVA em uma linha;
       · reagentes químicos Biolog saem de "Descartáveis e plásticos" e vão para "Reagentes químicos P.A." (ficha com CAS/pureza).
  /categoria/ · grade refeita a partir das páginas /p/ (preço, selo de mínimo e "Comprar agora" em cada item), filtro funcionando,
       textos pró-compra, FAQ "preço único", canonical da categoria duplicada, página nova reagentes-quimicos-pa.html.

Listas de pedido mínimo: _ferramentas/pedido_minimo_itens.json (PIX3, TR_TOP e refrigerados, extraídos da loja).
"""
import glob
import html
import json
import os
import re
import sys
from urllib.parse import quote

R = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/'
sys.path.insert(0, R + '_ferramentas')
import dados_site as ds  # noqa: E402

SITE = 'https://lojasullabrj.com.br'
SEED = ds.ler_catalogo()
PRE = ds.ler_precos()
INFO = {str(p['c']): p for p in SEED}
MIN = json.load(open(R + '_ferramentas/pedido_minimo_itens.json', encoding='utf-8'))
PIX3 = set(MIN['pix3'])
TR_TOP = set(MIN['tr_top'])
REFRIG = set(MIN['refrigerados'])

NOVA_CAT = 'reagentes-quimicos-pa'
NOVA_CAT_NOME = 'Reagentes químicos P.A.'
DESC_CAT = 'descartaveis-e-plasticos'
CHEM = re.compile(r'CAS|\bp\.?\s?a\b|pur[ií]ssim|aquos|solu[cç][aã]o|\d\s?%|\b\d+[,.]?\d*\s?[NM]\b|reativo|certificad|\bsal\b|salt\b|'
                  r'cloreto|sulfato|nitrato|[áa]cido|hidr[óo]xido|[óo]xido|carbonato|fosfato|acetato|[áa]lcool|citrato|iodeto|iodide|'
                  r'brometo|tartarato|oxalato|bicarbonato|permanganato|dicromato|cromato|tiossulfato|acetona|xilol|formol|glicerina|'
                  r'reagente|indicador|amido|dextrose|glicose|sacarose|lactose|ur[ée]ia|tamp[ãa]o|buffer|ninidrina|fenol|metanol|etanol|'
                  r'EDTA|corante|SIGMA|Benedict|Dim[ií]dio|TEMED|Tween|Vermelho|Tamponado', re.I)
NAO_CHEM = re.compile(r'Suplemento|Extrato|Bile|Deterbio|Detribio|Biodoriza|Bidoriza|Bio-Steam|Bio-Oxidase|Escala|Emuls[ãa]o|'
                      r'Lecitina|Litmus|Skim|Triptose|Gelatina|Yeast|Base Levedura|Cabo Kohle|Sais Bileares|Sais Wesson', re.I)

PIX_AVISO = 'Pix somente na chave CNPJ 32.198.434/0001-34 — nunca pedimos pagamento em outra conta.'
MOVA_LINHA = ('<div class="movaL" style="grid-column:1/-1;text-align:center;font-size:11.5px;color:#9aa7ba;padding:6px 0 0">'
              'Site criado por <a href="https://www.instagram.com/movafilms_/" target="_blank" rel="noopener" '
              'style="display:inline;color:#7a8aa0;text-decoration:underline">MOVA Films</a></div>')
FOOT_EXTRA = ('<br>📞 <a href="tel:+552433236532">(24) 3323-6532</a> · WhatsApp <a href="https://wa.me/5524988383100" '
              'target="_blank" rel="noopener">(24) 98838-3100</a> · segunda a sexta, em horário comercial · Instagram '
              '<a href="https://www.instagram.com/sullabrj/" target="_blank" rel="noopener">@sullabrj</a><br>🔒 ' + PIX_AVISO)
FAQ_PRECO_Q = 'O preço é o mesmo para empresa e pessoa física?'
FAQ_PRECO_A = ('Sim. O preço do site é único para empresa (CNPJ) e pessoa física (CPF), sem cadastro: coloque no carrinho, '
               'informe o CEP para o frete e finalize. Todo pedido sai com NF-e.')


def brl(v):
    return 'R$ ' + f'{v:,.2f}'.replace(',', 'X').replace('.', ',').replace('X', '.')


def preco(c):
    r = PRE.get(c)
    return r[1] if r and len(r) > 1 and r[1] else 0


def cod_catalogo(c):
    if c in INFO:
        return c
    if c.startswith('BIO-') and c[4:] in INFO:
        return c[4:]
    return None


def minimo(c):
    if c in PIX3:
        return 250
    if c in TR_TOP:
        return 150
    if c in REFRIG:
        return 150
    return 0


def pix_pct(c):
    return 3 if c in PIX3 else 5


def link_comprar(c):
    return f'{SITE}/?carrinho={quote(c, safe="")}:1&amp;add=1'


def selo_min_html(c, grande=False):
    m = minimo(c)
    if not m:
        return ''
    # 31/10/2026 (dono): selo curto nos cards confundia (parecia mínimo do item). Só a versão longa, na página do produto.
    if not grande:
        return ''
    txt = ('Pedido mínimo de R$ 250 somando tubos e agulhas Vacuette — pode misturar com outros itens no mesmo pedido' if m == 250
           else ('Pedido mínimo de R$ 150 somando testes rápidos — vale o total do pedido' if c in TR_TOP
                 else 'Pedido mínimo de R$ 150 em pedidos com produto refrigerado — vale o total do pedido'))
    est = ('display:inline-block;margin:2px 0 6px;background:#fff7e8;border:1px solid #f1d3a1;color:#7a4b00;border-radius:8px;'
           'padding:4px 10px;font-size:13px;font-weight:700') if grande else ''
    return f'<div class="pmin"{" style=" + chr(34) + est + chr(34) if est else ""}>📦 {txt}</div>'


def ficha_quimico(nome):
    cas = re.search(r'CAS\s*[\[\{\(]?\s*([0-9]{2,7}-[0-9]{2}-[0-9])', nome)
    pur = re.search(r'(\d+(?:[,.]\d+)?\s?%)', nome)
    grau = [g for g, rx in (('P.A.', r'\bp\.?\s?a\b'), ('puríssimo', r'pur[ií]ssim'), ('USP', r'\bUSP\b'), ('certificado', r'certificad'),
                            ('ultra-puro (biologia molecular)', r'ultra-?puro'), ('bacteriológico', r'bacteriol')) if re.search(rx, nome, re.I)]
    emb = nome.split('—')[-1].strip() if '—' in nome else ''
    linhas = ['Reagente químico para uso laboratorial.']
    if cas:
        linhas.append(f'<b>CAS:</b> {cas.group(1)}')
    if pur:
        linhas.append(f'<b>Pureza/concentração:</b> {pur.group(1)}')
    if grau:
        linhas.append('<b>Grau:</b> ' + ', '.join(grau))
    if emb:
        linhas.append(f'<b>Embalagem:</b> {html.escape(emb)}')
    linhas.append('Marca: Biolog.')
    txt_ld = ' · '.join(re.sub('<[^>]+>', '', x) for x in linhas)
    return '<br>'.join(linhas), txt_ld


# ---------------------------------------------------------------- páginas /p/
def ler_paginas():
    pags = {}
    for f in sorted(glob.glob(R + 'p/*.html')):
        t = open(f, encoding='utf-8').read()
        if len(t) < 2000:
            continue
        m = re.search(r'C[óo]digo:(?:</b>)?\s*([^<·]+?)\s*(?=<|·)', t)
        code = html.unescape(m.group(1).strip()) if m else None
        c = re.search(r'class="crumb">.*?href="[^"]*/categoria/([^"]+)\.html"', t)
        h1 = re.search(r'<h1>(.*?)</h1>', t, re.S)
        marca = re.search(r'class="brand">(?:<b>Marca:</b>)?\s*([^<·]+)', t)
        pags[f] = dict(code=code, cat=c.group(1) if c else None, nome=html.unescape(re.sub('<[^>]+>', '', h1.group(1))).strip() if h1 else '',
                       marca=(marca.group(1).strip() if marca else ''), url=SITE + '/p/' + os.path.basename(f))
    return pags


def eh_quimico(info):
    return (info['cat'] in (DESC_CAT, NOVA_CAT) and 'biolog' in info['marca'].lower()
            and CHEM.search(info['nome']) and not NAO_CHEM.search(info['nome']))


def faq_html():
    return ('<details><summary>' + FAQ_PRECO_Q + '</summary><p>' + FAQ_PRECO_A + '</p></details>'
            '<details><summary>Tem pedido mínimo?</summary><p>No site o pedido mínimo é de R$ 100. Com item refrigerado, R$ 150; '
            'com testes rápidos, R$ 150; com tubos e agulhas Vacuette, R$ 250; no boleto, R$ 400.</p></details>'
            '<details><summary>Como pago e recebo a nota fiscal?</summary><p>Pix com 5% de desconto (3% em tubos e agulhas Vacuette) '
            'ou cartão de crédito; boleto a partir de R$ 400. O frete é calculado pelo CEP no carrinho e todo pedido sai com NF-e. '
            + PIX_AVISO + '</p></details>')


def processar_p(f, info, quimicos):
    t = open(f, encoding='utf-8').read()
    o = t
    code = info['code']
    cc = cod_catalogo(code) if code else None
    pr = preco(cc) if cc else 0
    # 1) botão de compra: soma ao carrinho; "Pedir orçamento" vira "Comprar agora" quando há preço
    if cc and pr:
        t = re.sub(r'<a class="btn-whats"[^>]*>[^<]*</a>',
                   f'<a class="btn-whats" style="background:#2f9e63" href="{link_comprar(cc)}">🛒 Comprar agora</a>', t, count=1)
    # 2) selo de pedido mínimo logo depois do preço
    if cc and minimo(cc) and 'class="pmin"' not in t:
        m = re.search(r'<div class="preco"[^>]*>.*?</div>', t, re.S)
        if m:
            t = t[:m.end()] + selo_min_html(cc, True) + t[m.end():]
    t = t.replace('por embalagem · empresas (CNPJ), com NF-e', 'por embalagem · preço único para empresa e pessoa física, com NF-e')
    # 3) meta description pró-compra
    def nova_desc(d):
        d = html.unescape(d)
        if 'Compre direto no site' in d or '· NF-e · frete por CEP' in d:
            return d
        if pr:
            base = d.split(' no CNPJ')[0] if ' no CNPJ' in d else (info['nome'] + ': ' + brl(pr))
            return base.rstrip(' .') + f' · Compre direto no site · Pix {pix_pct(cc)}% · NF-e · frete por CEP.'
        base = d.split(' no CNPJ')[0] if ' no CNPJ' in d else info['nome']
        base = re.split(r'\.\s', base)[0]
        return base.rstrip(' .') + ' · NF-e · frete por CEP · entrega para todo o Brasil.'
    for attr in ('name="description"', 'property="og:description"', 'name="twitter:description"'):
        t = re.sub(r'(<meta ' + re.escape(attr) + r' content=")([^"]*)(")',
                   lambda m: m.group(1) + html.escape(nova_desc(m.group(2)), quote=True) + m.group(3), t, count=1)
    # 4) reagentes químicos Biolog: nova categoria e ficha com CAS/pureza
    if f in quimicos:
        nova = f'{SITE}/categoria/{NOVA_CAT}.html'
        velha = f'{SITE}/categoria/{DESC_CAT}.html'
        t = t.replace(f'<a href="{velha}">Descartáveis e plásticos</a> ›', f'<a href="{nova}">{NOVA_CAT_NOME}</a> ›')
        t = t.replace(f'<a class="btn2" href="{velha}">Ver Descartáveis e plásticos</a>', f'<a class="btn2" href="{nova}">Ver {NOVA_CAT_NOME}</a>')
        t = t.replace('"category": "Descartáveis e plásticos"', f'"category": "{NOVA_CAT_NOME}"')
        t = t.replace('{"@type": "ListItem", "position": 2, "name": "Descartáveis e plásticos", "item": "' + velha + '"}',
                      '{"@type": "ListItem", "position": 2, "name": "' + NOVA_CAT_NOME + '", "item": "' + nova + '"}')
        fh, fl = ficha_quimico(info['nome'])
        t = re.sub(r'(<div class="ficha">🔬 <b>Ficha técnica</b><br>)Descartável/plástico para uso laboratorial\.<br>Marca: Biolog\.(</div>)',
                   lambda m: m.group(1) + fh + m.group(2), t, count=1)
        t = t.replace('"description": "Descartável/plástico para uso laboratorial. · Marca: Biolog."', '"description": ' + json.dumps(fl, ensure_ascii=False))
        info['cat'] = NOVA_CAT
    # 5) FAQ curta (preço único, mínimo, pagamento)
    if FAQ_PRECO_Q not in t:
        if 'class="faq"' in t:
            t = t.replace('<div class="faq">', '<div class="faq"><details><summary>' + FAQ_PRECO_Q + '</summary><p>' + FAQ_PRECO_A + '</p></details>', 1)
        else:
            bloco = '<h2>Perguntas frequentes</h2><div class="faq">' + faq_html() + '</div>\n'
            k = t.find('<h2>Produtos relacionados</h2>')
            if k < 0:
                k = t.find('<footer class="siteftr">')
            if k > 0:
                t = t[:k] + bloco + t[k:]
    t = comum(t)
    t = t.replace('/pm.js?v=4', '/pm.js?v=5')
    if t != o:
        open(f, 'w', encoding='utf-8').write(t)
        return True
    return False


def comum(t):
    """Trechos comuns a /p/ e /categoria/: faixa da MOVA, rodapé com contato e link da categoria nova."""
    t = re.sub(r'(?:<!-- crédito MOVA Films -->)?<div class="mova-band".*?</a></div>', MOVA_LINHA, t, count=1, flags=re.S)
    if PIX_AVISO not in t:
        t = re.sub(r'(<div class="foot">.*?)(</div>)', lambda m: m.group(1) + FOOT_EXTRA + m.group(2), t, count=1, flags=re.S)
    lk = f'<a href="{SITE}/categoria/{DESC_CAT}.html">Descartáveis e plásticos</a>'
    k = t.find('<footer class="siteftr">')
    if k >= 0:
        ft = t[k:]
        if lk in ft and f'/categoria/{NOVA_CAT}.html">' not in ft:
            t = t[:k] + ft.replace(lk, lk + f'<a href="{SITE}/categoria/{NOVA_CAT}.html">{NOVA_CAT_NOME}</a>', 1)
    return t


# ---------------------------------------------------------------- categorias
CAT_CSS = ('.grid .it{content-visibility:auto;contain-intrinsic-size:auto 150px}.grid .it{display:flex;flex-direction:column;gap:3px;font-size:13px;background:#fff;border:1px solid #e8eef7;border-radius:9px;'
           'padding:9px 11px;line-height:1.35}.grid .it .nm{font-size:13.5px;color:#1f3a5f;line-height:1.3;text-decoration:none;font-weight:600}'
           '.grid .it .nm:hover{text-decoration:underline}.grid .it .pr{font-size:15px;font-weight:800;color:#127a2e}.grid .it .pr small{font-size:13px;'
           'color:#5a6b80;font-weight:600}.grid .it .cs{font-size:13px;color:#5a6b80}.grid .it .pmin{align-self:flex-start;background:#fff7e8;'
           'border:1px solid #f1d3a1;color:#7a4b00;border-radius:7px;padding:1px 7px;font-size:12.5px;font-weight:700}.grid .it .cpr{margin-top:auto;'
           'align-self:flex-start;background:#1f8a4c;color:#fff;text-decoration:none;font-weight:800;font-size:13.5px;padding:8px 12px;'
           'border-radius:8px}.grid .it .cpr:hover{background:#17703d}.grid .it .vp{font-size:13px;font-weight:700;color:#1f3a5f}')
FX_JS = ('<script>(function(){var fx=document.getElementById("fx");if(!fx)return;var cards=[].slice.call(document.querySelectorAll(".grid>.it"));'
         'var n=document.getElementById("fxn");function norm(s){return s.toLowerCase().normalize("NFD").replace(/[\\u0300-\\u036f]/g,"")}'
         'var idx=cards.map(function(c){return norm(c.textContent)});fx.addEventListener("input",function(){var q=norm(fx.value.trim());var v=0;'
         'cards.forEach(function(c,i){var show=!q||idx[i].indexOf(q)>-1;c.style.display=show?"":"none";if(show)v++});'
         'if(n)n.textContent=q?v+" itens encontrados":""})})();</script>')


def item_cat(info):
    cc = cod_catalogo(info['code']) if info['code'] else None
    pr = preco(cc) if cc else 0
    nome = html.escape(info['nome'])
    h = f'<div class="it"><a class="nm" href="{info["url"]}">{nome}</a>'
    if pr:
        h += f'<span class="pr">{brl(pr)} <small>· Pix {pix_pct(cc)}% off</small></span>{selo_min_html(cc)}'
    else:
        h += '<span class="vp">Preço sob consulta</span>'
    if info['code']:
        h += f'<span class="cs">cód. {html.escape(info["code"])}</span>'
    h += (f'<a class="cpr" href="{link_comprar(cc)}" rel="nofollow">🛒 Comprar agora</a>' if pr
          else f'<a class="cpr" style="background:#1f3a5f" href="{info["url"]}" aria-label="Ver produto: {nome}">Ver produto</a>')
    return h + '</div>'


def processar_cat(f, itens):
    t = open(f, encoding='utf-8').read()
    o = t
    slug = os.path.basename(f)[:-5]
    if slug == 'reagentes-bioquimica':
        # categoria duplicada: aponta o canonical para a página principal de bioquímica
        t = t.replace(f'<link rel="canonical" href="{SITE}/categoria/reagentes-bioquimica.html">',
                      f'<link rel="canonical" href="{SITE}/categoria/reagentes-de-bioquimica.html">')
    if '<div class="grid">' in t and itens:
        # mantém a ordem da grade atual e acrescenta as páginas que faltavam (por nome)
        g0 = t.index('<div class="grid">')
        g1 = t.index('\n</div>', g0) + len('\n</div>') if '\n</div>' in t[g0:] else t.index('</div>', g0) + 6
        antes = re.findall(r'href="(' + re.escape(SITE) + r'/p/[^"]+)"', t[g0:g1])
        por_url = {i['url']: i for i in itens}
        ordem = [u for u in dict.fromkeys(antes) if u in por_url]
        resto = sorted((u for u in por_url if u not in ordem), key=lambda u: (not preco(cod_catalogo(por_url[u]['code']) or ''), por_url[u]['nome'].lower()))
        lista = [por_url[u] for u in ordem + resto]
        grade = '<div class="grid">\n' + '\n'.join(item_cat(i) for i in lista) + '\n</div>'
        t = t[:g0] + grade + t[g1:]
        n = len(lista)
        t = re.sub(r'(<h2>Produtos de [^<(]*\()\d+(\)</h2>)', lambda m: m.group(1) + str(n) + m.group(2), t, count=1)
        il = {"@context": "https://schema.org", "@type": "ItemList",
              "itemListElement": [{"@type": "ListItem", "position": k + 1, "url": i['url'], "name": i['nome']} for k, i in enumerate(lista)]}
        t = re.sub(r'<script type="application/ld\+json">\{"@context": "https://schema.org", "@type": "ItemList".*?</script>',
                   lambda m: '<script type="application/ld+json">' + json.dumps(il, ensure_ascii=False) + '</script>', t, count=1, flags=re.S)
        # filtro da categoria: garante a caixa e o script (antes só 3 categorias filtravam)
        if 'id="fx"' not in t:
            t = re.sub(r'(<h2>Produtos de [^<]*</h2>)', r'\1\n<div class="fxwrap"><input id="fx" type="search" aria-label="Filtrar itens desta categoria" '
                       r'placeholder="🔍 Digite para filtrar os itens..."><p id="fxn"></p></div>', t, count=1)
        t = re.sub(r'<script>\(function\(\)\{var fx=document.getElementById\("fx"\).*?</script>\n?', '', t, flags=re.S)
        t = t.replace('</body>', FX_JS + '\n</body>', 1)
        pcts = {pix_pct(cod_catalogo(i['code']) or '') for i in lista if i['code'] and preco(cod_catalogo(i['code']) or '')}
        pixtxt = 'Pix 3%' if pcts == {3} else ('Pix 3% a 5%' if pcts == {3, 5} else 'Pix 5%')
    else:
        n = None
        pixtxt = 'Pix 5%'
    if CAT_CSS not in t:
        t = t.replace('</style>', CAT_CSS + '</style>', 1)
        if '.fxwrap' not in t:
            t = t.replace('</style>', '.fxwrap{margin:6px 0 4px}.fxwrap input{width:100%;box-sizing:border-box;padding:11px 12px;border:1px solid #cdd8e6;'
                          'border-radius:10px;font-size:16px}.fxwrap p{margin:4px 0 0;font-size:13px;color:#5a6b80}</style>', 1)

    def nova_desc(d):
        d = html.unescape(d)
        d = d.replace('Preço CNPJ, NF-e e entrega para todo o Brasil.', f'Compre direto no site · {pixtxt} · NF-e · frete por CEP.')
        if n is not None:
            d = re.sub(r'\s*\d+ itens em estoque\.', f' {n} produtos.', d)
        return d
    for attr in ('name="description"', 'property="og:description"'):
        t = re.sub(r'(<meta ' + re.escape(attr) + r' content=")([^"]*)(")',
                   lambda m: m.group(1) + html.escape(nova_desc(m.group(2)), quote=True) + m.group(3), t, count=1)
    t = t.replace('disponíveis para orçamento.', 'disponíveis para compra direta no site, com Pix, NF-e e frete calculado pelo CEP.')
    t = re.sub(r'(<a class="btn" href="[^"]*">)Ver na loja e montar orçamento →(</a>)', r'\1Comprar no site →\2', t)
    t = t.replace('<span>💰 Preço CNPJ</span>', '<span>💚 Pix com desconto</span>')
    t = t.replace('🏆 <b>Melhor preço em testes rápidos, por teste:</b>', '🏆 <b>Preço exclusivo do site em testes rápidos, por teste:</b>')
    # FAQ "preço único" (visível e no JSON-LD)
    if FAQ_PRECO_Q not in t and '<div class="faq">' in t:
        t = t.replace('<div class="faq">', '<div class="faq"><details><summary>' + FAQ_PRECO_Q + '</summary><p>' + FAQ_PRECO_A + '</p></details>', 1)

        def add_ld(m):
            d = json.loads(m.group(1))
            d['mainEntity'].insert(0, {"@type": "Question", "name": FAQ_PRECO_Q, "acceptedAnswer": {"@type": "Answer", "text": FAQ_PRECO_A}})
            return '<script type="application/ld+json">' + json.dumps(d, ensure_ascii=False) + '</script>'
        t = re.sub(r'<script type="application/ld\+json">(\{"@context": "https://schema.org", "@type": "FAQPage".*?)</script>', add_ld, t, count=1, flags=re.S)
    t = comum(t)
    if t != o:
        open(f, 'w', encoding='utf-8').write(t)
        return True
    return False


def criar_categoria_quimicos():
    """Cria categoria/reagentes-quimicos-pa.html a partir do molde da categoria de descartáveis (cabeçalho, estilo e rodapé)."""
    dest = R + f'categoria/{NOVA_CAT}.html'
    if os.path.exists(dest):
        return False
    t = open(R + f'categoria/{DESC_CAT}.html', encoding='utf-8').read()
    url = f'{SITE}/categoria/{NOVA_CAT}.html'
    titulo = 'Reagentes químicos P.A. para laboratório: compre com NF-e | SULLAB'
    desc = 'Reagentes químicos P.A., puríssimos e soluções prontas Biolog para laboratório. Compre direto no site · Pix 5% · NF-e · frete por CEP.'
    head_fim = t.index('</head>')
    estilo = re.search(r'<style>.*?</style>', t, re.S).group(0)
    rodape = t[t.index('<footer class="siteftr">'):]
    faq = [("Os reagentes vêm com número CAS e grau de pureza?",
            "Quando o fabricante informa, o número CAS e o grau (P.A., puríssimo, USP, certificado) aparecem no nome e na ficha técnica de cada produto."),
           ("Vocês emitem nota fiscal?", "Sim. Todo pedido sai com NF-e e o frete é calculado pelo CEP no carrinho."),
           ("Preciso de licença para comprar reagentes controlados?",
            "Produtos sujeitos a controle (Polícia Federal/Exército) só são vendidos com a documentação exigida; em caso de dúvida, fale com o atendimento antes de comprar.")]
    faq_ld = {"@context": "https://schema.org", "@type": "FAQPage",
              "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faq]}
    bc = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Início", "item": SITE + "/"},
        {"@type": "ListItem", "position": 2, "name": NOVA_CAT_NOME, "item": url}]}
    il = {"@context": "https://schema.org", "@type": "ItemList", "itemListElement": []}
    h = ('<!DOCTYPE html><html lang="pt-BR"><head>\n<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">\n'
         f'<title>{titulo}</title>\n<meta name="description" content="{desc}">\n<link rel="canonical" href="{url}">\n'
         '<meta name="robots" content="index,follow">\n'
         f'<meta property="og:type" content="website"><meta property="og:title" content="{titulo}">\n'
         f'<meta property="og:description" content="{desc}">\n<meta property="og:url" content="{url}">\n\n'
         f'<script type="application/ld+json">{json.dumps(bc, ensure_ascii=False)}</script>\n'
         f'<script type="application/ld+json">{json.dumps(faq_ld, ensure_ascii=False)}</script>\n'
         f'<script type="application/ld+json">{json.dumps(il, ensure_ascii=False)}</script>\n'
         + estilo + '<link rel="icon" href="/favicon.ico" sizes="any"><link rel="icon" type="image/png" sizes="48x48" href="/favicon-48.png">'
         '<link rel="icon" type="image/png" sizes="192x192" href="/favicon.png"><link rel="apple-touch-icon" href="/apple-touch-icon.png">'
         '<script defer src="/rastreio.js?v=7"></script>\n</head><body>\n<div class="wrap">\n'
         f'<div class="top"><img src="{SITE}/img/sullab-topo.webp" alt="SULLAB" width="65" height="34"><a href="{SITE}/">SULLAB</a></div>\n'
         f'<div class="crumb"><a href="{SITE}/">Início</a> › {NOVA_CAT_NOME}</div>\n<h1>{NOVA_CAT_NOME}</h1>\n'
         '<p class="lead">Reagentes químicos Biolog em grau P.A., puríssimo e analítico — sais, ácidos, indicadores, corantes e soluções prontas '
         'para uso laboratorial. Compre direto no site, com Pix, NF-e e frete calculado pelo CEP. A SULLAB é distribuidora de produtos para '
         'laboratório e diagnóstico clínico há 40 anos.</p>\n'
         '<div class="tb"><span>🧾 NF-e</span><span>💚 Pix com desconto</span><span>🚚 Envio 24h</span><span>🏭 Sem taxa de marketplace</span></div>'
         '<h2>Produtos de Reagentes químicos P.A. (0)</h2>\n<div class="grid">\n</div>\n'
         '<h2>Perguntas frequentes</h2><div class="faq">' + ''.join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q, a in faq) + '</div>\n'
         + rodape)
    open(dest, 'w', encoding='utf-8').write(h)
    return True


def sitemap_categoria():
    f = R + 'sitemap-categorias.xml'
    if not os.path.exists(f):
        return
    t = open(f, encoding='utf-8').read()
    u = f'{SITE}/categoria/{NOVA_CAT}.html'
    if u in t:
        return
    m = re.search(r'<url>\s*<loc>' + re.escape(f'{SITE}/categoria/{DESC_CAT}.html') + r'</loc>.*?</url>', t, re.S)
    if m:
        bloco = m.group(0).replace(f'{DESC_CAT}.html', f'{NOVA_CAT}.html')
        t = t.replace(m.group(0), m.group(0) + '\n' + bloco, 1)
        open(f, 'w', encoding='utf-8').write(t)


CAT_MBAR = ('<style id="mbarCss">.mbar{display:none}@media(max-width:700px){body.temCart .mbar{display:flex;position:fixed;left:0;right:0;bottom:0;z-index:70;'
            'gap:10px;align-items:center;background:#fff;border-top:1px solid #dfe6ef;padding:9px 12px calc(9px + env(safe-area-inset-bottom));'
            'box-shadow:0 -6px 18px rgba(16,32,60,.14);font-family:inherit}body.temCart{padding-bottom:70px}body.temCart .fab{bottom:80px}'
            '.mbar span{flex:1;font-size:14px;color:#1f3a5f;line-height:1.25}.mbar span small{display:block;font-size:13px;color:#5a6b80}'
            '.mbar a{background:#1f7d4c;color:#fff;font-weight:800;font-size:15px;padding:13px 18px;border-radius:11px;text-decoration:none;white-space:nowrap}}</style>')
CAT_MBAR_JS = ('<script>(function(){try{var c=JSON.parse(localStorage.getItem("sullab_cart")||"[]");if(!c.length)return;'
               'var n=c.reduce(function(s,x){return s+(x.qty||1)},0);var l="/?carrinho="+c.map(function(x){return encodeURIComponent(x.c)+":"+x.qty}).join(",");'
               'var b=document.createElement("div");b.className="mbar";b.innerHTML="<span><b>\\uD83D\\uDED2 "+n+(n===1?" item":" itens")+" no carrinho</b><small>Frete pelo CEP · NF-e</small></span><a href=\\""+l+"\\">Finalizar</a>";'
               'document.body.appendChild(b);document.body.classList.add("temCart")}catch(e){}})();</script>')


def processar_catalogo(pags):
    """catalogo.html: itens abrem a página do produto, assistência técnica só para clientes com contrato, fonte dos números do ML,
    faixa da MOVA em uma linha e barra fixa do carrinho no celular."""
    f = R + 'catalogo.html'
    t = open(f, encoding='utf-8').read()
    o = t
    url_de = {}
    for i in pags.values():
        if i['code']:
            url_de.setdefault(i['code'], i['url'])
            cc = cod_catalogo(i['code'])
            if cc:
                url_de.setdefault(cc, i['url'])

    def troca(m):
        cod = html.unescape(m.group(1))
        from urllib.parse import unquote
        cod = unquote(cod)
        u = url_de.get(cod)
        return f'href="{u}"' if u else m.group(0)
    t = re.sub(r'href="https://lojasullabrj\.com\.br/\?q=([^"]+)"', troca, t)
    t = t.replace('<li>Manutenção com equipe técnica <b>7 dias por semana, 24h</b></li>',
                  '<li>Assistência técnica própria em analisadores <b>(clientes com contrato de assistência técnica)</b></li>')
    t = t.replace('<b>suporte técnico 7 dias por semana, 24 horas</b>', '<b>assistência técnica própria (clientes com contrato)</b>')
    t = t.replace('<span>laboratórios, clínicas e hospitais<br>já atendidos</span>',
                  '<span>laboratórios atendidos<br><small>reputação pública no Mercado Livre</small></span>')
    t = t.replace('<span>pedidos faturados<br>nos últimos 12 meses</span>',
                  '<span>pedidos em 12 meses<br><small>reputação pública no Mercado Livre</small></span>')
    t = re.sub(r'(?:<!-- crédito MOVA Films -->)?<div class="mova-band".*?</a></div>',
               '<div class="movaL" style="text-align:center;font-size:11.5px;color:#9aa7ba;padding:8px 0 0">Site criado por '
               '<a href="https://www.instagram.com/movafilms_/" target="_blank" rel="noopener" style="color:#7a8aa0">MOVA Films</a></div>', t, count=1, flags=re.S)
    if 'id="mbarCss"' not in t:
        t = t.replace('</head>', CAT_MBAR + '\n</head>', 1)
        t = t.replace('</body>', CAT_MBAR_JS + '\n</body>', 1)
    if t != o:
        open(f, 'w', encoding='utf-8').write(t)
        return True
    return False


def main():
    pags = ler_paginas()
    quimicos = {f for f, i in pags.items() if eh_quimico(i)}
    mud_p = sum(processar_p(f, i, quimicos) for f, i in pags.items())
    criar_categoria_quimicos()
    # 31/10/2026: páginas duplicadas do mesmo produto (molde antigo) ficam fora das grades e do catálogo; o canonical vai para a principal
    import seo_paginas
    sec = seo_paginas.duplicados()
    pags = {f: i for f, i in pags.items() if os.path.relpath(f, R) not in sec}
    por_cat = {}
    for f, i in pags.items():
        if i['cat']:
            por_cat.setdefault(i['cat'], []).append(i)
    mud_c = 0
    for f in sorted(glob.glob(R + 'categoria/*.html')):
        mud_c += processar_cat(f, por_cat.get(os.path.basename(f)[:-5], []))
    sitemap_categoria()
    processar_catalogo(pags)
    print(f'/p/: {len(pags)} páginas, {mud_p} alteradas · reagentes químicos movidos: {len(quimicos)} · categorias alteradas: {mud_c}')
    # 31/10/2026 (check-up de SEO): migalhas, JSON-LD, Open Graph, rodapé e títulos — sempre por último, para nada ser desfeito
    seo_paginas.main()
    # 31/10/2026: ficha técnica em tabela (data/ficha.json) e galeria sem a arte, em todas as /p/
    import subprocess, sys
    subprocess.run([sys.executable, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'ficha_paginas.py')], check=True)


if __name__ == '__main__':
    main()
