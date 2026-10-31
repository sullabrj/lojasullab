#!/usr/bin/env python3
"""Calcula pares "quem compra X leva Y" a partir da aba Itens (export CSV/XLSX da planilha oficial)
e grava data/pares.json para o site (window.PARES_REAIS, lido pelo bloco de relacionados em js/loja.js).
Corte: par visto em >= 3 pedidos e em >= 10% dos pedidos do item X. Uso: python3 pares.py itens.csv
"""
import csv, json, sys, collections, itertools
src = sys.argv[1]
cestas = collections.defaultdict(set)
with open(src, newline='', encoding='utf-8') as f:
    for r in csv.DictReader(f):
        c = str(r.get('Código') or '').strip().replace('.0', '')
        if r.get('Controle') and c:
            cestas[r['Controle']].add(c)
freq = collections.Counter(); pares = collections.Counter()
for cs in cestas.values():
    cs = sorted(cs); freq.update(cs)
    for a, b in itertools.combinations(cs, 2):
        pares[(a, b)] += 1; pares[(b, a)] += 1
out = collections.defaultdict(list)
for (a, b), n in pares.items():
    if n >= 3 and n / freq[a] >= 0.10:
        out[a].append((n, b))
res = {a: [b for n, b in sorted(v, reverse=True)[:4]] for a, v in out.items()}
json.dump(res, open('data/pares.json', 'w'), ensure_ascii=False, indent=0)
print(len(cestas), 'cestas;', len(res), 'itens com pares')
