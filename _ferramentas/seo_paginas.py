#!/usr/bin/env python3
"""Ajustes de SEO nas páginas estáticas (check-up de 31/10/2026).

Idempotente: pode rodar quantas vezes quiser; o conversao_paginas.py chama este script no final.
  python3 _ferramentas/seo_paginas.py

O que faz (só cabeçalho, marcação e links — não mexe em preço, URL nem regra de negócio):
  todas · rodapé .siteftr: títulos de coluna <h6> viram <p class="sfh"> (o h6 depois de h2 quebrava a hierarquia de títulos)
          e os links ganham alvo de toque de 24 px;
        · og:url igual ao canonical; og:image padrão onde faltava; Open Graph completo nas páginas institucionais; twitter:card.
  /p/   · páginas duplicadas do mesmo produto (molde antigo, mesmo código, sem preço atualizado): canonical para a página principal,
          links internos trocados para a principal e saem do sitemap-produtos.xml (o conversao_paginas.py também as tira das grades);
        · migalha (breadcrumb) que apontava para "/?cat=..." passa a apontar para a página /categoria/ (só nas páginas principais);
        · JSON-LD: BreadcrumbList onde faltava; Offer com o preço que a página mostra onde o Product não tinha offers;
          FAQPage montado a partir das perguntas visíveis da página (sempre em sincronia com o HTML);
        · títulos repetidos entre embalagens diferentes do mesmo produto ganham a embalagem (ex.: "— 25 g").
  outras · catalogo/index.html: canonical para /catalogo.html (é a mesma página, versão antiga);
         · catalogo.html: alt das fotos de referência = legenda da foto;
         · títulos/descrições longos demais das páginas institucionais e guias (texto escrito à mão, ver TEXTOS).
  categoria duplicada reagentes-bioquimica.html · sai do rodapé; links internos vão para reagentes-de-bioquimica.html.
  sitemaps · sitemap-categorias.xml sem a categoria duplicada reagentes-bioquimica; sitemap-produtos.xml sem as páginas duplicadas.
"""
import collections
import glob
import html
import json
import os
import re

R = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/'
SITE = 'https://lojasullabrj.com.br'
OG_PADRAO = SITE + '/og-sullab.png'
IGNORAR = ('_ferramentas/', 'materiais-afiliados/', 'node_modules/', '.git/', 'img/')

# migalhas antigas (/?cat=chave) -> página de categoria
CAT_ANTIGA = {
    'bioq': ('reagentes-de-bioquimica', 'Reagentes de bioquímica'),
    'meio': ('meios-de-cultura', 'Meios de cultura'),
    'vagulha': ('agulhas', 'Agulhas'),
    'coletor': ('coletores-de-amostra', 'Coletores de amostra'),
    'lamina': ('vidraria-de-laboratorio', 'Vidraria de laboratório'),
}

# títulos e descrições escritos à mão (páginas fora do gerador de produtos): arquivo -> (title, description)
TEXTOS = {
    'index.html': (None, 'Distribuidora de produtos para laboratório: tubos a vácuo, testes rápidos, reagentes, meios de cultura '
                         'e descartáveis. Compra no site, NF-e e entrega no Brasil.'),
    'catalogo.html': (None, 'Catálogo SULLAB 2026: 371 itens de 8 marcas para análises clínicas, com preço e link de compra. '
                            'Vacuette, Newprov, Biolog, Ebram, CRAL, Cecon, DeepBlue e Zybio.'),
    'categoria/seringas-e-agulhas.html': (None, 'Seringas descartáveis Luer Slip, seringas para gasometria com heparina de lítio e '
                                                'agulhas para coleta a vácuo. NF-e e entrega para todo o Brasil.'),
    'categoria/vidraria-de-laboratorio.html': (None, 'Vidraria em borossilicato 3.3: béqueres, provetas, Erlenmeyer, balões, pipetas, '
                                                     'buretas, funis, frascos e placas de Petri. Pix 5% · NF-e · frete por CEP.'),
    'ofertas.html': (None, 'Canal da SULLAB no WhatsApp com as ofertas da semana em tubos a vácuo, agulhas, testes rápidos e '
                           'descartáveis para laboratório. Sem grupo, sem conversa.'),
    'privacidade.html': (None, 'Política de privacidade da SULLAB (LGPD): dados que coletamos no site, para que usamos, Google '
                               'Analytics e Google Ads e como exercer seus direitos.'),
    'categoria/reagentes-quimicos-pa.html': ('Reagentes químicos P.A. para laboratório com NF-e | SULLAB', None),
    'guia/como-ler-teste-rapido-linha-c-e-t.html': ('Como ler teste rápido: linha C e T | SULLAB',
                                                    'Veja como ler um teste rápido pelas linhas C (controle) e T (teste): quando o '
                                                    'resultado é positivo, negativo ou inválido, e os erros mais comuns.'),
    'guia/diferenca-tubo-edta-e-soro.html': ('Tubo EDTA ou tubo de soro: qual usar | SULLAB',
                                             'Tubo de EDTA (tampa roxa) ou tubo de soro com gel (tampa amarela)? Para que serve cada '
                                             'um, quando usar e por que não dá para trocar um pelo outro.'),
    'guia/meios-de-cultura-tsi-tioglicolato-stuart-mrvp.html': ('TSI, Tioglicolato, Stuart e MR-VP: para que servem | SULLAB',
                                                                'Para que servem o ágar TSI, o caldo tioglicolato, o meio de Stuart '
                                                                '(swab) e o caldo MR-VP na microbiologia: guia rápido da SULLAB.'),
    'guia/qual-tubo-usar-para-cada-exame.html': ('Qual tubo a vácuo usar em cada exame | SULLAB',
                                                 'Qual tubo a vácuo usar em cada exame: glicose, hemograma, coagulação, bioquímica e '
                                                 'sorologia. Tabela por cor de tampa, ordem de coleta e dicas.'),
    'devolucao.html': ('Trocas e devoluções: 7 dias para devolver | SULLAB', None),
    'trocas-e-devolucoes.html': ('Trocas e devoluções: 7 dias para devolver | SULLAB',
                                 'Trocas e devoluções na SULLAB: 7 dias para devolver com frete de volta por nossa conta, reembolso '
                                 'em até 10 dias úteis e 30 dias para defeito de fábrica.'),
    'sobre.html': ('Sobre a SULLAB: 40 anos em produtos para laboratório', None),
    'politica-de-entrega.html': ('Política de entrega: prazos, frete e envio | SULLAB', None),
    'termos.html': ('Termos de uso da loja SULLAB: compra, pagamento e NF-e',
                    'Termos de uso da loja SULLAB: cadastro, preços, pagamento (Pix, cartão em até 2x sem juros, boleto faturado), '
                    'pedido mínimo, entrega e trocas.'),
}


def ler(f):
    return open(R + f, encoding='utf-8').read()


def gravar(f, t, o):
    if t != o:
        open(R + f, 'w', encoding='utf-8').write(t)
        return True
    return False


def meta(t, attr, nome):
    m = re.search(r'<meta ' + attr + r'="' + re.escape(nome) + r'" content="([^"]*)"', t)
    return html.unescape(m.group(1)) if m else None


def set_meta(t, attr, nome, valor, depois_de=None):
    """Troca o content de uma meta existente ou insere depois da tag indicada (ou antes de </head>)."""
    esc = html.escape(valor, quote=True)
    rx = r'(<meta ' + attr + r'="' + re.escape(nome) + r'" content=")[^"]*(")'
    if re.search(rx, t):
        return re.sub(rx, lambda m: m.group(1) + esc + m.group(2), t, count=1)
    tag = f'<meta {attr}="{nome}" content="{esc}">'
    if depois_de:
        m = re.search(depois_de, t)
        if m:
            return t[:m.end()] + tag + t[m.end():]
    return t.replace('</head>', tag + '\n</head>', 1)


def canonical(t):
    m = re.search(r'<link rel="canonical" href="([^"]+)"', t)
    return m.group(1) if m else None


def ld_blocos(t):
    return list(re.finditer(r'<script type="application/ld\+json">\s*(.*?)\s*</script>', t, re.S))


def tem_tipo(t, tipo):
    for m in ld_blocos(t):
        try:
            j = json.loads(m.group(1))
        except Exception:
            continue
        if isinstance(j, dict) and j.get('@type') == tipo:
            return True
    return False


def inserir_ld(t, obj):
    s = '<script type="application/ld+json">' + json.dumps(obj, ensure_ascii=False) + '</script>\n'
    blocos = ld_blocos(t)
    if blocos:
        k = blocos[-1].end()
        return t[:k] + '\n' + s.rstrip('\n') + t[k:]
    return t.replace('</head>', s + '</head>', 1)


def texto(h):
    return html.unescape(re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', h))).strip()


CODIGO = re.compile(r'C[óo]digo:(?:</b>)?\s*([^<·]+?)\s*(?=<|·)')


def slug(s):
    return re.sub(r'[^a-z0-9]+', '-', s.lower()).strip('-')


def duplicados(paginas=None):
    """{arquivo secundário: URL da página principal} para produtos com mais de uma página /p/ (mesmo código).
    Principal = a que termina com o código no nome (molde novo, com preço e compra direta); senão, a maior."""
    por_cod = collections.defaultdict(list)
    for p in sorted(glob.glob(R + 'p/*.html')):
        f = os.path.relpath(p, R)
        t = paginas[f] if paginas and f in paginas else ler(f)
        if len(t) < 2000 or '<meta name="robots" content="noindex' in t:
            continue
        m = CODIGO.search(t)
        if m:
            por_cod[html.unescape(m.group(1).strip())].append((f, len(t)))
    sec = {}
    for cod, fs in por_cod.items():
        if len(fs) < 2:
            continue
        com_cod = [f for f, _ in fs if f.endswith('-' + slug(cod) + '.html')]
        princ = com_cod[0] if len(com_cod) == 1 else max(fs, key=lambda x: x[1])[0]
        for f, _ in fs:
            if f != princ:
                sec[f] = SITE + '/' + princ
    return sec


def links_para_principal(t, sec):
    for f, u in sec.items():
        t = t.replace(f'href="{SITE}/{f}"', f'href="{u}"').replace(f'href="/{f}"', f'href="{u}"')
    return t


# ------------------------------------------------------------------ todas as páginas
def rodape(t):
    k = t.find('<footer class="siteftr">')
    if k >= 0 and '<h6>' in t[k:]:
        t = t[:k] + t[k:].replace('<h6>', '<p class="sfh">').replace('</h6>', '</p>')
    t = t.replace('.siteftr h6{', '.siteftr .sfh{')
    # categoria duplicada (canonical em reagentes-de-bioquimica): sai do rodapé e os demais links vão direto para a principal
    t = t.replace(f'<a href="{SITE}/categoria/reagentes-bioquimica.html">Reagentes para Bioquímica Clínica</a>', '')
    t = t.replace(f'href="{SITE}/categoria/reagentes-bioquimica.html"', f'href="{SITE}/categoria/reagentes-de-bioquimica.html"')
    # alvo de toque de 24 px nos links do rodapé (auditoria target-size do Lighthouse); o espaçamento visual fica quase igual
    return t.replace('.siteftr a{display:block;font-size:12px;color:#7a8aa0;text-decoration:none;margin:0 0 5px;line-height:1.4}',
                     '.siteftr a{display:block;font-size:12px;color:#7a8aa0;text-decoration:none;margin:0;padding:4px 0;line-height:1.4}')


def open_graph(f, t):
    if '<meta name="robots" content="noindex' in t or 'http-equiv="refresh"' in t:
        return t
    can = canonical(t)
    tit = re.search(r'<title>(.*?)</title>', t, re.S)
    desc = meta(t, 'name', 'description')
    if not can or not tit:
        return t
    if meta(t, 'property', 'og:title') is None:
        t = set_meta(t, 'property', 'og:title', html.unescape(tit.group(1).strip()), r'<link rel="canonical"[^>]*>')
    if meta(t, 'property', 'og:type') is None:
        t = set_meta(t, 'property', 'og:type', 'website', r'<link rel="canonical"[^>]*>')
    if desc and meta(t, 'property', 'og:description') is None:
        t = set_meta(t, 'property', 'og:description', desc, r'<meta property="og:title"[^>]*>')
    if meta(t, 'property', 'og:url') != can:
        t = set_meta(t, 'property', 'og:url', can, r'<meta property="og:(?:description|title)"[^>]*>')
    if meta(t, 'property', 'og:image') is None:
        t = set_meta(t, 'property', 'og:image', OG_PADRAO, r'<meta property="og:url"[^>]*>')
    if meta(t, 'name', 'twitter:card') is None:
        t = set_meta(t, 'name', 'twitter:card', 'summary' if f.startswith('p/') else 'summary_large_image',
                     r'<meta property="og:image"[^>]*>')
    return t


def textos(f, t):
    if f not in TEXTOS:
        return t
    tit, desc = TEXTOS[f]
    if tit:
        t = re.sub(r'<title>.*?</title>', '<title>' + html.escape(tit, quote=False) + '</title>', t, count=1, flags=re.S)
    if desc:
        t = set_meta(t, 'name', 'description', desc)
        if meta(t, 'property', 'og:description') is not None:
            t = set_meta(t, 'property', 'og:description', desc)
    return t


# ------------------------------------------------------------------ /p/
def migalha(t):
    def troca(m):
        k = m.group(1)
        if k not in CAT_ANTIGA:
            return m.group(0)
        slug, nome = CAT_ANTIGA[k]
        return f'<a href="{SITE}/categoria/{slug}.html">{nome}</a>'
    return re.sub(r'<a href="' + re.escape(SITE) + r'/\?cat=([a-z]+)">[^<]*</a>',
                  lambda m: troca(m), t)


def breadcrumb_ld(t, url):
    if tem_tipo(t, 'BreadcrumbList'):
        return t
    m = re.search(r'<div class="crumb">(.*?)</div>', t, re.S)
    h1 = re.search(r'<h1>(.*?)</h1>', t, re.S)
    if not m or not h1:
        return t
    itens = []
    for a in re.finditer(r'<a href="([^"]+)">(.*?)</a>', m.group(1)):
        href = a.group(1)
        if '/?' in href:   # links de filtro da loja (ex.: /?cat=kit) não são páginas
            continue
        itens.append((texto(a.group(2)), href if href.startswith('http') else SITE + href))
    itens.append((texto(h1.group(1)), url))
    obj = {"@context": "https://schema.org", "@type": "BreadcrumbList",
           "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": n, "item": u} for i, (n, u) in enumerate(itens)]}
    return inserir_ld(t, obj)


def offer_ld(t, url):
    """Product sem offers: acrescenta o Offer com o preço que a própria página mostra (sem preço visível = não declara preço)."""
    for m in ld_blocos(t):
        try:
            j = json.loads(m.group(1))
        except Exception:
            continue
        if not (isinstance(j, dict) and j.get('@type') == 'Product') or j.get('offers'):
            continue
        p = re.search(r'<div class="preco"[^>]*>\s*💰\s*<b>R\$\s*([\d.]+,\d{2})</b>', t)
        if not p:
            return t
        valor = p.group(1).replace('.', '').replace(',', '.')
        if float(valor) <= 0:
            return t
        j['offers'] = {"@type": "Offer", "priceCurrency": "BRL", "price": valor,
                       "availability": "https://schema.org/InStock", "url": url,
                       "itemCondition": "https://schema.org/NewCondition", "seller": {"@type": "Organization", "name": "SULLAB"}}
        novo = '<script type="application/ld+json">' + json.dumps(j, ensure_ascii=False) + '</script>'
        return t[:m.start()] + novo + t[m.end():]
    return t


def tabela_links(t):
    """Tabelas comparativas das categorias: "Ver produto →" vira "Ver <nome do item> →" (texto de link descritivo)."""
    def troca(m):
        nome = texto(m.group(2))
        return m.group(1) + f'>Ver {html.escape(nome, quote=False)} →</a>'
    return re.sub(r'(<tr><td><b>(.*?)</b></td>(?:(?!</tr>).)*?<a href="[^"]+")>Ver produto →</a>', troca, t, flags=re.S)


def blog_breadcrumb(t, url):
    if tem_tipo(t, 'BreadcrumbList'):
        return t
    h1 = re.search(r'<h1[^>]*>(.*?)</h1>', t, re.S)
    if not h1:
        return t
    obj = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Início", "item": SITE + "/"},
        {"@type": "ListItem", "position": 2, "name": texto(h1.group(1)), "item": url}]}
    return inserir_ld(t, obj)


def faq_ld(t, sincronizar=True):
    m = re.search(r'<div class="faq">(.*?)</div>', t, re.S)
    if not m:
        return t
    qs = [(texto(q), texto(a)) for q, a in re.findall(r'<details><summary>(.*?)</summary>(.*?)</details>', m.group(1), re.S)]
    if not qs:
        return t
    obj = {"@context": "https://schema.org", "@type": "FAQPage",
           "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in qs]}
    novo = '<script type="application/ld+json">' + json.dumps(obj, ensure_ascii=False) + '</script>'
    for b in ld_blocos(t):
        try:
            j = json.loads(b.group(1))
        except Exception:
            continue
        if isinstance(j, dict) and j.get('@type') == 'FAQPage':
            return t if (j == obj or not sincronizar) else t[:b.start()] + novo + t[b.end():]
    return inserir_ld(t, obj)


def titulos_unicos(paginas):
    """Produtos com o mesmo <title> (mesmo item em embalagens diferentes): acrescenta a embalagem que está no h1."""
    por_titulo = collections.defaultdict(list)
    for f, t in paginas.items():
        if '<meta name="robots" content="noindex' in t or canonical(t) != SITE + '/' + f:
            continue
        m = re.search(r'<title>(.*?)</title>', t, re.S)
        if m:
            por_titulo[m.group(1).strip()].append(f)
    mud = {}
    for tit, fs in por_titulo.items():
        if len(fs) < 2 or not tit.endswith(' | SULLAB'):
            continue
        base = tit[:-len(' | SULLAB')]
        novos = {}
        for f in fs:
            h1 = re.search(r'<h1>(.*?)</h1>', paginas[f], re.S)
            nome = texto(h1.group(1)) if h1 else ''
            emb = nome.split('—')[-1].strip() if '—' in nome else ''
            if not emb or html.escape(emb, quote=False) in base:
                cod = re.search(r'C[óo]digo:(?:</b>)?\s*([^<·]+?)\s*(?=<|·)', paginas[f])
                emb = ('cód. ' + html.unescape(cod.group(1).strip())) if cod else ''
            novos[f] = f'{base} — {html.escape(emb, quote=False)} | SULLAB' if emb else tit
        if len(set(novos.values())) < len(novos):   # embalagem não resolveu: usa o código
            for f in fs:
                cod = re.search(r'C[óo]digo:(?:</b>)?\s*([^<·]+?)\s*(?=<|·)', paginas[f])
                if cod:
                    novos[f] = f'{base} — cód. {html.escape(html.unescape(cod.group(1).strip()), quote=False)} | SULLAB'
        for f, nt in novos.items():
            t = paginas[f]
            t = t.replace(f'<title>{tit}</title>', f'<title>{nt}</title>', 1)
            t = t.replace(f'<meta property="og:title" content="{html.escape(html.unescape(tit), quote=True)}">',
                          f'<meta property="og:title" content="{html.escape(html.unescape(nt), quote=True)}">', 1)
            mud[f] = t
    return mud


# ------------------------------------------------------------------ páginas específicas
def catalogo_alt(t):
    def troca(m):
        return m.group(1) + 'alt="' + html.escape(texto(m.group(3)), quote=True) + '"' + m.group(2) + m.group(3) + m.group(4)
    return re.sub(r'(<img [^>]*?)alt=""(>\s*</div>\s*<figcaption>)(.*?)(</figcaption>)', troca, t, flags=re.S)


def sitemap_sem_duplicada(sec):
    n = 0
    for f, urls in (('sitemap-categorias.xml', [SITE + '/categoria/reagentes-bioquimica.html']),
                    ('sitemap-produtos.xml', [SITE + '/' + s for s in sec])):
        if not os.path.exists(R + f):
            continue
        t = ler(f)
        o = t
        for u in urls:
            t = re.sub(r'\s*<url>\s*<loc>' + re.escape(u) + r'</loc>.*?</url>', '', t, flags=re.S)
        n += gravar(f, t, o)
    return n


def main():
    arqs = sorted(os.path.relpath(p, R) for p in glob.glob(R + '**/*.html', recursive=True))
    arqs = [a for a in arqs if not a.startswith(IGNORAR)]
    pags = {f: ler(f) for f in arqs}
    orig = dict(pags)
    sec = duplicados(pags)
    for f in arqs:
        t = links_para_principal(rodape(pags[f]), sec)
        if f in sec:
            t = re.sub(r'<link rel="canonical" href="[^"]*">', f'<link rel="canonical" href="{sec[f]}">', t, count=1)
            t = breadcrumb_ld(t, SITE + '/' + f)
            t = faq_ld(t)
        elif f.startswith('p/') and len(t) > 2000:
            url = canonical(t) or SITE + '/' + f
            t = migalha(t)
            t = breadcrumb_ld(t, url)
            t = offer_ld(t, url)
            t = faq_ld(t)
        elif not f.startswith('p/') and '<meta name="robots" content="noindex' not in t:
            t = tabela_links(t)
            t = faq_ld(t, sincronizar=False)
            if f.startswith('blog/'):
                t = blog_breadcrumb(t, canonical(t) or SITE + '/' + f)
        if f == 'catalogo/index.html':
            t = t.replace(f'<link rel="canonical" href="{SITE}/catalogo">', f'<link rel="canonical" href="{SITE}/catalogo.html">')
        if f in ('catalogo.html', 'catalogo/index.html'):
            t = catalogo_alt(t)
        t = textos(f, t)
        t = open_graph(f, t)
        pags[f] = t
    pags.update(titulos_unicos({f: t for f, t in pags.items() if f.startswith('p/')}))
    n = sum(gravar(f, pags[f], orig[f]) for f in arqs)
    sm = sitemap_sem_duplicada(sec)
    print(f'seo_paginas: {len(arqs)} páginas lidas, {n} alteradas · {len(sec)} páginas duplicadas de produto com canonical '
          f'para a principal' + (f' · {sm} sitemap(s) atualizado(s)' if sm else ''))


if __name__ == '__main__':
    main()
