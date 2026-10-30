# Notas do código — check-up de 30/10/2026

## Pendências fora do repositório (fazer à mão)

### 1. Apps Script (SHEET_ENDPOINT) precisa validar o campo `t`
Desde 30/10/2026 o site manda um campo `t` com um token fixo nos POSTs de **eventos** e **indicação** para o Apps Script
(`https://script.google.com/macros/s/AKfycbyPK…/exec`):

- `sullabEvent(type, extra)` em `index.html` — todos os eventos (carrinho, busca sem resultado, conta_cadastro, etc.);
- `conv_meta` (sendBeacon depois do pagamento) em `index.html`;
- `indicador_cadastro` em `indique.html`.

Token atual: `sl-2d26d03b37c9301cd7f3ac49` (constante `SULLAB_EVT_TOKEN`, definida em `index.html` e em `indique.html`).

O que fazer no Apps Script (não está no repositório e não foi alterado):
```js
var EVT_TOKEN = 'sl-2d26d03b37c9301cd7f3ac49';
// no doPost(e), antes de gravar um evento/indicação:
var b = JSON.parse(e.postData.contents);
var ehEvento = b.type || b.action === 'conv_meta';
if (ehEvento && b.t !== EVT_TOKEN) return ContentService.createTextOutput('{"ok":false}');
```
Não exigir o token nas ações da área do cliente (`loginDoc`, `meuspedidos`, `danfe`, `verificaremail`, `definirSenha`) nem no
rastreio por JSONP (`?action=rastreio`): essas chamadas não mandam `t` e já têm a própria validação (idToken/chave).
O token fica visível no código-fonte do site: ele só barra spam automático genérico, não é senha. Para trocar, mudar
nos dois arquivos e no Apps Script ao mesmo tempo.

### 2. Programa de indicação: comissão passou de 3% para 5%
Os textos do site (`index.html`, `indique.html`, `termos.html`) já dizem 5%. O cálculo da comissão não está no
repositório (é feito na planilha/Apps Script): ajustar lá para 5%.

### 3. Catálogo JSON (SEED e window.PRECOS) — não movido nesta rodada
Mover `var SEED=[…]` e `window.PRECOS={…}` para `data/catalogo.json` foi avaliado e **não** foi feito:
- `_ferramentas/atualiza_biolog.py` (Action diária de preços Biolog), `build_pm.py`, `ebram_linha_menor.py` e
  `adiciona_cral_vidraria.py` leem e reescrevem `window.PRECOS=` / `var SEED=` dentro de `index.html`; o
  `atualiza_biolog.py` também troca o preço nas entradas `"código": [v, v, null]` do index;
- o JS da home usa `SEED`, `CATALOG` e `window.PRECOS` de forma síncrona logo no carregamento (boot(), cartões
  pré-montados, carrinho salvo, deep-links `?orcar=`, `?lista=`, carrinho por link), e os blocos seguintes
  embrulham funções que dependem disso já estarem prontos.
Para mover com segurança é preciso: (a) mudar os 4 scripts para ler/gravar `data/catalogo.json`; (b) transformar o
boot em assíncrono (esperar o fetch) e revisar todos os pontos que leem SEED/PRECOS antes do boot. Ganho estimado:
~370 KB a menos no HTML da home (o JSON passa a ficar em cache do navegador).

---

# Comentários retirados do HTML público em 30/10/2026

Estes comentários estavam no HTML publicado (visíveis a qualquer visitante com "ver código-fonte"). Foram movidos para cá
para não expor regras internas (margens, casos de clientes, decisões). O código não mudou: a árvore sintática (AST) de cada
bloco `<script>` foi comparada antes/depois e é idêntica.

Formato: arquivo · linha (no arquivo ANTES da limpeza) · tipo · comentário · trecho de código logo depois do comentário.


## 404.html

- L35 · JS · marcas antigas que apareciam como prefixo de caminho (ex.: /descarpack/seringas/)  
  → `var MARCAS = ['descarpack','cral','cralplast','biocon','uniqmed','kasvi','newprov','labt`
- L38 · JS · pega o "miolo" pra virar termo de busca  
  → `var termo = seg;`
- L41 · JS · 1) /produtos/<slug>/... -> usa o slug do produto  
  → `var mp = seg.match(/produtos?\/([^\/]+)/);`
- L46 · JS · 2) /<marca>/<categoria>/ -> usa a categoria (parte mais útil pra busca)  
  → `var parts = seg.split('/').filter(Boolean);`
- L51 · JS · 3) caminho simples: usa a última parte significativa  
  → `termo = parts[parts.length - 1] || seg;`
- L56 · JS · limpa o termo: tira hifens, "1" no fim (coleções antigas), tamanhos/qtd e códigos  
  → `termo = termo`
- L60 · JS · "swabs1" -> "swabs", "testes-rapidos1" -> "testes rapidos"  
  → `.replace(/\s+/g,' ')`

## catalogo.html

- L8 · CSS · ---------- capa ----------  
  → `.capa{position:relative;background:linear-gradient(140deg,#16456e 0%,#123a5e 45%,#0b2740 1`
- L28 · CSS · ---------- nav ----------  
  → `.nav{position:sticky;top:0;z-index:50;background:rgba(255,255,255,.93);backdrop-filter:sat`
- L44 · CSS · ---------- blocos institucionais ----------  
  → `.stats{display:grid;grid-template-columns:repeat(auto-fit,minmax(140px,1fr));gap:12px;marg`
- L56 · CSS · ---------- seções ----------  
  → `h2{scroll-margin-top:112px;font-size:clamp(1.12rem,3.2vw,1.48rem);color:var(--brand);margi`
- L61 · CSS · ---------- cards ----------  
  → `.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(186px,1fr));gap:14px;marg`
- L83 · CSS · ---------- mosaico de fotos ----------  
  → `.notaimg{font-size:.77rem;color:#7a6534;background:#fdf6e6;border:1px solid #f0e0bb;border`
- L91 · CSS · ---------- tabelas ----------  
  → `.tw{background:var(--card);border:1px solid var(--line);border-radius:var(--r);box-shadow:`
- L105 · CSS · ---------- equipamentos ----------  
  → `.eq{display:grid;grid-template-columns:196px 1fr;gap:20px;background:var(--card);border:1p`
- L118 · CSS · ---------- cta final ----------  
  → `.cta{background:linear-gradient(135deg,#16456e,#0b2740);color:#fff;border-radius:18px;padd`
- L128 · CSS · ---------- flutuantes ----------  
  → `.fab{position:fixed;right:15px;bottom:15px;z-index:60;display:flex;flex-direction:column;g`
- L138 · CSS · ---------- responsivo ----------  
  → `@media(max-width:900px){.eq{grid-template-columns:150px 1fr;gap:16px}}`
- L161 · CSS · ---------- impressão ----------  
  → `@media print{`
- L190 · HTML · crédito MOVA Films  
  → `<div class="mova-band" style="background:repeating-linear-gradient(90deg,#3a3f47 0 14px,tr`

## faq.html

- L91 · HTML · crédito MOVA Films  
  → `<div class="mova-band" style="background:repeating-linear-gradient(90deg,#3a3f47 0 14px,tr`

## index.html

- L52 · CSS · TOP UTILITY  
  → `.util{background:var(--navy-d);color:#cdddf0;font-size:12.5px}`
- L59 · CSS · HEADER  
  → `header{background:#fff;border-bottom:1px solid var(--line);position:sticky;top:0;z-index`
- L79 · CSS · TRUST BAR  
  → `.trust{background:linear-gradient(90deg,var(--navy),var(--navy-l))}`
- L84 · CSS · DEPT NAV  
  → `.deptbar{background:#fff;border-bottom:1px solid var(--line);position:sticky;top:80px;z-`
- L94 · CSS · HERO  
  → `.hero{display:grid;grid-template-columns:1.75fr 1fr;gap:16px;margin:18px 0}`
- L124 · CSS · SECTION HEADERS  
  → `.sec{margin:34px 0 14px;display:flex;align-items:center;justify-content:space-between;ga`
- L129 · CSS · CATEGORY TILES  
  → `.cats{display:grid;grid-template-columns:repeat(4,1fr);gap:13px}`
- L136 · CSS · BRANDS  
  → `.brands{display:grid;grid-template-columns:repeat(5,1fr);gap:13px}`
- L142 · CSS · SHOP  
  → `.shop{display:grid;grid-template-columns:240px 1fr;gap:20px;align-items:start;margin-bot`
- L208 · CSS · WHY US  
  → `.why{background:#fff;border:1px solid var(--line);border-radius:18px;padding:24px;margin`
- L212 · CSS · RFQ BANNER  
  → `.rfqbig{background:radial-gradient(640px 200px at 92% 0,rgba(47,158,99,.32),transparent`
- L216 · CSS · FOOTER  
  → `footer{background:var(--navy-d);color:#aec6e0;margin-top:10px;padding:38px 0 24px;font-s`
- L224 · CSS · CART DRAWER  
  → `.ov{position:fixed;inset:0;background:rgba(16,32,60,.5);z-index:90;display:none}`
- L288 · CSS · PRODUCT MODAL  
  → `.pmodal{position:fixed;inset:0;z-index:95;display:none;align-items:center;justify-conten`
- L309 · CSS · MOBILE BOTTOM BAR  
  → `.mbar{display:none}`
- L324 · CSS · CHECKOUT  
  → `.cko{position:fixed;inset:0;z-index:97;display:none;align-items:center;justify-content:c`
- L362 · CSS · ===== MOBILE MAIS LEGÍVEL E FÁCIL DE TOCAR =====  
  → `@media(max-width:600px){`
- L384 · CSS · ===== AVISO: MELHOR NO COMPUTADOR (pop-up 1x no celular) =====  
  → `.deskNote{position:fixed;inset:0;z-index:130;display:none;align-items:center;justify-con`
- L396 · CSS · ===== AJUSTES CELULAR v2 (22/10/2026): cabeçalho compacto, botões sem sobreposição, CEP sem estourar =====  
  → `@media(max-width:600px){`
- L466 · HTML · Google Analytics GA4  
  → `<script async src="https://www.googletagmanager.com/gtag/js?id=G-RK2PX868MS"></script>`
- L471 · CSS · Home enxuta: só busca + catálogo (banners da home ocultos)  
  → `#heroBlock{display:none!important}#deskNote{display:none!important}</style>`
- L511 · CSS · ===== CELULAR MAIS FÁCIL (26/10/2026) — 70% das visitas vêm do celular =====  
  → `.fcalc{display:flex;align-items:center;gap:10px;font-size:14px;font-weight:700;color:var(-`
- L525 · CSS · buscas populares: uma linha que rola, botões grandes  
  → `.popq{flex-wrap:nowrap;overflow-x:auto;margin:12px -16px 4px;padding:2px 16px 6px;scroll`
- L530 · CSS · banner institucional vai para depois das ofertas e categorias; botões duplicados somem  
  → `.bannerHome .bact{display:none!important}`
- L541 · CSS · cards do catálogo  
  → `.pt{-webkit-line-clamp:3!important;font-size:15px!important;line-height:1.32!important;m`
- L549 · CSS · categorias compactas: 3 por linha  
  → `.cats{grid-template-columns:repeat(3,1fr)!important;gap:8px!important}`
- L556 · CSS · cabeçalho mais baixo: sobra tela para os produtos  
  → `.head{padding:6px 14px!important;gap:6px!important}`
- L562 · CSS · ofertas em carrossel: desliza para o lado e chega rápido nas categorias  
  → `.ofgrid{display:flex!important;overflow-x:auto;scroll-snap-type:x mandatory;gap:10px!imp`
- L570 · JS · celular: ofertas e categorias primeiro (o banner institucional desce)  
  → `document.addEventListener('DOMContentLoaded',function(){try{`
- L579 · CSS · 28/10: CEP no topo, categorias em destaque, campanha compacta  
  → `.cepTop{margin:14px 0 10px!important;padding:14px 18px!important;border:2px solid #1F4E79!`
- L598 · CSS · 28/10 noite: ajustes celular — setas nos carrosséis, cards, carrinho com resumo em cima, aviso de carrinho  
  → `.hsw{position:relative}`
- L615 · CSS · carrinho: resumo, frete e finalizar em cima; produtos embaixo  
  → `.drawer .dbody{display:flex!important;flex-direction:column}`
- L650 · HTML · TOP UTILITY  
  → `<div class="util"><div class="wrap">`
- L662 · HTML · HEADER  
  → `<header><div class="wrap head">`
- L677 · HTML · TRUST  
  → `<div class="trust"><div class="wrap">`
- L686 · HTML · DEPT NAV  
  → `<div class="deptbar"><div class="wrap" id="deptNav"></div></div>`
- L691 · HTML · CEP primeiro: o CEP fica salvo e vale para todos os carrinhos  
  → `<section class="fgx cepTop" id="fgx"><div class="fgt"><span class="cepIc">📍</span><div><`
- L693 · HTML · CATEGORY TILES  
  → `<div id="catPanel"><div class="sec" id="catSec"><h2>Compre por categoria</h2><span class`
- L696 · HTML · 28/10/2026: campanha "o menor preço do mercado" (Greiner Vacuette e testes rápidos)  
  → `<section class="mpBox" id="mpBox">`
- L709 · HTML · HERO  
  → `<section class="hero" id="heroBlock">`
- L733 · HTML · OFERTAS / QUEIMA DE ESTOQUE: edite a lista window.OFERTAS (código do produto, selo, texto e, se quiser, preço "de")  
  → `<section id="grSec" style="display:none"><div class="ofh"><h2>🏆 Tubos e agulhas Greiner`
- L739 · HTML · (seção de marcas removida — loja organizada por categoria de produto)
- L741 · HTML · BANNER HOME  
  → `<section class="bannerHome" id="bannerHome">`
- L756 · HTML · SHOP  
  → `<div class="sec" id="shopAnchor"><h2 id="shopTitle">Catálogo</h2>`
- L775 · HTML · RFQ  
  → `<div class="rfqbig">`
- L783 · HTML · FOOTER  
  → `<footer class="ft2">`
- L798 · HTML · crédito MOVA Films  
  → `<div class="mova-band" style="background:repeating-linear-gradient(90deg,#3a3f47 0 14px,tr`
- L801 · HTML · CART DRAWER  
  → `<div class="ov" id="ov" onclick="if(window.__mdT===this)fecharCarrinho()"></div>`
- L819 · HTML · PRODUCT MODAL  
  → `<div class="pmodal" id="pmodal" onclick="if(event.target===this&&window.__mdT===this)fecha`
- L824 · HTML · CHECKOUT  
  → `<div class="cko" id="cko" onclick="if(event.target===this&&window.__mdT===this)fecharCheck`
- L868 · HTML · CONTATO P/ ORÇAMENTO WHATSAPP (caixa única: todos os botões de orçamento/WhatsApp abrem esta)  
  → `<div class="cko" id="waq" onclick="if(event.target===this)fecharContatoWA()">`
- L911 · HTML · RASTREIO  
  → `<div class="cko" id="rast" onclick="if(event.target===this&&window.__mdT===this)fecharRast`
- L927 · HTML · CONTA (Firebase)  
  → `<div class="cko" id="acc" onclick="if(event.target===this&&window.__mdT===this)fecharConta`
- L985 · JS · ====== OFERTAS / QUEIMA DE ESTOQUE — edite aqui ====== c = código do produto (como no catálogo) · tag = selo · txt = linha de apoio · de = preço antigo (opcional, só se for real)  
  → `window.OFERTAS=[`
- L997 · JS · 28/10/2026: destaque dos itens Greiner Vacuette (menor preço do mercado; "de" = preço até 28/10)  
  → `window.TR_TOP={'TR 017-1 RP':1,'TR 009 IST':1,'TR 009-1 IST':1,'TR 009-1 DT':1,'TR 010 DT'`
- L1030 · JS · ============ CATÁLOGO ============ Mapeamento de categorias (departamentos amigáveis)  
  → `var DEPTS=[`
- L1059 · JS · SEED — produtos reais confirmados (preview offline). Quando publicada na mesma origem da loja, a função carregarLive() substitui por TODOS os 229 produtos ao vivo.  
  → `var SEED=[{"c":"25492","n":"Lanceta com dispositivo de segurança 28G (1,8 mm) Biomass — ca`
- L1065 · JS · mostrar preço CNPJ por padrão  
  → `var FILTRO={dept:'', marca:'', busca:''};`
- L1067 · JS · 28/10/2026: catálogo paginado (24 por página) — sem rolagem infinita  
  → `var WHATS='5524988383100';`
- L1075 · JS · ====== RENDER ESTRUTURAS ======  
  → `function montarDeptNav(){`
- L1092 · JS · footer cats  
  → `document.getElementById('footCats').innerHTML=DEPTS.filter(d=>CATALOG.some(p=>deptOf(p.k`
- L1100 · JS · popular o select de busca por categoria  
  → `var _sp=document.getElementById('statProdutos'); if(_sp)_sp.textContent=CATALOG.length.t`
- L1116 · JS · ====== GRID ======  
  → `var KWMAP=null,_kwLoading=false;`
- L1137 · JS · itens que mais vendem/mais são vistos no site (pedidos, GA4 e Clarity, out/2026)  
  → `var TOP_VENDA=['25492','454087','454036','456001','454921','PA03','PA36','PA31','PA186','7`
- L1154 · JS · 26/10/2026: "Mais procurados" = mais vendidos/mais vistos primeiro, depois quem tem preço e foto; sob consulta por último  
  → `var _sc=function(p){var t=TOP_VENDA.indexOf(String(p.c));var v=(t>=0?1000-t:0)+(p.selo`
- L1160 · JS · 26/10/2026: busca sem resultado vai para a planilha (aba Eventos, tipo busca_sem_resultado) — mostra produto que o cliente procura e não achou  
  → `var _bvT=null,_bvSent={};`
- L1198 · JS · ====== AÇÕES DE FILTRO/BUSCA ======  
  → `function setDept(k){FILTRO.dept=k;FILTRO.marca='';FILTRO.busca='';document.getElementById(`
- L1207 · JS · ====== STEPPER + CARRINHO ======  
  → `function step(i,d,btn){var sp=btn.parentElement.querySelector('span');var v=Math.max(1,(pa`
- L1252 · JS · ====== BUSCA DENTRO DO CARRINHO ======  
  → `var _csT=null;`
- L1308 · JS · 28/10/2026: oferta direta do item que ativa o frete grátis  
  → `h+='<div class="gnudge"><div style="font-weight:800;color:var(--green-d)">'+(s0?'🎁 Ati`
- L1350 · JS · ====== ORÇAMENTO / WHATSAPP ======  
  → `function abrirWhats(msg){window.open('https://wa.me/'+WHATS+'?text='+encodeURIComponent(ms`
- L1354 · JS · sempre abre o formulário curto (já preenchido para quem voltou): nome, WhatsApp, CEP e lista  
  → `abrirContatoWA();`
- L1380 · JS · frete estimado do site (mesma API do checkout); se falhar ou demorar, segue sem estimativa  
  → `function _freteEstimado(cep,cb){`
- L1437 · JS · lê e valida a caixa única; devolve a ficha ou null (já mostra o erro)  
  → `function _waLer(arquivo){`
- L1477 · JS · 26/10/2026: guarda a ficha enquanto o cliente digita (o telefone serve para o lembrete do carrinho)  
  → `document.addEventListener('change',function(e){try{if(e.target&&e.target.closest&&e.target`
- L1479 · JS · 26/10/2026: robô do WhatsApp (lembrete de carrinho abandonado e aviso de pagamento)  
  → `var ROBO_URL='https://whatsapp-sullab-production.up.railway.app';`
- L1482 · JS · 26/10/2026: dúvida no carrinho/checkout -> WhatsApp com o carrinho junto (o robô avisa o vendedor na hora)  
  → `function duvidaCheckout(onde){`
- L1493 · JS · 28/10/2026: boleto à vista (Mercado Pago, R$ 3,49) e boleto faturado 28/45 dias (CNPJ, pelo WhatsApp/Tiny) só a partir de R$ 400  
  → `var BOLETO_MIN=400;`
- L1495 · JS · 28/10/2026: tubos e agulhas Vacuette só com pedido mínimo de R$ 400 em produtos (o carrinho todo conta)  
  → `var TUBO_MIN=400;`
- L1497 · JS · 28/10/2026: testes rápidos DeepBlue também com mínimo de R$ 400  
  → `/* 30/10/2026 (Eduardo, simulação de pedido mínimo): R$ 100 no geral, R$ 150 com item refr`
- L1498 · JS · 30/10/2026 (Eduardo, simulação de pedido mínimo): R$ 100 no geral, R$ 150 com item refrigerado, R$ 400 com tubos/agulhas Vacuette ou testes rápidos  
  → `var PED_MIN_GERAL=100,PED_MIN_REFRIG=150;`
- L1515 · JS · ====== CHECKOUT / PAGAMENTO (Mercado Pago) ======  
  → `var MP_WORKER='https://sullab-mp.comercial-0a2.workers.dev/';`
- L1526 · JS · ==== Conversão GA4: mede cada orçamento enviado (p/ importar no Google Ads) ====  
  → `try{ if(typeof gtag==='function'){ gtag('event', (type==='pedido_wa'?'gerar_orcamento':(`
- L1538 · JS · 28/10/2026: Pix 5% de desconto; tubos e agulhas Vacuette (margem menor) com 3%  
  → `window.PIX3={"450071":1,"450072":1,"454036":1,"454087":1,"454921":1,"454235":1,"456211":1,`
- L1553 · JS · 26/10/2026 (Himalaia SLB-1792698754293 e Aline SLB-1792691910142 pagaram sem frete): o frete só vale para o CEP e o carrinho cotados. Mudou CEP, carrinho ou a cotação falhou: o frete zera e o pagamento fica bloqueado até nova cotação. Grátis só quando a API diz gratis.ativo.  
  → `var _freteOk=null;`
- L1591 · JS · 26/10/2026: valor real da compra (itens com desconto do Pix + frete) para a conversão do Google Ads na página obrigado  
  → `try{var vtot=items.reduce(function(s,i){return s+i.unit_price*i.quantity;},0);`
- L1596 · JS · 26/10/2026: Pix pago no app do banco não volta para a página "obrigado", então a compra não era medida. Guarda no servidor o ID do GA4, a sessão e o gclid; quando o Mercado Pago aprova, o servidor envia a compra ao GA4/Ads.  
  → `try{var _o=window.SULLAB_ORIGEM||{};var _cm={action:'conv_meta',pedido:pedido,v:(functio`
- L1613 · JS · ====== CONTA / LOGIN (Firebase) ======  
  → `var FBCFG={apiKey:"AIzaSyBoIPsSsAAg0dPsd8rmwNmuXz7SQHwQw68",authDomain:"sullab.firebaseapp`
- L1647 · JS · ====== ÁREA DO CLIENTE: meus pedidos (servidor), DANFE, definir senha ======  
  → `var _MP=null;`
- L1689 · JS · ====== RASTREIO DE PEDIDO ======  
  → `function meusPedidos(){try{return JSON.parse(localStorage.getItem('sullab_meus_pedidos')||`
- L1738 · JS · ====== MODAL PRODUTO ======  
  → `var __pmL=[],__pmI=0;`
- L1772 · JS · ====== CARREGAR CATÁLOGO AO VIVO (quando publicada na mesma origem) ======  
  → `function carregarLive(){`
- L1774 · JS · só tenta se estiver hospedada (http/https), não em file://  
  → `if(!/^https?:/.test(location.origin))return;`
- L1777 · JS · extrair var P=[...]  
  → `var m=html.match(/var\s+P\s*=\s*(\[[\s\S]*?\]);/);`
- L1781 · JS · extrair preços dos cards  
  → `var doc=new DOMParser().parseFromString(html,'text/html');`
- L1791 · JS · cubetas CRAL: forçar preço correto por pacote enquanto o site antigo não corrige  
  → `if(p.cod==='18150'||p.cod==='18153'){pr={pub:1098.90,cnpj:1000.00};}`
- L1797 · JS · mantém SEED  
  → `});`
- L1800 · JS · ====== BOOT ======  
  → `function fecharDeskNote(){var n=document.getElementById('deskNote');if(n)n.classList.remov`
- L1810 · JS · carregarLive() desligado: baixava de novo a página inteira (~390 KB) a cada visita e atrasava o carrinho no celular  
  → `/* Deep-link: aplica ?q= (busca) e ?dept=/?cat= (categoria) vindos da URL — ex.: anúncios`
- L1811 · JS · Deep-link: aplica ?q= (busca) e ?dept=/?cat= (categoria) vindos da URL — ex.: anúncios do Google e redirects do 404.html  
  → `(function(){`
- L1902 · JS · link "Pedir orçamento" das páginas de produto/categoria: /?orcar=CODIGO abre a caixa única já com o item  
  → `(function(){try{`
- L1927 · JS · ===== Referência (indique e ganhe) e link de carrinho =====  
  → `try{var q=new URLSearchParams(location.search);`
- L1936 · JS · link de carrinho SUBSTITUI o carrinho: abrir o link 2x não dobra a quantidade nem mistura com itens antigos  
  → `var novos=[];c.split(',').forEach(function(par){var a=par.split(':'),cod=decodeURIComp`
- L1943 · JS · roda no fim do <body> (antes de imagens, Firebase e Analytics); o load fica só de reserva  
  → `window.addEventListener('load',function(){window.__aplicarCarrinhoUrl();});`
- L1946 · JS · ===== Carrinho: salvar por WhatsApp, copiar link, selos =====  
  → `var _ac2=window.atualizarCart;`
- L1965 · JS · 30/10/2026: exposto no window — Clarity registrou "Can't find variable: linkCarrinho" (iOS/GoogleApp)  
  → `window.copiarLinkCarrinho=function(){var l=linkCarrinho(),m=document.getElementById('svMsg`
- L1970 · JS · ===== Aviso para quem volta com itens no carrinho + evento de abandono =====  
  → `var PREV_VISIT=0;try{PREV_VISIT=parseInt(localStorage.getItem('sullab_last')||'0',10);}cat`
- L1986 · JS · 26/10/2026: o robô manda o link do carrinho no WhatsApp depois de 1 h (só em horário comercial; cancela se o cliente pagar ou falar com a gente)  
  → `roboPost('/site/carrinho-abandonado',{tel:t,nome:(f&&f.nome)||'',itens:CART.map(functi`
- L1990 · JS · ===== Selos de confiança no produto =====  
  → `var _ap3=window.abrirProd;`
- L2008 · JS · ===== Pedido direto (22/10/2026) ===== A lista que o cliente cola vira carrinho (o site acha os produtos); com tudo com preço, segue para o pagamento. Item sob consulta e pedido CPF são registrados para a equipe (e-mail), sem abrir WhatsApp. WhatsApp só para "Falar com a SULLAB" (dúvida) e para lista em foto/PDF/áudio.  
  → `(function(){`
- L2097 · JS · registra o pedido para a equipe (e-mail do site), sem abrir o WhatsApp  
  → `window.registrarPedidoEquipe=function(f,origem){`
- L2144 · JS · CPF no checkout: registra o pedido para a equipe (sem pagamento online), sem reabrir formulário nem WhatsApp  
  → `window.enviarPedidoCPF=function(){`
- L2155 · JS · 22/10/2026: CPF também paga online (Pix ou cartão), igual ao CNPJ  
  → `var _ck=window.ckModo;`
- L2158 · JS · carrinho: sem "orçamento pelo WhatsApp"; item sob consulta vira pedido para a equipe  
  → `var _ac=window.atualizarCart;`
- L2168 · JS · busca sem resultado: nada de WhatsApp  
  → `var _rd=window.render;`
- L2179 · JS · ?lista= : link que o robô do WhatsApp manda com o pedido do cliente (abre a conferência da lista)  
  → `function _listaUrl(){try{var t=new URLSearchParams(location.search).get('lista');if(!t)ret`
- L2188 · JS · ===== Refrigerados (22/10/2026, regra do Eduardo) ===== Placas, tubos e frascos de meio pronto, cromoágares, cepas e plasma vão sempre pela opção MAIS RÁPIDA, com entrega em até 3 dias úteis depois da postagem (o prazo da API já soma 1 dia de postagem: limite 4). Sem opção nesse prazo (ou sem conseguir cotar o CEP): não deixa pagar e não gera pedido.  
  → `(function(){`
- L2193 · JS · 28/10/2026: até 3 dias úteis após a postagem (48–72 h com gelo) + 1 dia de postagem da API  
  → `/* 28/10/2026 (estudo de 97 envios reais): estados sem entrega refrigerada segura e JeT só`
- L2194 · JS · 28/10/2026 (estudo de 97 envios reais): estados sem entrega refrigerada segura e JeT só dentro do RJ  
  → `var UF_BLOQ=/^(AC|AL|AM|AP|MT|PA|PB|PI|RO|RR|SE|TO)$/;`
- L2199 · JS · 29/10/2026: PA155 (Egg yolk) passou sem regra de refrigerado — incluídos biológicos e meios prontos em tubo/kit  
  → `var RX_SIM=/placa|biplaca|Ø\s?\d|cromo|caldo|[aá]gar|meio de|newp \d|plasma|egg yolk|gema|`
- L2202 · JS · 28/10/2026 (Eduardo): reagentes Ebram também são refrigerados (2–8 °C), exceto a linha de hematologia e as soluções de lavagem  
  → `var EBRAM_AMB=/^(21910|21805|23805|23920|23930|23940|22805|740|741|742|EBIO.*|EB\d{4}|EBCO`
- L2203 · JS · hematologia, soluções e equipamentos não são refrigerados  
  → `var ISOPOR=0; /* 30/10/2026: isopor embutido no preço (+R$ 8/un), não cobrar no frete (ant`
- L2204 · JS · 30/10/2026: isopor embutido no preço (+R$ 8/un), não cobrar no frete (antes: 15 por envio, premissa 28/10/2026)  
  → `/* 29/10/2026: armazenamento oficial da Lista de Preços NewProv 2026 (coluna Armazenamento`
- L2205 · JS · 29/10/2026: armazenamento oficial da Lista de Preços NewProv 2026 (coluna Armazenamento): 2–8 °C = refrigerado; 10–30 °C = ambiente. Vale antes da regra por nome.  
  → `var NP_REF={"PA242":1,"PA246":1,"PA149":1,"PA150":1,"PA352":1,"PA151":1,"PA152":1,"PA153":`
- L2208 · JS · 29/10/2026 (Eduardo): guardados a 2–8 °C, mas suportam o transporte em temperatura ambiente (120 dias) — liberados para frete acima de 3 dias úteis  
  → `var NP_TRANSP_AMB={"PA91":1,"PA315":1,"PA231":1};`
- L2230 · JS · 29/10/2026: LATAM fora só para refrigerado (cargas paradas)  
  → `});`
- L2231 · JS · 28/10/2026: refrigerado sem frete grátis automático (o cálculo do grátis não inclui isopor/gelo nem o envio rápido); soma isopor+gelo  
  → `if(!d.refrigSrv)ops=ops.map(function(x){var y=Object.assign({},x);if(y.gratis){y`
- L2246 · JS · 28/10/2026 (Eduardo, caso Angélica/Teresina): o cliente tem de entender na hora por que não dá para pagar  
  → `function nomesRefrig(){return CART.filter(function(x){return refrigCod(String(x.c));}).map`
- L2268 · JS · pagamento: carrinho refrigerado só paga com o frete rápido escolhido  
  → `var _pg=window.pagarMP;`
- L2280 · JS · 22/10/2026: SLB-1792698754293 (Himalaia) e SLB-1792691910142 pagaram sem frete. 26/10/2026: o frete vale só para o CEP + carrinho cotados (freteValido); sem isso o botão de pagar fica bloqueado com aviso, o frete é cotado sozinho quando o CEP fica completo e o próprio pagarMP recusa seguir.  
  → `(function(){`
- L2313 · JS · link direto do rastreio: /?pedido=SLB-123 (opcional &email=) abre "Rastrear pedido" já preenchido  
  → `(function(){try{var q=new URLSearchParams(location.search),n=(q.get('pedido')||'').replace`
- L2320 · JS · setas de rolagem lateral em tudo que desliza para o lado  
  → `(function(){`
- L2345 · JS · celular: no carrinho, "guardar carrinho" e selos vão para baixo dos produtos  
  → `(function(){var _ac=window.atualizarCart;window.atualizarCart=function(){_ac.apply(this,ar`
- L2351 · JS · aviso "você deixou itens no carrinho": some sozinho depois de 12 s  
  → `setInterval(function(){var b=document.getElementById('retBar');if(b&&!b.__t){b.__t=setTime`
- L2355 · JS · celular: catálogo em fileiras por categoria, deslizando para o lado  
  → `(function(){`

## indique.html

- L70 · HTML · crédito MOVA Films  
  → `<div class="mova-band" style="background:repeating-linear-gradient(90deg,#3a3f47 0 14px,tr`

## obrigado.html

- L91 · JS · 26/10/2026: dados da compra guardados no checkout (valor com desconto do Pix + frete, itens, telefone)  
  → `var _lp=null;try{_lp=JSON.parse(localStorage.getItem('sullab_last_purchase')||'null');if`
- L93 · JS · pago ou Pix/boleto em processamento: cancela o lembrete de carrinho abandonado no WhatsApp  
  → `if(/approv|success|paid|pend|process|in_process|authorized/.test(status)&&_lp&&_lp.tel){`
- L95 · JS · Pix/boleto pendente também esvazia o carrinho: o pedido já foi feito (26/10/2026)  
  → `try{if(!extRef||_lp.ped===extRef)localStorage.removeItem('sullab_cart');}catch(e){}`
- L104 · JS · uma conversão por pedido, mesmo se a página for recarregada  
  → `var _env={};try{_env=JSON.parse(localStorage.getItem('sullab_purchase_enviadas')||'{}'`
- L110 · JS · 28/10/2026: conversão nativa do Google Ads (Compra no site — tag do Google), principal para lances  
  → `try{gtag('config','AW-11390766577');gtag('event','conversion',{send_to:'AW-113907665`
- L115 · JS · pedido pago: esvazia o carrinho para não aparecer o aviso "você deixou itens no carrinho"  
  → `try{if(!extRef||!_lp||_lp.ped===extRef)localStorage.removeItem('sullab_cart');}catch(e`
- L127 · JS · detalhes  
  → `var any=false, box=document.getElementById('detbox');`
- L133 · JS · WhatsApp com a mensagem certa  
  → `var msg='Olá! Acabei de finalizar um pedido no site da SULLAB';`
- L140 · JS · === Boleto: opção de enviar comprovante para acelerar a liberação ===  
  → `var pmId=(qp('payment_method_id')||qp('payment_type_id')||'').toLowerCase();`

## sobre.html

- L81 · HTML · crédito MOVA Films  
  → `<div class="mova-band" style="background:repeating-linear-gradient(90deg,#3a3f47 0 14px,tr`
