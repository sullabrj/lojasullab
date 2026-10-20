/* SULLAB — rastreio de visitas, cliques e leads (GA4 + Google Ads). v1 20/10/2026
   Eventos (GA4): view_item, add_to_cart, view_cart, begin_checkout, add_payment_info, generate_lead,
   iniciar_orcamento, search, select_content, whatsapp_click, contact_click, clique_elemento,
   scroll_depth, tempo_na_pagina, cadastro_cnpj_tentativa, login_clique, rastrear_pedido_abrir,
   alternar_preco_cnpj, cupom_tentativa, pagar_clique. Origem (utm/gclid) guardada em localStorage. */
(function(){
  var CLARITY_ID='z0ww8oyptt'; /* opcional: colar aqui o ID do projeto do Microsoft Clarity (mapa de calor e gravação de tela) */
  var AW_ID='AW-11390766577';
  function G(){try{window.dataLayer=window.dataLayer||[];if(typeof window.gtag==='function')window.gtag.apply(null,arguments);}catch(e){}}
  function ev(n,p){G('event',n,p||{});}
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
    wrap('abrirCheckout',function(){try{if(CART.length)ev('begin_checkout',{currency:'BRL',value:total(),items:cartItens()});}catch(e){}});
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
    wrap('sullabEvent',function(type,extra){try{if(extra&&typeof extra==='object'&&window.SULLAB_ORIGEM)extra.origem=window.SULLAB_ORIGEM;}catch(e){}});
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
})();
