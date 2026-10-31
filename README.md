# lojasullab
Site da loja SULLAB (lojasullabrj.com.br) — catálogo de produtos para laboratório. GitHub Pages atrás da Cloudflare.

## Onde ficam os dados da loja (desde 30/10/2026)

| Arquivo | O que tem | Quem grava |
|---|---|---|
| `data/catalogo.json` | produtos da home (código, nome, marca, categoria, foto, miniatura `t`) — era o `var SEED` do index.html | `adiciona_cral_vidraria.py`, `miniaturas.py` |
| `data/precos.json` | preços `"código": [preço, preço, null]` — era o `window.PRECOS` do index.html | robô Biolog (`atualiza_biolog.py`), `ebram_linha_menor.py`, `adiciona_*` |
| `js/loja.js` | todo o JavaScript da loja (busca, grade, carrinho, checkout, frete, QTD, DEPTS, fileiras do celular) | à mão |
| `index.html` | só a página; carrega os três arquivos acima com `?v=<hash>` | `dados_site.py` grava o hash |

**Mexeu em `data/*.json` ou `js/loja.js` à mão? Rode `python3 _ferramentas/dados_site.py`** — ele atualiza o `?v=` no
`index.html`. Sem isso o navegador/Cloudflare pode continuar com o arquivo antigo (preço velho). Os scripts de
`_ferramentas/` já fazem isso sozinhos.

O robô do WhatsApp (repositório `whatsapp-sullab`, `app/site_catalogo.py`) lê o catálogo e os preços do site para montar
o link `?carrinho=`: precisa da versão que entende os JSON (branch `catalogo-json-site-2026-10-30` daquele repositório).

## Ferramentas (`_ferramentas/`)
- `dados_site.py` — leitura/gravação de `data/*.json` e `js/loja.js` + hash no index.html.
- `atualiza_biolog.py` — preços Biolog pelo dólar (Action diária `biolog-dolar.yml`).
- `gerar_pdfs.py` — tabela e catálogos em PDF (Action `pdfs.yml`).
- `miniaturas.py` — miniaturas WebP 320 px (`img/t/`) para os cartões; rodar depois de cadastrar foto ou produto.
- `build_pm.py`, `ebram_linha_menor.py`, `adiciona_cral_vidraria.py`, `fotos_cral.py` — manutenção do catálogo.
- `CLOUDFLARE_REGRAS_2026-10-30.md` — regras de cache e cabeçalhos de segurança para aplicar na Cloudflare.
