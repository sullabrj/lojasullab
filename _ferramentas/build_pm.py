import re,glob,json,html,sys
import os; R=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+'/'
idx=open(R+'index.html',encoding='utf-8').read()
i=idx.find('var SEED=')+len('var SEED='); dec=json.JSONDecoder()
seed,_=dec.raw_decode(idx[i:])
info={str(p['c']).lower():p for p in seed}
j=idx.find('window.PRECOS='); pre,_=dec.raw_decode(idx[j+len('window.PRECOS='):])
pre={k.lower():v for k,v in pre.items()}
def brl(v): return 'R$ '+f'{v:,.2f}'.replace(',','X').replace('.',',').replace('X','.')
pages={}; cat={}
fs=sorted(glob.glob(R+'p/*.html'))
for f in fs:
    t=open(f,encoding='utf-8').read()
    if len(t)<2000: continue
    m=re.search(r'<b>C[óo]digo:</b>\s*([^<\s·]+)',t)
    code=m.group(1).strip().lower() if m else None
    c=re.search(r'class="crumb">.*?href="[^"]*/categoria/([^"]+)\.html"',t)
    url='https://lojasullabrj.com.br/p/'+f.split('/')[-1]
    pages[url]=(code,c.group(1) if c else None,f)
    if c: cat.setdefault(c.group(1),[]).append(url)
def card(url):
    code=pages.get(url,(None,))[0]; p=info.get(code) if code else None
    if not p: return None
    img=p.get('img') or ''
    if img and not img.startswith('http'): img='https://lojasullabrj.com.br/'+img.lstrip('/')
    if not img: img='https://lojasullabrj.com.br/img/logo-sullab.webp'
    pr=pre.get(code); v=pr[1] if pr and len(pr)>1 and pr[1] else 0
    ptxt=f'<b class="rp">{brl(v)}</b>' if v else '<b class="rp sc">Sob consulta</b>'
    n=html.escape(p['n'])
    return f'<a class="rc" href="{url}"><img src="{img}" alt="{n}" loading="lazy" width="160" height="160"><span class="rn">{n}</span>{ptxt}<span class="rv">Ver produto</span></a>'
TOP=['25492','454087','454036','456001','pa03','pa36','pa31','743','prd00003','450072']
ch=0;empty=0
for url,(code,ct,f) in pages.items():
    t=open(f,encoding='utf-8').read(); o=t
    if 'pm.css' not in t:
        t=t.replace('</head>','<link rel="stylesheet" href="/pm.css?v=1"><script src="/pm.js?v=1" defer></script>\n</head>',1)
    m=re.search(r'<div class="rel(?: rcards)?">(.*?)</div>',t,re.S)
    if m:
        links=re.findall(r'href="([^"]+)"',m.group(1))
        links=[l for l in links if l in pages and l!=url]
        if len(links)<4 and ct:
            pool=sorted([u for u in cat.get(ct,[]) if u!=url and u not in links],
                key=lambda u:(-(1 if pre.get(pages[u][0] or '') else 0),TOP.index(pages[u][0]) if pages[u][0] in TOP else 99))
            if not links: empty+=1
            links+=pool[:8-len(links)]
        if len(links)<4:
            tops=[u for u,v in pages.items() if v[0] in TOP and u!=url and u not in links]
            tops.sort(key=lambda u:TOP.index(pages[u][0]))
            links+=tops[:8-len(links)]
        cards=[c for c in (card(l) for l in links[:8]) if c]
        if cards:
            t=t[:m.start()]+'<div class="rel rcards">\n'+'\n'.join(cards)+'\n</div>'+t[m.end():]
    if t!=o:
        ch+=1
        if '--dry' not in sys.argv: open(f,'w',encoding='utf-8').write(t)
print('pages',len(pages),'changed',ch,'empty filled',empty)
