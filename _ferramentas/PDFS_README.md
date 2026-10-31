# PDFs comerciais automáticos (tabela de preços e catálogos)

Gerador: `_ferramentas/gerar_pdfs.py` · Workflow: `.github/workflows/pdfs.yml`

## O que é gerado (em `docs/`)

| Arquivo | Conteúdo |
|---|---|
| `Tabela_de_Precos_SULLAB.pdf` | Tubos e agulhas Greiner Vacuette e testes rápidos: código, produto, embalagem, preço da embalagem e preço por unidade/teste. Cada linha tem link "Comprar" que abre o carrinho do site com o item. QR Code na capa. Regras comerciais no fim e resumo no rodapé de toda página. |
| `Catalogo_SULLAB_Vacuette_e_Testes_Rapidos.pdf` | O mesmo conteúdo com foto pequena (JPEG q70, máx. 360 px), descrição curta, código, embalagem, preço e link. Fica abaixo de 1 MB. |
| `Tabela_SULLAB_Tubos_Vacuette.pdf` / `Catalogo_SULLAB_Tubos_Vacuette.pdf` | Só tubos e agulhas Vacuette (catálogo com guia de uso). Anúncio "Tubos de coleta a vácuo Vacuette". |
| `Tabela_SULLAB_Testes_Rapidos.pdf` / `Catalogo_SULLAB_Testes_Rapidos.pdf` | Só testes rápidos. Anúncio de testes rápidos. |
| `Tabela_SULLAB_Meios_de_Cultura_NewProv.pdf` / `Catalogo_SULLAB_Meios_de_Cultura_NewProv.pdf` | Placas prontas, tubos e frascos NewProv (`k=meio`, marca Newprov, com preço). Anúncio "Microbiologia de alimentos e água" / placas. |
| `Catalogo_SULLAB_Completo.pdf` | Todas as categorias do site (mesmas de `DEPTS` no index.html), sem fotos, em tabela, com índice clicável e botão "Comprar" por item (itens sem preço: "Sob consulta" e botão "Consultar", que abre a busca do site). Substitui `pdf/SULLAB_Catalogo_Precos_CNPJ.pdf`. |

Links dos produtos: `https://lojasullabrj.com.br/?carrinho=COD:1&add=1&utm_source=pdf&utm_medium=<tabela|catalogo|catalogo_completo>`
(o `aplicarUrl()` do index.html lê `carrinho=` e abre o carrinho). QR Code: `/?utm_source=pdf&utm_medium=qr&utm_campaign=<pdf>`.

Padrão visual (PDF ao cliente): letra grande, modelo simples e espaçado, só azul `#1F4E79` (sem degradê), logo `img/logo-sullab.png`,
**sem data impressa** — só "versão mmm/aaaa" discreta no rodapé (mês do último commit que mexeu nos preços; `--versao` muda).
Fonte Liberation Sans embutida em `_ferramentas/fontes/` (licença OFL em `LICENSE-OFL.txt`) para o PDF sair igual em qualquer máquina.

## Como rodar

```bash
pip install reportlab==5.0.1 qrcode==8.2 pillow==12.3.0      # (no Mac/Linux local: --break-system-packages se pedir)
python3 _ferramentas/gerar_pdfs.py --fonte auto                # padrão
python3 _ferramentas/gerar_pdfs.py --fonte html                # força index.html
python3 _ferramentas/gerar_pdfs.py --fonte json                # força data/catalogo.json + data/precos.json
python3 _ferramentas/gerar_pdfs.py --saida /tmp/teste          # testar sem mexer em docs/
python3 _ferramentas/gerar_pdfs.py --versao "nov/2026"         # texto da versão no rodapé
```

Fonte dos dados (`--fonte auto`): se existirem **os dois** `data/catalogo.json` e `data/precos.json`, usa eles; senão lê do
`index.html` (`window.PRECOS` = preços, `SEED` = catálogo, `window.QTD` = itens por embalagem, `GREINER_ORDEM`/`TR_TOP` = ordem
e seleção da tabela, `DEPTS` = categorias). Formatos JSON aceitos:
- `precos.json`: `{"COD": [de, por, x]}` (igual a `window.PRECOS`), `{"COD": 12.3}`, `{"COD": {"preco": 12.3}}` ou `{"precos": {...}}`;
- `catalogo.json`: lista ou `{"produtos": [...]}`, cada item com `c/n/m/k/img` (igual ao `SEED`) ou `codigo/nome/marca/categoria/imagem`, `qtd` opcional;
- `data/qtd.json` opcional (igual a `window.QTD`).

Determinístico e idempotente: reportlab em modo `invariant` (sem data/ID aleatório no PDF), fotos recomprimidas sempre do mesmo
jeito; o arquivo só é regravado se o conteúdo mudou (a saída mostra o sha256 e "sem mudança"/"atualizado").

O script avisa (`AVISO: ...`) se o index.html deixar de conter algum trecho das regras comerciais (2x sem juros, 28 ou 45 dias,
R$ 100/150/400, Pix 5%/3%, 40 anos). Se a regra mudar no site, atualizar a lista `REGRAS` e `CONFERE_SITE` no gerador.

## Workflow (`.github/workflows/pdfs.yml`)

Roda quando `index.html`, `data/*.json` ou o gerador mudam na `main`, todo dia às **08:20 de Brasília** (depois do robô
"Preços Biolog pelo dólar do dia" das 08:07 — o push desse robô usa `GITHUB_TOKEN` e por isso não dispara outros workflows; o
horário diário cobre isso) e manualmente (`workflow_dispatch`). Faz commit só se algum PDF mudou.
As versões das bibliotecas estão fixas no workflow para o PDF do robô sair idêntico ao gerado localmente.

## Pendências fora deste branch

1. **PDF antigo `/pdf/SULLAB_Catalogo_Precos_CNPJ.pdf` (setembro, 875 preços defasados, "12x") deve ser retirado** — foi
   mantido de propósito. Substituto: `docs/Catalogo_SULLAB_Completo.pdf`. Antes de apagar, trocar qualquer link externo
   (WhatsApp, e-mail, Google, anúncios) que aponte para `/pdf/SULLAB_Catalogo_Precos_CNPJ.pdf`; no repositório nenhum arquivo
   aponta para ele hoje (conferido em 30/10/2026). `pdf/SULLAB_Apresentacao.pdf` não foi avaliado.
2. **Linkar o catálogo completo no site**: o `index.html` hoje só linka `/docs/Catalogo_SULLAB_Vacuette_e_Testes_Rapidos.pdf`.
   Incluir `/docs/Catalogo_SULLAB_Completo.pdf` e `/docs/Tabela_de_Precos_SULLAB.pdf` onde fizer sentido (fica para quem edita o index.html).
3. **Robô de WhatsApp (repositório `whatsapp-sullab`)**: ele envia cópias guardadas em `app/material/`. Essas cópias ficam
   desatualizadas a cada mudança de preço. Escolher um caminho:
   - **preferido:** o robô passa a enviar os PDFs direto do site (`https://lojasullabrj.com.br/docs/Tabela_de_Precos_SULLAB.pdf`,
     `.../docs/Catalogo_SULLAB_Vacuette_e_Testes_Rapidos.pdf`, `.../docs/Catalogo_SULLAB_Completo.pdf`) — a API do WhatsApp aceita
     documento por link; os nomes de arquivo aqui são estáveis;
   - **ou** um workflow no `whatsapp-sullab` (ou um passo extra neste) copia os PDFs de `docs/` para `app/material/` quando
     mudarem (precisa de token com escrita no outro repositório).
   Até isso ser feito, as cópias de `app/material/` podem estar com a tabela antiga ("2x sem juros acima de R$ 800", errado).
