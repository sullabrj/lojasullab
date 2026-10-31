#!/usr/bin/env python3
"""Limpa termos genéricos do kw.json (31/10/2026).

Problema: muitos produtos receberam a mesma lista enorme de palavras (ex.: os 259 meios Biolog têm
"thayer martin chocolate mueller hinton cled ..."), então a busca por "chocolate" trazia 259 itens.

Regra: um termo que aparece no kw de MAIS DE 50 produtos sai do kw do produto, exceto quando
  - o termo está na lista GERAIS (palavra de categoria que vale para todos: "microbiologia", "reagente"...), ou
  - o termo está em MANTER_POR_CATEGORIA para a categoria (campo k) do produto ("sangue" nos tubos/agulhas).
Fica também quando o termo, sem espaços, está no nome do produto ("macconkey" no "Ágar Mac Conkey").
Uso: python3 _ferramentas/limpa_kw.py [--dry]
"""
import collections
import json
import os
import re
import sys
import unicodedata

R = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/'
LIMITE = 50
GERAIS = set('''microbiologia bacteriologia cultura meio agar caldo semeadura placa placas laboratorio descartavel plastico
consumivel vidro vidraria borossilicato reagente bioquimica corante seletivo diferencial isolamento dosagem analito clinico
disco discos antibiograma antibiotico sensibilidade teste frasco esteril hematologia graduado tubo tubos'''.split())
MANTER_POR_CATEGORIA = {
    'sangue': {'tubo', 'agulha', 'lanceta', 'coletoram', 'seringa'},
    'soro': {'tubo', 'bioq', 'sorol', 'controle', 'hemat'},
    'plasma': {'tubo', 'bioq', 'hemat', 'controle'},
    'tampa': {'tubo', 'coletoram', 'plast', 'vidraria', 'cubeta', 'pipeta'},
    'azul': {'tubo', 'pipeta', 'plast', 'cubeta', 'micro', 'equip'},
    'citrato': {'tubo', 'hemat'},
}


def sa(s):
    return unicodedata.normalize('NFKD', s.lower()).encode('ascii', 'ignore').decode()


def main():
    kw = json.load(open(R + 'kw.json', encoding='utf-8'))
    cat = {p['c']: p for p in json.load(open(R + 'data/catalogo.json', encoding='utf-8'))}
    df = collections.Counter()
    for v in kw.values():
        df.update(set(v.split()))
    grandes = {t for t, n in df.items() if n > LIMITE}
    tirados = collections.Counter()
    novo = {}
    for c, v in kw.items():
        p = cat.get(c, {})
        k = p.get('k', '')
        nome = re.sub(r'[^a-z0-9]+', '', sa(p.get('n', '') + p.get('m', '')))
        fica = []
        for t in v.split():
            tc = re.sub(r'[^a-z0-9]+', '', t)
            if len(tc) >= 4 and tc in nome:
                fica.append(t)  # ex.: "macconkey" fica no "Ágar Mac Conkey"
                continue
            if t in grandes and t not in GERAIS and k not in MANTER_POR_CATEGORIA.get(t, ()):
                tirados[t] += 1
                continue
            fica.append(t)
        novo[c] = ' '.join(fica)
    df2 = collections.Counter()
    for v in novo.values():
        df2.update(set(v.split()))
    print('termos com mais de %d produtos: %d' % (LIMITE, len(grandes)))
    print('retirados:', ', '.join('%s(%d)' % x for x in tirados.most_common()))
    print('maiores depois:', ', '.join('%s(%d)' % x for x in df2.most_common(12)))
    if '--dry' not in sys.argv:
        json.dump(novo, open(R + 'kw.json', 'w', encoding='utf-8'), ensure_ascii=False, separators=(',', ':'))


if __name__ == '__main__':
    main()
