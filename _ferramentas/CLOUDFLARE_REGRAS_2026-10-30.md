# Cloudflare — regras de cache e cabeçalhos de segurança (30/10/2026)

**Nada disto foi aplicado.** Este arquivo serve para o Eduardo aplicar no painel da Cloudflare, ou autorizar que alguém aplique.
Zona: `lojasullabrj.com.br` (o GitHub Pages fica atrás da Cloudflare, com proxy laranja ligado).

Por que fazer: o GitHub Pages manda `Cache-Control: max-age=600` (10 min) em tudo e não deixa mudar isso. O PageSpeed
mostra "1.207 KiB a economizar com cache" porque cada visita volta ao servidor depois de 10 min. Com as regras abaixo a
Cloudflare passa a guardar as fotos, os PDFs e os dados da loja por 1 ano, e o navegador do cliente também.

**Por que dá para cachear 1 ano sem servir preço velho:**
- `data/catalogo.json`, `data/precos.json` e `js/loja.js` são chamados com `?v=<hash do conteúdo>` (gravado no
  `index.html` pelo `_ferramentas/dados_site.py`; o robô Biolog e os outros scripts chamam isso sozinhos). Mudou o preço,
  muda o hash, muda a URL, e o cache antigo não é mais usado.
- As miniaturas `img/t/<hash>.webp` têm o hash da foto original no nome.
- A página `index.html` e as demais páginas `.html` **não** entram no cache longo (ficam como estão hoje), porque são
  elas que levam os endereços novos.

Atenção às fotos e aos PDFs: eles são trocados **com o mesmo nome** (ex.: `docs/Tabela_de_Precos_SULLAB.pdf`,
`img/p/454036.webp`). Com 1 ano de cache, uma foto ou um PDF trocado com o mesmo nome demora a aparecer. Por isso:
- no navegador do cliente (Browser TTL), 1 ano só para o que tem versão na URL; fotos e PDFs ficam com 1 dia;
- na Cloudflare (Edge TTL), 1 ano para tudo de `/img`, `/docs` e `/data`, e depois de trocar foto ou PDF com o mesmo
  nome é preciso **Purge** (Caching → Configuration → Custom Purge → URL). O workflow de PDFs não faz esse purge
  sozinho; se quiser automatizar, gerar um API Token com "Zone.Cache Purge" e me pedir para colocar no workflow.

---

## 1. Cache Rules (Caching → Cache Rules → Create rule)

Ordem: de cima para baixo, na ordem abaixo. Em todas: **Cache eligibility = Eligible for cache**.

### Regra 1 — "Dados e JS da loja com versão (1 ano)"
- **When incoming requests match** → Custom filter expression → Edit expression:
  ```
  (http.host in {"lojasullabrj.com.br" "www.lojasullabrj.com.br"} and (starts_with(http.request.uri.path, "/data/") or starts_with(http.request.uri.path, "/js/")) and http.request.uri.query contains "v=")
  ```
- **Edge TTL**: Ignore cache-control header and use this TTL → **1 year**
- **Browser TTL**: Override origin and use this TTL → **1 year**
- **Cache key**: deixar padrão (a query string `?v=` faz parte da chave; não ativar "Ignore query string")

### Regra 2 — "Miniaturas com hash (1 ano)"
- Expression:
  ```
  (http.host in {"lojasullabrj.com.br" "www.lojasullabrj.com.br"} and starts_with(http.request.uri.path, "/img/t/"))
  ```
- **Edge TTL**: Ignore cache-control header → **1 year**
- **Browser TTL**: Override origin → **1 year**

### Regra 3 — "Fotos, PDFs e dados sem versão (borda 1 ano, navegador 1 dia)"
- Expression:
  ```
  (http.host in {"lojasullabrj.com.br" "www.lojasullabrj.com.br"} and (starts_with(http.request.uri.path, "/img/") or starts_with(http.request.uri.path, "/docs/") or starts_with(http.request.uri.path, "/pdf/") or starts_with(http.request.uri.path, "/data/") or http.request.uri.path.extension in {"jpg" "jpeg" "png" "webp" "ico"}))
  ```
- **Edge TTL**: Ignore cache-control header → **1 year**
- **Browser TTL**: Override origin → **1 day**
- Obs.: `data/biolog_usd.json` (sem `?v=`) também cai aqui — ele só é lido pelo robô no GitHub Actions, não pelo site.

### Regra 4 — "kw.json, ft.json, rastreio.js, pm.js, pm.css (1 dia)"
- Expression:
  ```
  (http.host in {"lojasullabrj.com.br" "www.lojasullabrj.com.br"} and http.request.uri.path in {"/kw.json" "/ft.json" "/rastreio.js" "/pm.js" "/pm.css"})
  ```
- **Edge TTL**: Ignore cache-control header → **1 day**
- **Browser TTL**: Override origin → **1 day**
- (`rastreio.js`, `pm.js` e `pm.css` são chamados com `?v=N`; ao mudar o arquivo, subir o número em todas as páginas.)

**Não criar regra para `*.html` nem para `/`.** A página inicial e as páginas de produto têm de continuar sem cache longo.

---

## 2. Cabeçalhos de segurança (Rules → Transform Rules → Modify Response Header → Create rule)

### Regra "Cabeçalhos de segurança"
- **When incoming requests match** → Custom filter expression:
  ```
  (http.host in {"lojasullabrj.com.br" "www.lojasullabrj.com.br"})
  ```
- **Then** → Modify response header → **Set static** (um item por cabeçalho):

| Cabeçalho | Valor |
|---|---|
| `Strict-Transport-Security` | `max-age=31536000; includeSubDomains` |
| `X-Content-Type-Options` | `nosniff` |
| `Referrer-Policy` | `strict-origin-when-cross-origin` |
| `Permissions-Policy` | `camera=(), microphone=(), geolocation=(), interest-cohort=(), payment=(self)` |
| `X-Frame-Options` | `SAMEORIGIN` |

Notas:
- **HSTS**: antes, confirmar em SSL/TLS que o modo é **Full** (ou Full strict) e que "Always Use HTTPS" está ligado.
  `includeSubDomains` vale também para `api.lojasullabrj.com.br` (Worker de frete), que já é HTTPS, então não há
  problema. **Não** marcar `preload` agora: depois de entrar na lista de preload do navegador não dá para voltar atrás
  rápido. Alternativa no painel: SSL/TLS → Edge Certificates → HTTP Strict Transport Security (HSTS) → Enable, com
  Max Age 12 months, Include subdomains ligado, Preload desligado, No-Sniff ligado — tem o mesmo efeito dos dois primeiros
  itens da tabela; nesse caso, não repetir esses dois na Transform Rule.
- **X-Frame-Options SAMEORIGIN**: a loja não é aberta dentro de iframe de outro site. Os banners de afiliado
  (`materiais-afiliados/`) são imagens com link, não iframes, então continuam funcionando.
- **Permissions-Policy**: `payment=(self)` mantém o Pix/cartão do Mercado Pago dentro do site; câmera, microfone e
  localização ficam bloqueados (o site não usa).
- Não foi incluída Content-Security-Policy: o site usa muito JavaScript inline e scripts de Google, Meta, Clarity,
  Firebase e Mercado Pago; uma CSP errada quebra o checkout. Se quiser, preparo uma em modo "Report-Only" primeiro.

---

## 3. Como conferir depois de aplicar

No Terminal do Mac:
```
curl -sI "https://lojasullabrj.com.br/data/precos.json?v=teste" | grep -i "cache-control\|cf-cache-status"
curl -sI "https://lojasullabrj.com.br/img/logo-sullab.webp" | grep -i "cache-control\|cf-cache-status"
curl -sI "https://lojasullabrj.com.br/" | grep -i "cache-control\|strict-transport\|x-frame\|x-content\|referrer\|permissions"
```
Esperado: `cache-control: max-age=31536000` no JSON (`cf-cache-status: HIT` na segunda chamada), `max-age=86400` na foto,
e na página inicial o `cache-control` de antes mais os cinco cabeçalhos de segurança.

Se algo der errado: desligar a regra (botão ao lado dela) e fazer **Purge Everything** em Caching → Configuration.
