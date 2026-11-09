#!/usr/bin/env python3
"""Insere os guias novos no rodapé (lista 'Guias e conteúdo') de todas as páginas. Idempotente."""
import glob, os
R=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+'/'
B='https://lojasullabrj.com.br/guia/'
NOVOS=[('agar-sangue-de-carneiro-para-que-serve','Ágar sangue de carneiro: para que serve'),
('agar-mueller-hinton-antibiograma','Ágar Mueller-Hinton e antibiograma'),
('agar-macconkey-para-que-serve','Ágar MacConkey: como ler as colônias'),
('plasma-de-coelho-prova-da-coagulase','Plasma de coelho e prova da coagulase')]
ANC='<a href="'+B+'agar-thayer-martin-quando-usar.html">Ágar Thayer-Martin: quando usar</a>'
n=0
for f in glob.glob(R+'**/*.html',recursive=True):
    s=open(f,encoding='utf8').read()
    if ANC not in s: continue
    add=''.join(f'<a href="{B}{k}.html">{t}</a>' for k,t in NOVOS if f'guia/{k}.html">' not in s.split('<footer class="siteftr">')[-1])
    if not add: continue
    s=s.replace(ANC,ANC+add,1); open(f,'w',encoding='utf8').write(s); n+=1
print('arquivos alterados:',n)
