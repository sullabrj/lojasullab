# -*- coding: utf-8 -*-
"""Tabela de preços de VIDRARIA para laboratório (aulas práticas) no modelo padrão dos PDFs do site.

Página 1 = compilado de fotos; depois, tabelas por família; no fim, condições de compra.
A entrada é o arquivo de preços do portal do fornecedor (fica FORA do repositório: contém custo).
Formato da entrada, uma linha por produto:  CÓDIGO|DESCRIÇÃO|PREÇO_DO_PORTAL|ESTOQUE|UNIDADE
Preço do PDF = preço do portal x --markup (padrão 1,70, ordem do Eduardo em 31/10 e 01/11/2026).
Itens sem estoque no fornecedor não entram. Fotos: img/p/<CÓDIGO>.jpg (as mesmas do site).

Uso:  python3 _ferramentas/gerar_vidraria_pdf.py --entrada /caminho/vidraria_cral.txt [--saida docs] [--markup 1.70]
"""
import argparse, io, os, re, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gerar_pdfs as G  # estilos, Doc, cabecalho, caixa_regras, foto_comprimida
from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.platypus import CondPageBreak, Image, KeepTogether, PageBreak, Paragraph, Spacer, Table, TableStyle

CATS = [
    ('Béqueres (copos Becker)', r'^COPO BECKER'),
    ('Erlenmeyers', r'^FRASCO ERLENMEYER'),
    ('Provetas', r'^PROVETA'),
    ('Balões volumétricos', r'^BALAO VOLUMETRICO'),
    ('Balões de fundo chato e redondo', r'^BALAO FUNDO'),
    ('Balões de destilação', r'^BALAO DE DESTILACAO'),
    ('Buretas', r'^BURETA'),
    ('Pipetas volumétricas e sorológicas', r'^PIPETA (VOLUMETRICA|SOROLOGICA)'),
    ('Pipetas Pasteur e Westergreen', r'^PIPETA (PASTEUR|DE WESTERGREEN)'),
    ('Funis analíticos e de separação', r'^FUNIL'),
    ('Frascos reagente', r'^FRASCO REAGENTE'),
    ('Kitassatos e sistemas de filtração', r'^(FRASCO KITAZATO|SISTEMA DE FILTRACAO)'),
    ('Tubos de ensaio e Duran', r'^TUBO DE (VIDRO|DURAN)'),
    ('Tubos capilares', r'^TUBO CAPILAR'),
    ('Placas de Petri e de Kline', r'^PLACA DE (PETRI|KLINE)'),
    ('Lâminas e lamínulas', r'^LAMIN'),
    ('Câmaras de contagem', r'^CAMARA'),
    ('Cubas de coloração', r'^CUBA'),
    ('Dessecadores', r'^DESSECADOR'),
    ('Vidros de relógio', r'^VIDRO RELOGIO'),
]
UN = {'PC': 'peça', 'CX': 'caixa', 'PT': 'pacote', 'FR': 'frasco', 'RC': 'rack'}

# Fotos do compilado: (código da foto, rótulo, índice da família em CATS para o "a partir de")
FOTOS = [('BEFA50', 'Béquer forma alta', 0), ('BEFB250', 'Béquer forma baixa', 0),
         ('ERLBE250', 'Erlenmeyer', 1), ('PROBPH100', 'Proveta', 2),
         ('BVAB100', 'Balão volumétrico', 3), ('BFC500', 'Balão fundo chato', 4),
         ('BURE50', 'Bureta', 6), ('PVO10ML', 'Pipeta volumétrica', 7),
         ('19150', 'Pipeta Pasteur', 8), ('FUHC100', 'Funil analítico', 9),
         ('FUTP250', 'Funil de separação', 9), ('FRATR500', 'Frasco reagente', 10),
         ('KITA500', 'Kitassato', 11), ('P13100', 'Tubo de ensaio', 12),
         ('PV8015', 'Placa de Petri', 14), ('DV210', 'Dessecador', 18)]

REGRAS_VIDRARIA = [
    '<b>Como pedir:</b> envie os itens e as quantidades pelo WhatsApp (24) 3323-6532 ou por comercial@sullabrj.com.br.',
    '<b>Pagamento:</b> Pix, cartão de crédito até 2x sem juros ou boleto faturado em 28 ou 45 dias para CNPJ, '
    'em pedidos a partir de R$ 400 (mediante análise de crédito).',
    '<b>Pedido mínimo:</b> R$ 100.',
    '<b>Frete</b> calculado pelo CEP de entrega.',
    '<b>NF-e</b> em todo pedido.',
    '<b>Disponibilidade</b> confirmada no fechamento do pedido.',
]


def cap_key(nome):
    m = re.search(r'(\d+(?:\.\d{3})?)\s*ML', nome)
    if m:
        return float(m.group(1).replace('.', ''))
    m = re.search(r'(\d+)\s*MM', nome)
    if m:
        return float(m.group(1))
    m = re.search(r'(\d+)X(\d+)', nome)
    if m:
        return float(m.group(1)) * 1000 + float(m.group(2))
    return 0.0


FIXES = {'becker': 'Becker', 'berzelius': 'Berzelius', 'griffin': 'Griffin', 'erlenmeyer': 'Erlenmeyer',
         'kitazato': 'Kitassato', 'pasteur': 'Pasteur', 'westergreen': 'Westergreen', 'squib': 'Squib',
         'neubauer': 'Neubauer', 'fuchs-rosenthal': 'Fuchs-Rosenthal', 'bright line': 'Bright Line',
         'improved double': 'Improved Double', 'improved-double': 'Improved Double', 'kline': 'Kline',
         'petri': 'Petri', 'teflon': 'Teflon', 'classe a': 'Classe A', 'duran': 'Duran',
         'borosilicato': 'borossilicato', 'coloracao': 'coloração', 'destilacao': 'destilação',
         'separacao': 'separação', 'filtracao': 'filtração', 'volumetrico': 'volumétrico',
         'volumetrica': 'volumétrica', 'sorologica': 'sorológica', 'analitico': 'analítico',
         'plastica': 'plástica', 'laminas': 'lâminas', 'lamina': 'lâmina', 'laminula': 'lamínula',
         'ambar': 'âmbar', 'pecas': 'peças', 'tracao': 'traço', 'traco': 'traço',
         'esg.total': 'esgotamento total', 'camara': 'câmara', 'microhematocrito': 'microhematócrito',
         'relogio': 'relógio', 'saida': 'saída', 'coagulo': 'coágulo', 'aluminio': 'alumínio',
         'laticinios': 'laticínios', 'diametro': 'diâmetro', 'p/': 'para'}


def titulo(nome):
    n = nome.replace('CAP.', '').replace('GRAD.', 'graduado ')
    n = re.sub(r'\s+', ' ', n).strip().lower()
    s = n[0].upper() + n[1:]
    for k, v in FIXES.items():
        s = re.sub(r'(?<![\w])' + re.escape(k) + r'(?![\w])', v, s)
    s = re.sub(r'(\d) ?ml\b', r'\1 mL', s)
    s = re.sub(r'(\d)\.(\d{3}) mL', r'\1\2 mL', s)
    s = re.sub(r'(\d) ?mm\b', r'\1 mm', s)
    s = re.sub(r'\bcx/(\d+)', r'cx/\1', s)
    s = re.sub(r'\bpecas\b', 'peças', s)
    return s.replace(' - ', ' · ').replace('  ', ' ').rstrip('.')


def chave_familia(nome):
    pre = re.sub(r'\d.*', '', nome)
    pre = re.sub(r'[^A-Z ]', ' ', pre)
    pre = re.sub(r'\b(GRIFFIN|BERZELIUS|GRADUADO|CAP|GRAD)\b', ' ', pre)
    return re.sub(r'\s+', ' ', pre).strip()


def carregar(entrada, markup, precos=None):
    """precos: arquivo opcional COD|PRECO_DE_VENDA que substitui custo x markup (sem custo dentro)."""
    fixo = {}
    if precos:
        for ln in open(precos, encoding='utf-8'):
            if '|' in ln:
                k, v = ln.strip().split('|')
                fixo[k] = float(v)
    rows = []
    for linha in open(entrada, encoding='utf-8'):
        linha = linha.strip()
        if not linha:
            continue
        cod, nome, preco, est, un = linha.split('|')
        if int(est) <= 0:
            continue
        venda = fixo[cod] if cod in fixo else round(float(preco) * markup + 1e-9, 2)
        rows.append((cod, nome, venda, un))
    grupos, usados = [], set()
    for tit, rx in CATS:
        itens = [r for r in rows if re.match(rx, r[1]) and r[0] not in usados]
        usados.update(r[0] for r in itens)
        itens.sort(key=lambda r: (chave_familia(r[1]), cap_key(r[1])))
        grupos.append((tit, itens))
    sobra = [r for r in rows if r[0] not in usados]
    if sobra:
        grupos.append(('Outros itens de vidraria', sobra))
    return [g for g in grupos if g[1]], len(rows)


def pagina_fotos(grupos, W):
    preco_item = {r[0]: r[2] for _, itens in grupos for r in itens}
    cel_w = W / 4
    lado = 29 * mm
    st_leg = G.estilo('fleg', fontName='Sans-Bold', fontSize=10, leading=12, textColor=G.TEXTO, alignment=1)
    st_pre = G.estilo('fpre', fontSize=9, leading=11, textColor=G.CINZA, alignment=1)
    celulas = []
    for cod, rotulo, ic in FOTOS:
        fb = G.foto_comprimida(f'img/p/{cod}.jpg', lado=420, qualidade=72)
        if not fb:
            continue
        pre = G.brl(preco_item[cod]) if cod in preco_item else ''
        celulas.append([Image(fb, width=lado, height=lado), Paragraph(rotulo, st_leg),
                        Paragraph(f'Cód. {cod}', st_pre), Paragraph(f'<b>{pre}</b>', st_pre)])
    while len(celulas) % 4:
        celulas.append('')
    linhas = [celulas[i:i + 4] for i in range(0, len(celulas), 4)]
    t = Table(linhas, colWidths=[cel_w] * 4)
    t.setStyle(TableStyle([('ALIGN', (0, 0), (-1, -1), 'CENTER'), ('VALIGN', (0, 0), (-1, -1), 'TOP'),
                           ('TOPPADDING', (0, 0), (-1, -1), 3), ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
                           ('BOX', (0, 0), (-1, -1), 0.8, G.AZUL_LINHA),
                           ('INNERGRID', (0, 0), (-1, -1), 0.4, G.AZUL_LINHA)]))
    return t


def gerar(entrada, destino, markup, versao, precos=None):
    grupos, total = carregar(entrada, markup, precos)
    doc = G.Doc(destino, 'Tabela de preços SULLAB — Vidraria para laboratório', versao, rodape_regras=False)
    W = doc.width
    sub = ('Vidraria de borossilicato 3.3 para aulas práticas e rotina de laboratório: béqueres, erlenmeyers, '
           'provetas, balões, buretas, pipetas, funis, placas de Petri e muito mais.')
    hist = G.cabecalho('Tabela de preços — Vidraria para laboratório', sub, 'tabela_vidraria', W)
    hist += [Paragraph(f'Alguns dos <b>{total} modelos</b> da tabela', G.S_H2), pagina_fotos(grupos, W),
             Spacer(1, 3 * mm),
             Paragraph('Fotos ilustrativas de um modelo de cada família, com o preço do item mostrado. Todos os tamanhos e preços nas páginas seguintes.',
                       G.S_PEQ),
             PageBreak()]
    cw = [25 * mm, W - 25 * mm - 17 * mm - 27 * mm, 17 * mm, 27 * mm]
    for tit, itens in grupos:
        linhas = [[Paragraph('Código', G.S_CAB), Paragraph('Produto', G.S_CAB), Paragraph('Unid.', G.S_CAB),
                   Paragraph('Preço', G.S_CAB_R)]]
        for cod, nome, preco, un in itens:
            linhas.append([Paragraph(G.esc(cod), G.S_COD), Paragraph(G.esc(titulo(nome)), G.S_CEL),
                           Paragraph(UN.get(un, un), G.S_CEL_P), Paragraph(G.brl(preco), G.S_PRECO)])
        t = Table(linhas, colWidths=cw, repeatRows=1)
        t.setStyle(G.estilo_tabela(len(linhas)))
        topo = Paragraph(f'{tit} <font size="10" color="#555555">· {len(itens)} '
                         f'{"modelo" if len(itens) == 1 else "modelos"}</font>', G.S_H2)
        hist += [CondPageBreak(45 * mm), topo, t, Spacer(1, 5 * mm)]
    hist.append(KeepTogether([G.caixa_regras(W, 'Condições de compra')]))
    doc.build(hist)
    return total, len(grupos)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--entrada', required=True)
    ap.add_argument('--saida', default=os.path.join(G.RAIZ, 'docs'))
    ap.add_argument('--markup', type=float, default=1.70)
    ap.add_argument('--precos', default=None, help='COD|PRECO de venda (substitui o markup)')
    ap.add_argument('--versao', default='nov/2026')
    ap.add_argument('--nome', default='Tabela_SULLAB_Vidraria_Laboratorio.pdf')
    a = ap.parse_args()
    G.REGRAS[:] = REGRAS_VIDRARIA  # condições próprias da linha (sem Vacuette/testes rápidos)
    os.makedirs(a.saida, exist_ok=True)
    dest = os.path.join(a.saida, a.nome)
    n, g = gerar(a.entrada, dest, a.markup, a.versao, a.precos)
    print(f'{dest}: {n} itens em {g} famílias · {os.path.getsize(dest) / 1024:.0f} KB')


if __name__ == '__main__':
    main()
