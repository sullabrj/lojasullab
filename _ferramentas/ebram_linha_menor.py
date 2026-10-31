#!/usr/bin/env python3
"""Ebram: linha menor (200 mL / kits fracionados) com markup 10 pontos acima da linha Bulk equivalente (28/10/2026).

Regra do Eduardo: a Bulk fica no markup atual do site; o item igual de menor volume fica um pouco mais caro
(markup da Bulk + 10 p.p.), para o cliente ver vantagem na Bulk. Só sobe preço, nunca baixa.
Custos: Tabela_Precos_Ebram_2026 (Lista Distribuidor jan/26). Uso: python3 _ferramentas/ebram_linha_menor.py [--dry]
"""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import atualiza_biolog as ab

# (bulk, menor, custo bulk, custo menor)
PARES = [("13000","3000",170.11,77.23),("13001","3001",43.39,22.73),("13002","3002",97.18,81.66),
 ("13003","3003",97.18,81.66),("13004","3004",96.77,51.60),("13034","3034",42.01,22.20),("13006","3006",39.47,24.52),
 ("13007","3007",259.97,111.82),("13008","3008",188.57,73.50),("13036","3036",182.37,96.53),("13010","3010",124.99,46.27),
 ("13011","3011",151.07,95.27),("13012","3012",111.61,54.61),("13026","3026",570.08,209.77),("13014","3014",270.22,129.61),
 ("13046","3046",468.20,183.75),("13016","3016",240.03,102.01),("13017","3017",240.03,102.01),("13049","3041",262.99,117.13),
 ("13050","3042",558.33,274.93),("13043","3043",157.87,78.95),("13037","3037",107.52,76.71),("13044","3044",189.17,93.29),
 ("13029","3029",72.13,50.35)]

def main():
    PRE = ab.ds.ler_precos()  # data/precos.json (30/10/2026)
    OLD, NEW = {}, {}
    for b, m, cb, cm in PARES:
        if b not in PRE or m not in PRE:
            print('fora do site:', b, m); continue
        mk = PRE[b][1] / cb
        novo = round(cm * (mk + 0.10), 2)
        atual = PRE[m][1]
        if novo > atual + 0.009:
            OLD[m], NEW[m] = atual, novo
        print(f'{m}: bulk {b} markup {mk-1:.0%} -> menor {mk-1+0.10:.0%} | {atual:.2f} -> {max(novo, atual):.2f}')
    if '--dry' in sys.argv or not NEW:
        return
    ab.trocar(OLD, NEW)
    json.dump(NEW, open('/tmp/ebram_novos.json', 'w'))

if __name__ == '__main__':
    main()
