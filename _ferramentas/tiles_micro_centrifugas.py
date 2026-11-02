# -*- coding: utf-8 -*-
"""Cartões (800x600) da página inicial: Microscópios e Centrífugas, a partir das fotos já salvas em img/p/. Uso: python3 tiles_micro_centrifugas.py [microsc|centrif]"""
import os, sys
from PIL import Image, ImageFilter
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/'
TILES = {'microsc': ['MICB-10', 'MICBTRI10', 'MIBEST'], 'centrif': ['CT-10000', 'CT-4000Y', 'CT-12000']}

def carrega(cod):
    im = Image.open(R + f'img/p/{cod}.jpg').convert('RGB')
    m = Image.eval(im.convert('L'), lambda p: 0 if p > 245 else 255)
    box = m.getbbox() or (0, 0) + im.size
    return im.crop(box)

def fundo():
    t = Image.new('RGB', (800, 600))
    for y in range(600):
        v = 230 + int(10 * y / 600); t.paste((v, v + 5, v + 11), (0, y, 800, y + 1))
    return t

for k in (sys.argv[1:] or TILES):
    lista = TILES[k]; t = fundo(); larg = 800 // len(lista)
    for i, cod in enumerate(lista):
        im = carrega(cod); im.thumbnail((larg - 40, 380))
        m = Image.eval(im.convert('L'), lambda p: 0 if p > 245 else 255).filter(ImageFilter.MedianFilter(3))
        t.paste(im, (i * larg + (larg - im.width) // 2, 300 - im.height // 2 + 20), m)
    t.save(R + f'img/cat/{k}.jpg', 'JPEG', quality=84); t.save(R + f'img/cat/{k}.webp', 'WEBP', quality=80)
    s = t.resize((400, 300), Image.LANCZOS); s.save(R + f'img/cat/{k}-400.jpg', 'JPEG', quality=82); s.save(R + f'img/cat/{k}-400.webp', 'WEBP', quality=78)
    print('tile', k)
