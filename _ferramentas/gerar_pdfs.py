#!/usr/bin/env python3
"""Gera os PDFs comerciais do site da SULLAB a partir dos preços e do catálogo do site.

Uso:
    python3 _ferramentas/gerar_pdfs.py --fonte auto      # padrão
    python3 _ferramentas/gerar_pdfs.py --fonte html      # força index.html
    python3 _ferramentas/gerar_pdfs.py --fonte json      # força data/catalogo.json + data/precos.json
    python3 _ferramentas/gerar_pdfs.py --saida /tmp/x    # grava em outra pasta (teste)
    python3 _ferramentas/gerar_pdfs.py --versao "nov/2026"

Saídas (em docs/):
    Tabela_de_Precos_SULLAB.pdf                    Vacuette + testes rápidos, 1 linha por item, links
    Catalogo_SULLAB_Vacuette_e_Testes_Rapidos.pdf  o mesmo com foto pequena e descrição curta (< 1 MB)
    Catalogo_SULLAB_Completo.pdf                   todas as categorias, sem fotos, com links

Determinístico: mesmo input -> mesmo PDF (reportlab em modo invariant, sem data do dia).
O arquivo só é regravado se o conteúdo mudou.
Dependências: reportlab, qrcode, Pillow (pip install reportlab qrcode pillow).
"""
import argparse
import hashlib
import io
import json
import os
import re
import subprocess
import sys
from urllib.parse import quote

from PIL import Image as PILImage
import qrcode
from reportlab import rl_config
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_RIGHT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (BaseDocTemplate, Frame, Image, KeepTogether, PageBreak, PageTemplate,
                                Paragraph, Spacer, Table, TableStyle)

rl_config.useA85 = 0  # fluxos binários (PDF menor)
RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = 'https://lojasullabrj.com.br'

# ---------------------------------------------------------------- identidade visual (só azul)
AZUL = colors.HexColor('#1F4E79')
AZUL_CLARO = colors.HexColor('#EAF1F8')
AZUL_LINHA = colors.HexColor('#C9D8E8')
TEXTO = colors.HexColor('#1A1A1A')
CINZA = colors.HexColor('#555555')

FONTES = os.path.join(RAIZ, '_ferramentas', 'fontes')
pdfmetrics.registerFont(TTFont('Sans', os.path.join(FONTES, 'LiberationSans-Regular.ttf')))
pdfmetrics.registerFont(TTFont('Sans-Bold', os.path.join(FONTES, 'LiberationSans-Bold.ttf')))
pdfmetrics.registerFontFamily('Sans', normal='Sans', bold='Sans-Bold', italic='Sans', boldItalic='Sans-Bold')


def estilo(nome, **kw):
    base = dict(fontName='Sans', fontSize=11, leading=14.5, textColor=TEXTO)
    base.update(kw)
    return ParagraphStyle(nome, **base)


S_TIT = estilo('tit', fontName='Sans-Bold', fontSize=24, leading=29, textColor=AZUL)
S_SUB = estilo('sub', fontSize=13, leading=17, textColor=CINZA)
S_H2 = estilo('h2', fontName='Sans-Bold', fontSize=15, leading=19, textColor=AZUL, spaceBefore=6, spaceAfter=6)
S_TXT = estilo('txt', fontSize=11.5, leading=16)
S_CEL = estilo('cel', fontSize=10.5, leading=13)
S_CEL_P = estilo('celp', fontSize=9, leading=11.5, textColor=CINZA)
S_COD = estilo('cod', fontName='Sans-Bold', fontSize=9.5, leading=12, textColor=AZUL)
S_PRECO = estilo('pre', fontName='Sans-Bold', fontSize=11.5, leading=14, alignment=TA_RIGHT)
S_UNIT = estilo('uni', fontSize=9.5, leading=12, textColor=CINZA, alignment=TA_RIGHT)
S_BOT = estilo('bot', fontName='Sans-Bold', fontSize=10, leading=12, textColor=colors.white, alignment=TA_CENTER)
S_CAB = estilo('cab', fontName='Sans-Bold', fontSize=10, leading=12, textColor=colors.white)
S_CAB_R = estilo('cabr', fontName='Sans-Bold', fontSize=10, leading=12, textColor=colors.white, alignment=TA_RIGHT)
S_REGRA = estilo('regra', fontSize=11, leading=15.5, leftIndent=10, bulletIndent=0)
S_PEQ = estilo('peq', fontSize=9.5, leading=12.5, textColor=CINZA)

# ---------------------------------------------------------------- regras comerciais (iguais ao site)
CONTATO = 'comercial@sullabrj.com.br · (24) 3323-6532 · lojasullabrj.com.br'
REGRAS = [
    '<b>Preços exclusivos para compra no site</b> lojasullabrj.com.br.',
    '<b>Pix:</b> 5% de desconto (3% em tubos e agulhas Vacuette).',
    '<b>Cartão de crédito:</b> até 2x sem juros.',
    '<b>Boleto faturado em 28 ou 45 dias</b> para CNPJ, em pedidos a partir de R$ 400 (mediante análise de crédito).',
    '<b>Pedido mínimo:</b> R$ 100 (geral) · R$ 150 com item refrigerado · '
    'R$ 400 com tubos/agulhas Vacuette ou testes rápidos, ou no boleto.',
    '<b>Frete</b> calculado pelo CEP no carrinho do site.',
    '<b>NF-e</b> em todo pedido.',
]
SOBRE = ('SULLAB · 40 anos de mercado. Distribuidora com centro de distribuição e frota próprios, '
         'e assistência técnica própria em analisadores de bioquímica e hematologia para clientes com contrato.')
# Trechos que o index.html precisa conter para as regras acima continuarem iguais ao site.
CONFERE_SITE = ['até 2x sem juros', '28 ou 45 dias', 'R$ 100,00', 'R$ 150,00', 'R$ 400,00',
                '5% de desconto', '3% em tubos e agulhas Vacuette', '40 anos']


# ---------------------------------------------------------------- leitura dos dados
def _js_valor(html, nome):
    """Lê `window.NOME=...` ou `var NOME=...` (JSON) do index.html."""
    m = re.search(r'(?:window\.|var\s+)' + nome + r'\s*=\s*', html)
    if not m:
        return None
    txt = html[m.end():]
    try:
        val, _ = json.JSONDecoder().raw_decode(txt)
        return val
    except json.JSONDecodeError:
        # objetos com aspas simples (ex.: TR_TOP={'TR 017-1 RP':1,...})
        fim = {'{': '}', '[': ']'}[txt[0]]
        bloco = txt[:txt.index(fim) + 1]
        return json.loads(bloco.replace("'", '"'))


def _depts(html):
    i = html.find('var DEPTS=[')
    if i < 0:
        return []
    bloco = html[i:html.find('];', i)]
    out = []
    for key, nome, cats in re.findall(r"key:'([^']+)',\s*nome:'([^']+)'.*?cats:\[([^\]]*)\]", bloco):
        out.append({'key': key, 'nome': nome, 'cats': re.findall(r"'([^']+)'", cats)})
    return out


def _normaliza_precos(p):
    if isinstance(p, dict) and 'precos' in p and isinstance(p['precos'], dict):
        p = p['precos']
    out = {}
    for c, v in p.items():
        if isinstance(v, list):
            v = v[1] if len(v) > 1 else v[0]
        elif isinstance(v, dict):
            v = v.get('preco') or v.get('p') or v.get('v')
        out[str(c)] = float(v) if v else 0.0
    return out


def _normaliza_catalogo(cat):
    if isinstance(cat, dict):
        cat = cat.get('produtos') or cat.get('catalogo') or cat.get('itens') or []
    out = []
    for x in cat:
        out.append({'c': str(x.get('c') or x.get('codigo')), 'n': x.get('n') or x.get('nome') or '',
                    'm': x.get('m') or x.get('marca') or '', 'k': x.get('k') or x.get('categoria') or '',
                    'img': x.get('img') or x.get('imagem') or '', 'q': x.get('q') or x.get('qtd')})
    return out


def carregar(fonte):
    html_path = os.path.join(RAIZ, 'index.html')
    html = open(html_path, encoding='utf-8').read() if os.path.exists(html_path) else ''
    jcat, jpre = os.path.join(RAIZ, 'data', 'catalogo.json'), os.path.join(RAIZ, 'data', 'precos.json')
    tem_json = os.path.exists(jcat) and os.path.exists(jpre)
    if fonte == 'json' and not tem_json:
        sys.exit('ERRO: --fonte json, mas data/catalogo.json e data/precos.json não existem')
    usar_json = fonte == 'json' or (fonte == 'auto' and tem_json)
    if usar_json:
        catalogo = _normaliza_catalogo(json.load(open(jcat, encoding='utf-8')))
        precos = _normaliza_precos(json.load(open(jpre, encoding='utf-8')))
        arquivos = [jcat, jpre]
        origem = 'data/catalogo.json + data/precos.json'
    else:
        if not html:
            sys.exit('ERRO: index.html não encontrado')
        catalogo = _normaliza_catalogo(_js_valor(html, 'SEED') or [])
        precos = _normaliza_precos(_js_valor(html, 'PRECOS') or {})
        arquivos = [html_path]
        origem = 'index.html (window.PRECOS + SEED)'
    qtd = {}
    jq = os.path.join(RAIZ, 'data', 'qtd.json')
    if usar_json and os.path.exists(jq):
        qtd = json.load(open(jq, encoding='utf-8'))
    elif html:
        qtd = _js_valor(html, 'QTD') or {}
    for x in catalogo:
        if x.get('q') and x['c'] not in qtd:
            qtd[x['c']] = x['q']
    dados = {
        'catalogo': catalogo, 'precos': precos, 'qtd': qtd, 'origem': origem, 'arquivos': arquivos,
        'depts': _depts(html),
        'pix3': (_js_valor(html, 'PIX3') if html else None) or {},
        'tr_top': (_js_valor(html, 'TR_TOP') if html else None) or {},
        'ordem_greiner': (_js_valor(html, 'GREINER_ORDEM') if html else None) or [],
        'html': html,
    }
    if not dados['catalogo'] or not dados['precos']:
        sys.exit('ERRO: catálogo ou preços vazios na fonte ' + origem)
    return dados


def conferir_regras(html):
    faltam = [t for t in CONFERE_SITE if t not in html]
    for t in faltam:
        print(f'AVISO: o index.html não contém mais "{t}" — confira se as regras comerciais do PDF ainda batem com o site.')
    return faltam


def versao_padrao(arquivos):
    """Mês/ano do último commit que mexeu na fonte de dados (nunca a data do dia)."""
    meses = 'jan fev mar abr mai jun jul ago set out nov dez'.split()
    try:
        rel = [os.path.relpath(a, RAIZ) for a in arquivos]
        s = subprocess.run(['git', '-C', RAIZ, 'log', '-1', '--format=%cd', '--date=format:%m %Y', '--'] + rel,
                           capture_output=True, text=True, check=True).stdout.split()
        if len(s) == 2:
            return f'{meses[int(s[0]) - 1]}/{s[1]}'
    except Exception:
        pass
    return ''


# ---------------------------------------------------------------- utilidades
def brl(v, casas=2):
    s = f'{v:,.{casas}f}'
    return 'R$ ' + s.replace(',', 'X').replace('.', ',').replace('X', '.')


def preco_unit(preco, q):
    """Mesma regra do unitLn do site: 3 casas abaixo de R$ 0,10."""
    if not q or not preco:
        return ''
    u = preco / q[0]
    return f'{brl(u, 3 if u < 0.1 else 2)} por {q[1]}'


def embalagem(q):
    return f'{q[2]} c/ {q[0]} {q[1]}{"s" if q[0] > 1 and not q[1].endswith("s") else ""}' if q else ''


def link_carrinho(cod, meio):
    return f'{SITE}/?carrinho={quote(cod, safe="")}:1&add=1&utm_source=pdf&utm_medium={meio}'


def link_busca(cod, meio):
    return f'{SITE}/?q={quote(cod, safe="")}&utm_source=pdf&utm_medium={meio}'


def esc(t):
    return t.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')


def nome_curto(n):
    return re.sub(r'\s*[—·]\s*(rack|caixa|pacote)\s+c/\s*\d+.*$', '', n).strip()


def png_qr(url):
    qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_M, box_size=8, border=2)
    qr.add_data(url)
    qr.make(fit=True)
    im = qr.make_image(fill_color='#1F4E79', back_color='white').convert('RGB')
    b = io.BytesIO()
    im.save(b, 'PNG', optimize=True)
    b.seek(0)
    return b


def logo():
    for p in ('img/logo-sullab.png', 'og-sullab.png'):
        f = os.path.join(RAIZ, p)
        if os.path.exists(f):
            return f
    return None


def foto_comprimida(caminho, lado=360, qualidade=70):
    """JPEG leve (fundo branco, máx. `lado` px — sempre <= 600) para embutir no catálogo."""
    if not caminho:
        return None
    caminho = caminho.replace(SITE + '/', '').lstrip('/')
    f = os.path.join(RAIZ, caminho)
    if not os.path.exists(f):
        alt = os.path.splitext(f)[0] + '.jpg'
        if not os.path.exists(alt):
            return None
        f = alt
    im = PILImage.open(f)
    if im.mode in ('RGBA', 'LA', 'P'):
        im = im.convert('RGBA')
        fundo = PILImage.new('RGB', im.size, 'white')
        fundo.paste(im, mask=im.split()[-1])
        im = fundo
    else:
        im = im.convert('RGB')
    lado = min(lado, 600)
    im.thumbnail((lado, lado), PILImage.LANCZOS)
    b = io.BytesIO()
    im.save(b, 'JPEG', quality=qualidade, optimize=True, progressive=False)
    b.seek(0)
    return b


# ---------------------------------------------------------------- seleção dos produtos
DESC_TUBO = [
    (r'citrato|coagula', 'Coagulação (TP, TTPa, fibrinogênio).'),
    (r'glicose|lactato', 'Dosagem de glicose e lactato.'),
    (r'traços', 'Análise de elementos-traço.'),
    (r'heparina', 'Bioquímica em plasma e gasometria venosa.'),
    (r'EDTA K2 com gel', 'Plasma EDTA com gel: biologia molecular e carga viral.'),
    (r'EDTA', 'Hematologia: hemograma e tipagem.'),
    (r'gel', 'Soro com gel separador: bioquímica e sorologia.'),
    (r'sorologia|soro sem gel', 'Soro sem gel: bioquímica, sorologia e imunologia.'),
    (r'sem aditivo', 'Tubo sem aditivo para coleta e descarte.'),
    (r'Agulha', 'Agulha múltipla para coleta a vácuo, com trifacetado.'),
]


def descricao(p):
    n = p['n']
    if p['k'] == 'tr':
        return 'Teste imunocromatográfico de uso profissional, com registro ANVISA. Preço por teste em destaque.'
    for rx, d in DESC_TUBO:
        if re.search(rx, n, re.I):
            return d + ' Greiner Bio-One Vacuette®.'
    return ''


def secoes_destaque(d):
    por_cod = {p['c']: p for p in d['catalogo']}
    ordem = [c for c in d['ordem_greiner'] if c in por_cod] or \
        [p['c'] for p in d['catalogo'] if p['m'].lower() == 'vacuette']
    vac = [por_cod[c] for c in ordem]
    tubos = [p for p in vac if not p['n'].lower().startswith('agulha')]
    agulhas = [p for p in vac if p['n'].lower().startswith('agulha')]
    trs_cod = list(d['tr_top']) or [p['c'] for p in d['catalogo'] if p['k'] == 'tr']
    trs = [por_cod[c] for c in trs_cod if c in por_cod]
    trs.sort(key=lambda p: p['n'])
    return [('Tubos para coleta a vácuo Greiner Vacuette®', tubos, 'Pix 3% de desconto'),
            ('Agulhas para coleta a vácuo Greiner Vacuette®', agulhas, 'Pix 3% de desconto'),
            ('Testes rápidos', trs, 'Pix 5% de desconto')]


# ---------------------------------------------------------------- documento base
class Doc(BaseDocTemplate):
    def __init__(self, destino, titulo, versao, rodape_regras=False, **kw):
        super().__init__(destino, pagesize=A4, leftMargin=16 * mm, rightMargin=16 * mm, topMargin=16 * mm,
                         bottomMargin=22 * mm, title=titulo, author='SULLAB', subject=titulo,
                         creator='SULLAB · gerar_pdfs.py', producer='SULLAB', invariant=1, lang='pt-BR', **kw)
        self.versao = versao
        self.rodape_regras = rodape_regras
        fr = Frame(self.leftMargin, self.bottomMargin, self.width, self.height, id='f', leftPadding=0,
                   rightPadding=0, topPadding=0, bottomPadding=0)
        self.addPageTemplates([PageTemplate(id='p', frames=[fr], onPage=self._rodape)])

    def _rodape(self, c, doc):
        c.saveState()
        w, _ = A4
        y = 12 * mm
        c.setStrokeColor(AZUL)
        c.setLineWidth(0.8)
        c.line(16 * mm, y + 6 * mm, w - 16 * mm, y + 6 * mm)
        c.setFont('Sans-Bold', 9)
        c.setFillColor(AZUL)
        c.drawString(16 * mm, y + 1.5 * mm, 'SULLAB')
        c.setFont('Sans', 9)
        c.setFillColor(CINZA)
        c.drawString(16 * mm + pdfmetrics.stringWidth('SULLAB  ', 'Sans-Bold', 9), y + 1.5 * mm, CONTATO)
        dir_ = f'pág. {doc.page}' + (f' · versão {self.versao}' if self.versao else '')
        c.drawRightString(w - 16 * mm, y + 1.5 * mm, dir_)
        if self.rodape_regras:
            c.setFont('Sans', 8)
            c.drawString(16 * mm, y - 2.5 * mm, 'Preços do site · Pix 5% (3% Vacuette) · cartão até 2x sem juros · '
                         'boleto 28/45 dias p/ CNPJ a partir de R$ 400 · frete por CEP · NF-e em todo pedido')
        c.linkURL(SITE + '/?utm_source=pdf&utm_medium=rodape', (16 * mm, y, w - 16 * mm, y + 5 * mm), relative=0)
        c.restoreState()


def cabecalho(titulo, subtitulo, utm, largura):
    lg = logo()
    qr_url = f'{SITE}/?utm_source=pdf&utm_medium=qr&utm_campaign={utm}'
    esq = []
    if lg:
        im = PILImage.open(lg)
        r = im.size[1] / im.size[0]
        esq.append(Image(lg, width=34 * mm, height=34 * mm * r))
    txt = [Paragraph(titulo, S_TIT), Spacer(1, 3), Paragraph(subtitulo, S_SUB)]
    qr = [Image(png_qr(qr_url), width=30 * mm, height=30 * mm),
          Paragraph(f'<link href="{qr_url}">lojasullabrj.com.br</link>',
                    estilo('qrl', fontSize=9, leading=11, textColor=AZUL, alignment=TA_CENTER))]
    t = Table([[esq, txt, qr]], colWidths=[38 * mm, largura - 38 * mm - 34 * mm, 34 * mm])
    t.setStyle(TableStyle([('VALIGN', (0, 0), (-1, -1), 'MIDDLE'), ('LEFTPADDING', (0, 0), (-1, -1), 0),
                           ('RIGHTPADDING', (0, 0), (-1, -1), 0), ('ALIGN', (2, 0), (2, 0), 'CENTER')]))
    return [t, Spacer(1, 4 * mm)]


def caixa_regras(largura, titulo='Condições de compra no site'):
    corpo = [Paragraph(titulo, S_H2)]
    corpo += [Paragraph(r, S_REGRA, bulletText='•') for r in REGRAS]
    corpo += [Spacer(1, 4), Paragraph(SOBRE, S_PEQ), Spacer(1, 2),
              Paragraph(f'<b>Contato:</b> {CONTATO}', S_PEQ)]
    t = Table([[corpo]], colWidths=[largura])
    t.setStyle(TableStyle([('BOX', (0, 0), (-1, -1), 1, AZUL), ('BACKGROUND', (0, 0), (-1, -1), AZUL_CLARO),
                           ('LEFTPADDING', (0, 0), (-1, -1), 12), ('RIGHTPADDING', (0, 0), (-1, -1), 12),
                           ('TOPPADDING', (0, 0), (-1, -1), 8), ('BOTTOMPADDING', (0, 0), (-1, -1), 10)]))
    return t


def botao(url, texto='Comprar ›'):
    return Paragraph(f'<link href="{url}">{texto}</link>', S_BOT)


def estilo_tabela(n_linhas, col_botao=None):
    st = [('BACKGROUND', (0, 0), (-1, 0), AZUL), ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
          ('LINEBELOW', (0, 1), (-1, -1), 0.5, AZUL_LINHA), ('TOPPADDING', (0, 0), (-1, -1), 5),
          ('BOTTOMPADDING', (0, 0), (-1, -1), 5), ('LEFTPADDING', (0, 0), (-1, -1), 4),
          ('RIGHTPADDING', (0, 0), (-1, -1), 4)]
    for i in range(2, n_linhas, 2):
        st.append(('BACKGROUND', (0, i), (-1, i), AZUL_CLARO))
    if col_botao is not None:
        st += [('BACKGROUND', (col_botao, 1), (col_botao, -1), AZUL),
               ('LINEBELOW', (col_botao, 1), (col_botao, -1), 3, colors.white)]
    return TableStyle(st)


# ---------------------------------------------------------------- a) tabela de preços
def gerar_tabela(d, destino, versao):
    doc = Doc(destino, 'Tabela de preços SULLAB — Vacuette e testes rápidos', versao, rodape_regras=True)
    W = doc.width
    meio = 'tabela'
    hist = cabecalho('Tabela de preços do site',
                     'Tubos e agulhas Greiner Vacuette® e testes rápidos. Preços exclusivos para compra no site '
                     '— toque em <b>Comprar</b> para abrir o carrinho.', 'tabela', W)
    cw = [24 * mm, W - 24 * mm - 30 * mm - 38 * mm - 22 * mm, 30 * mm, 38 * mm, 22 * mm]
    for titulo, itens, pix in secoes_destaque(d):
        if not itens:
            continue
        linhas = [[Paragraph('Código', S_CAB), Paragraph('Produto', S_CAB), Paragraph('Embalagem', S_CAB),
                   Paragraph('Preço', S_CAB_R), '']]
        for p in itens:
            q = d['qtd'].get(p['c'])
            pr = d['precos'].get(p['c'], 0)
            url = link_carrinho(p['c'], meio)
            linhas.append([
                Paragraph(esc(p['c']), S_COD),
                Paragraph(f'<link href="{url}">{esc(nome_curto(p["n"]))}</link>', S_CEL),
                Paragraph(esc(embalagem(q)), S_CEL_P),
                [Paragraph(brl(pr) if pr else 'Sob consulta', S_PRECO),
                 Paragraph(preco_unit(pr, q), S_UNIT)],
                botao(url)])
        t = Table(linhas, colWidths=cw, repeatRows=1)
        t.setStyle(estilo_tabela(len(linhas), col_botao=4))
        hist += [Paragraph(f'{titulo} <font size="10" color="#555555">· {pix}</font>', S_H2), t, Spacer(1, 5 * mm)]
    hist.append(KeepTogether([caixa_regras(W)]))
    doc.build(hist)


# ---------------------------------------------------------------- b) catálogo com fotos
def gerar_catalogo(d, destino, versao):
    doc = Doc(destino, 'Catálogo SULLAB — Vacuette e testes rápidos', versao)
    W = doc.width
    meio = 'catalogo'
    hist = cabecalho('Catálogo Vacuette® e testes rápidos',
                     'Tubos e agulhas Greiner Vacuette® e testes rápidos com registro ANVISA. '
                     'Preços exclusivos do site — toque em <b>Comprar</b> para abrir o carrinho.', 'catalogo', W)
    hist += [caixa_regras(W), Spacer(1, 4 * mm)]
    FOTO = 22 * mm
    cw = [FOTO + 4, W - FOTO - 4 - 36 * mm - 24 * mm, 36 * mm, 24 * mm]
    for titulo, itens, pix in secoes_destaque(d):
        if not itens:
            continue
        linhas = []
        for p in itens:
            q = d['qtd'].get(p['c'])
            pr = d['precos'].get(p['c'], 0)
            url = link_carrinho(p['c'], meio)
            fb = foto_comprimida(p['img'])
            foto = Image(fb, width=FOTO, height=FOTO) if fb else ''
            info = [Paragraph(f'<link href="{url}"><b>{esc(nome_curto(p["n"]))}</b></link>', S_CEL),
                    Paragraph(esc(descricao(p)), S_CEL_P),
                    Paragraph(f'Cód. <b>{esc(p["c"])}</b> · {esc(embalagem(q))}', S_CEL_P)]
            linhas.append([foto, info, [Paragraph(brl(pr) if pr else 'Sob consulta', S_PRECO),
                                        Paragraph(preco_unit(pr, q), S_UNIT)], botao(url)])
        t = Table(linhas, colWidths=cw)
        st = estilo_tabela(len(linhas) + 1, col_botao=3)
        st.add('BACKGROUND', (0, 0), (-1, 0), colors.white)  # sem cabeçalho nesta tabela
        st.add('BACKGROUND', (3, 0), (3, -1), AZUL)
        st.add('LINEBELOW', (0, 0), (-1, -1), 0.5, AZUL_LINHA)
        st.add('LINEBELOW', (3, 0), (3, -1), 3, colors.white)
        t.setStyle(st)
        hist += [Paragraph(f'{titulo} <font size="10" color="#555555">· {pix}</font>', S_H2), t, Spacer(1, 6 * mm)]
    doc.build(hist)


# ---------------------------------------------------------------- c) catálogo completo
def gerar_completo(d, destino, versao):
    doc = Doc(destino, 'Catálogo completo SULLAB', versao, rodape_regras=True)
    W = doc.width
    meio = 'catalogo_completo'
    hist = cabecalho('Catálogo completo', f'{len(d["catalogo"]):,} produtos para laboratório e saúde. '.replace(',', '.') +
                     'Preços exclusivos do site — toque em <b>Comprar</b> para abrir o carrinho.',
                     'catalogo_completo', W)
    hist += [caixa_regras(W), Spacer(1, 5 * mm)]
    depts = d['depts'] or [{'key': k, 'nome': k, 'cats': [k]} for k in sorted({p['k'] for p in d['catalogo']})]
    usados = set()
    grupos = []
    for dp in depts:
        itens = [p for p in d['catalogo'] if p['k'] in dp['cats']]
        usados.update(p['c'] for p in itens)
        grupos.append((dp['nome'], itens))
    resto = [p for p in d['catalogo'] if p['c'] not in usados]
    grupos.append(('Outros produtos', resto))
    # índice
    idx = [Paragraph('Categorias', S_H2)]
    idx += [Paragraph(f'<a href="#cat{i}" color="#1F4E79">{esc(n)}</a> <font color="#555555">({len(it)})</font>',
                      S_TXT) for i, (n, it) in enumerate(grupos) if it]
    hist += idx + [PageBreak()]
    cw = [27 * mm, W - 27 * mm - 20 * mm - 36 * mm - 22 * mm, 20 * mm, 36 * mm, 22 * mm]
    for i, (nome, itens) in enumerate(grupos):
        if not itens:
            continue
        itens = sorted(itens, key=lambda p: (p['n'].lower(), p['c']))
        linhas = [[Paragraph('Código', S_CAB), Paragraph('Produto', S_CAB), Paragraph('Marca', S_CAB),
                   Paragraph('Preço', S_CAB_R), '']]
        for p in itens:
            pr = d['precos'].get(p['c'], 0)
            q = d['qtd'].get(p['c'])
            url = link_carrinho(p['c'], meio) if pr else link_busca(p['c'], meio)
            linhas.append([Paragraph(esc(p['c']), S_COD),
                           Paragraph(esc(p['n']), S_CEL),
                           Paragraph(esc(p['m']), S_CEL_P),
                           [Paragraph(brl(pr) if pr else 'Sob consulta', S_PRECO)] +
                           ([Paragraph(preco_unit(pr, q), S_UNIT)] if q and pr else []),
                           botao(url, 'Comprar ›' if pr else 'Consultar ›')])
        t = Table(linhas, colWidths=cw, repeatRows=1)
        t.setStyle(estilo_tabela(len(linhas), col_botao=4))
        hist += [Paragraph(f'<a name="cat{i}"/>{esc(nome)} <font size="10" color="#555555">· {len(itens)} '
                           f'produto{"s" if len(itens) > 1 else ""}</font>', S_H2), t, Spacer(1, 5 * mm)]
    doc.build(hist)


# ---------------------------------------------------------------- principal
PDFS = [('Tabela_de_Precos_SULLAB.pdf', gerar_tabela),
        ('Catalogo_SULLAB_Vacuette_e_Testes_Rapidos.pdf', gerar_catalogo),
        ('Catalogo_SULLAB_Completo.pdf', gerar_completo)]


def main():
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    ap.add_argument('--fonte', choices=['auto', 'html', 'json'], default='auto')
    ap.add_argument('--saida', default=os.path.join(RAIZ, 'docs'))
    ap.add_argument('--versao', default=os.environ.get('PDF_VERSAO'),
                    help='texto discreto no rodapé (ex.: "out/2026"); padrão: mês do último commit da fonte')
    a = ap.parse_args()
    d = carregar(a.fonte)
    versao = a.versao if a.versao is not None else versao_padrao(d['arquivos'])
    print(f'Fonte: {d["origem"]} · {len(d["catalogo"])} produtos · {len(d["precos"])} preços · versão "{versao}"')
    if d['html']:
        conferir_regras(d['html'])
    os.makedirs(a.saida, exist_ok=True)
    for nome, fn in PDFS:
        buf = io.BytesIO()
        fn(d, buf, versao)
        novo = buf.getvalue()
        alvo = os.path.join(a.saida, nome)
        antigo = open(alvo, 'rb').read() if os.path.exists(alvo) else None
        if antigo == novo:
            estado = 'sem mudança'
        else:
            with open(alvo + '.tmp', 'wb') as f:
                f.write(novo)
            os.replace(alvo + '.tmp', alvo)
            estado = 'atualizado'
        print(f'{nome}: {len(novo) / 1024:.0f} KB · sha256 {hashlib.sha256(novo).hexdigest()[:12]} · {estado}')


if __name__ == '__main__':
    main()
