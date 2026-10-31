# Cloudflare — passo a passo no painel (31/10/2026)

Roteiro de cliques para aplicar no Chrome o que está em `_ferramentas/CLOUDFLARE_REGRAS_2026-10-30.md`
(4 regras de cache + 1 regra de cabeçalhos de segurança). Tempo estimado: 15 minutos. Nada aqui mexe em DNS.

> **Correção em relação ao arquivo de 30/10:** na Cloudflare, quando duas Cache Rules casam com o mesmo endereço,
> vale a configuração da regra **de baixo** (a última). No arquivo de 30/10 a regra 3 ("fotos e dados sem versão,
> navegador 1 dia") ficava abaixo das regras 1 e 2 e anularia o "1 ano no navegador" delas. Abaixo a regra 3 ganhou
> uma exclusão na expressão (`not ...`), então a ordem deixa de importar. Mesmo assim, crie na ordem indicada.

---

## 0. Antes de começar (1 minuto)

1. Abrir `https://dash.cloudflare.com` e entrar na conta.
2. Na lista **Domains** (ou "Websites"), clicar em **lojasullabrj.com.br**.
3. No menu da esquerda: **SSL/TLS → Overview**. Conferir que o modo está **Full** ou **Full (strict)**.
   Se estiver "Flexible", **parar** e me avisar (o HSTS da parte 2 não pode ser ligado com Flexible).
4. Menu da esquerda: **SSL/TLS → Edge Certificates**. Conferir que **Always Use HTTPS** está **On**.

---

## 1. Cache Rules (4 regras)

Caminho: menu da esquerda **Caching → Cache Rules** → botão azul **Create rule**
(no painel novo o mesmo lugar também aparece em **Rules → Overview → Create rule → Cache Rule**).
Se aparecer uma lista de modelos ("templates"), escolher **Create rule** / **Custom rule** (em branco).

Em cada regra a tela tem sempre os mesmos blocos. Para cada uma:

1. **Rule name**: colar o nome indicado.
2. **If incoming requests match…** → marcar **Custom filter expression**.
3. Clicar no link **Edit expression** (fica à direita, acima dos campos) → apagar o que houver → colar a expressão.
4. **Then… → Cache eligibility** → marcar **Eligible for cache**.
5. **Edge TTL** → clicar **+ Add setting** se não estiver visível → escolher
   **Ignore cache-control header and use this TTL** → no campo de tempo escolher o valor indicado.
6. **Browser TTL** → **+ Add setting** se preciso → escolher **Override origin and use this TTL** → valor indicado.
7. Não mexer em **Cache key**, **Serve stale**, **Respect strong ETags** etc. (deixar padrão; a `?v=` faz parte da chave).
8. Rolar até o fim → botão **Deploy** (não usar "Save as Draft").

### Regra A — criar primeiro
- **Rule name:** `Fotos, PDFs e dados sem versão (borda 1 ano, navegador 1 dia)`
- **Expressão:**
```
(http.host in {"lojasullabrj.com.br" "www.lojasullabrj.com.br"} and (starts_with(http.request.uri.path, "/img/") or starts_with(http.request.uri.path, "/docs/") or starts_with(http.request.uri.path, "/pdf/") or starts_with(http.request.uri.path, "/data/") or http.request.uri.path.extension in {"jpg" "jpeg" "png" "webp" "ico"}) and not starts_with(http.request.uri.path, "/img/t/") and not (starts_with(http.request.uri.path, "/data/") and http.request.uri.query contains "v="))
```
- **Edge TTL:** `1 year` · **Browser TTL:** `1 day`

### Regra B
- **Rule name:** `kw, ft, rastreio, pm (1 dia)`
- **Expressão:**
```
(http.host in {"lojasullabrj.com.br" "www.lojasullabrj.com.br"} and http.request.uri.path in {"/kw.json" "/ft.json" "/rastreio.js" "/pm.js" "/pm.css"})
```
- **Edge TTL:** `1 day` · **Browser TTL:** `1 day`

### Regra C
- **Rule name:** `Dados e JS da loja com versão (1 ano)`
- **Expressão:**
```
(http.host in {"lojasullabrj.com.br" "www.lojasullabrj.com.br"} and (starts_with(http.request.uri.path, "/data/") or starts_with(http.request.uri.path, "/js/")) and http.request.uri.query contains "v=")
```
- **Edge TTL:** `1 year` · **Browser TTL:** `1 year`

### Regra D
- **Rule name:** `Miniaturas com hash (1 ano)`
- **Expressão:**
```
(http.host in {"lojasullabrj.com.br" "www.lojasullabrj.com.br"} and starts_with(http.request.uri.path, "/img/t/"))
```
- **Edge TTL:** `1 year` · **Browser TTL:** `1 year`

Ao final, a lista em **Caching → Cache Rules** deve mostrar as 4 regras **Active**, nesta ordem: A, B, C, D.
Se a ordem ficou outra, arrastar pelo ícone de seis pontinhos à esquerda (opcional: com a exclusão da regra A não muda o resultado).

**Não criar regra para páginas `.html` nem para `/`.**

---

## 2. Cabeçalhos de segurança (1 regra)

Caminho: menu da esquerda **Rules → Transform Rules** → aba **Modify Response Header** → **Create rule**
(no painel novo: **Rules → Overview → Create rule → Response Header Transform Rule**).

1. **Rule name:** `Cabeçalhos de segurança`
2. **If incoming requests match…** → **Custom filter expression** → **Edit expression** → colar:
```
(http.host in {"lojasullabrj.com.br" "www.lojasullabrj.com.br"})
```
3. **Then… Modify response header** → no primeiro item escolher **Set static**, preencher **Header name** e **Value**;
   para cada linha seguinte clicar **+ Set new header** e repetir (sempre **Set static**):

| Header name | Value |
|---|---|
| `Strict-Transport-Security` | `max-age=31536000; includeSubDomains` |
| `X-Content-Type-Options` | `nosniff` |
| `Referrer-Policy` | `strict-origin-when-cross-origin` |
| `Permissions-Policy` | `camera=(), microphone=(), geolocation=(), interest-cohort=(), payment=(self)` |
| `X-Frame-Options` | `SAMEORIGIN` |

4. **Deploy**.

Se em **SSL/TLS → Edge Certificates → HTTP Strict Transport Security (HSTS)** já estiver ligado, **não** colocar as
duas primeiras linhas (Strict-Transport-Security e X-Content-Type-Options) — ficariam repetidas.
Não marcar "Preload" em lugar nenhum.

---

## 3. Conferir (2 minutos)

Abrir no Chrome, uma de cada vez, com **F12 → aba Network → recarregar (Ctrl+R / Cmd+R) → clicar na linha do arquivo → Headers**:

| Endereço | O que deve aparecer em "Response Headers" |
|---|---|
| `https://lojasullabrj.com.br/data/precos.json?v=teste` (abrir 2 vezes) | `cache-control: max-age=31536000` e, na 2ª vez, `cf-cache-status: HIT` |
| `https://lojasullabrj.com.br/img/logo-sullab.webp` | `cache-control: max-age=86400` |
| `https://lojasullabrj.com.br/` | o `cache-control` de antes (curto) + `strict-transport-security`, `x-frame-options`, `x-content-type-options`, `referrer-policy`, `permissions-policy` |

Depois, testar a loja: buscar "tubo", pôr um item no carrinho, abrir o checkout e calcular o frete com um CEP.

## 4. Se algo der errado

- Em **Caching → Cache Rules** (ou **Transform Rules**), desligar a chave da regra suspeita.
- **Caching → Configuration → Purge Everything** → confirmar.
- Trocou foto ou PDF com o mesmo nome? **Caching → Configuration → Custom Purge → URL** → colar o endereço completo
  do arquivo (ex.: `https://lojasullabrj.com.br/img/p/454036.webp`) → **Purge**.
