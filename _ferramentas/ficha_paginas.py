# -*- coding: utf-8 -*-
"""Páginas /p/: troca o texto solto da .ficha pela tabela de data/ficha.json (mesma do painel da loja)
e tira a arte (img/a) da galeria — a ficha passa a ter tudo. Idempotente. 31/10/2026 (dono)."""
import json, os, re, glob, html
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
F = json.load(open('data/ficha.json', encoding='utf-8'))
CSS = ".ficha table{width:100%;border-collapse:collapse;font-size:13.5px;line-height:1.45;margin-top:6px}.ficha th{text-align:left;color:#5f6b7c;font-weight:600;padding:5px 10px 5px 0;vertical-align:top;white-space:nowrap;width:36%}.ficha td{color:#1f2a3d;font-weight:600;padding:5px 0;vertical-align:top}.ficha tr+tr th,.ficha tr+tr td{border-top:1px solid #eef2f8}.ficha ul{margin:6px 0 0;padding-left:18px}.ficha li{margin:2px 0}"
RX_FICHA = re.compile(r'<div class="ficha">(.*?)</div>', re.S)
RX_ARTE = re.compile(r'<button type="button" aria-label="Informações técnicas"[^>]*>.*?</button>', re.S)
RX_SKU = re.compile(r'"sku":\s*"([^"]+)"')
def troca_ficha(s, novo):
    i = s.find('<div class="ficha">')
    if i < 0: return s
    j = i + len('<div class="ficha">'); prof = 1
    rx = re.compile(r'<div\b|</div>')
    while prof:
        m = rx.search(s, j)
        if not m: return s
        prof += 1 if m.group(0) != '</div>' else -1
        j = m.end()
    return s[:i] + novo + s[j:]
def tabela(f):
    h = '🔬 <b>Ficha técnica</b><table>' + ''.join('<tr><th>%s</th><td>%s</td></tr>' % (html.escape(k), html.escape(v)) for k, v in f['rows']) + '</table>'
    if f.get('why'):
        h += '<div style="margin-top:8px"><b>Por que escolher</b><ul>' + ''.join('<li>%s</li>' % html.escape(w) for w in f['why']) + '</ul></div>'
    return h
n_f = n_a = 0
for p in glob.glob('p/*.html'):
    s = open(p, encoding='utf-8').read()
    if 'http-equiv="refresh"' in s: continue
    o = s
    m = RX_SKU.search(s); c = m.group(1) if m else None
    f = F.get(c)
    if f and f.get('rows'):
        s2 = troca_ficha(s, '<div class="ficha">' + tabela(f) + '</div>')
        if s2 != s:
            s = s2; n_f += 1
        if '.ficha table{' not in s and '.ficha{' in s:
            s = s.replace('.ficha{', CSS + '.ficha{', 1)
    s2 = RX_ARTE.sub('', s)
    if s2 != s: s = s2; n_a += 1
    # faixa de miniaturas com uma foto só não faz sentido
    s = re.sub(r'<div class="th">(?:(?!</div>).)*?<button[^>]*>(?:(?!</div>).)*?</button></div>', lambda m: '' if m.group(0).count('<button') == 1 else m.group(0), s, count=1, flags=re.S)
    if s != o: open(p, 'w', encoding='utf-8').write(s)
print('fichas em tabela:', n_f, '| artes tiradas da galeria:', n_a)
