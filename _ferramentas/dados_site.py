#!/usr/bin/env python3
"""Dados da loja (home do site) fora do index.html — 30/10/2026.

Onde fica cada coisa:
  data/catalogo.json  lista de produtos (antigo `var SEED=[...]` do index.html): c, n, m, k, img, img2, t (miniatura)
  data/precos.json    preços (antigo `window.PRECOS={...}`): "código": [preço, preço, null]
  js/loja.js          todo o JavaScript da loja (catálogo, carrinho, checkout, frete, QTD, DEPTS, fileiras do celular)

O index.html carrega esses arquivos com `?v=<hash>` (cache longo na Cloudflare sem servir preço velho).
Quem grava qualquer um deles TEM de chamar atualizar_versoes() no fim — as funções gravar_* já chamam.
Uso direto: python3 _ferramentas/dados_site.py   (só recalcula os hashes no index.html)
"""
import hashlib
import json
import os
import re

R = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/'
CATALOGO = R + 'data/catalogo.json'
PRECOS = R + 'data/precos.json'
LOJA_JS = R + 'js/loja.js'
INDEX = R + 'index.html'
VERSIONADOS = ['data/catalogo.json', 'data/precos.json', 'js/loja.js']


def ler_catalogo():
    return json.load(open(CATALOGO, encoding='utf-8'))


def ler_precos():
    return json.load(open(PRECOS, encoding='utf-8'))


def _grava(path, txt):
    old = open(path, encoding='utf-8').read() if os.path.exists(path) else None
    if old != txt:
        open(path, 'w', encoding='utf-8').write(txt)
        return True
    return False


def texto_catalogo(seed):
    # um produto por linha: diff legível no git e mesmo formato compacto do antigo SEED
    return '[\n' + ',\n'.join(json.dumps(p, ensure_ascii=False, separators=(',', ':')) for p in seed) + '\n]\n'


def texto_precos(pre):
    # mesmo formato do antigo window.PRECOS ("cód": [v, v, null]), um por linha
    return '{\n' + ',\n'.join(json.dumps(k, ensure_ascii=False) + ': ' + json.dumps(v) for k, v in pre.items()) + '\n}\n'


def gravar_catalogo(seed):
    mud = _grava(CATALOGO, texto_catalogo(seed))
    atualizar_versoes()
    return mud


def gravar_precos(pre):
    mud = _grava(PRECOS, texto_precos(pre))
    atualizar_versoes()
    return mud


def hash_arquivo(rel):
    return hashlib.sha1(open(R + rel, 'rb').read()).hexdigest()[:10]


def atualizar_versoes():
    """Grava no index.html o ?v=<hash> de cada arquivo versionado. Devolve True se o index mudou."""
    t = open(INDEX, encoding='utf-8').read()
    o = t
    for rel in VERSIONADOS:
        h = hash_arquivo(rel)
        t = re.sub(r'(/' + re.escape(rel) + r')\?v=[0-9a-f]+', r'\1?v=' + h, t)
    if t != o:
        open(INDEX, 'w', encoding='utf-8').write(t)
        return True
    return False


def ler_loja_js():
    return open(LOJA_JS, encoding='utf-8').read()


def gravar_loja_js(txt):
    mud = _grava(LOJA_JS, txt)
    atualizar_versoes()
    return mud


if __name__ == '__main__':
    print('index.html atualizado' if atualizar_versoes() else 'versões já corretas')
