# -*- coding: utf-8 -*-
"""Monta data/ficha.json = {codigo: {"rows": [[rotulo, valor], ...], "why": [...]}} a partir de:
- _ferramentas/fontes/conteudo_p1.json / conteudo_p2.json (texto que antes virava a arte img/a/*)
- GUIA e GUIA_TR de gerar_pdfs.py (tampa, aditivo, indicação, inversões, registro ANVISA dos Vacuette e testes rápidos)
- data/ft.json (texto solto "a · b · c") como complemento, sem repetir o que já está nas linhas.
31/10/2026 (dono): a arte duplicava a ficha; a ficha do painel passa a ter tudo e a arte sai da galeria.
"""
import json, os, re, sys, importlib.util
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
spec = importlib.util.spec_from_file_location('gp', '_ferramentas/gerar_pdfs.py')
src = open('_ferramentas/gerar_pdfs.py', encoding='utf-8').read()
ns = {}
for nome in ('GUIA', 'GUIA_TR'):
    m = re.search(nome + r'\s*=\s*\{[\s\S]*?\n\}', src)
    exec(m.group(0), ns)
GUIA, GUIA_TR = ns['GUIA'], ns['GUIA_TR']

cont = {}
for f in ('conteudo_p1.json', 'conteudo_p2.json'):
    p = os.path.join('_ferramentas/fontes', f)
    if os.path.exists(p):
        cont.update(json.load(open(p, encoding='utf-8')))
ft = json.load(open('ft.json' if os.path.exists('ft.json') else 'data/ft.json', encoding='utf-8'))
cat = {x['c']: x for x in json.load(open('data/catalogo.json', encoding='utf-8'))}

def norm(s): return re.sub(r'\s+', ' ', str(s or '')).strip()
GENERICO = re.compile(r'nota fiscal|envio para todo|NF-e|todo o brasil', re.I)

out = {}
for c, p in cat.items():
    rows, why = [], []
    seen = set()
    def add(k, v):
        k, v = norm(k), norm(v)
        if not v or k.lower() in seen or v.lower() in seen: return
        seen.add(k.lower()); seen.add(v.lower()); rows.append([k, v])
    cc = cont.get(c) or {}
    if c in GUIA:
        tampa, aditivo, uso, inv, anvisa = GUIA[c]
        if tampa: add('Tampa', tampa)
        if aditivo: add('Aditivo', aditivo)
        if uso: add('Indicação', uso)
    for k, v in (cc.get('rows') or []):
        if k.lower() in ('código',): continue
        add(k, v)
    if c in GUIA:
        tampa, aditivo, uso, inv, anvisa = GUIA[c]
        if inv: add('Inversões após a coleta', inv)
        if anvisa: add('Registro ANVISA', anvisa)
        if tampa and p.get('k') == 'tubo': add('Fechamento', 'Tampa de rosca Vacuette® — não solta no transporte e reabre com segurança')
    if c in GUIA_TR:
        uso, anvisa = GUIA_TR[c]
        if uso: add('Amostra / uso', uso)
        if anvisa: add('Registro ANVISA', anvisa)
    # complemento do ft.json: pedaços "Rótulo: valor" que ainda não existem
    for peca in [x.strip(' .') for x in norm(ft.get(c, '')).split(' · ') if x.strip()]:
        m = re.match(r'^([A-Za-zÀ-ÿ ]{2,24}):\s*(.+)$', peca)
        if m: add(m.group(1), m.group(2))
        elif not seen and len(peca) > 8: add('Descrição', peca)
    if 'marca' not in seen and p.get('m'): add('Marca', p['m'])
    for w in (cc.get('why') or []):
        w = norm(w)
        if w and not GENERICO.search(w) and w not in why and w.lower() not in seen: why.append(w)
    if rows or why:
        out[c] = {'rows': rows, 'why': why}
json.dump(out, open('data/ficha.json', 'w', encoding='utf-8'), ensure_ascii=False, separators=(',', ':'))
print('fichas:', len(out), 'de', len(cat))
print(json.dumps(out.get('454036'), ensure_ascii=False, indent=1))
print(json.dumps(out.get('TR 017-1 RP'), ensure_ascii=False))
