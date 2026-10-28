#!/usr/bin/env python3
"""Atualiza todo dia os preços Biolog do site pelo dólar (28/10/2026, pedido do Eduardo).

Regra da Biolog (Lista Preços Revendas, observação 2): valores em US$, convertidos pela cotação oficial de VENDA do
Banco Central (PTAX) no fechamento do dia útil anterior, arredondados (reais inteiros).
Custo = round(US$ × PTAX)   ·   Preço de venda = custo × MARKUP (1,70, o mesmo da Tabela_Biolog_Precificada)

Fonte do US$: data/biolog_usd.json (código do site → US$ da lista Setembro-15/2026). Itens fora dessa base não mudam.
Saída: index.html (window.PRECOS), páginas de produto/categoria/catálogo, feed do Google e biolog_precos.json
(lido pelo robô do WhatsApp). Sem cotação nova (BCB fora do ar, feriado) = nada muda.
Uso: python3 _ferramentas/atualiza_biolog.py [--ptax 5.3346] [--dry]
"""
import datetime as dt
import glob
import json
import os
import re
import sys
import urllib.request

MARKUP = 1.70
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
    usd = json.load(open(R + 'data/biolog_usd.json'))
    idx = open(R + 'index.html', encoding='utf-8').read()
    j = idx.find('window.PRECOS=') + len('window.PRECOS=')
    PRE, _ = json.JSONDecoder().raw_decode(idx[j:])
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
        if f.endswith('index.html') and os.path.dirname(f) + '/' == R:
            for k, n in NEW.items():
                t = re.sub(r'"' + re.escape(k) + r'": \[[0-9.]+, [0-9.]+, null\]', f'"{k}": [{n}, {n}, null]', t, count=1)
        if t != o:
            mud += 1
            open(f, 'w', encoding='utf-8').write(t)
    print('arquivos alterados:', mud)


if __name__ == '__main__':
    main()
