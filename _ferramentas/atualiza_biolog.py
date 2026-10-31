#!/usr/bin/env python3
"""Atualiza todo dia os preços Biolog do site pelo dólar (28/10/2026, pedido do Eduardo).

Regra da Biolog (Lista Preços Revendas, observação 2): valores em US$, convertidos pela cotação oficial de VENDA do
Banco Central (PTAX) no fechamento do dia útil anterior, arredondados (reais inteiros).
Custo = round(US$ × PTAX)   ·   Preço de venda = custo × MARKUP (1,70, o mesmo da Tabela_Biolog_Precificada)

Fonte do US$: data/biolog_usd.json (código do site → US$ da lista Setembro-15/2026). Itens fora dessa base não mudam.
Saída: data/precos.json (+ hash ?v= no index.html), páginas de produto/categoria/catálogo, feed do Google e biolog_precos.json
(lido pelo robô do WhatsApp). Sem cotação nova (BCB fora do ar, feriado) = nada muda.
Gatilho: só muda os preços quando a PTAX varia 3% ou mais em relação à última aplicada (biolog_precos.json).
Uso: python3 _ferramentas/atualiza_biolog.py [--ptax 5.3346] [--dry] [--forcar]
"""
import datetime as dt
import glob
import json
import os
import re
import sys
import urllib.request

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import dados_site as ds  # noqa: E402  (30/10/2026: preços saíram do index.html para data/precos.json)

MARKUP = 1.70
LIMITE_VARIACAO = 0.03   # só reprecifica se o dólar mudar 3% ou mais desde o último aplicado
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/'
DRY = '--dry' in sys.argv


def ptax_venda(hoje: dt.date):
    """(data, cotação de venda) do último fechamento ANTES de hoje."""
    ini = (hoje - dt.timedelta(days=10)).strftime('%m-%d-%Y')
    fim = (hoje - dt.timedelta(days=1)).strftime('%m-%d-%Y')
    url = ("https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/CotacaoDolarPeriodo("
           "dataInicial=@dataInicial,dataFinalCotacao=@dataFinalCotacao)?"
           f"@dataInicial='{ini}'&@dataFinalCotacao='{fim}'&$format=json&$orderby=dataHoraCotacao%20desc&$top=1")
    with urllib.request.urlopen(url, timeout=30) as r:
        v = json.load(r)['value']
    if not v:
        raise SystemExit('BCB sem cotação no período')
    return v[0]['dataHoraCotacao'][:10], float(v[0]['cotacaoVenda'])


def br(v):
    return f'{v:,.2f}'.replace(',', 'X').replace('.', ',').replace('X', '.')


def main():
    if '--ptax' in sys.argv:
        data_ptax, ptax = 'manual', float(sys.argv[sys.argv.index('--ptax') + 1])
    else:
        data_ptax, ptax = ptax_venda(dt.date.today())
    # 28/10/2026 (Eduardo): só reprecificar quando o dólar variar 3% ou mais em relação ao último dólar aplicado
    # (evita trocar preço todo dia no site/Google). --forcar aplica mesmo assim.
    try:
        ant = json.load(open(R + 'biolog_precos.json', encoding='utf-8')).get('ptax_venda')
    except Exception:
        ant = None
    if ant and '--forcar' not in sys.argv and abs(ptax / float(ant) - 1) < LIMITE_VARIACAO:
        print(f'PTAX {data_ptax} = {ptax} · variação {abs(ptax / float(ant) - 1):.2%} sobre o aplicado ({ant}) '
              f'< {LIMITE_VARIACAO:.0%}: preços mantidos')
        return
    usd = json.load(open(R + 'data/biolog_usd.json'))
    PRE = ds.ler_precos()
    OLD, NEW = {}, {}
    for c, u in usd.items():
        if c not in PRE or not PRE[c][1]:
            continue
        novo = round(round(u * ptax) * MARKUP, 2)
        if abs(novo - PRE[c][1]) >= 0.01:
            OLD[c], NEW[c] = PRE[c][1], novo
    saida = {'atualizado_em': dt.datetime.now().strftime('%Y-%m-%d %H:%M'), 'ptax_venda': ptax,
             'data_ptax': data_ptax, 'markup': MARKUP,
             'precos': {c: round(round(u * ptax) * MARKUP, 2) for c, u in usd.items() if c in PRE}}
    print(f'PTAX {data_ptax} = {ptax} · {len(NEW)} preço(s) Biolog mudam')
    if DRY:
        for c in list(NEW)[:10]:
            print(c, OLD[c], '->', NEW[c])
        return
    if NEW:
        trocar(OLD, NEW)
    open(R + 'biolog_precos.json', 'w', encoding='utf-8').write(json.dumps(saida, ensure_ascii=False, indent=0))


def trocar(OLD, NEW):
    codes = sorted(NEW, key=len, reverse=True)
    ref = re.compile(r'(?<![0-9A-Za-z\-])(' + '|'.join(re.escape(c) for c in codes) + r')(?![0-9])')

    def swap(seg, code):
        o, n = OLD[code], NEW[code]
        s = seg.replace('R$ ' + br(o), 'R$ ' + br(n)).replace('R$&nbsp;' + br(o), 'R$&nbsp;' + br(n))
        s = re.sub(r'"price":\s*"' + re.escape(f'{o:.2f}') + '"', f'"price": "{n:.2f}"', s)
        for tag in ('g:price', 'g:sale_price'):
            s = s.replace(f'<{tag}>{o:.2f} BRL</{tag}>', f'<{tag}>{n:.2f} BRL</{tag}>')
        return s

    def own_code(t):
        m = re.search(r'<b>C[óo]digo:</b>\s*([^<\s·]+)', t)
        c = m.group(1).strip() if m else None
        return c if c in NEW else None

    BLOCK = re.compile(r'<tr\b.*?</tr>|<a\b[^>]*>.*?</a>|<item>.*?</item>|<url>.*?</url>', re.S)
    arquivos = [f for f in glob.glob(R + '**/*', recursive=True)
                if f.endswith(('.html', '.xml')) and '/.git/' not in f and '/_ferramentas/' not in f]
    arquivos.append(ds.LOJA_JS)  # o JS da home (antes dentro do index.html) também tem textos com preço
    mud = 0
    for f in arquivos:
        t = open(f, encoding='utf-8').read()
        o = t
        me = own_code(t)
        out, last = [], 0
        for m in BLOCK.finditer(t):
            seg = m.group(0)
            cs = set(ref.findall(seg))
            if len(cs) == 1:
                seg = swap(seg, cs.pop())
            rest = t[last:m.start()]
            out.append(swap(rest, me) if me else rest)
            out.append(seg)
            last = m.end()
        rest = t[last:]
        out.append(swap(rest, me) if me else rest)
        t = ''.join(out)
        if t != o:
            mud += 1
            open(f, 'w', encoding='utf-8').write(t)
    # preços da loja: data/precos.json (mesmo formato do antigo window.PRECOS: "código": [v, v, null])
    pre = ds.ler_precos()
    for k, n in NEW.items():
        if k in pre and isinstance(pre[k], list) and len(pre[k]) == 3 and pre[k][2] is None:
            pre[k] = [n, n, None]
    if ds.gravar_precos(pre):  # também grava o novo ?v=<hash> no index.html (cache não serve preço velho)
        mud += 1
    print('arquivos alterados:', mud)


if __name__ == '__main__':
    main()
