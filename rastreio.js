/* SULLAB — rastreio de visitas, cliques e leads (GA4 + Google Ads). v3 29/10/2026 (+ Pixel do Meta) · v5 30/10/2026: espera o js/loja.js na home · v7 31/10/2026: begin_checkout só acima do pedido mínimo
   Eventos (GA4): view_item, add_to_cart, view_cart, begin_checkout, add_payment_info, generate_lead,
   iniciar_orcamento, search, select_content, whatsapp_click, contact_click, clique_elemento,
   scroll_depth, tempo_na_pagina, cadastro_cnpj_tentativa, login_clique, rastrear_pedido_abrir,
   alternar_preco_cnpj, cupom_tentativa, pagar_clique. Origem (utm/gclid) guardada em localStorage. */
(function(){
  var CLARITY_ID='z0ww8oyptt'; /* opcional: colar aqui o ID do projeto do Microsoft Clarity (mapa de calor e gravação de tela) */
  var AW_ID='AW-11390766577';
  /* v2 22/10/2026: páginas sem a tag do GA4 no HTML (categorias, guias, blog, ofertas, indique, institucionais) carregam o gtag.js aqui */
  if(typeof window.gtag!=='function'){try{window.dataLayer=window.dataLayer||[];window.gtag=function(){window.dataLayer.push(arguments);};(function(){var c='';try{c=localStorage.getItem('sl_consent')||'';}catch(e){}var g=c==='sim'?'granted':'denied';window.gtag('consent','default',{ad_storage:g,ad_user_data:g,ad_personalization:g,analytics_storage:'granted',wait_for_update:500});window.gtag('set','ads_data_redaction',g==='denied');})();window.gtag('js',new Date());window.gtag('config','G-RK2PX868MS');var gs=document.createElement('script');gs.async=1;gs.src='https://www.googletagmanager.com/gtag/js?id=G-RK2PX868MS';document.head.appendChild(gs);}catch(e){}}
  function G(){try{window.dataLayer=window.dataLayer||[];if(typeof window.gtag==='function')window.gtag.apply(null,arguments);}catch(e){}}
  /* 26/10/2026: os passos do checkout também viram eventos do Clarity, para filtrar as gravações de quem desistiu */
  var CLARITY_EVS={begin_checkout:1,add_payment_info:1,pagar_clique:1,view_cart:1,add_to_cart:1,whatsapp_click:1,sullab_frete_gratis_consulta:1};
  /* 29/10/2026: Pixel do Meta (conjunto "Pixel - SULLAB RJ") — remarketing do catálogo e anúncios de clique para o WhatsApp.
     Só envia depois do "Aceitar" dos cookies (consent revoke/grant). content_ids = código do produto = id do catálogo do Meta. */
  var META_PIXEL='222353024257094';
  (function(){try{if(window.fbq)return;
    var n=window.fbq=function(){n.callMethod?n.callMethod.apply(n,arguments):n.queue.push(arguments);};
    if(!window._fbq)window._fbq=n;n.push=n;n.loaded=!0;n.version='2.0';n.queue=[];
    var t=document.createElement('script');t.async=!0;t.src='https://connect.facebook.net/en_US/fbevents.js';
    var y=document.getElementsByTagName('script')[0];y.parentNode.insertBefore(t,y);
    var c='';try{c=localStorage.getItem('sl_consent')||'';}catch(e){}
    if(c!=='sim')window.fbq('consent','revoke');
    window.fbq('init',META_PIXEL);window.fbq('track','PageView');
  }catch(e){}})();
  function FB(){try{if(typeof window.fbq==='function')window.fbq.apply(null,arguments);}catch(e){}}
  function idsDe(p){var its=(p&&p.items)||[];return its.map(function(x){return String(x.item_id||'');}).filter(Boolean);}
  function meta(n,p){p=p||{};var ids=idsDe(p),base={currency:'BRL'};if(p.value)base.value=Math.round(p.value*100)/100;
    if(ids.length){base.content_ids=ids;base.content_type='product';base.num_items=(p.items||[]).reduce(function(s,x){return s+(x.quantity||1);},0);}
    if(n==='view_item'&&ids.length)FB('track','ViewContent',base);
    else if(n==='add_to_cart')FB('track','AddToCart',base);
    else if(n==='begin_checkout')FB('track','InitiateCheckout',base);
    else if(n==='add_payment_info')FB('track','AddPaymentInfo',base);
    else if(n==='generate_lead')FB('track','Lead',base);
    else if(n==='whatsapp_click')FB('track','Contact',{content_name:p.origem||'whatsapp'});
    else if(n==='search'&&p.search_term)FB('track','Search',{search_string:p.search_term});}
  function ev(n,p){G('event',n,p||{});try{meta(n,p);}catch(e){}try{if(CLARITY_EVS[n]&&window.clarity)window.clarity('event',n);}catch(e){}}
  var isProd=/^\/p\//.test(location.pathname);
  var $=function(id){return document.getElementById(id);};

  /* ---- origem do visitante (utm / gclid), última origem com parâmetro ---- */
  try{
    var q=new URLSearchParams(location.search),u={},ks=['utm_source','utm_medium','utm_campaign','utm_term','utm_content','gclid','gbraid','wbraid'];
    ks.forEach(function(k){if(q.get(k))u[k]=q.get(k);});
    var s=null;try{s=JSON.parse(localStorage.getItem('sullab_origem')||'null');}catch(e){}
    if(Object.keys(u).length||!s){
      s={ref:document.referrer||'',lp:location.pathname,ts:Date.now()};for(var k in u)s[k]=u[k];
      try{localStorage.setItem('sullab_origem',JSON.stringify(s));}catch(e){}
    }
    window.SULLAB_ORIGEM=s;
  }catch(e){}

  /* ---- remarketing / conversão do Google Ads também na loja e nas demais páginas ---- */
  if(!isProd)G('config',AW_ID);

  /* ---- Microsoft Clarity (só carrega se houver ID) ---- */
  if(CLARITY_ID){(function(c,l,a,r,i,t,y){c[a]=c[a]||function(){(c[a].q=c[a].q||[]).push(arguments);};t=l.createElement(r);t.async=1;t.src='https://www.clarity.ms/tag/'+i;y=l.getElementsByTagName(r)[0];y.parentNode.insertBefore(t,y);})(window,document,'clarity','script',CLARITY_ID);}


  /* ---- 26/10/2026: aviso de cookies (LGPD) + Consent Mode do Google. Analytics sempre; anúncios personalizados só com "Aceitar" ---- */
  (function(){try{
    var c='';try{c=localStorage.getItem('sl_consent')||'';}catch(e){}
    if(c)return;
    var mk=function(){if(document.getElementById('slCk'))return;
      var st=document.createElement('style');st.textContent='#slCk{position:fixed;left:12px;right:12px;bottom:12px;z-index:100000;max-width:720px;margin:0 auto;background:#fff;color:#1a2433;border:1px solid #dbe4f0;border-radius:14px;box-shadow:0 10px 34px rgba(20,40,70,.22);padding:14px 16px;font:14px/1.45 -apple-system,Segoe UI,Roboto,Arial,sans-serif;display:flex;gap:12px;align-items:center;flex-wrap:wrap}#slCk p{margin:0;flex:1 1 260px}#slCk a{color:#1f4e79;font-weight:700}#slCk .b{display:flex;gap:8px;flex:0 0 auto}#slCk button{border:0;border-radius:10px;font-weight:800;font-size:15px;min-height:44px;padding:0 18px;cursor:pointer}#slCk .ok{background:#2f9e63;color:#fff}#slCk .no{background:#eef3fb;color:#1f3a5f}@media(max-width:700px){#slCk{left:8px;right:8px;bottom:8px}#slCk .b{width:100%}#slCk button{flex:1}body.slCkBar #slCk{bottom:84px}}';
      document.head.appendChild(st);
      var d=document.createElement('div');d.id='slCk';d.setAttribute('role','dialog');d.setAttribute('aria-label','Aviso de cookies');
      d.innerHTML='<p>Usamos cookies para melhorar sua experiência e mostrar ofertas relevantes. Veja a <a href="/privacidade.html">Política de Privacidade</a>.</p><div class="b"><button type="button" class="no">Recusar</button><button type="button" class="ok">Aceitar</button></div>';
      if(document.getElementById('pmBar'))document.body.classList.add('slCkBar');
      document.body.appendChild(d);
      var fim=function(v){try{localStorage.setItem('sl_consent',v);}catch(e){}
        var g=v==='sim'?'granted':'denied';G('consent','update',{ad_storage:g,ad_user_data:g,ad_personalization:g,analytics_storage:'granted'});
        try{if(window.clarity)window.clarity('consent',v==='sim');}catch(e){}
        FB('consent',v==='sim'?'grant':'revoke');
        ev('cookies_'+(v==='sim'?'aceitou':'recusou'),{});d.remove();};
      d.querySelector('.ok').onclick=function(){fim('sim');};
      d.querySelector('.no').onclick=function(){fim('nao');};
    };
    /* 30/10/2026: aviso entra junto com a página (antes: 1,2 s depois). Aparecendo atrasado, ele virava o "maior elemento"
       da tela no celular e empurrava o LCP do PageSpeed para depois de 1,2 s */
    if(document.body)mk();else document.addEventListener('DOMContentLoaded',mk);
  }catch(e){}})();

  function wrap(name,fn){
    var o=window[name];if(typeof o!=='function'||o.__w)return;
    var w=function(){try{fn.apply(this,arguments);}catch(e){}return o.apply(this,arguments);};
    w.__w=1;window[name]=w;
  }
  function itemDe(p,q){return {item_id:p.c,item_name:p.n,item_brand:p.m,quantity:q||1};}
  function cartItens(){try{return CART.map(function(x){return {item_id:x.c,item_name:x.n,item_brand:x.m,quantity:x.qty};});}catch(e){return [];}}
  function total(){try{return totalCart()||0;}catch(e){return 0;}}

  function instalarLoja(){
    if(typeof window.CATALOG==='undefined'||typeof window.addCart!=='function')return;
    wrap('abrirProd',function(i){var p=CATALOG[i];if(p)ev('view_item',{items:[itemDe(p,1)]});});
    wrap('addCart',function(i,btn){var p=CATALOG[i];if(!p)return;var q=1;try{q=parseInt(btn.parentElement.querySelector('.stepper span').textContent)||1;}catch(e){}
      var pr=((window.PRECOS||{})[p.c]||[])[1]||0;ev('add_to_cart',{currency:'BRL',value:pr*q,items:[itemDe(p,q)]});});
    wrap('abrirCarrinho',function(){ev('view_cart',{currency:'BRL',value:total(),items:cartItens()});});
    /* 31/10/2026: o wrap roda ANTES da função; abrirCheckout volta ao carrinho quando falta valor para o pedido mínimo — só conta begin_checkout quando o checkout abre de fato */
    wrap('abrirCheckout',function(){try{if(CART.length&&!(typeof faltaTubo==='function'&&faltaTubo()>0))ev('begin_checkout',{currency:'BRL',value:total(),items:cartItens()});}catch(e){}});
    wrap('abrirContatoWA',function(){ev('iniciar_orcamento',{itens:cartItens().length});});
    wrap('pagarMP',function(){ev('pagar_clique',{currency:'BRL',value:total()});});
    wrap('dispararPedido',function(type){
      window.__nowa=true;setTimeout(function(){window.__nowa=false;},4000);
      try{if(!CART.length)return;}catch(e){}
      var o=window.SULLAB_ORIGEM||{};
      if(type==='pedido_wa')ev('generate_lead',{currency:'BRL',value:total(),lead_source:'orcamento_whatsapp',utm_source:o.utm_source||'',utm_campaign:o.utm_campaign||'',gclid_presente:o.gclid?1:0});
      if(type==='pedido_mp')ev('add_payment_info',{currency:'BRL',value:total(),items:cartItens()});
    });
    wrap('fazerBusca',function(){var el=$('searchInput');var t=el&&el.value.trim();if(t)ev('search',{search_term:t});});
    wrap('setDept',function(k){if(k)ev('select_content',{content_type:'categoria',content_id:k});});
    wrap('setMarca',function(m){if(m)ev('select_content',{content_type:'marca',content_id:m});});
    wrap('abrirWhats',function(){if(!window.__nowa)ev('whatsapp_click',{origem:'loja',page:location.pathname});});
    wrap('waArquivoWhats',function(){ev('whatsapp_click',{origem:'orcamento_arquivo',page:location.pathname});});
    wrap('abrirRastreio',function(){ev('rastrear_pedido_abrir');});
    wrap('toggleCNPJ',function(){ev('alternar_preco_cnpj');});
    wrap('aplicarCupom',function(){ev('cupom_tentativa');});
    wrap('abrirConta',function(){ev('abrir_conta');});
    wrap('fbCadastro',function(){ev('cadastro_cnpj_tentativa');});
    wrap('fbLogin',function(){ev('login_clique');});
    /* envia a origem junto do pedido para a planilha (atribuição do lead) */
    wrap('sullabEvent',function(type,extra){try{if(extra&&typeof extra==='object'&&window.SULLAB_ORIGEM)extra.origem=window.SULLAB_ORIGEM;}catch(e){}
      /* v2: espelha no GA4 os eventos que antes iam só para a planilha */
      try{if(/^(kit_add|carrinho_abandonado|carrinho_retorno|carrinho_por_link|conta_cadastro|cross_sell_add|frete_gratis_consulta|indicacao_cadastro|indicacao_pedido)$/.test(type)){var x=extra||{};ev('sullab_'+type,{ref:x.ref||'',kit:x.kit||x.id||'',valor:x.total||x.valor||0});}}catch(e){}});
  }

  /* ---- página de produto estática ---- */
  function viewItemEstatico(){
    if(!isProd)return;
    try{var ld=document.querySelectorAll('script[type="application/ld+json"]');
      for(var i=0;i<ld.length;i++){var j=JSON.parse(ld[i].textContent);if(j&&j['@type']==='Product'){
        var b=j.brand&&(j.brand.name||j.brand);ev('view_item',{items:[{item_id:j.sku||'',item_name:j.name||document.title,item_brand:b||''}]});return;}}
    }catch(e){}
    ev('view_item',{items:[{item_name:document.title}]});
  }

  /* ---- cliques: telefone, e-mail e mapa de cliques da loja ---- */
  document.addEventListener('click',function(e){
    try{
      var t=e.target;if(!t||!t.closest)return;
      var a=t.closest('a');
      if(a){var h=a.getAttribute('href')||'';
        if(h.indexOf('tel:')===0){ev('contact_click',{tipo:'telefone',page:location.pathname});return;}
        if(h.indexOf('mailto:')===0){ev('contact_click',{tipo:'email',page:location.pathname});return;}}
      var el=t.closest('.hbtn,.promo,.ctile,.popq span,.dept,footer a,header a,.btn,button,nav a,.card,.pcard');
      if(!el)return;
      var rot=(el.getAttribute('aria-label')||el.textContent||'').replace(/\s+/g,' ').trim().slice(0,50);
      var sec=el.closest('header,footer,nav,section,.promo,#catSec,.cko,.drawer,.pmodal');
      ev('clique_elemento',{rotulo:rot,secao:sec?(sec.id||sec.tagName.toLowerCase()):'pagina',page:location.pathname});
    }catch(err){}
  },true);

  /* ---- rolagem (25/50/75/100%) e tempo real de leitura ---- */
  var feitos={};
  function onScroll(){
    var d=document.documentElement,h=(d.scrollHeight-d.clientHeight);if(h<=0)return;
    var p=Math.round(100*(window.pageYOffset||d.scrollTop)/h);
    [25,50,75,100].forEach(function(m){if(p>=m&&!feitos[m]){feitos[m]=1;ev('scroll_depth',{percent:m,page:location.pathname});}});
  }
  window.addEventListener('scroll',onScroll,{passive:true});
  var seg=0,marcas={30:0,60:0,120:0,300:0};
  setInterval(function(){
    if(document.visibilityState!=='visible')return;
    seg++;if(marcas[seg]===0){marcas[seg]=1;ev('tempo_na_pagina',{segundos:seg,page:location.pathname});}
  },1000);

  function iniciar(){instalarLoja();viewItemEstatico();}
  if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',iniciar);else iniciar();
  /* 30/10/2026: na home o JS da loja (js/loja.js) chega depois do catálogo em JSON — instala os eventos quando ele avisar */
  if(!window.__lojaPronta)window.addEventListener('sullab:loja',instalarLoja);
})();
