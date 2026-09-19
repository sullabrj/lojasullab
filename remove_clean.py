#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Remove all "Clean" brand products from the SULLAB catalog (lojasullab repo).
Run from the repo root. Prints a summary and writes removed_urls.txt with the
old URLs that now need 301 redirects (for the Cloudflare Worker)."""
import re, json, os, glob, sys

ROOT = os.getcwd()

def read(path):
    with open(os.path.join(ROOT, path), encoding='utf-8') as f:
        return f.read()

def write(path, content):
    with open(os.path.join(ROOT, path), 'w', encoding='utf-8') as f:
        f.write(content)

removed_urls = []

# ---------- 1. index.html: remove Clean entries from SEED + footer link ----------
html = read('index.html')
idx = html.find('var SEED=[')
if idx == -1:
    sys.exit('ERRO: var SEED= nao encontrado em index.html')
start = idx + len('var SEED=')
decoder = json.JSONDecoder()
seed, end = decoder.raw_decode(html, start)
clean_items = [x for x in seed if x.get('m') == 'Clean']
clean_codes = [x['c'] for x in clean_items]
print(f'[index.html] Clean no catalogo: {len(clean_items)}')
if len(clean_items) != 46:
    print(f'AVISO: esperava 46, encontrei {len(clean_items)} -- confira antes de prosseguir')

kept = [x for x in seed if x.get('m') != 'Clean']
new_seed_json = json.dumps(kept, ensure_ascii=False)
html = html[:idx] + 'var SEED=' + new_seed_json + ';' + html[end:]

footer_link = '<a href="/marca/clean.html" style="display:inline-block;color:#aec6e0;margin:0 14px 7px 0;font-size:12px">Clean</a>'
if footer_link in html:
    html = html.replace(footer_link, '')
    print('[index.html] link "Clean" removido do rodape (Marcas)')
else:
    print('AVISO: link do rodape "Clean" nao encontrado exatamente -- confira manualmente')
write('index.html', html)

# ---------- 2. map clean codes -> product page URLs via sitemap-produtos.xml ----------
sitemap_prod = read('sitemap-produtos.xml')
locs = re.findall(r'<loc>(https://lojasullabrj\.com\.br/p/[^<]+)</loc>', sitemap_prod)
code_to_url = {}
for code in clean_codes:
    suffix = '-' + code.lower() + '.html'
    found = [loc for loc in locs if loc.rsplit('/', 1)[-1].lower().endswith(suffix)]
    if len(found) != 1:
        print(f'AVISO: codigo {code} teve {len(found)} correspondencias no sitemap: {found}')
        continue
    code_to_url[code] = found[0]

print(f'[sitemap] {len(code_to_url)}/{len(clean_codes)} produtos localizados')

# ---------- 3. delete /p/*.html files ----------
deleted_files = 0
for code, url in code_to_url.items():
    fname = url.rsplit('/', 1)[-1]
    path = os.path.join(ROOT, 'p', fname)
    if os.path.exists(path):
        os.remove(path)
        deleted_files += 1
        removed_urls.append(url)
    else:
        print(f'AVISO: arquivo nao encontrado para remover: {path}')
print(f'[p/] {deleted_files} paginas de produto removidas')

# ---------- 4. delete marca/clean.html ----------
marca_path = os.path.join(ROOT, 'marca', 'clean.html')
if os.path.exists(marca_path):
    os.remove(marca_path)
    removed_urls.append('https://lojasullabrj.com.br/marca/clean.html')
    print('[marca/] clean.html removido')
else:
    print('AVISO: marca/clean.html nao encontrado')

# ---------- 5. sitemap-produtos.xml: remove the 46 <url> blocks ----------
removed_set = set(code_to_url.values())
def strip_urls(xml_text, urls_to_remove):
    count = 0
    for u in urls_to_remove:
        pattern = re.compile(r'<url>\s*<loc>' + re.escape(u) + r'</loc>.*?</url>\s*', re.S)
        new_text, n = pattern.subn('', xml_text)
        if n:
            count += n
            xml_text = new_text
    return xml_text, count

sitemap_prod_new, n1 = strip_urls(sitemap_prod, removed_set)
write('sitemap-produtos.xml', sitemap_prod_new)
print(f'[sitemap-produtos.xml] {n1} entradas removidas')

# ---------- 6. sitemap-categorias.xml: remove marca/clean.html ----------
sitemap_cat = read('sitemap-categorias.xml')
sitemap_cat_new, n2 = strip_urls(sitemap_cat, {'https://lojasullabrj.com.br/marca/clean.html'})
write('sitemap-categorias.xml', sitemap_cat_new)
print(f'[sitemap-categorias.xml] {n2} entradas removidas')

# ---------- 7. categoria/curativos-gaze-e-algodao.html: remove cards + JSON-LD + count ----------
cat_path = 'categoria/curativos-gaze-e-algodao.html'
if os.path.exists(os.path.join(ROOT, cat_path)):
    cat_html = read(cat_path)
    before_len = len(cat_html)
    card_removed = 0
    for u in removed_set:
        # card format: <a href="URL"><span class="nm">...</span><span class="prc">...</span><span class="cs">...</span></a>
        pattern = re.compile(r'<a href="' + re.escape(u) + r'"><span class="nm">.*?</span></a>')
        new_html, n = pattern.subn('', cat_html)
        if n:
            card_removed += n
            cat_html = new_html

    # JSON-LD ItemList: parse & filter
    ld_match = re.search(r'(<script type="application/ld\+json">)(\{"@context": "https://schema\.org", "@type": "ItemList".*?)(</script>)', cat_html, re.S)
    ld_removed = 0
    if ld_match:
        data = json.loads(ld_match.group(2))
        items = data['itemListElement']
        new_items = [it for it in items if it['url'] not in removed_set]
        ld_removed = len(items) - len(new_items)
        for i, it in enumerate(new_items, start=1):
            it['position'] = i
        data['itemListElement'] = new_items
        new_ld_json = json.dumps(data, ensure_ascii=False)
        cat_html = cat_html[:ld_match.start()] + ld_match.group(1) + new_ld_json + ld_match.group(3) + cat_html[ld_match.end():]

    # update visible count "(72)" -> new count, and h2
    m_h2 = re.search(r'<h2>Produtos de Curativos, gaze e algodão \((\d+)\)</h2>', cat_html)
    if m_h2:
        old_count = int(m_h2.group(1))
        new_count = old_count - card_removed
        cat_html = cat_html.replace(m_h2.group(0), f'<h2>Produtos de Curativos, gaze e algodão ({new_count})</h2>')
        print(f'[categoria] contagem do h2: {old_count} -> {new_count}')

    write(cat_path, cat_html)
    print(f'[categoria/curativos-gaze-e-algodao.html] {card_removed} cards removidos, {ld_removed} itens removidos do ItemList (bytes {before_len} -> {len(cat_html)})')
else:
    print('AVISO: pagina de categoria nao encontrada')

# ---------- 8. ft.json / kw.json: remove the 46 codes ----------
for fname in ('ft.json', 'kw.json'):
    if os.path.exists(os.path.join(ROOT, fname)):
        data = json.loads(read(fname))
        n_before = len(data)
        for code in clean_codes:
            data.pop(code, None)
        write(fname, json.dumps(data, ensure_ascii=False))
        print(f'[{fname}] {n_before - len(data)} entradas removidas')

# ---------- 9. write removed_urls.txt for the Cloudflare Worker redirect update ----------
with open(os.path.join(ROOT, 'removed_urls_clean.txt'), 'w', encoding='utf-8') as f:
    for u in removed_urls:
        f.write(u + '\n')
print(f'\nTotal de URLs antigas que precisam de redirect 301: {len(removed_urls)}')
print('Gravado em removed_urls_clean.txt')
