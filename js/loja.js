/* SULLAB — JavaScript da loja (home). Gerado em 30/10/2026 a partir dos <script> que ficavam no index.html.
   Carregado pelo index.html DEPOIS de data/catalogo.json e data/precos.json (window.SEED e window.PRECOS).
   Os blocos estão na mesma ordem de antes. Editou este arquivo? Rode: python3 _ferramentas/dados_site.py
   (atualiza o ?v= no index.html para o cache não servir a versão antiga). */
(function(){
  /* o arquivo pode rodar depois do DOMContentLoaded/load (ele espera o catálogo): quem se inscrever nesses
     eventos durante a execução é chamado logo em seguida, como se tivesse chegado antes */
  var W=window,D=document,aw=W.addEventListener,ad=D.addEventListener;
  function tarde(t){return (t==='load'&&D.readyState==='complete')||(t==='DOMContentLoaded'&&D.readyState!=='loading');}
  W.addEventListener=function(t,f,o){if(tarde(t)&&typeof f==='function'){setTimeout(function(){f.call(W,new Event(t));},0);return;}return aw.apply(this,arguments);};
  D.addEventListener=function(t,f,o){if(tarde(t)&&typeof f==='function'){setTimeout(function(){f.call(D,new Event(t));},0);return;}return ad.apply(this,arguments);};
  W.__lojaFimShim=function(){W.addEventListener=aw;D.addEventListener=ad;delete W.__lojaFimShim;};
})();

/* ==== qtdJs (quantidade por embalagem e preço unitário) ==== */
try{
window.QTD={"25492":[100,"unidade","caixa"],"18286-10":[10,"unidade","pacote"],"18288-10":[10,"unidade","pacote"],"CLT50SM":[100,"unidade","pacote"],"CLT80SNM":[100,"unidade","pacote"],"18151":[500,"unidade","pacote"],"18153":[1000,"unidade","pacote"],"18150":[1000,"unidade","pacote"],"25001":[100,"unidade","pacote"],"19001NM":[100,"unidade","caixa"],"GRL36":[25,"unidade","caixa"],"P22X22":[100,"unidade","caixa"],"7102":[50,"unidade","caixa"],"7105":[50,"unidade","caixa"],"7105-1":[50,"unidade","caixa"],"PHFIX100":[100,"unidade","pacote"],"18432":[500,"unidade","pacote"],"VHS-P":[25,"unidade","pacote"],"EV21":[50,"unidade","caixa"],"P10ML":[10,"unidade","caixa"],"18248A":[10,"unidade","pacote"],"181401":[5,"unidade","pacote"],"18142E":[10,"unidade","pacote"],"18266":[300,"unidade","pacote"],"18260NM":[1000,"unidade","pacote"],"181727E":[100,"unidade","rack"],"CITO3":[100,"unidade","pacote"],"23007":[100,"unidade","caixa"],"23010P":[100,"unidade","caixa"],"18056":[1000,"unidade","pacote"],"18010":[1000,"unidade","pacote"],"P7X40":[250,"unidade","caixa"],"GD095FRNR":[100,"unidade","rack"],"17022":[50,"unidade","pacote"],"A01015":[50,"disco","caixa"],"A01016":[50,"disco","caixa"],"A01017":[50,"disco","caixa"],"A01020":[50,"disco","caixa"],"A01023":[50,"disco","caixa"],"A01024":[50,"disco","caixa"],"A01027":[50,"disco","caixa"],"A01028":[50,"disco","caixa"],"A01029":[50,"disco","caixa"],"A01030":[50,"disco","caixa"],"A01031":[50,"disco","caixa"],"A01032":[50,"disco","caixa"],"A01033":[50,"disco","caixa"],"A01034":[50,"disco","caixa"],"A01035":[50,"disco","caixa"],"A01067":[50,"disco","cartela"],"A01036":[50,"disco","caixa"],"A01040":[50,"disco","caixa"],"A01041":[50,"disco","caixa"],"A01073":[50,"disco","caixa"],"A01077":[50,"disco","caixa"],"A01026":[50,"disco","caixa"],"A01078":[50,"disco","caixa"],"A01047":[50,"disco","caixa"],"A01049":[50,"disco","caixa"],"A01075":[50,"disco","caixa"],"A01056":[50,"disco","caixa"],"A01074":[50,"disco","caixa"],"A01058":[50,"disco","caixa"],"A01061":[50,"disco","caixa"],"A01063":[50,"disco","caixa"],"A01010":[50,"disco","caixa"],"450071":[100,"unidade","caixa"],"450072":[100,"unidade","caixa"],"454921":[50,"unidade","rack"],"456211":[50,"unidade","rack"],"454030":[50,"unidade","rack"],"454482":[50,"unidade","rack"],"450539":[50,"unidade","rack"],"456080":[50,"unidade","rack"],"454327":[50,"unidade","rack"],"454036":[50,"unidade","rack"],"454087":[50,"unidade","rack"],"454085":[50,"unidade","rack"],"454091":[50,"unidade","rack"],"454092":[50,"unidade","rack"],"454071":[50,"unidade","rack"],"456071":[50,"unidade","rack"],"455071":[50,"unidade","rack"],"455092":[50,"unidade","rack"],"456001":[50,"unidade","rack"],"TR 010 DT":[50,"teste","caixa"],"TR 017-1 RP":[25,"teste","caixa"],"TR 009-1 DT":[50,"teste","caixa"],"TR 008-1 DT":[50,"teste","caixa"],"TR 009 IST":[50,"teste","caixa"],"TR 009-1 IST":[50,"teste","caixa"],"TR 007 IST":[50,"teste","caixa"],"TR 016-1 RP":[25,"teste","caixa"],"TR 008-1 IST":[25,"teste","caixa"],"258":[50,"unidade","caixa"],"PA149":[10,"teste","caixa"],"PA150":[10,"teste","caixa"],"PA02":[10,"placa","pacote"],"PA03":[10,"placa","pacote"],"PA04":[10,"placa","pacote"],"PA406":[10,"placa","pacote"],"PA06":[10,"placa","pacote"],"PA52":[10,"tubo","caixa"],"PA53":[10,"tubo","caixa"],"PA07":[8,"placa","pacote"],"PA08":[10,"placa","pacote"],"PA54":[8,"tubo","caixa"],"PA09":[10,"placa","caixa"],"PA42":[10,"placa","caixa"],"PA55":[10,"tubo","caixa"],"PA344":[10,"placa","caixa"],"PA10":[10,"placa","caixa"],"PA43":[10,"placa","caixa"],"PA11":[10,"placa","pacote"],"PA345":[10,"placa","pacote"],"PA12":[10,"placa","pacote"],"PA56":[10,"tubo","caixa"],"PA13":[8,"placa","pacote"],"PA14":[8,"placa","caixa"],"PA15":[10,"placa","caixa"],"PA57":[10,"tubo","caixa"],"PA16":[8,"placa","pacote"],"PA330":[10,"placa","caixa"],"PA17":[10,"placa","caixa"],"PA340":[10,"placa","caixa"],"PA341":[10,"placa","caixa"],"PA18":[10,"placa","caixa"],"PA19":[10,"placa","caixa"],"PA58":[8,"tubo","caixa"],"PA314":[10,"tubo","caixa"],"PA20":[10,"placa","pacote"],"PA347":[10,"placa","pacote"],"PA346":[10,"placa","pacote"],"PA59":[10,"tubo","caixa"],"PA22":[10,"placa","pacote"],"PA60":[10,"tubo","caixa"],"PA313":[10,"tubo","caixa"],"PA23":[10,"placa","pacote"],"PA61":[8,"tubo","caixa"],"PA316":[10,"tubo","caixa"],"PA24":[5,"placa","pacote"],"PA25":[8,"placa","pacote"],"PA26":[10,"placa","pacote"],"PA380":[10,"placa","pacote"],"PA27":[10,"placa","caixa"],"PA28":[10,"placa","caixa"],"PA29":[10,"placa","caixa"],"PA30":[10,"placa","caixa"],"PA31":[10,"placa","caixa"],"PA32":[10,"placa","pacote"],"PA45":[10,"placa","pacote"],"PA334":[10,"placa","caixa"],"PA46":[10,"placa","caixa"],"PA338":[10,"placa","caixa"],"PA339":[10,"placa","caixa"],"PA384":[10,"placa","pacote"],"PA47":[10,"placa","pacote"],"PA48":[10,"placa","caixa"],"PA33":[10,"placa","pacote"],"PA34":[10,"placa","pacote"],"PA63":[8,"tubo","caixa"],"PA35":[10,"placa","caixa"],"PA36":[10,"placa","pacote"],"PA64":[10,"tubo","caixa"],"PA37":[5,"placa","pacote"],"PA65":[10,"tubo","caixa"],"PA66":[10,"tubo","caixa"],"PA38":[10,"placa","pacote"],"PA39":[8,"placa","pacote"],"PA312":[10,"placa","pacote"],"PA40":[10,"placa","pacote"],"PA335":[10,"placa","caixa"],"PA242":[25,"disco","caixa"],"PA67":[10,"tubo","caixa"],"PA68":[10,"tubo","caixa"],"PA87":[10,"tubo","caixa"],"PA69":[10,"tubo","caixa"],"PA70":[10,"tubo","caixa"],"PA71":[10,"tubo","caixa"],"PA72":[8,"tubo","caixa"],"PA73":[10,"tubo","caixa"],"PA74":[10,"tubo","caixa"],"PA75":[10,"tubo","caixa"],"PA76":[10,"tubo","caixa"],"PA77":[10,"tubo","caixa"],"PA78":[10,"tubo","caixa"],"PA79":[10,"tubo","caixa"],"PA80":[10,"tubo","caixa"],"PA81":[10,"tubo","caixa"],"PA82":[10,"tubo","caixa"],"PA374":[10,"tubo","caixa"],"PA83":[10,"tubo","caixa"],"PA84":[10,"tubo","caixa"],"PA402":[10,"tubo","caixa"],"PA375":[10,"tubo","caixa"],"PA85":[10,"tubo","caixa"],"PA86":[10,"tubo","caixa"],"PA249":[5,"disco","caixa"],"PA354":[10,"tubo","caixa"],"PA88":[10,"tubo","caixa"],"PA353":[10,"tubo","caixa"],"PA349":[10,"placa","pacote"],"PA328":[10,"placa","pacote"],"PA308":[10,"placa","pacote"],"PA350":[10,"placa","pacote"],"PA323":[10,"placa","caixa"],"PA322":[10,"placa","caixa"],"PA325":[10,"placa","pacote"],"PA324":[10,"placa","pacote"],"PA319":[10,"placa","caixa"],"PA318":[10,"placa","caixa"],"PA395":[10,"placa","caixa"],"PA49":[10,"placa","pacote"],"PA329":[10,"placa","caixa"],"PA41":[10,"placa","caixa"],"PA333":[10,"placa","pacote"],"PA321":[10,"placa","pacote"],"PA320":[10,"placa","pacote"],"PA336":[10,"tubo","caixa"],"PA250":[5,"disco","caixa"],"PA251":[5,"disco","caixa"],"PA252":[5,"disco","caixa"],"PA253":[5,"disco","caixa"],"PA254":[5,"disco","caixa"],"PA255":[5,"disco","caixa"],"PA256":[5,"disco","caixa"],"PA291":[10,"unidade","pacote"],"PA292":[10,"unidade","pacote"],"PA352":[5,"flaconete","caixa"],"PA89":[50,"tubo","caixa"],"PA163":[10,"frasco","caixa"],"PA164":[10,"frasco","caixa"],"PA165":[10,"frasco","caixa"],"PA166":[10,"frasco","caixa"],"PA167":[10,"frasco","caixa"],"PA168":[10,"frasco","caixa"],"PA115":[25,"teste","caixa"],"PA116":[16,"teste","caixa"],"PA117":[25,"teste","caixa"],"PA118":[10,"teste","caixa"],"PA120":[10,"teste","caixa"],"PA257":[5,"disco","caixa"],"PA90":[10,"tubo","caixa"],"PA91":[8,"tubo","caixa"],"PA315":[10,"tubo","caixa"],"PA92":[10,"tubo","caixa"],"PA93":[10,"tubo","caixa"],"PA94":[10,"tubo","caixa"],"PA382":[10,"tubo","caixa"],"PA95":[10,"tubo","caixa"],"PA114":[10,"tubo","caixa"],"PA121":[50,"tubo","caixa"],"PA96":[10,"tubo","caixa"],"PA122":[25,"teste","caixa"],"PA123":[5,"teste","caixa"],"PA124":[10,"teste","caixa"],"PA151":[8,"teste","caixa"],"PA153":[5,"teste","caixa"],"PA246":[25,"disco","caixa"],"PA258":[5,"disco","caixa"],"PA260":[5,"disco","caixa"],"PA259":[5,"disco","caixa"],"PA261":[5,"disco","caixa"],"PA262":[5,"disco","caixa"],"PA263":[5,"disco","caixa"],"PA264":[5,"disco","caixa"],"PA265":[5,"disco","caixa"],"PA266":[5,"disco","caixa"],"PA159":[10,"frasco","caixa"],"PA379":[100,"unidade","pacote"],"PA385":[5,"unidade","caixa"],"PA311":[10,"tira","caixa"],"PA161":[12,"frasco","caixa"],"PA50":[10,"placa","caixa"],"PA356":[10,"tubo","caixa"],"PA355":[10,"tubo","caixa"],"PA365":[10,"tubo","caixa"],"PA369":[100,"tubo","caixa"],"PA363":[10,"tubo","caixa"],"PA407":[10,"tubo","caixa"],"PRD00003":[500,"unidade","caixa"],"PRD00005":[500,"unidade","caixa"],"GT2020111":[2000,"unidade","caixa"],"S350RAZPA":[100,"unidade","pacote"],"S240RB":[100,"unidade","pacote"],"3215":[160,"unidade","caixa"],"3266":[200,"unidade","caixa"],"17004":[50,"unidade","pacote"],"18433-NAC":[500,"unidade","pacote"],"454235":[50,"unidade","rack"],"CLT80ES-RGM":[100,"unidade","pacote"],"407":[12,"unidade","dúzia"],"408":[12,"unidade","dúzia"],"409":[12,"unidade","dúzia"],"410":[12,"unidade","dúzia"],"411":[12,"unidade","dúzia"],"412":[12,"unidade","dúzia"],"795":[12,"unidade","dúzia"],"739":[12,"unidade","dúzia"],"CLT50ES-RGM":[1000,"unidade","caixa"],"16":[500,"unidade","pacote"],"CLN-17":[500,"unidade","pacote"],"18":[500,"unidade","pacote"],"CLN-741":[500,"unidade","pacote"],"CLN-742":[500,"unidade","pacote"],"743":[500,"unidade","pacote"],"1210":[25,"suporte","caixa"],"1211":[25,"suporte","caixa"],"1212":[25,"suporte","caixa"],"19150":[250,"unidade","caixa"],"19230":[250,"unidade","caixa"],"P1275":[250,"unidade","caixa"],"P1075":[250,"unidade","caixa"],"P12120":[250,"unidade","caixa"],"P13100":[250,"unidade","caixa"],"P15100":[250,"unidade","caixa"],"P16150":[250,"unidade","caixa"],"P18150":[250,"unidade","caixa"],"P18180":[250,"unidade","caixa"],"P20150":[100,"unidade","caixa"],"P20200":[100,"unidade","caixa"],"P25150":[100,"unidade","caixa"],"P13100B":[250,"unidade","caixa"],"P15100B":[100,"unidade","caixa"],"P16100B":[100,"unidade","caixa"],"P16150B":[250,"unidade","caixa"],"P18180B":[100,"unidade","caixa"],"P20150B":[100,"unidade","caixa"],"P20200B":[100,"unidade","caixa"],"P25150B":[50,"unidade","caixa"],"P25200B":[50,"unidade","caixa"],"P1ML":[10,"unidade","caixa"],"P2ML":[10,"unidade","caixa"],"P5ML":[10,"unidade","caixa"],"P20ML":[10,"unidade","caixa"],"P25ML":[10,"unidade","caixa"],"PV6015":[48,"unidade","caixa"],"PV8015":[48,"unidade","caixa"],"PV10015":[48,"unidade","caixa"],"PV12020":[48,"unidade","caixa"],"PV15020":[24,"unidade","caixa"]};window.unitLn=function(c,pr){var q=(window.QTD||{})[c];if(!q||!pr)return "";var u=pr/q[0];var t="R$ "+u.toLocaleString("pt-BR",{minimumFractionDigits:u<0.1?3:2,maximumFractionDigits:u<0.1?3:2});return '<div class="unl">≈ <b>'+t+'</b> por '+q[1]+' <span>('+q[2]+' c/ '+q[0]+')</span></div>';};
}catch(e){try{console.error(e);}catch(_){}}

/* ==== celular: placeholder da busca ==== */
try{
document.addEventListener('DOMContentLoaded',function(){try{
  if(!matchMedia('(max-width:700px)').matches)return;
  var b=document.getElementById('bannerHome');if(!b)return;
  var pq=document.querySelector('.popq'),of=document.getElementById('ofSec'),cp=document.getElementById('catPanel');
  
  var si=document.getElementById('searchInput');if(si)si.placeholder='Buscar produto, marca ou código';
}catch(e){}});
}catch(e){try{console.error(e);}catch(_){}}

/* ==== ofertas e destaques Greiner ==== */
/* sem try: as function declarations daqui precisam ficar globais, como no <script> antigo */
window.OFERTAS=[
  {c:'TR 017-1 RP',tag:'🏆 Preço do site',txt:'R$ 4,00 por teste · COVID-19 antígeno · pronta entrega',de:146.62},
  {c:'TR 009-1 IST',tag:'🏆 Preço do site',txt:'R$ 1,68 por teste · HBsAg (hepatite B) em tira · pronta entrega',de:89.7},
  {c:'TR 009-1 DT',tag:'🏆 Preço do site',txt:'R$ 4,99 por teste · Dengue IgG/IgM · pronta entrega',de:287.5},
  {c:'TR 010 DT',tag:'🏆 Preço do site',txt:'R$ 10,84 por teste · Dengue NS1 + IgG/IgM · pronta entrega',de:568.67},
  {c:'TR 008-1 IST',tag:'🏆 Preço do site',txt:'R$ 2,35 por teste · Sífilis · pronta entrega'},
  {c:'TR 007 IST',tag:'🏆 Preço do site',txt:'R$ 2,22 por teste · HIV 1/2 · pronta entrega'},
  {c:'TR 008-1 DT',tag:'🏆 Preço do site',txt:'R$ 4,99 por teste · Dengue NS1 · pronta entrega',de:273.12},
  {c:'TR 016-1 RP',tag:'🏆 Preço do site',txt:'R$ 14,90 por teste · RSV (VSR) · pronta entrega',de:431.25}
];
window.TR_TOP={'TR 017-1 RP':1,'TR 009 IST':1,'TR 009-1 IST':1,'TR 009-1 DT':1,'TR 010 DT':1,'TR 008-1 IST':1,'TR 007 IST':1,'TR 008-1 DT':1,'TR 016-1 RP':1};
window.GREINER_DE={"450071": 68.44, "450072": 68.44, "454921": 31.61, "456211": 58.09, "454030": 37.01, "454482": 47.49, "450539": 100.56, "456080": 41.9, "454327": 44.69, "454036": 23.74, "454087": 25.14, "454085": 43.37, "454091": 43.99, "454092": 26.54, "454071": 36.39, "456071": 37.01, "455071": 52.37, "455092": 37.01, "456001": 27.93, "454235": 56.1};
window.GREINER_ORDEM=["454036", "454071", "456071", "454327", "450071", "450072", "454087", "455071", "456001", "455092", "454921", "454092", "454482", "454030", "456211", "454235", "454085", "454091", "456080", "450539"];
function irSecao(id){try{var e=document.getElementById(id);if(e)e.scrollIntoView({behavior:'smooth',block:'start'});}catch(x){}}
function verTodosGreiner(){try{FILTRO.busca='Vacuette';var b=document.getElementById('busca')||document.querySelector('input[type=search]');if(b)b.value='Vacuette';render();var a=document.getElementById('shopAnchor');if(a)a.scrollIntoView({behavior:'smooth'});}catch(e){}}
function montarGreiner(){
  try{
    var sec=document.getElementById('grSec'),g=document.getElementById('grGrid');if(!sec||!g)return;
    var L=GREINER_ORDEM.map(function(c){var i=CATALOG.findIndex(function(p){return p.c===c;});return i<0?null:{i:i,p:CATALOG[i]};}).filter(Boolean);
    if(!L.length){sec.style.display='none';return;}
    g.innerHTML=L.slice(0,8).map(function(x){
      var pr=(window.PRECOS||{})[x.p.c],v=pr&&pr[1]?pr[1]:0;if(!v)return '';var de=GREINER_DE[x.p.c];
      return '<div class="ofc" onclick="abrirProd('+x.i+')"><span class="oft">🏆 Preço do site</span><div class="ofi"><img '+imgMini(x.p,'120px')+' width="120" height="120" loading="lazy" decoding="async" alt=""'+x.p.n.replace(/"/g,'&quot;')+'"></div><div class="ofn">'+x.p.n+'</div><div class="ofp">'+(de&&de>v?'<s>'+brl(de)+'</s>':'')+brl(v)+'</div>'+(typeof unitLn==='function'?'<div class="ofu">'+unitLn(x.p.c,v)+'</div>':'')+'</div>';
    }).join('');
    sec.style.display='';
  }catch(e){}
}
function montarOfertas(){
  try{
    var L=(window.OFERTAS||[]).map(function(o){var i=CATALOG.findIndex(function(p){return p.c===o.c;});return i<0?null:{o:o,i:i,p:CATALOG[i]};}).filter(Boolean);
    var sec=document.getElementById('ofSec'),g=document.getElementById('ofGrid');
    if(!sec||!g||!L.length){if(sec)sec.style.display='none';return;}
    g.innerHTML=L.slice(0,8).map(function(x){
      var pr=(window.PRECOS||{})[x.p.c],v=pr&&pr[1]?pr[1]:0;
      var preco=v?'<div class="ofp">'+(x.o.de?'<s>'+brl(x.o.de)+'</s>':'')+brl(v)+'</div>'+(typeof unitLn==='function'?'<div class="ofu">'+unitLn(x.p.c,v)+'</div>':''):'<div class="ofp" style="font-size:14px;color:#1f3c73">Sob consulta</div>';
      return '<div class="ofc" onclick="abrirProd('+x.i+')"><span class="oft">'+(x.o.tag||'Oferta')+'</span><div class="ofi"><img '+imgMini(x.p,'120px')+' width="120" height="120" loading="lazy" decoding="async" alt=""'+x.p.n.replace(/"/g,'&quot;')+'"></div><div class="ofn">'+x.p.n+'</div><div class="ofd">'+(x.o.txt||x.p.m)+'</div>'+preco+'<button class="ofb" onclick="event.stopPropagation();abrirProd('+x.i+')">Ver oferta</button></div>';
    }).join('');
    sec.style.display='';
  }catch(e){}
}

/* ==== catálogo, carrinho, checkout, conta (bloco principal) ==== */
/* sem try: as function declarations daqui precisam ficar globais, como no <script> antigo */
var DEPTS=[
  {key:'tubo', nome:'Tubos a vácuo', icon:'🩸', cats:['tubo']},
  {key:'agulha', nome:'Seringas e agulhas', icon:'💉', cats:['agulha','seringa','scalp']},
  {key:'lanceta', nome:'Lancetas', icon:'🔺', cats:['lanceta']},
  {key:'coletoram', nome:'Coletores de amostra', icon:'🥤', cats:['coletoram']},
  {key:'curativo', nome:'Curativos, gaze e algodão', icon:'🩹', cats:['curativo']},
  {key:'lamina', nome:'Lâminas e bisturis', icon:'🔬', cats:['lamina']},
  {key:'cubeta', nome:'Cubetas', icon:'🥼', cats:['cubeta']},
  {key:'pipeta', nome:'Pipetas e ponteiras', icon:'💧', cats:['pipeta']},
  {key:'plast', nome:'Descartáveis e plásticos', icon:'🧴', cats:['plast']},
  {key:'meio', nome:'Meios de cultura', icon:'🧫', cats:['meio']},
  {key:'micro', nome:'Microbiologia (discos e corantes)', icon:'🦠', cats:['micro']},
  {key:'bioq', nome:'Reagentes de bioquímica', icon:'⚗️', cats:['bioq']},
  {key:'hemat', nome:'Reagentes de hematologia / coagulação', icon:'🩸', cats:['hemat']},
  {key:'sorol', nome:'Reagentes de sorologia/imunologia', icon:'🧬', cats:['sorol']},
  {key:'controle', nome:'Controles e calibradores', icon:'🎯', cats:['controle']},
  {key:'tr', nome:'Testes rápidos', icon:'🧪', cats:['tr']},
  {key:'equip', nome:'Equipamentos e acessórios', icon:'🖥️', cats:['equip']},
  {key:'vidraria', nome:'Vidraria de laboratório', icon:'⚗️', cats:['vidraria']}
];
/* 31/10/2026 (SEO): cada departamento tem página estática em /categoria/ — os links da loja levam o href dela (o robô do Google segue; o clique continua filtrando na própria loja) */
var CAT_URL={tubo:'tubos-a-vacuo',agulha:'seringas-e-agulhas',lanceta:'lancetas',coletoram:'coletores-de-amostra',curativo:'curativos-gaze-e-algodao',lamina:'laminas-e-bisturis',cubeta:'cubetas',pipeta:'pipetas-e-ponteiras',plast:'descartaveis-e-plasticos',meio:'meios-de-cultura',micro:'microbiologia',bioq:'reagentes-de-bioquimica',hemat:'reagentes-de-hematologia-e-coagulacao',sorol:'reagentes-de-sorologia-e-imunologia',controle:'controles-e-calibradores',tr:'testes-rapidos',equip:'equipamentos-e-acessorios',vidraria:'vidraria-de-laboratorio'};
function catHref(k){return CAT_URL[k]?'/categoria/'+CAT_URL[k]+'.html':'#shopAnchor';}
var _DEPTOF={};function deptOf(catCode){var k=String(catCode);if(_DEPTOF.hasOwnProperty(k))return _DEPTOF[k];for(var d of DEPTS){if(d.cats.indexOf(catCode)>-1)return (_DEPTOF[k]=d.key);}return (_DEPTOF[k]='outros');}

var SEED=window.SEED||[];

var CATALOG=SEED.slice();
var CART=(function(){try{var v=JSON.parse(localStorage.getItem('sullab_cart')||'[]');return Array.isArray(v)?v:[];}catch(e){return [];}})();
var CNPJ=true; 
var FILTRO={dept:'', marca:'', busca:''};
var _CUR=[],_SHOWN=0,_PAGE=24,_PG=1,_card=null,_io=null;  
var WHATS='5524988383100';

/* 30/10/2026: cartões usam a miniatura WebP de 320 px (campo t do catálogo); a foto grande fica no srcset (telas densas) e no modal */
function imgMini(p,sz){if(!p)return '';var t=p.t,g=p.img||'';if(!t)return 'src="'+g+'"';t='/'+String(t).replace(/^\//,'');return 'src="'+t+'" srcset="'+t+' 320w, '+g+' 1000w" sizes="'+(sz||'160px')+'"';}
function miniDe(c){for(var i=0;i<CATALOG.length;i++){if(CATALOG[i].c===c)return CATALOG[i];}return null;}
/* 30/10/2026: formatador criado uma vez (toLocaleString a cada preço custava ~90 ms no celular); mesmo texto de antes */
var _NFBRL=null;try{_NFBRL=new Intl.NumberFormat('pt-BR',{minimumFractionDigits:2,maximumFractionDigits:2});}catch(e){}
function brl(v){return 'R$ '+(_NFBRL?_NFBRL.format(Number(v)):Number(v).toLocaleString('pt-BR',{minimumFractionDigits:2,maximumFractionDigits:2}));}
function precoDe(p){var r=(window.PRECOS||{})[p.c];return r&&r[1]?r[1]:0;}
function precoItem(x){var r=(window.PRECOS||{})[x.c];var b=r&&r[1]?r[1]:0;if(b&&x.kq&&x.kd&&x.qty){var q=Math.min(x.kq,x.qty);return (b*(x.qty-q)+b*(1-x.kd)*q)/x.qty;}return b;}
function precoBase(x){var r=(window.PRECOS||{})[x.c];return r&&r[1]?r[1]:0;}

function montarDeptNav(){
  var el=document.getElementById('deptNav');
  var html='<div class="dept all" onclick="setDept(\'\')">☰ Todos os departamentos</div>';
  DEPTS.forEach(function(d){
    var n=CATALOG.filter(p=>deptOf(p.k)===d.key).length;
    if(n>0) html+='<div class="dept" data-d="'+d.key+'" onclick="setDept(\''+d.key+'\')">'+d.icon+' '+d.nome+'</div>';
  });
  el.innerHTML=html;
}
function montarCatTiles(){
  var el=document.getElementById('catTiles');var html='';
  DEPTS.forEach(function(d){
    var n=CATALOG.filter(p=>deptOf(p.k)===d.key).length; if(!n)return;
    html+='<div class="ctile" onclick="setDept(\''+d.key+'\')"><div class="ci">'+d.icon+'</div><div><b>'+d.nome+'</b><small>'+n+' produto'+(n>1?'s':'')+'</small></div></div>';
  });
  if(!el.querySelector('.cph'))el.innerHTML=html;
  document.getElementById('footCats').innerHTML=DEPTS.filter(d=>CATALOG.some(p=>deptOf(p.k)===d.key)).slice(0,6).map(d=>'<a href="'+catHref(d.key)+'" onclick="setDept(\''+d.key+'\');return false">'+d.nome+'</a>').join('');
}
function montarBrands(){
  var brands={};CATALOG.forEach(p=>{if(p.m)brands[p.m]=(brands[p.m]||0)+1;});
  var top=Object.keys(brands).sort((a,b)=>brands[b]-brands[a]).slice(0,5);
  var desc={'Vacuette':'Tubos a vácuo','Greiner':'Coleta a vácuo','Newprov':'Meios & corantes','DeepBlue':'Testes rápidos','Ebram':'Reagentes & equipamentos','CRAL':'Cubetas & descartáveis','SULLAB Kit':'Kits prontos'};
  var _bs=document.getElementById('brandStrip'); if(_bs)_bs.innerHTML='';
  var _sp=document.getElementById('statProdutos'); if(_sp)_sp.textContent=CATALOG.length.toLocaleString('pt-BR');
  var sc=document.getElementById('searchCat');
  sc.innerHTML='<option value="">Todas as categorias</option>'+DEPTS.filter(d=>CATALOG.some(p=>deptOf(p.k)===d.key)).map(d=>'<option value="'+d.key+'">'+d.nome+'</option>').join('');
}
function montarFiltros(){
  var f=document.getElementById('filters');
  var deptCounts=DEPTS.map(d=>({d:d, n:CATALOG.filter(p=>deptOf(p.k)===d.key).length})).filter(x=>x.n>0);
  var brands={};CATALOG.forEach(p=>{if(p.m)brands[p.m]=(brands[p.m]||0)+1;});
  var html='<div class="fg"><h4>Categoria</h4>';
  html+='<label class="fopt"><input type="radio" name="fd" '+(FILTRO.dept===''?'checked':'')+' onclick="setDept(\'\')"> Todas <span class="n">'+CATALOG.length+'</span></label>';
  deptCounts.forEach(x=>{html+='<label class="fopt"><input type="radio" name="fd" '+(FILTRO.dept===x.d.key?'checked':'')+' onclick="setDept(\''+x.d.key+'\')"> '+x.d.nome+' <span class="n">'+x.n+'</span></label>';});
  html+='</div>';
  f.innerHTML=html;
}

var KWMAP=null,_kwLoading=false;
function ensureKw(cb){if(KWMAP){return cb&&cb();}if(_kwLoading){return setTimeout(function(){ensureKw(cb);},120);}_kwLoading=true;fetch('kw.json').then(function(r){return r.json();}).then(function(d){KWMAP=d;cb&&cb();}).catch(function(){KWMAP={};cb&&cb();});}
var FTMAP=null,_ftLoading=false;
function ensureFT(cb){if(FTMAP){return cb&&cb();}if(_ftLoading){return setTimeout(function(){ensureFT(cb);},120);}_ftLoading=true;fetch('ft.json').then(function(r){return r.json();}).then(function(d){FTMAP=d;cb&&cb();}).catch(function(){FTMAP={};cb&&cb();});}
function semAcento(s){return String(s).toLowerCase().normalize('NFD').replace(/[\u0300-\u036f]/g,'');}
function _nrmMed(t){return String(t).replace(/[×✕]/g,'x').replace(/ø/g,' ').replace(/(\d)\s*x\s*(\d)/g,'$1x$2').replace(/(\d)\s+(mm|ml|cm|ul)\b/g,'$1$2');}
/* ==== busca (31/10/2026): sinônimos, plurais, código sem espaço/hífen, 1 erro de digitação e relevância ==== */
var BUSCA_STOP={de:1,do:1,da:1,dos:1,das:1,para:1,pra:1,com:1,e:1,em:1,o:1,a:1,os:1,as:1,um:1,uma:1,no:1,na:1,ml:1,mls:1};
/* troca: o termo vira só a alternativa (marca/apelido que não existe no catálogo) */
var SINON_TROCA={vacutainer:['vacuette'],vacuntainer:['vacuette'],vacutaine:['vacuette'],vacutainner:['vacuette'],bd:['vacuette'],greiner:['vacuette'],eppendorf:['microtubo'],eppendorff:['microtubo'],
  hcg:['gravidez','hcg'],covid19:['covid'],coronavirus:['covid'],sarscov2:['covid'],'sars-cov-2':['covid']};
/* soma: o termo continua valendo e ganha alternativas (cor de tampa: "ponteira amarela" continua achando a ponteira) */
var SINON_SOMA={roxo:['edta'],roxa:['edta'],lilas:['edta'],amarelo:['gel'],amarela:['gel'],vermelho:['soro','ativador'],vermelha:['soro','ativador'],
  azul:['citrato'],verde:['heparina'],cinza:['fluoreto','glicose'],gravidez:['hcg']};
/* frases que viram um termo só (antes de separar as palavras) */
var SINON_FRASE=[[/\btampa (roxa|roxo|lilas)\b/g,'edta'],[/\btampa (amarela|amarelo)\b/g,'gel'],[/\btampa (vermelha|vermelho)\b/g,'vermelho'],[/\btampa azul\b/g,'citrato'],
  [/\btampa verde\b/g,'heparina'],[/\btampa cinza\b/g,'cinza'],[/\bteste (de )?gravidez\b/g,'gravidez'],[/\bbeta ?hcg\b/g,'hcg']];
function _bNorm(t){return _nrmMed(semAcento(t)).replace(/(\d)\s*mls?\b/g,'$1ml');}
function _bComp(t){return String(t).replace(/[\s\-\.\/_]+/g,'');}
/* plural → singular (-s, -es, -ões, -ais, -éis, -is) */
function _bVaris(t){var v=[t];if(t.length>3&&/s$/.test(t)){v.push(t.slice(0,-1));if(/es$/.test(t)&&t.length>4)v.push(t.slice(0,-2));
  if(/oes$/.test(t))v.push(t.slice(0,-3)+'ao');if(/ais$/.test(t))v.push(t.slice(0,-3)+'al');if(/eis$/.test(t)){v.push(t.slice(0,-3)+'el');v.push(t.slice(0,-3)+'il');}
  if(/[^ae]is$/.test(t)&&t.length>4)v.push(t.slice(0,-2)+'il');}
  return v;}
/* distância de edição ≤ 1 (troca, falta, sobra ou inversão de duas letras) */
function _bDist1(a,b){if(a===b)return true;var la=a.length,lb=b.length;if(Math.abs(la-lb)>1)return false;var i=0;while(i<la&&i<lb&&a[i]===b[i])i++;
  if(la===lb){if(a.slice(i+1)===b.slice(i+1))return true;return a[i]===b[i+1]&&a[i+1]===b[i]&&a.slice(i+2)===b.slice(i+2);}
  return la>lb?a.slice(i+1)===b.slice(i):a.slice(i)===b.slice(i+1);}
var _bVoc=null,_bVocTxt='',_bVocN=-1;
function _bVocab(){var n=CATALOG.length+(KWMAP?1e6:0);if(_bVoc&&_bVocN===n)return _bVoc;var s={};
  CATALOG.forEach(function(p){(_bNorm(p.n+' '+p.m)+' '+_bNorm((KWMAP&&KWMAP[p.c])||'')).split(/[^a-z0-9]+/).forEach(function(w){if(w.length>=4&&!/^\d+$/.test(w))s[w]=1;});});
  _bVoc=Object.keys(s);_bVocTxt=' '+_bVoc.join(' ')+' ';_bVocN=n;_bPrepC={};return _bVoc;}
function _bFuzzy(t){var out=[];if(t.length<5)return out;_bVocab();
  for(var i=0;i<_bVoc.length;i++){var w=_bVoc[i];if(Math.abs(w.length-t.length)<=1&&w!==t&&_bDist1(t,w))out.push(w);}return out;}
var _bPrepC={};
/* prepara o termo: lista de grupos; cada grupo = alternativas [{t, f(fator)}]; o produto precisa casar todos os grupos */
function buscaPrep(termo){var key=String(termo||'');if(_bPrepC[key])return _bPrepC[key];
  var q=_bNorm(key);SINON_FRASE.forEach(function(r){q=q.replace(r[0],r[1]);});
  var tk=q.split(/[^a-z0-9\-,]+/).map(function(t){return t.replace(/^[\-,]+|[\-,]+$/g,'');}).filter(function(t){return t&&!BUSCA_STOP[t];});
  if(tk.length>1)tk=tk.filter(function(t){return t!=='kit'&&t!=='kits';});
  var grupos=tk.map(function(t){var alt=[],vis={};var add=function(x,f){if(x&&!vis[x]){vis[x]=1;alt.push({t:x,f:f});}};
    if(SINON_TROCA[t]){SINON_TROCA[t].forEach(function(x){add(x,0.9);});}
    else{_bVaris(t).forEach(function(x,i){add(x,i?0.95:1);});if(SINON_SOMA[t])SINON_SOMA[t].forEach(function(x){add(x,0.85);});}
    return {t:t,alt:alt,c:_bComp(t)};});
  var r={q:q,qc:_bComp(q),g:grupos};
  /* erro de digitação: só para palavra (≥5 letras) que não aparece em nenhum produto */
  if(CATALOG&&CATALOG.length){_bVocab();grupos.forEach(function(g){if(g.t.length<5||/\d/.test(g.t))return;
    var acha=g.alt.some(function(a){return _bVocTxt.indexOf(a.t)>=0;});if(acha)return;
    _bFuzzy(g.t).forEach(function(w){g.alt.push({t:w,f:0.7,fz:1});});});}
  _bPrepC[key]=r;return r;}
function _bTem(h,g){var best=0;for(var i=0;i<g.alt.length;i++){var a=g.alt[i];if(a.f>best&&h.indexOf(a.t)>=0)best=a.f;}return best;}
/* campos de um produto para a busca (cache por produto) */
var _bCache={};
function _bCampos(p){var k=(KWMAP?'k':'s')+p.c,o=_bCache[p.c];if(o&&o.k===k)return o;
  var kw=_bNorm((KWMAP&&KWMAP[p.c])||'');if(/covid/.test(_bNorm(p.n)+kw))kw+=' coronavirus sars-cov-2 sarscov2 covid19';
  return (_bCache[p.c]={k:k,n:_bNorm(p.n),m:_bNorm(p.m||''),c:_bNorm(p.c),cc:_bComp(_bNorm(p.c)),kw:kw});}
/* relevância: nome (4) > marca (3) > código (2,5) > palavras-chave (1); 0 = não casa */
function buscaPontua(p,termo){var r=typeof termo==='string'?buscaPrep(termo):termo,F=_bCampos(p);if(!r.g.length)return 0;
  if(r.qc.length>=3&&/\d/.test(r.qc)&&(F.cc===r.qc||F.cc.indexOf(r.qc)===0))return 100+(F.cc===r.qc?10:0);
  var tot=0;for(var i=0;i<r.g.length;i++){var g=r.g[i],s=Math.max(4*_bTem(F.n,g),3*_bTem(F.m,g),2.5*_bTem(F.c,g),(g.c.length>=3&&/\d/.test(g.c)&&F.cc.indexOf(g.c)>=0)?2.5:0,1*_bTem(F.kw,g));
    if(!s)return 0;tot+=s;}
  tot=tot/r.g.length;if(r.q.length>3&&F.n.indexOf(r.q)>=0)tot+=3;return tot;}
/* compatível com o uso antigo (busca do carrinho): hay = texto livre do produto */
function buscaCasa(hay,termo){var r=buscaPrep(termo),h=_nrmMed(String(hay));if(!r.g.length)return false;
  var hc=_bComp(h);if(r.qc.length>=3&&/\d/.test(r.qc)&&hc.indexOf(r.qc)>=0)return true;
  return r.g.every(function(g){return _bTem(h,g)>0||(g.c.length>=3&&/\d/.test(g.c)&&hc.indexOf(g.c)>=0);});}
/* "Você quis dizer…": troca cada palavra sem resultado pela mais parecida do catálogo (até 2 letras de diferença) */
function _bDist(a,b){var m=a.length,n=b.length,d=[],i,j;for(i=0;i<=m;i++){d[i]=[i];}for(j=0;j<=n;j++)d[0][j]=j;
  for(i=1;i<=m;i++)for(j=1;j<=n;j++){d[i][j]=Math.min(d[i-1][j]+1,d[i][j-1]+1,d[i-1][j-1]+(a[i-1]===b[j-1]?0:1));}return d[m][n];}
function buscaSugestao(termo){try{var r=buscaPrep(termo);_bVocab();var mud=false;
  var pal=r.g.map(function(g){if(g.t.length<5||/\d/.test(g.t))return g.t;if(_bVocTxt.indexOf(g.t)>=0)return g.t;
    var best=null,bd=3,lim=g.t.length>=8?2:1;for(var i=0;i<_bVoc.length;i++){var w=_bVoc[i];if(Math.abs(w.length-g.t.length)>2)continue;var d=_bDist(g.t,w);if(d<bd){bd=d;best=w;}}
    if(best&&bd<=lim){mud=true;return best;}return g.t;});
  if(!mud)return '';var s=pal.join(' ');return CATALOG.some(function(p){return buscaPontua(p,s)>0;})?s:'';}catch(e){return '';}}
/* tela de busca sem resultado */
var BUSCA_VAZIA_CATS=[['tr','Testes rápidos'],['tubo','Tubos a vácuo'],['agulha','Seringas e agulhas'],['meio','Meios de cultura'],['pipeta','Pipetas e ponteiras'],['plast','Descartáveis e plásticos']];
function buscaVaziaHtml(t){var e=function(s){return String(s).replace(/[&<>"']/g,function(c){return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c];});};
  var sug=buscaSugestao(t),js=function(s){return e(String(s).replace(/[\\'"]/g,''));};
  var cats=BUSCA_VAZIA_CATS.filter(function(c){return CATALOG.some(function(p){return deptOf(p.k)===c[0];});});
  return '<div class="empty bvz"><div style="font-size:16px;color:var(--navy);font-weight:700;margin-bottom:6px">Nenhum produto encontrado para “'+e(t)+'”.</div>'+
    (sug?'<div style="margin:8px 0 12px">Você quis dizer <a class="lk" style="color:var(--navy-l);cursor:pointer;font-weight:700;text-decoration:underline" onclick="buscarTermo(\''+js(sug)+'\')">'+e(sug)+'</a>?</div>':'')+
    '<div style="margin:10px 0 6px">Veja as categorias:</div><div class="popq" style="justify-content:center;margin:0 0 14px">'+
    cats.map(function(c){return '<span onclick="setDept(\''+c[0]+'\')">'+e(c[1])+'</span>';}).join('')+'</div>'+
    '<div style="margin-top:6px">Tem uma lista de itens? <button type="button" class="ckwa" style="display:inline-block;width:auto;margin:6px 4px;padding:8px 14px" onclick="abrirListaOrcamento()">📋 Colar lista</button></div>'+
    '<div style="margin-top:8px;font-size:13px">Não achou? <a class="lk" onclick="abrirContatoWA(\'equipe\',\''+js(t)+'\')" style="color:var(--navy-l);cursor:pointer;font-weight:700">Avise a equipe que você precisa</a> — verificamos se temos.</div></div>';}
/* ==== fim busca ==== */
var TOP_VENDA=['25492','454087','454036','456001','454921','PA03','PA36','PA31','PA186','743','PRD00003','450072','410','CLT24H2LT','18260NM','18248A','PA26','PA384','PA85','PA14','PA187','PA406','454482','454235','456211','454071','455071','CLT80SNM','CLT50SM','S240RB'];
function filtrados(){
  var _rel={},_bq=FILTRO.busca?buscaPrep(FILTRO.busca):null;
  var arr=CATALOG.filter(function(p){
    if(FILTRO.dept && deptOf(p.k)!==FILTRO.dept) return false;
    if(FILTRO.marca && p.m!==FILTRO.marca) return false;
    if(FILTRO.busca){
      var _r=buscaPontua(p,_bq);if(!_r)return false;_rel[p.c]=_r;
    }
    return true;
  });
  var s=document.getElementById('sortSel').value;
  if(s==='menor')arr.sort((a,b)=>(precoDe(a)||9e9)-(precoDe(b)||9e9));
  else if(s==='maior')arr.sort((a,b)=>(precoDe(b)||0)-(precoDe(a)||0));
  else if(s==='az')arr.sort((a,b)=>a.n.localeCompare(b.n));
  else{  
    var _sc=function(p){var t=TOP_VENDA.indexOf(String(p.c));var v=(t>=0?1000-t:0)+(p.selo?300:0);var pr=(window.PRECOS||{})[p.c];if(pr&&pr[1])v+=100;if(p.img&&!/logo-sullab/.test(p.img))v+=20;return v;};
    /* com busca: relevância primeiro (nome > marca > código > palavras-chave); mais vendidos desempatam */
    arr=arr.map(function(p,ix){return [p,_sc(p),ix,_rel[p.c]||0];}).sort(function(a,b){return (b[3]-a[3])||(b[1]-a[1])||(a[2]-b[2]);}).map(function(x){return x[0];});
  }
  return arr;
}
var _bvT=null,_bvSent={};
function _logBuscaVazia(t){try{t=String(t||'').trim().slice(0,80);if(t.length<2)return;clearTimeout(_bvT);_bvT=setTimeout(function(){var k=t.toLowerCase();if(_bvSent[k])return;_bvSent[k]=1;
  sullabEvent('busca_sem_resultado',{termo:t,produto:(window.matchMedia&&matchMedia('(max-width:700px)').matches)?'celular':'computador'});
  try{if(window.gtag){gtag('event','busca_sem_resultado',{search_term:t});gtag('event','busca_vazia',{search_term:t,termo:t});}}catch(e){}},1500);}catch(e){}}
function render(){
  var arr=filtrados();
  document.getElementById('resCount').textContent=arr.length;
  var t=document.getElementById('shopTitle');
  if(FILTRO.busca)t.textContent='Resultados para "'+FILTRO.busca+'"';
  else if(FILTRO.dept){var d=DEPTS.find(x=>x.key===FILTRO.dept);t.textContent=d?d.nome:'Catálogo';}
  else if(FILTRO.marca)t.textContent=FILTRO.marca;
  else t.textContent='Catálogo';
  var g=document.getElementById('grid');
  if(!arr.length){if(FILTRO.busca)_logBuscaVazia(FILTRO.busca);g.innerHTML=FILTRO.busca?buscaVaziaHtml(FILTRO.busca):'<div class="empty">Nenhum produto encontrado.<br>Tente outro termo ou <a class="lk" onclick="abrirContatoWA(\'duvida\')" style="color:var(--navy-l);cursor:pointer">peça pelo WhatsApp</a>.</div>';_CUR=[];_SHOWN=0;var _mw=document.getElementById('moreWrap');if(_mw)_mw.innerHTML='';return;}
  _CUR=arr;_PG=1;_SHOWN=Math.min(arr.length,_PAGE);_card=function(p){
    var i=CATALOG.indexOf(p);
    var selo=((window.PIX3&&window.PIX3[p.c])||(window.TR_TOP&&window.TR_TOP[p.c]))?'<span class="selo best">🏆 Tabela exclusiva do site</span>':p.selo==='hot'?'<span class="selo hot">🔥 Mais procurado</span>':(p.selo==='top'?'<span class="selo">⭐ Mais vendido</span>':'');
    var precoBloco='';var _pr=(window.PRECOS||{})[p.c];if(_pr&&_pr[1]){precoBloco='<div style="margin:6px 0 2px;line-height:1.32"><div style="font-size:19px;font-weight:800;color:#2f9e63">'+brl(_pr[1])+'</div>'+unitLn(p.c,_pr[1])+'<div class="pixl">💚 <b>'+brl(Math.round(_pr[1]*(100-pixPct(p.c)*100))/100)+'</b> no Pix <span>'+Math.round(pixPct(p.c)*100)+'% off</span></div>'+seloMinHtml(p.c)+'</div>';}
    var btns='<div class="stepper"><button onclick="step('+i+',-1,this)">−</button><span>1</span><button onclick="step('+i+',1,this)">+</button></div><button class="add" onclick="addCart('+i+',this)">+ Carrinho</button>';
    return '<div class="prod" data-c="'+String(p.c).replace(/"/g,'&quot;')+'" onclick="cardClick(event,'+i+')">'+selo+
      '<div class="ph"><img '+imgMini(p,'160px')+' loading="lazy" decoding="async" width="160" height="160" alt="'+p.n+'" onerror="this.removeAttribute(\'srcset\');this.src=\'/img/logo-sullab.png\';this.style.opacity=.35"></div>'+
      '<div class="pb"><span class="bc">'+p.m+' · cód. '+p.c+'</span>'+
      '<div class="pt">'+p.n+'</div>'+
      precoBloco+
      '<div class="pf">'+btns+'</div></div></div>';
  };g.innerHTML=_CUR.slice(0,_SHOWN).map(_card).join('');_more();
}
function _pags(){return Math.max(1,Math.ceil(_CUR.length/_PAGE));}
function _more(){var w=document.getElementById('moreWrap');if(!w)return;var n=_pags();if(n<=1){w.innerHTML='';return;}
  var a=(_PG-1)*_PAGE+1,b=Math.min(_CUR.length,_PG*_PAGE),h='',L=[],k;
  L.push(1);for(k=_PG-2;k<=_PG+2;k++)if(k>1&&k<n)L.push(k);L.push(n);
  var last=0;L.forEach(function(k){if(k-last>1)h+='<span class="pgDots">…</span>';h+='<button class="pgB'+(k===_PG?' on':'')+'" onclick="irPag('+k+')">'+k+'</button>';last=k;});
  w.innerHTML='<div class="pgWrap"><div class="pgInfo">Mostrando '+a+'–'+b+' de '+_CUR.length+' produtos</div><div class="pgNav">'+(_PG>1?'<button class="pgB pgS" onclick="irPag('+(_PG-1)+')">‹ Anterior</button>':'')+h+(_PG<n?'<button class="pgB pgS" onclick="irPag('+(_PG+1)+')">Próxima ›</button>':'')+'</div></div>';}
function irPag(n){if(!_card)return;n=Math.max(1,Math.min(_pags(),n));_PG=n;var g=document.getElementById('grid');var ini=(n-1)*_PAGE;_SHOWN=Math.min(_CUR.length,ini+_PAGE);g.innerHTML=_CUR.slice(ini,_SHOWN).map(_card).join('');_more();try{var t=document.getElementById('shopTitle')||g;var y=t.getBoundingClientRect().top+window.pageYOffset-90;window.scrollTo({top:Math.max(0,y),behavior:'smooth'});}catch(e){}}
function verMais(){irPag(_PG+1);}
function _setupIO(){}

function setDept(k){FILTRO.dept=k;FILTRO.marca='';FILTRO.busca='';document.getElementById('searchInput').value='';montarFiltros();render();irProdutos();marcarNav();}
function setMarca(m){FILTRO.marca=m;FILTRO.busca='';montarFiltros();render();irProdutos();}
function buscarTermo(t){var el=document.getElementById('searchInput');el.value=t;fazerBusca();}
function fazerBusca(){FILTRO.busca=document.getElementById('searchInput').value.trim();var sc=document.getElementById('searchCat').value;if(sc)FILTRO.dept=sc;FILTRO.marca='';ensureKw(function(){montarFiltros();render();irProdutos();});}
function marcarNav(){[...document.querySelectorAll('#deptNav .dept')].forEach(e=>e.classList.toggle('on',e.getAttribute('data-d')===FILTRO.dept));}
function irProdutos(){document.getElementById('shopAnchor').scrollIntoView({behavior:'smooth',block:'start'});}
function toggleCNPJ(){CNPJ=!CNPJ;document.getElementById('cnpjSwitch').classList.toggle('off',!CNPJ);render();atualizarCart();}

function step(i,d,btn){var sp=btn.parentElement.querySelector('span');var v=Math.max(1,(parseInt(sp.textContent)||1)+d);sp.textContent=v;}
function addCart(i,btn){
  var qty=parseInt(btn.parentElement.querySelector('.stepper span').textContent)||1;
  var p=CATALOG[i];
  var ex=CART.find(x=>x.c===p.c);
  if(ex)ex.qty+=qty; else CART.push({c:p.c,n:p.n,m:p.m,img:p.img,pub:p.pub,cnpj:p.cnpj,qty:qty});
  salvarCart();atualizarCart();
  btn.textContent='✓ Adicionado';btn.style.background='var(--green)';
  setTimeout(()=>{btn.textContent='Adicionar';btn.style.background='';},1100);
  abrirCarrinho();
}
function salvarCart(){localStorage.setItem('sullab_cart',JSON.stringify(CART));}
function rmCart(c){CART=CART.filter(x=>x.c!==c);salvarCart();atualizarCart();}
function qtyCart(c,d){var it=CART.find(x=>x.c===c);if(!it)return;it.qty=Math.max(1,Math.min(99999,it.qty+d));salvarCart();atualizarCart();}
function setQtyCart(c,v){var it=CART.find(x=>x.c===c);if(!it)return;var n=parseInt(String(v).replace(/\D/g,''),10);if(!n||n<1)n=1;it.qty=Math.min(99999,n);salvarCart();atualizarCart();}
function totalCart(){return CART.reduce((s,x)=>s+precoItem(x)*x.qty,0);}
function atualizarCart(){
  var n=CART.reduce((s,x)=>s+x.qty,0);
  document.getElementById('cartBadge').textContent=n;
  document.getElementById('cartLabel').textContent=n?(n+(n===1?' item':' itens')):'vazio';
  var dc=document.getElementById('dhCount');if(dc)dc.textContent=CART.length?('· '+CART.length+(CART.length===1?' produto':' produtos')+' · '+n+(n===1?' unidade':' unidades')):'';
  var di=document.getElementById('ditems'),db=document.getElementById('dbar');
  if(!CART.length){di.innerHTML='<div class="dempty">🛒 Seu carrinho está vazio.<br><span style="font-size:13px">Use a busca acima para encontrar produtos e montar seu pedido.</span></div>';document.getElementById('df').innerHTML='';if(db)db.innerHTML='';return;}
  di.innerHTML=CART.map(function(x){
    var c=String(x.c).replace(/'/g,"\\'");
    return '<div class="citem"><img '+imgMini(miniDe(x.c)||x,'76px')+' alt="" width="76" height="76" decoding="async" onerror="this.removeAttribute(\'srcset\');this.src=\'/img/logo-sullab.png\'"><div style="min-width:0"><div class="ct">'+x.n+'</div><div class="cc">'+x.m+' · cód. '+x.c+'</div></div>'+
      '<div class="qctl"><div class="stepper"><button onclick="qtyCart(\''+c+'\',-1)" aria-label="Diminuir">−</button><input type="text" inputmode="numeric" value="'+x.qty+'" aria-label="Quantidade" onfocus="this.select()" onchange="setQtyCart(\''+c+'\',this.value)" onkeydown="if(event.key===\'Enter\'){this.blur();}"><button onclick="qtyCart(\''+c+'\',1)" aria-label="Aumentar">+</button></div><button class="rm" onclick="rmCart(\''+c+'\')">🗑 remover</button></div>'+
      _cpLinha(x)+'</div>';
  }).join('');
  var sub=totalCart(),semPreco=CART.some(function(x){return !precoItem(x);});
  document.getElementById('df').innerHTML=
    '<div style="font-size:16px;font-weight:800;color:var(--navy);margin-bottom:10px">Resumo do pedido</div>'+
    '<div class="row"><span>'+CART.length+(CART.length===1?' produto':' produtos')+' · '+n+(n===1?' unidade':' unidades')+'</span></div>'+
    (sub>0?'<div class="row"><span>Subtotal</span><b class="tot">'+brl(sub)+'</b></div><div class="pixbox">💚 <span>Pague no <b>Pix</b> e ganhe <b>'+(CART.every(function(x){return window.PIX3[x.c];})?'3% de desconto':(CART.some(function(x){return window.PIX3[x.c];})?'desconto (5%; tubos e agulhas Vacuette 3%)':'5% de desconto'))+'</b><small>Total no Pix: <b>'+brl(Math.round(CART.reduce(function(s2,x){return s2+(Math.round(precoItem(x)*(1-pixPct(x.c))*100)/100)*x.qty;},0)*100)/100)+'</b> · NF-e em todo pedido</small></span></div>':'')+
    (sub>0?'<div id="progMin" class="progMin">'+progHtml()+'</div>':'')+
    '<div class="gbox" id="gbox"></div>'+
    (semPreco?'<div class="note">Alguns itens são sob consulta: peça o orçamento pelo WhatsApp.</div>':'')+
    (sub>0?btnFinalizarHtml(semPreco):'')+
    '<a class="wbtn" style="background:#fff;color:#128c4a;border:1px solid #25D366" onclick="enviarOrcamento()">📄 Pedir orçamento pelo WhatsApp</a>'+
    (!semPreco&&sub>0?'<button class="ckwa ckduv" onclick="duvidaCheckout(\'carrinho\')">💬 Dúvida? Falar com um vendedor</button>':'');
  if(db)db.innerHTML='<div class="bt">'+n+(n===1?' unidade':' unidades')+(sub>0?'<b>'+brl(sub)+'</b>':'')+'</div>'+((!semPreco&&sub>0)?(faltaTubo()>0?'<a class="dmin" role="button" onclick="minimoBloqueado(\'barra_carrinho\')">Faltam '+brl(faltaTubo())+'</a>':'<a role="button" onclick="abrirCheckout()">Finalizar compra</a>'):'<a role="button" onclick="enviarOrcamento()">Pedir orçamento</a>');
  gboxRender();
}

var _csT=null;
function cartBuscar(){clearTimeout(_csT);_csT=setTimeout(_cartBuscarGo,140);}
function _cartBuscarGo(){
  var el=document.getElementById('cartSearch'),box=document.getElementById('cartRes');if(!el||!box)return;
  var q=el.value.trim();
  if(q.length<2){box.className='cres';box.innerHTML='';return;}
  ensureKw(function(){
    if(el.value.trim()!==q)return;
    var arr=CATALOG.filter(function(p){
      var hay=semAcento(p.n+' '+p.m+' '+p.c+' '+((KWMAP&&KWMAP[p.c])||''));
      if(/covid/.test(hay))hay+=' coronavirus sars-cov-2 sarscov2 covid19';
      return buscaCasa(hay,q);
    });
    arr.sort(function(a,b){return (precoDe(b)>0?1:0)-(precoDe(a)>0?1:0)||(b.selo?1:0)-(a.selo?1:0);});
    var tot=arr.length,list=arr.slice(0,10);
    if(!tot){box.className='cres on';box.innerHTML='<div class="none">Nenhum produto encontrado para “'+q.replace(/</g,'&lt;')+'”.<br><a class="lk" style="color:var(--navy-l,#1f5fa8);cursor:pointer;font-weight:700" onclick="abrirContatoWA(\'duvida\',\'Procuro: '+q.replace(/[\\\'"<]/g,'')+'\')">Peça pelo WhatsApp</a></div>';return;}
    box.className='cres on';
    box.innerHTML='<div class="rhd"><span>'+tot+(tot===1?' resultado':' resultados')+(tot>10?' · mostrando 10':'')+'</span>'+(tot>10?'<a onclick="cartVerTodos()">Ver todos no catálogo →</a>':'<a onclick="document.getElementById(\'cartSearch\').value=\'\';cartBuscar()">Limpar</a>')+'</div>'+
      list.map(function(p){
        var pr=precoDe(p),ex=CART.find(function(x){return x.c===p.c;}),c=String(p.c).replace(/"/g,'');
        return '<div class="rr" data-c="'+c+'"><img '+imgMini(p,'52px')+' alt="" loading="lazy" width="52" height="52" onerror="this.removeAttribute(\'srcset\');this.src=\'/img/logo-sullab.png\'"><div class="rn">'+p.n+'<small>'+p.m+' · cód. '+p.c+'</small>'+(ex?'<span class="incart">✓ no carrinho: '+ex.qty+'</span>':'')+'</div>'+
          (pr?'<div class="rp">'+brl(pr)+'</div><div class="stepper"><button type="button" onclick="cartStepRes(this,-1)" aria-label="Diminuir">−</button><input type="text" inputmode="numeric" value="1" aria-label="Quantidade" onfocus="this.select()"><button type="button" onclick="cartStepRes(this,1)" aria-label="Aumentar">+</button></div><button type="button" class="addb" onclick="cartAddRes(this)">+ Adicionar</button>'
              :'<div class="rp" style="font-size:12px;color:#217a4b">Sob consulta</div><button type="button" class="addb q" onclick="cartAddRes(this)">+ Orçamento</button>')+'</div>';
      }).join('');
  });
}
function cartStepRes(btn,d){var inp=btn.parentElement.querySelector('input');var v=Math.max(1,(parseInt(inp.value)||1)+d);inp.value=v;}
function cartAddRes(btn){
  var row=btn.closest('.rr');var c=row.getAttribute('data-c');var inp=row.querySelector('input');var q=Math.max(1,parseInt(inp?inp.value:1)||1);
  addCodigo(c,q);
  try{sullabEvent&&sullabEvent('cart_search_add',{c:c,q:q});}catch(e){}
  var ex=CART.find(function(x){return x.c===c;});
  var tag=row.querySelector('.incart');if(!tag){tag=document.createElement('span');tag.className='incart';row.querySelector('.rn').appendChild(tag);}
  tag.textContent='✓ no carrinho: '+(ex?ex.qty:q);
  if(inp)inp.value=1;
  btn.textContent='✓ Adicionado';var bg=btn.style.background;btn.style.background='#14653b';setTimeout(function(){btn.textContent=(btn.classList.contains('q')?'+ Orçamento':'+ Adicionar');btn.style.background=bg;},1100);
}
function cartVerTodos(){var q=document.getElementById('cartSearch').value.trim();fecharCarrinho();var si=document.getElementById('searchInput');if(si){si.value=q;}fazerBusca();}

function _cpLinha(x){var p=precoItem(x);if(!p)return '<div class="cp" style="font-size:12.5px;color:#217a4b">Preço sob consulta</div>';var q=(x.kq&&x.kd)?Math.min(x.kq,x.qty):0;var tot=Math.round(p*x.qty*100)/100;return '<div class="cp">'+brl(tot)+'<small>'+(q?('<span style="color:#14653b;font-weight:800">Kit −'+Math.round(x.kd*100)+'%</span> em '+q+' un'):(x.qty+' × '+brl(p)))+'</small></div>';}
var _gTimer=null,_gKey='',_gRes=null;
function _nomeCat(c){for(var i=0;i<CATALOG.length;i++){if(CATALOG[i].c===c)return CATALOG[i].n;}return c;}
function addCodigo(c,q){var p=null;for(var i=0;i<CATALOG.length;i++){if(CATALOG[i].c===c){p=CATALOG[i];break;}}if(!p)return;var ex=CART.find(function(x){return x.c===c;});if(ex)ex.qty+=q;else CART.push({c:p.c,n:p.n,m:p.m,img:p.img,pub:p.pub,cnpj:p.cnpj,qty:q});salvarCart();atualizarCart();}
function _gratisHtml(d){
  var g=d&&d.gratis,o=d&&d.opcoes&&d.opcoes[0];
  if(!o&&!(g&&(g.ativo||g.falta)))return '';
  var frp=o&&!o.gratis?o.preco:(o&&o.economia?o.economia:0);
  var pz=o&&o.prazo?(' · '+o.prazo+' dias úteis'):'';
  if(g&&g.ativo)return '<div style="font-weight:800;color:var(--green-d);font-size:13.5px">✅ Frete GRÁTIS neste pedido!</div>'+(o&&o.economia?'<div style="margin-top:2px">Você economizou <b>'+brl(o.economia)+'</b> de frete'+pz+'.</div>':'<div style="margin-top:2px">Opção econômica'+pz+'. Outras transportadoras continuam disponíveis.</div>');
  if(g&&g.sobConsulta)return (o?'<div>🚚 Frete a partir de <b>'+brl(o.preco)+'</b>'+pz+'.</div>':'')+'<div style="font-size:11.5px">Frete grátis não se aplica a um ou mais itens deste pedido.</div>';
  var h='';
  if(o)h+='<div>🚚 Frete: <b>'+brl(o.preco)+'</b> · '+(o.retirada?'por conta do cliente (retirada na SULLAB)':String(o.nome||'').slice(0,28))+pz+'</div>';
  if(g&&g.falta){
    var V=0;try{V=totalCart();}catch(e){}
    var pct=V>0?Math.max(6,Math.min(96,Math.round(V/(V+g.falta)*100))):6;
    var s0=g.sugestoes&&g.sugestoes[0];  
    h+='<div class="gnudge"><div style="font-weight:800;color:var(--green-d)">'+(s0?'🎁 Ative o <b>FRETE GRÁTIS</b>: acrescente <b>'+s0.q+' × '+String(_nomeCat(s0.c)).split(' · caixa')[0].slice(0,60)+'</b> ('+brl(s0.valor)+')'+(frp?' e economize <b>'+brl(frp)+'</b> no frete!':'!')+(s0.c===g.sugestoes[0].c?' <button onclick="addCodigo(\''+s0.c+'\','+s0.q+')" style="margin-left:6px;background:var(--green-d);color:#fff;border:0;border-radius:8px;padding:4px 10px;font-weight:800;cursor:pointer">+ Acrescentar</button>':''):'🎁 Adicione mais <b>'+brl(g.falta)+'</b> em produtos e ganhe <b>FRETE GRÁTIS</b>'+(frp?' — você economiza <b>'+brl(frp)+'</b>!':'!'))+'</div><div class="gbar"><i style="width:'+pct+'%"></i></div></div>';
    if(g.sugestoes&&g.sugestoes.length){h+=(g.sugestoes.length>1?'<div style="font-size:11.5px;margin-top:5px;font-weight:700">Ou ative o frete grátis com outro item'+(frp?' e economize '+brl(frp)+' no frete':'')+':</div>':'')+g.sugestoes.slice(1).map(function(s){return '<div class="gadd"><span>+ '+s.q+' × '+String(_nomeCat(s.c)).slice(0,44)+' <b>('+brl(s.valor)+')</b><br><em style="font-style:normal;font-size:11px;color:var(--green-d)">ativa o frete grátis'+(frp?' · economize '+brl(frp)+' no frete':'')+'</em></span><button onclick="addCodigo(\''+s.c+'\','+s.q+')">+ Adicionar</button></div>';}).join('');}
  }
  return h;
}
function gboxRender(){
  var b=document.getElementById('gbox');if(!b)return;
  var cep=soDig((fichaSalva().cep)||'');
  var base='<div class="gin"><input id="cartCep" inputmode="numeric" maxlength="9" placeholder="Seu CEP — veja o frete" value="'+(cep.length===8?cep.slice(0,5)+'-'+cep.slice(5):'')+'" onkeydown="if(event.key===\'Enter\')cotarFreteCarrinho()"><button onclick="cotarFreteCarrinho()">Calcular</button></div>';
  if(cep.length!==8){b.className='gbox';b.innerHTML=base+'<div>🚚 Muitos pedidos ganham <b>frete grátis</b>. Informe o CEP e veja o seu.</div>';return;}
  b.className='gbox';b.innerHTML=base+'<div id="gmsg">Calculando frete…</div>';
  clearTimeout(_gTimer);_gTimer=setTimeout(function(){cotarFreteCarrinho(true);},350);
}
function cotarFreteCarrinho(auto){
  var el=document.getElementById('cartCep');var cep=soDig(el?el.value:(fichaSalva().cep||''));
  var msg=document.getElementById('gmsg');var b=document.getElementById('gbox');
  if(cep.length!==8){if(b)b.querySelector('div:last-child').innerHTML='Informe um CEP com 8 números.';return;}
  try{var f=fichaSalva();f.cep=cep;localStorage.setItem('sullab_ficha',JSON.stringify(f));}catch(e){}try{document.getElementById('utilCep').innerHTML='📍 Entregar no CEP <b>'+cep.slice(0,5)+'-'+cep.slice(5)+'</b> · alterar';document.getElementById('fgx').classList.add('ok');}catch(e){}
  if(!msg){var d0=document.createElement('div');d0.id='gmsg';b.appendChild(d0);msg=d0;}
  var itens=CART.filter(function(x){return precoItem(x)>0;}).map(function(x){return {c:String(x.c),q:x.qty,v:precoItem(x)};});
  if(!itens.length||itens.length!==CART.length){msg.innerHTML='🚚 Frete confirmado no atendimento (item sob consulta).';return;}
  var key=cep+'|'+itens.map(function(i){return i.c+'x'+i.q;}).join(',');
  if(key===_gKey&&_gRes){msg.innerHTML=_gratisHtml(_gRes);b.className='gbox'+((_gRes.gratis&&_gRes.gratis.ativo)?' ok':'');return;}
  msg.innerHTML='Calculando frete…';
  fetch(FRETE2,{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({cep:cep,itens:itens})}).then(function(r){return r.json();}).then(function(d){
    var m2=document.getElementById('gmsg'),b2=document.getElementById('gbox');if(!m2)return;
    if((!d||!d.opcoes||!d.opcoes.length)&&!(d&&d.gratis&&(d.gratis.ativo||d.gratis.falta))){m2.innerHTML=(d&&(d.consulta||d.bloqueado))?'🚚 Frete será confirmado no atendimento.':(window.refrigSemMsg&&window.cartRefrigerado&&cartRefrigerado()&&window._refrigSemOpcao)?refrigSemMsg():'⚠️ <b>Frete não encontrado para o CEP '+cep.replace(/^(\d{5})(\d{3})$/,'$1-$2')+'.</b> Confira se o CEP está correto ou fale com a gente no WhatsApp.';return;}
    _gKey=key;_gRes=d;m2.innerHTML=_gratisHtml(d);if(b2)b2.className='gbox'+((d.gratis&&d.gratis.ativo)?' ok':'');
  }).catch(function(){var m3=document.getElementById('gmsg');if(m3)m3.innerHTML='Não foi possível calcular o frete agora — confirmamos no atendimento.';});
}
function ckModo(){var online=(DOCT==='cnpj');var b=document.getElementById('ckPayBtn'),p=document.getElementById('pays'),l=document.getElementById('paysLb'),sb=document.getElementById('ckSub'),sf=document.getElementById('ckSafe'),tt=document.getElementById('ckTit');
  if(b){b.textContent=online?'Pagar agora →':'Enviar pedido para orçamento →';b.setAttribute('onclick',online?'pagarMP()':'salvarFichaCheckout();fecharCheckout();enviarOrcamento()');}
  if(p)p.style.display=online?'grid':'none';if(l)l.style.display=online?'block':'none';
  if(tt)tt.textContent=online?'Finalizar pedido':'Enviar pedido para orçamento';
  if(sb)sb.textContent=online?'Pagamento seguro pelo Mercado Pago · NF-e em todo pedido':'Para CPF o pedido segue por orçamento: enviamos preço final e frete pelo WhatsApp';
  if(sf)sf.innerHTML=online?'🔒 Pagamento processado pelo Mercado Pago. Seus dados não ficam no nosso site.':'🔒 Sem pagamento online: retornamos com preço final, frete e NF-e pelo WhatsApp.';
}
function abrirCarrinho(){try{var _pm=document.getElementById('pmodal');if(_pm&&_pm.classList.contains('on'))fecharProd();}catch(e){}atualizarCart();document.getElementById('ov').classList.add('on');document.getElementById('drawer').classList.add('on');}
function abrirCarrinhoBusca(){abrirCarrinho();setTimeout(function(){var e=document.getElementById('cartSearch');if(e)e.focus();},260);}
function fecharCarrinho(){document.getElementById('ov').classList.remove('on');document.getElementById('drawer').classList.remove('on');}

function abrirWhats(msg){window.open('https://wa.me/'+WHATS+'?text='+encodeURIComponent(msg),'_blank');}
function _ehMobile(){return /Android|iPhone|iPad|iPod|Mobile/i.test(navigator.userAgent||'')||window.innerWidth<700;}
function enviarOrcamento(){
  abrirContatoWA();
}
function abrirListaOrcamento(){try{fecharCarrinho();}catch(e){} abrirContatoWA();}
function _copiaFicha(f,extra){var o={},k;for(k in f)o[k]=f[k];for(k in (extra||{}))o[k]=extra[k];return o;}
function _linhasCart(){return CART.map(function(x){return '• '+x.qty+'x '+x.n+' (cód '+x.c+')';});}
function _fichaCompleta(f){
  var l=[];
  l.push('— Dados do cliente —');
  l.push('Nome/Empresa: '+(f.nome||''));
  l.push((f.doct==='cpf'?'CPF: ':'CNPJ: ')+(f.doc||''));
  l.push('WhatsApp: '+(f.tel||''));
  l.push('E-mail: '+(f.email||''));
  var rua=[f.log,f.num].filter(Boolean).join(', ')+(f.compl?(' — '+f.compl):'');
  l.push('— Endereço de entrega —');
  l.push(rua);
  l.push([f.bairro,[f.cidade,f.uf].filter(Boolean).join('/')].filter(Boolean).join(' · ')+(f.cep?(' · CEP '+f.cep):''));
  return l.join('\n');
}
function _itensTexto(lista){
  var corpo=CART.map(function(x){var p=precoItem(x);return '• '+x.qty+'x '+x.n+' (cód '+x.c+')'+(p?(' — '+brl(p)+' un = '+brl(p*x.qty)):' — sob consulta');}).join('\n');
  var sub=totalCart();
  if(CART.length&&sub>0)corpo+='\n\nSubtotal (preço do site): '+brl(sub);
  if(lista)corpo+=(corpo?'\n\n':'')+'Lista do cliente:\n'+lista.slice(0,1500);
  return corpo;
}
function _freteEstimado(cep,cb){
  if(!CART.length){cb(null);return;}
  var fim=false,t=setTimeout(function(){if(!fim){fim=true;cb(null);}},4500);
  try{
    var itens=CART.map(function(x){return {c:String(x.c),q:x.qty,v:precoItem(x)};});
    fetch(FRETE2,{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({cep:soDig(cep),itens:itens})}).then(function(r){return r.json();}).then(function(d){
      if(fim)return;fim=true;clearTimeout(t);var ok=(d&&d.opcoes)||[];
      if(!ok.length){cb(null);return;}
      var o=ok[0];cb({nome:String(o.nome||'Transportadora'),preco:o.preco,prazo:o.prazo||0,gratis:!!o.gratis,peso:d.peso,pacotes:d.pacotes});
    }).catch(function(){if(!fim){fim=true;clearTimeout(t);cb(null);}});
  }catch(e){if(!fim){fim=true;clearTimeout(t);cb(null);}}
}
function _freteTexto(fr){
  if(!fr)return 'Frete: a calcular por nossa equipe (CEP informado).';
  return 'Frete estimado no site: '+(fr.gratis?'GRÁTIS':brl(fr.preco))+' ('+fr.nome+(fr.prazo?(', '+fr.prazo+' dias úteis'):'')+')'+(fr.peso?(' · peso ~'+fr.peso+' kg'):'');
}
function _enviarOrcamentoCom(f,arquivo){
  var lista=((f&&f.lista)||'').trim();
  if(!CART.length&&!lista&&!arquivo)return;
  var _pid='SLB-'+Date.now();window._pedAtual=_pid;
  var btn=document.getElementById('waqBtn');
  _freteEstimado(f.cep,function(fr){
    if(fr){freteSelLoja=fr.gratis?0:(parseFloat(fr.preco)||0);freteLabelLoja=fr.nome;freteSelPrazo=fr.prazo||0;freteMeta={pesoKg:fr.peso,pacotes:fr.pacotes};}
    dispararPedido('pedido_wa','whatsapp',f,_pid);
    var msg='Olá! Quero um orçamento na SULLAB (pedido '+_pid+').\n\n'+
      (arquivo?'Vou enviar minha lista (foto, PDF, Excel ou áudio) logo em seguida.\n'+(CART.length?'\nJá escolhi no site:\n'+_itensTexto('')+'\n':'')
              :'— Itens —\n'+_itensTexto(lista)+'\n')+
      '\n'+_freteTexto(fr)+'\n\n'+_fichaCompleta(f)+'\n\nPodem me passar preço final, disponibilidade, frete e NF-e?';
    fecharContatoWA();
    abrirWhats(msg);
  });
}
function waArquivoWhats(){
  var f=_waLer(true);if(!f)return;
  _enviarOrcamentoCom(_copiaFicha(f,{lista:'[cliente vai enviar foto/PDF/Excel/áudio pelo WhatsApp]',arquivoWA:1}),true);
}
var WA_DOCT='cnpj';
function waSetDoc(d){WA_DOCT=d;var c=document.getElementById('waTabCnpj'),p=document.getElementById('waTabCpf');if(c)c.classList.toggle('on',d==='cnpj');if(p)p.classList.toggle('on',d==='cpf');
  var t=function(id,v){var e=document.getElementById(id);if(e)e.textContent=v;};
  t('waDocLb',d==='cnpj'?'CNPJ *':'CPF *');t('waNomeLb',d==='cnpj'?'Nome fantasia / Empresa *':'Nome completo *');
  var i=document.getElementById('waDoc');if(i)i.placeholder=d==='cnpj'?'00.000.000/0000-00':'000.000.000-00';}
function waCepAuto(){var c=soDig(val('waCep'));if(c.length!==8)return;
  fetch('https://brasilapi.com.br/api/cep/v1/'+c).then(function(r){return r.json();}).then(function(d){
    if(!d||!d.street&&!d.city)return;var set=function(id,v){var e=document.getElementById(id);if(e&&v&&!e.value.trim())e.value=v;};
    set('waLog',d.street);set('waBairro',d.neighborhood);
    var ci=document.getElementById('waCidade');if(ci&&d.city)ci.value=d.city;var uf=document.getElementById('waUf');if(uf&&d.state)uf.value=d.state;
    var n=document.getElementById('waNum');if(n&&!n.value&&!_ehMobile())n.focus();
  }).catch(function(){});}
function waDocAuto(){var c=soDig(val('waDoc'));if(c.length===14&&WA_DOCT!=='cnpj')waSetDoc('cnpj');if(c.length!==14)return;
  fetch('https://brasilapi.com.br/api/cnpj/v1/'+c).then(function(r){return r.json();}).then(function(d){
    if(!d||!d.razao_social)return;var set=function(id,v){var e=document.getElementById(id);if(e&&v&&!e.value.trim())e.value=v;};
    set('waNome',d.nome_fantasia||d.razao_social);
    if(d.cep&&!val('waCep')){document.getElementById('waCep').value=String(d.cep).replace(/^(\d{5})(\d{3})$/,'$1-$2');
      set('waLog',[d.descricao_tipo_de_logradouro,d.logradouro].filter(Boolean).join(' ').toLowerCase().replace(/(^|\s)\S/g,function(m){return m.toUpperCase();}));
      set('waNum',d.numero);set('waCompl',d.complemento);set('waBairro',d.bairro);set('waCidade',d.municipio);set('waUf',d.uf);}
  }).catch(function(){});}
function _waLer(arquivo){
  var nome=val('waNome'),tel=val('waTel'),cep=val('waCep'),doc=val('waDoc'),email=val('waEmail'),lista=val('waLista');
  var log=val('waLog'),num=val('waNum'),compl=val('waCompl'),bairro=val('waBairro'),cidade=val('waCidade'),uf=val('waUf').toUpperCase();
  var nd=soDig(doc).length;
  if(WA_DOCT==='cnpj'&&!/^[0-9A-Z]{12}[0-9]{2}$/.test(docLimpo(doc)))return waqErro('Informe o CNPJ com 14 caracteres (números, ou letras e números no CNPJ novo) — ou troque para CPF.'),null;
  if(WA_DOCT==='cpf'&&nd!==11)return waqErro('Informe o CPF com 11 números (ou troque para CNPJ).'),null;
  if(!nome)return waqErro(WA_DOCT==='cnpj'?'Informe o nome da empresa.':'Informe seu nome completo.'),null;
  if(soDig(tel).length<10)return waqErro('Informe um WhatsApp com DDD — ex.: (24) 90000-0000.'),null;
  if(!/.+@.+\..+/.test(email))return waqErro('Informe um e-mail válido: é com ele que você acompanha o pedido.'),null;
  if(soDig(cep).length!==8)return waqErro('Informe o CEP com 8 números, para calcular o frete.'),null;
  if(!log||!num)return waqErro('Informe a rua e o número do endereço de entrega.'),null;
  if(!bairro||!cidade||uf.length!==2)return waqErro('Complete bairro, cidade e UF do endereço.'),null;
  if(!arquivo&&!CART.length&&lista.length<3)return waqErro('Digite pelo menos um item — ou toque em "mandar foto, PDF, Excel ou áudio" logo abaixo.'),null;
  var f=fichaSalva();f.nome=nome;f.tel=tel;f.cep=cep;f.doc=doc;f.doct=WA_DOCT;f.email=email;f.log=log;f.num=num;f.compl=compl;f.bairro=bairro;f.cidade=cidade;f.uf=uf;
  try{localStorage.setItem('sullab_ficha',JSON.stringify(f));}catch(e){}
  f.lista=lista;return f;
}
function abrirContatoWA(motivo,textoLista){
  var f=fichaSalva();
  var s=function(id,v){var e=document.getElementById(id);if(e)e.value=v||'';};
  s('waNome',f.nome);s('waTel',f.tel);s('waCep',f.cep);s('waDoc',f.doc);s('waEmail',f.email);
  s('waLog',f.log);s('waNum',f.num);s('waCompl',f.compl);s('waBairro',f.bairro);s('waCidade',f.cidade);s('waUf',f.uf);
  s('waLista',textoLista||'');
  waSetDoc(f.doct==='cpf'?'cpf':'cnpj');
  var vazio=!CART.length;
  var t=function(id,v){var e=document.getElementById(id);if(e)e.textContent=v;};
  t('waqTit',motivo==='duvida'?'Falar com a SULLAB':(vazio?'Pedir orçamento':'Seu orçamento está quase pronto'));
  t('waListaLb',vazio?'Itens do orçamento * (digite ou cole a lista)':'Mais itens? Digite ou cole (opcional)');
  var cb=document.getElementById('waqCart');
  if(cb){if(!vazio){var n=CART.reduce(function(a,x){return a+x.qty;},0);cb.style.display='block';cb.innerHTML='🛒 <b>'+n+(n===1?' item':' itens')+'</b> do carrinho vão junto no orçamento'+(totalCart()>0?(' · subtotal <b>'+brl(totalCart())+'</b>'):'')+'.';}else{cb.style.display='none';}}
  var err=document.getElementById('waqErr');if(err)err.style.display='none';
  window.__mdT=document.getElementById('waq');
  document.getElementById('waq').classList.add('on');
  setTimeout(function(){var ids=['waDoc','waNome','waTel','waEmail','waCep','waLog','waNum','waBairro','waCidade','waUf'],k;for(k=0;k<ids.length;k++){var e=document.getElementById(ids[k]);if(e&&!e.value.trim()){if(!_ehMobile())e.focus();return;}}if(!_ehMobile())document.getElementById('waLista').focus();},80);
}
function fecharContatoWA(){document.getElementById('waq').classList.remove('on');}
function waqErro(m){var e=document.getElementById('waqErr');if(!e)return;e.textContent=m;e.style.display='block';e.scrollIntoView&&e.scrollIntoView({block:'nearest'});}
function confirmarContatoWA(){var f=_waLer(false);if(!f)return;_enviarOrcamentoCom(f,false);}
function salvarFichaCheckout(){try{var f=coletarFicha(),cur=fichaSalva(),k;for(k in f){if(f[k])cur[k]=f[k];}localStorage.setItem('sullab_ficha',JSON.stringify(cur));}catch(e){}}
document.addEventListener('change',function(e){try{if(e.target&&e.target.closest&&e.target.closest('#cko'))salvarFichaCheckout();}catch(err){}},true);
var ROBO_URL='https://whatsapp-sullab-production.up.railway.app';
function roboPost(rota,dados){try{var b=JSON.stringify(dados);if(navigator.sendBeacon&&navigator.sendBeacon(ROBO_URL+rota,new Blob([b],{type:'text/plain'})))return;fetch(ROBO_URL+rota,{method:'POST',mode:'no-cors',keepalive:true,headers:{'Content-Type':'text/plain'},body:b});}catch(e){}}
function duvidaCheckout(onde){
  var l=CART.length?(location.origin+'/?carrinho='+CART.map(function(x){return encodeURIComponent(x.c)+':'+x.qty;}).join(',')):location.origin;
  var msg='Olá! Estou finalizando um pedido no site da SULLAB e tenho uma dúvida antes de pagar.\nMeu carrinho: '+l;
  try{if(typeof gtag==='function')gtag('event','whatsapp_click',{origem:onde||'checkout',page:location.pathname,value:totalCart()||0,currency:'BRL'});}catch(e){}
  try{if(window.clarity)clarity('event','duvida_checkout');}catch(e){}
  try{var f=fichaSalva();sullabEvent('checkout_duvida',{tel:f.tel||'',cliente:f.nome||'',total:totalCart(),itens:CART.map(function(x){return {cod:x.c,nome:x.n,q:x.qty};}),link:l,onde:onde||''});}catch(e){}
  try{sessionStorage.setItem('abSent','1');}catch(e){}
  window.open('https://wa.me/5524988383100?text='+encodeURIComponent(msg),'_blank','noopener');
}

var BOLETO_MIN=400;
var TUBO_MIN=400;
function temTubo(){return CART.some(function(x){return (window.PIX3&&window.PIX3[x.c])||(window.TR_TOP&&window.TR_TOP[x.c]);});}  
var PED_MIN_GERAL=100,PED_MIN_REFRIG=150;
function pedMin(){return temTubo()?TUBO_MIN:((window.cartRefrigerado&&window.cartRefrigerado())?PED_MIN_REFRIG:PED_MIN_GERAL);}
function msgMin(){return temTubo()?'Pedido mínimo de R$ 400,00 somando tubos, agulhas Vacuette e testes rápidos — pode misturar itens dessas categorias no mesmo pedido.':((window.cartRefrigerado&&window.cartRefrigerado())?'Pedido mínimo de R$ 150,00 para pedidos com produto refrigerado — vale o total do pedido, não o item.':'Pedido mínimo no site: R$ 100,00 no total do pedido.');}
function faltaTubo(){return Math.max(0,Math.round((pedMin()-totalCart())*100)/100);}
/* 31/10/2026: barra única de progresso no carrinho — primeiro o pedido mínimo, depois o frete grátis (quando o CEP já foi cotado) */
function _gratisAtual(){try{if(!_gRes||!_gKey)return null;var cep=soDig((fichaSalva().cep)||''),its=CART.filter(function(x){return precoItem(x)>0;});var k=cep+'|'+its.map(function(x){return String(x.c)+'x'+x.qty;}).join(',');return k===_gKey?(_gRes.gratis||null):null;}catch(e){return null;}}
function progHtml(){var sub=totalCart();if(!(sub>0))return '';var min=pedMin(),f=faltaTubo(),pct,lab,cls='';
  if(f>0){pct=Math.max(4,Math.min(100,Math.round(sub/min*100)));lab='📦 <b>Faltam '+brl(f)+'</b> para o pedido mínimo de '+brl(min)+'<small>'+msgMin()+'</small>';cls=' falta';}
  else{var g=_gratisAtual();
    if(g&&g.ativo){pct=100;lab='✅ Pedido mínimo atingido · <b>frete grátis</b> neste pedido';cls=' ok';}
    else if(g&&g.falta>0){pct=Math.max(4,Math.min(98,Math.round(sub/(sub+g.falta)*100)));lab='✓ Pedido mínimo atingido · faltam <b>'+brl(g.falta)+'</b> para o <b>frete grátis</b>';}
    else{pct=100;lab='✓ Pedido mínimo atingido'+((g&&g.sobConsulta)?'':'<small>Informe o CEP abaixo para ver o frete e o frete grátis.</small>');cls=' ok';}}
  return '<div class="pgL'+cls+'">'+lab+'</div><div class="pgB'+cls+'" role="progressbar" aria-label="Progresso do pedido" aria-valuemin="0" aria-valuemax="100" aria-valuenow="'+pct+'"><i style="width:'+pct+'%"></i></div>';}
function progRefresh(){var e=document.getElementById('progMin');if(e)e.innerHTML=progHtml();}
function btnFinalizarHtml(semPreco){
  if(semPreco)return '<a class="wbtn" role="button" aria-disabled="true" data-motivo="Há item com preço sob consulta no carrinho: peça o orçamento pelo WhatsApp (botão abaixo) ou remova esse item para pagar no site." style="background:var(--green-d);opacity:.55">🛒 Finalizar compra</a>';
  var f=faltaTubo();
  if(f>0)return '<button type="button" class="wbtn wmin" onclick="minimoBloqueado(\'carrinho\')">Faltam '+brl(f)+' para o pedido mínimo<small>Toque para ver sugestões e completar o pedido</small></button>';
  return '<a class="wbtn" role="button" style="background:var(--green-d)" onclick="abrirCheckout()">🛒 Finalizar compra</a>';}
function slAviso(msg){try{var d=document.getElementById('slToast');if(!d){d=document.createElement('div');d.id='slToast';d.setAttribute('role','status');d.setAttribute('aria-live','polite');document.body.appendChild(d);}d.textContent=msg;d.className='on';clearTimeout(slAviso._t);slAviso._t=setTimeout(function(){d.className='';},4200);}catch(e){}}
function minimoBloqueado(origem){
  var f=faltaTubo(),min=pedMin();
  try{if(typeof gtag==='function')gtag('event','minimo_bloqueado',{origem:origem||'',currency:'BRL',value:Math.round(totalCart()*100)/100,falta:f,minimo:min});}catch(e){}
  try{if(window.clarity)clarity('event','minimo_bloqueado');}catch(e){}
  var d=document.getElementById('drawer');if(!d||!d.classList.contains('on'))abrirCarrinho();
  if(f>0)slAviso('Faltam '+brl(f)+' para o pedido mínimo de '+brl(min)+'. Acrescente itens abaixo para finalizar.');
  setTimeout(function(){var cr=document.getElementById('crel'),alvo=(cr&&cr.querySelector('.relbox'))||document.getElementById('cartSearch');if(!alvo)return;try{alvo.scrollIntoView({behavior:'smooth',block:'center'});}catch(e){}alvo.classList.add('slPulse');setTimeout(function(){alvo.classList.remove('slPulse');},1800);if(alvo.id==='cartSearch'&&!_ehMobileSafe())alvo.focus();},260);}
function _ehMobileSafe(){try{return matchMedia('(max-width:700px)').matches;}catch(e){return false;}}
function totalPedidoBruto(){return totalCart()+(freteSelLoja||0);}
function boletoOk(){return totalPedidoBruto()>=BOLETO_MIN;}
function boletoFaturado(){
  if(!CART.length)return;
  if(totalPedidoBruto()<BOLETO_MIN)return ckErro('Boleto faturado disponível para pedidos a partir de R$ 400,00.');
  var f={};try{f=coletarFicha();}catch(e){}
  var l=location.origin+'/?carrinho='+CART.map(function(x){return encodeURIComponent(x.c)+':'+x.qty;}).join(',');
  var msg='Olá! Quero fechar este pedido no site da SULLAB com *boleto faturado* (28/45 dias) para empresa.'+(f.nome?('\nEmpresa: '+f.nome):'')+(f.doc?('\nCNPJ: '+f.doc):'')+(f.cep?('\nCEP de entrega: '+f.cep):'')+'\nMeu carrinho: '+l;
  try{sullabEvent('checkout_faturado',{tel:f.tel||'',cliente:f.nome||'',total:totalCart(),link:l});}catch(e){}
  try{sessionStorage.setItem('abSent','1');}catch(e){}
  window.open('https://wa.me/5524988383100?text='+encodeURIComponent(msg),'_blank','noopener');
}
var MP_WORKER='https://sullab-mp.comercial-0a2.workers.dev/';
var SHEET_ENDPOINT='https://script.google.com/macros/s/AKfycbyPKW71fCDUcjZiID5AicTox1a_inSgYqd-4fXHxzsV9ynX1xrIx5mwf4YIGx5lDpL_Lw/exec';
var SULLAB_EVT_TOKEN='sl-2d26d03b37c9301cd7f3ac49';
function sullabEvent(type,extra){try{var b={type:type},k;for(k in (extra||{}))b[k]=extra[k];b.t=SULLAB_EVT_TOKEN;fetch(SHEET_ENDPOINT,{method:'POST',mode:'no-cors',headers:{'Content-Type':'text/plain;charset=utf-8'},body:JSON.stringify(b)});}catch(e){}}
function _itensPedido(){return CART.map(function(x){return {cod:x.c,nome:x.n,q:x.qty,un:precoItem(x)};});}
function dispararPedido(type,pgto,ficha,pedido){
  if(!CART.length&&!(ficha&&ficha.lista))return;
  var f=ficha||fichaSalva();
  var ped=pedido||('SLB-'+Date.now());
  var end={end:f.log||'',num:f.num||'',comp:f.compl||'',bairro:f.bairro||'',cidade:f.cidade||'',uf:f.uf||'',cep:f.cep||''};
  var its=_itensPedido();
  try{ if(typeof gtag==='function'){ gtag('event', (type==='pedido_wa'?'gerar_orcamento':(type==='pedido_mp'?'iniciar_pagamento':'pedido')), {value: (totalCart()||0), currency:'BRL', transaction_id: ped, items_count: its.length}); } }catch(e){}
  sullabEvent(type,{pedido:ped,total:totalCart(),qtd:CART.reduce(function(s,x){return s+x.qty;},0),itens:its,pgto:pgto||'',cliente:f.nome||'',doc:f.doc||'',docTipo:f.doct||'',tel:f.tel||'',email:f.email||'',endereco:end,frete:freteSelLoja||0,freteNome:freteLabelLoja||'',fretePrazo:freteSelPrazo||0,freteServico:freteSelId||'',fretePesoKg:(freteMeta&&freteMeta.pesoKg)||0,fretePacotes:(freteMeta&&freteMeta.pacotes)||0,lista:String(f.lista||'').slice(0,3000),arquivoWA:f.arquivoWA?1:0,disp:(typeof _ehMobile==='function'&&_ehMobile())?'celular':'computador'});
  try{registrarMeuPedido({pedido:ped,ts:Date.now(),total:totalCart(),qtd:CART.reduce(function(s,x){return s+x.qty;},0),itens:its.map(function(x){return {q:x.q,nome:x.nome,cod:x.cod};}),canal:(type==='pedido_mp'?'online':'whatsapp'),status:'recebido'});}catch(e){}
}
var DOCT='cnpj', PG='pix';
var ORIGEM_CEP='27323450';
var CUPONS={},cupomPct=0,cupomCod='',freteSelLoja=0,freteLabelLoja='';
function val(id){return (document.getElementById(id).value||'').trim();}
function soDig(s){return (s||'').replace(/\D/g,'');}
function setDoc(d){DOCT=d;document.querySelectorAll('#docTab button').forEach(function(b){b.classList.toggle('on',b.getAttribute('data-d')===d);});document.getElementById('lbDoc').textContent=d==='cnpj'?'CNPJ':'CPF';document.getElementById('lbNome').textContent=d==='cnpj'?'Razão social':'Nome completo';
  /* 31/10/2026: CNPJ abre o teclado numérico; "CNPJ com letras?" troca para o teclado completo (CNPJ alfanumérico) */
  var dc=document.getElementById('ckDoc');dc.placeholder=d==='cnpj'?'00.000.000/0000-00':'000.000.000-00';dc.maxLength=18;dc.setAttribute('inputmode',(d==='cnpj'&&(window._docLetras||docAlfa(dc.value)))?'text':'numeric');
  var nm=document.getElementById('ckNome');if(nm){nm.setAttribute('autocomplete',d==='cnpj'?'organization':'name');nm.placeholder=d==='cnpj'?'Como está no cartão CNPJ':'Seu nome completo';}
  var dl=document.getElementById('ckDocLetras');if(dl)dl.hidden=(d!=='cnpj'||dc.getAttribute('inputmode')==='text');
  try{ckModo();}catch(e){}}
function docLetras(){window._docLetras=1;var dc=document.getElementById('ckDoc');if(!dc)return false;dc.setAttribute('inputmode','text');dc.blur();setTimeout(function(){try{dc.focus();}catch(e){}},30);var dl=document.getElementById('ckDocLetras');if(dl)dl.hidden=true;return false;}
/* 31/10/2026: CNPJ alfanumérico (Receita Federal, a partir de jul/2026): 12 posições 0-9/A-Z + 2 dígitos verificadores.
   Cálculo oficial: valor de cada posição = código ASCII − 48 (0-9 = 0-9, A = 17 … Z = 42), pesos 5..2/9..2 e 6..2/9..2, módulo 11. */
function docLimpo(s){return String(s||'').toUpperCase().replace(/[^0-9A-Z]/g,'');}
function docAlfa(s){return /[A-Z]/.test(docLimpo(s));}
function cnpjValido(s){var c=docLimpo(s);if(!/^[0-9A-Z]{12}[0-9]{2}$/.test(c)||/^(.)\1{13}$/.test(c))return false;
  var dv=function(n){var w=n===12?[5,4,3,2,9,8,7,6,5,4,3,2]:[6,5,4,3,2,9,8,7,6,5,4,3,2],t=0;for(var i=0;i<n;i++)t+=(c.charCodeAt(i)-48)*w[i];var r=t%11;return r<2?0:11-r;};
  return dv(12)===+c[12]&&dv(13)===+c[13];}
function cpfValido(s){var c=soDig(s);if(c.length!==11||/^(\d)\1{10}$/.test(c))return false;for(var n=9;n<11;n++){var t=0;for(var i=0;i<n;i++)t+=(+c[i])*(n+1-i);if((t*10)%11%10!==+c[n])return false;}return true;}
/* o Worker/Mercado Pago só entendem documento numérico (ele tira tudo que não é dígito): CNPJ com letras vai só para a planilha, não para o MP */
function docParaMP(s){return docAlfa(s)?'':String(s||'');}
function docInput(el){try{if(DOCT==='cnpj'&&/[a-z]/.test(el.value)){var p=el.selectionStart;el.value=el.value.toUpperCase();try{el.setSelectionRange(p,p);}catch(e){}}}catch(e){}if(DOCT==='cnpj')cnpjAuto();}
function setPg(p){if(p==='boleto'&&!boletoOk()){p='pix';var _r=document.querySelector('#pays input[value=pix]');if(_r)_r.checked=true;ckErro('Boleto disponível para pedidos a partir de R$ 400,00.');}PG=p;var _bi=document.getElementById('boletoInfo');if(_bi)_bi.style.display=(p==='boleto')?'block':'none';document.querySelectorAll('#pays .pay1').forEach(function(l){l.classList.toggle('on',l.querySelector('input').value===p);});ckTotais();}
window.PIX3={"450071":1,"450072":1,"454036":1,"454087":1,"454921":1,"454235":1,"456211":1,"454071":1,"454482":1,"456071":1,"455071":1,"454092":1,"455092":1,"456001":1,"454327":1,"454085":1,"454091":1,"454030":1,"456080":1,"450539":1};
function pixPct(c){return (c&&window.PIX3[c])?0.03:0.05;}
/* 31/10/2026: pedido mínimo visível no card, no modal e na página do produto (R$ 400 tubos/agulhas Vacuette e testes rápidos; R$ 150 refrigerados) */
function minItem(c){c=String(c);if((window.PIX3&&window.PIX3[c])||(window.TR_TOP&&window.TR_TOP[c]))return 400;if(window.itemRefrigerado&&window.itemRefrigerado(c))return 150;return 0;}
/* 31/10/2026 (dono): o selo por item confundia (parecia mínimo DAQUELE item). O mínimo é por categoria e vale o total do pedido: fica só no carrinho (msgMin) e na página do produto, com o texto completo. */
function seloMinHtml(c){return '';}
function cardClick(ev,i){try{var t=ev&&ev.target;if(t&&t.closest&&t.closest('.pf,button,input,select,a'))return;}catch(e){}abrirProd(i);}
function fatorPg(c){return PG==='pix'?(1-pixPct(c)):1;}
function _catOf(c){for(var i=0;i<CATALOG.length;i++){if(CATALOG[i].c===c)return CATALOG[i].k;}return '';}
function cartTodosTeste(){return CART.length>0&&CART.every(function(x){return _catOf(x.c)==='tr';});}
function freteInfo(uf,total){uf=(uf||'').toUpperCase();var rjsp=(uf==='RJ'||uf==='SP');var se=['SP','RJ','MG','ES'].indexOf(uf)>=0;
  return{free:false};}
function _freteBtn(){return '<button class="ckwa" style="text-align:left;color:var(--navy-l);font-weight:700;padding:8px 0" onclick="cotarFreteLoja()">📦 Calcular frete pelo CEP →</button><div id="freteOpts"></div>';}
function renderFrete(){var box=document.getElementById('freteBox');if(!box)return;var fi=freteInfo(val('ckUf'),totalCart());
  if(fi.free){freteSelLoja=0;freteLabelLoja='grátis';box.innerHTML='<div style="background:var(--green-soft);color:var(--green-d);font-weight:700;font-size:12.5px;padding:9px 11px;border-radius:9px">'+fi.label+'</div>';ckTotais();return;}
  if(fi.rjsp&&fi.falta>0){box.innerHTML='<div style="background:var(--navy-soft);color:var(--navy);font-size:12px;padding:9px 11px;border-radius:9px">🚚 Faltam <b>'+brl(fi.falta)+'</b> para <b>frete grátis</b> (RJ/SP).</div>'+_freteBtn();return;}
  box.innerHTML=_freteBtn();}
function selFreteLoja(v,nm,pz,id){freteSelLoja=parseFloat(v)||0;if(!(freteSelLoja>0)&&!(freteMeta&&freteMeta.gratis))freteSelLoja=0;freteLabelLoja=nm||'';freteSelPrazo=pz||0;freteSelId=id||'';var ns=document.querySelectorAll('#freteOpts .pay1');for(var i=0;i<ns.length;i++){ns[i].classList.toggle('on',parseFloat(ns[i].querySelector('input').value)===freteSelLoja);}ckTotais();}
var FRETE2='https://api.lojasullabrj.com.br/frete2',freteSelPrazo=0,freteSelId='',freteMeta=null;
var _freteOk=null;
function chaveFrete(){return soDig(val('ckCep'))+'|'+CART.map(function(x){return x.c+':'+x.qty;}).join(',');}
function freteValido(){return !!(_freteOk&&_freteOk.key===chaveFrete()&&(freteSelLoja>0||_freteOk.gratis||freteSelId==='retirada'));}
function zerarFrete(){freteSelLoja=0;freteLabelLoja='';freteSelPrazo=0;freteSelId='';freteMeta=null;_freteOk=null;}
function _freteOpcoes(d,opt,_kq){var ok=(d&&d.opcoes)||[];freteMeta={pesoKg:d.peso,pacotes:d.pacotes,gratis:!!(d.gratis&&d.gratis.ativo)};opt.innerHTML=_gratisHtml(d)+ok.map(function(o,ix){var nm=String(o.nome||'Transportadora').replace(/\x27/g,'');return '<label class="pay1'+(ix===0?' on':'')+'" style="margin-top:6px"><input type="radio" name="frt" value="'+o.preco+'" '+(ix===0?'checked':'')+' onchange="selFreteLoja('+o.preco+',\''+nm+'\','+(o.prazo||0)+',\''+String(o.id||'')+'\')"><span><span class="pn">'+nm+'</span> <span class="pd">'+(o.retirada?'· envie seu motoboy ou transportadora':(o.prazo?('· '+o.prazo+' dias úteis'):''))+'</span></span><span class="ptag" style="color:var(--navy)">'+(o.gratis?'Grátis':(o.retirada?'Por sua conta':brl(o.preco)))+'</span></label>';}).join('');selFreteLoja(ok[0].preco,String(ok[0].nome||'Transportadora').replace(/\x27/g,''),ok[0].prazo||0,String(ok[0].id||''));_freteOk={key:_kq,gratis:!!(d.gratis&&d.gratis.ativo)};}
/* 31/10/2026: abre o checkout com o frete que o cliente já cotou no carrinho (mesmo CEP e mesmos itens), sem zerar e cotar de novo */
function _freteDoCarrinho(){try{
  if(typeof _gRes==='undefined'||!_gRes||!_gKey||!(_gRes.opcoes&&_gRes.opcoes.length))return false;
  var cep=soDig(val('ckCep'));if(cep.length!==8)return false;
  if(!CART.length||CART.some(function(x){return !(precoItem(x)>0);}))return false;
  if(cep+'|'+CART.map(function(x){return String(x.c)+'x'+x.qty;}).join(',')!==_gKey)return false;
  var opt=document.getElementById('freteOpts');if(!opt)return false;
  _freteOpcoes(_gRes,opt,chaveFrete());return true;
}catch(e){return false;}}
function cotarFreteLoja(){if(window._fBusy)return;var cep=soDig(val('ckCep'));var opt=document.getElementById('freteOpts');if(!opt)return;if(cep.length!==8){opt.innerHTML='<div style="font-size:13.5px;color:var(--muted);padding:5px 0">Informe o CEP no campo acima.</div>';return;}opt.innerHTML='<div class="fcalc"><span class="spn"></span>Calculando o frete para o seu CEP…</div>';window._fBusy=1;try{var _fb=document.querySelectorAll('#freteBox .ckwa');for(var _i=0;_i<_fb.length;_i++){_fb[_i].disabled=true;_fb[_i].style.opacity=.55;}}catch(e){}var _fim=function(){window._fBusy=0;try{var _fb=document.querySelectorAll('#freteBox .ckwa');for(var _i=0;_i<_fb.length;_i++){_fb[_i].disabled=false;_fb[_i].style.opacity=1;}}catch(e){}};
  zerarFrete();try{ckTotais();}catch(e){}var _kq=chaveFrete();
  var itens=CART.map(function(x){return {c:String(x.c),q:x.qty,v:precoItem(x)};});
  fetch(FRETE2,{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({cep:cep,itens:itens})}).then(function(r){return r.json();}).then(function(d){_fim();var ok=(d&&d.opcoes)||[];if(!ok.length){freteMeta=null;_ckErroLog(((d&&(d.consulta||d.bloqueado))?'frete sob consulta ':'frete sem opcao ')+cep,'frete');opt.innerHTML=_gratisHtml(d)+'<div style="font-size:13.5px;color:var(--muted);padding:5px 0">'+((d&&(d.consulta||d.bloqueado))?'Frete será confirmado no checkout / WhatsApp.':'<b>Frete não encontrado para este CEP.</b> Confira se o CEP está correto ou fale com a gente no WhatsApp.')+'</div>';return;}if(_kq!==chaveFrete())return;_freteOpcoes(d,opt,_kq);}).catch(function(){_fim();zerarFrete();try{ckTotais();}catch(e){}_ckErroLog('frete falha de rede '+cep,'frete');opt.innerHTML='<div style="font-size:13.5px;color:var(--muted);padding:5px 0">Não foi possível calcular agora — o frete será confirmado pelo WhatsApp.</div>';});}
function aplicarCupom(){var c=(val('ckCupom')||'').toUpperCase().replace(/\s/g,'');var msg=document.getElementById('cupomMsg');if(!c){cupomPct=0;cupomCod='';if(msg)msg.textContent='';ckTotais();return;}if(CUPONS[c]){cupomPct=CUPONS[c];cupomCod=c;if(msg){msg.style.color='var(--green-d)';msg.innerHTML='✓ Cupom '+c+' aplicado — '+Math.round(cupomPct*100)+'% OFF.';}}else{cupomPct=0;cupomCod='';if(msg){msg.style.color='#b3261e';msg.textContent='Cupom inválido.';}}ckTotais();}
function _freteBarCart(){return '';}
function ckTotais(){try{var _ok=boletoOk();var _pb=document.getElementById('pgBoleto');if(_pb){_pb.style.opacity=_ok?'1':'.5';_pb.querySelector('input').disabled=!_ok;}if(!_ok&&PG==='boleto'){PG='pix';var _r=document.querySelector('#pays input[value=pix]');if(_r)_r.checked=true;document.querySelectorAll('#pays .pay1').forEach(function(l){l.classList.toggle('on',l.querySelector('input').value==='pix');});}}catch(e){}var t=CART.reduce(function(s,x){return s+(Math.round(precoItem(x)*fatorPg(x.c)*100)/100)*x.qty;},0)*(1-cupomPct)+(freteSelLoja||0);var n=CART.reduce(function(s,x){return s+x.qty;},0);document.getElementById('ckTot').textContent=brl(t);document.getElementById('ckQt').textContent='('+n+' '+(n===1?'item':'itens')+(PG==='pix'?' · desconto Pix':'')+(cupomPct?(' · −'+Math.round(cupomPct*100)+'%'):'')+(freteSelLoja?(' · frete '+brl(freteSelLoja)):'')+')';}
function abrirCheckout(){try{sullabFirebase();}catch(_e){}if(!CART.length){return;}if(faltaTubo()>0){abrirCarrinho();return;}fecharCarrinho();preencherFicha();ckModo();setPg(PG);cupomPct=0;cupomCod='';zerarFrete();try{window._freteReset&&window._freteReset();}catch(e){}var cc=document.getElementById('ckCupom');if(cc)cc.value='';var cm=document.getElementById('cupomMsg');if(cm)cm.textContent='';renderFrete();_freteDoCarrinho();ckTotais();document.getElementById('ckErr').style.display='none';pixMostrar(false);
  if(_PX&&!_PX.fim&&_PX.chave===chaveFrete()&&Date.now()<_PX.exp){_pxRender();pixMostrar(true);_pxTick();_PX.tick=setInterval(_pxTick,1000);_pxStatus();}
  document.getElementById('cko').classList.add('on');}
function fecharCheckout(){document.getElementById('cko').classList.remove('on');_pxParar();}
function fichaSalva(){try{return JSON.parse(localStorage.getItem('sullab_ficha')||'{}');}catch(e){return {};}}
function preencherFicha(){var f=fichaSalva();var map={ckDoc:'doc',ckNome:'nome',ckEmail:'email',ckTel:'tel',ckCep:'cep',ckNum:'num',ckCompl:'compl',ckLog:'log',ckBairro:'bairro',ckCidade:'cidade',ckUf:'uf'};for(var id in map){if(f[map[id]])document.getElementById(id).value=f[map[id]];}if(f.doct)setDoc(f.doct);}
function coletarFicha(){return {doct:DOCT,doc:val('ckDoc'),nome:val('ckNome'),email:val('ckEmail'),tel:val('ckTel'),cep:val('ckCep'),num:val('ckNum'),compl:val('ckCompl'),log:val('ckLog'),bairro:val('ckBairro'),cidade:val('ckCidade'),uf:val('ckUf')};}
function cepAuto(){var c=soDig(val('ckCep'));if(c.length!==8)return;fetch('https://brasilapi.com.br/api/cep/v1/'+c).then(function(r){return r.json();}).then(function(d){if(d&&d.street){if(!val('ckLog'))document.getElementById('ckLog').value=d.street;if(!val('ckBairro'))document.getElementById('ckBairro').value=d.neighborhood||'';document.getElementById('ckCidade').value=d.city||'';document.getElementById('ckUf').value=d.state||'';}if(!document.querySelector('#freteOpts label'))renderFrete();}).catch(function(){});}
function cnpjAuto(){var c=soDig(val('ckDoc'));if(c.length!==14||docAlfa(val('ckDoc')))return;fetch('https://brasilapi.com.br/api/cnpj/v1/'+c).then(function(r){return r.json();}).then(function(d){if(d&&d.razao_social){if(!val('ckNome'))document.getElementById('ckNome').value=d.razao_social;if(!val('ckCep')&&d.cep){document.getElementById('ckCep').value=String(d.cep);cepAuto();}if(!val('ckLog')&&d.logradouro)document.getElementById('ckLog').value=(d.descricao_tipo_de_logradouro?d.descricao_tipo_de_logradouro+' ':'')+d.logradouro;if(!val('ckNum')&&d.numero)document.getElementById('ckNum').value=String(d.numero);if(!val('ckBairro')&&d.bairro)document.getElementById('ckBairro').value=d.bairro;if(!val('ckCidade')&&d.municipio)document.getElementById('ckCidade').value=d.municipio;if(!val('ckUf')&&d.uf)document.getElementById('ckUf').value=d.uf;}renderFrete();}).catch(function(){});}
/* 31/10/2026: o motivo do erro vai também ao Clarity (tag "checkout_erro" filtrável nas gravações) e ao GA4 com a etapa */
function _ckErroLog(m,etapa){var mot=String(m||'').slice(0,90);try{if(typeof gtag==='function')gtag('event','checkout_erro',{motivo:mot,etapa:etapa||'form'});}catch(x){}
  try{if(window.clarity){clarity('set','checkout_erro',mot);if(etapa)clarity('set','checkout_erro_etapa',String(etapa));clarity('event','checkout_erro');}}catch(x){}}
function ckErro(m){var e=document.getElementById('ckErr');e.textContent=m;e.style.display='block';e.scrollIntoView({block:'nearest'});_ckErroLog(m,'form');}
function ckFoco(id){try{var e=document.getElementById(id);if(e&&!_ehMobile())e.focus();if(e)e.classList.add('ckbad');setTimeout(function(){if(e)e.classList.remove('ckbad');},2500);}catch(x){}}
/* ==== 31/10/2026: Pix transparente — QR na própria página (Worker: POST /pix e GET /pix/status a cada 4 s) ==== */
var _PX=null;
function _pxEv(n,p){try{if(typeof gtag==='function')gtag('event',n,p||{});}catch(e){}try{if(window.clarity)clarity('event',n);}catch(e){}}
function _pxEl(id){return document.getElementById(id);}
function pixMostrar(on){var a=_pxEl('ckForm'),b=_pxEl('ckPix');if(a)a.hidden=!!on;if(b)b.hidden=!on;
  if(on){var e=_pxEl('ckErr');if(e)e.style.display='none';try{_pxEl('cko').querySelector('.ckb').scrollTop=0;}catch(x){}}}
function _pxParar(){if(_PX){clearTimeout(_PX.timer);clearInterval(_PX.tick);_PX.timer=_PX.tick=null;}}
function _pxStat(t,m){var s=_pxEl('pxStat');if(!s)return;s.className='pxstat '+t;
  s.innerHTML=t==='esp'?'<span class="spn"></span><span>Aguardando o pagamento. Após o pagamento a confirmação aparece aqui em segundos.</span>'
    :t==='ok'?'<span class="pxi">✓</span><span><b>Pagamento confirmado!</b> Abrindo o seu pedido…</span>'
    :t==='exp'?'<span class="pxi">⏱</span><span><b>Este Pix expirou.</b> Gere um novo código para pagar. O pedido continua o mesmo.</span>'
    :'<span class="pxi">!</span><span></span>';
  if(t==='erro')s.lastChild.textContent=m||'Não foi possível gerar o Pix agora.';}
function _pxRender(){if(!_PX)return;var q=_pxEl('pxQr');if(q){if(_PX.qrb64){q.src='data:image/png;base64,'+_PX.qrb64;q.hidden=false;}else{q.removeAttribute('src');q.hidden=true;}}
  _pxEl('pxCode').value=_PX.qr;_pxEl('pxTot').textContent=brl(_PX.total);_pxEl('pxPed').textContent=_PX.pedido;
  _pxEl('pxNovo').hidden=true;var cb=_pxEl('pxCopyBtn');cb.textContent='Copiar';cb.disabled=false;_pxEl('pxQrBox').classList.remove('exp');_pxEl('pxExp').hidden=false;_pxStat('esp');}
function pixGerar(corpo,tent){
  var btn=_pxEl(tent>1?'pxNovo':'ckPayBtn'),orig=btn?btn.textContent:'';
  if(btn){btn.disabled=true;btn.textContent='Gerando o Pix…';}
  var b={},k;for(k in corpo)b[k]=corpo[k];if(tent>1)b.tentativa=tent;
  var falha=function(m,motivo){if(btn){btn.disabled=false;btn.textContent=orig;}
    if(tent>1){_pxStat('erro',m);_ckErroLog(motivo+': '+m,'pix_novo');}
    else{if(/e-mail/i.test(m))ckFoco('ckEmail');else if(/CPF|CNPJ/.test(m))ckFoco('ckDoc');ckErro(m);}};
  fetch(MP_WORKER+'pix',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(b)})
   .then(function(r){return r.json().catch(function(){return {};}).then(function(d){return {ok:r.ok,st:r.status,d:d||{}};});})
   .then(function(x){var d=x.d;
     if(!x.ok||!d.qr_code)return falha(d.error||'Não foi possível gerar o Pix agora. Tente de novo em instantes ou escolha outra forma de pagamento.','pix_'+x.st);
     if(btn){btn.disabled=false;btn.textContent=orig;}
     var exp=Date.parse(d.expira_em||'');if(!(exp>Date.now()))exp=Date.now()+30*60000;
     _pxParar();
     _PX={pedido:String(d.pedido||corpo.pedido),id:String(d.id),qr:String(d.qr_code),qrb64:d.qr_code_base64||'',total:+d.total||0,exp:exp,tent:tent,corpo:corpo,chave:chaveFrete()};
     try{var lp=JSON.parse(localStorage.getItem('sullab_last_purchase')||'{}');if(lp.ped===_PX.pedido&&_PX.total){lp.v=_PX.total;lp.pix=_PX.id;localStorage.setItem('sullab_last_purchase',JSON.stringify(lp));}}catch(e){}
     _pxRender();pixMostrar(true);
     _pxEv('pix_qr_exibido',{transaction_id:_PX.pedido,value:_PX.total,currency:'BRL',tentativa:tent});
     _pxTick();_PX.tick=setInterval(_pxTick,1000);_pxAgendar(4000);})
   .catch(function(){falha('Erro de conexão ao gerar o Pix. Confira a internet e tente de novo.','pix_rede');});
}
function _pxTick(){var P=_PX;if(!P||P.fim)return;var r=Math.max(0,P.exp-Date.now()),m=Math.floor(r/60000),s=Math.floor(r%60000/1000),c=_pxEl('pxCnt');
  if(c)c.textContent=(m<10?'0':'')+m+':'+(s<10?'0':'')+s;
  if(r<=0&&!P.venceu){P.venceu=1;clearTimeout(P.timer);_pxStatus();}}
function _pxAgendar(ms){var P=_PX;if(!P||P.fim)return;clearTimeout(P.timer);P.timer=setTimeout(function(){_pxStatus();},ms);}
function _pxStatus(){var P=_PX;if(!P||P.fim)return;
  fetch(MP_WORKER+'pix/status?id='+encodeURIComponent(P.id),{cache:'no-store'}).then(function(r){return r.json();}).then(function(d){
    if(_PX!==P||P.fim)return;var st=String((d&&d.status)||'');
    if(st==='approved')return _pxAprovado(P);
    if(/cancel|expir|reject/.test(st)||Date.now()>=P.exp)return _pxExpirado(P,st||'tempo');
    if(!P.tick)return;_pxAgendar(document.hidden?10000:4000);
  }).catch(function(){if(_PX!==P||P.fim)return;if(Date.now()>=P.exp+60000)return _pxExpirado(P,'tempo');if(P.tick)_pxAgendar(6000);});}
function _pxExpirado(P,motivo){P.fim=1;_pxParar();_pxStat('exp');_pxEl('pxNovo').hidden=false;_pxEl('pxQrBox').classList.add('exp');_pxEl('pxExp').hidden=true;_pxEl('pxCopyBtn').disabled=true;
  _pxEv('pix_expirado',{transaction_id:P.pedido,tentativa:P.tent,motivo:motivo||''});}
function pixNovo(){if(!_PX)return;pixGerar(_PX.corpo,(_PX.tent||1)+1);}
function pixVoltar(){_pxParar();_PX=null;pixMostrar(false);return false;}
function pixCopiar(){if(!_PX)return;var t=_PX.qr,b=_pxEl('pxCopyBtn'),P=_PX;
  var ok=function(){if(b){b.textContent='Copiado ✓';setTimeout(function(){if(b&&!P.fim)b.textContent='Copiar';},2500);}_pxEv('pix_copiado',{transaction_id:P.pedido});};
  var fb=function(){try{var i=_pxEl('pxCode');i.focus();i.select();try{i.setSelectionRange(0,t.length);}catch(e){}document.execCommand('copy');ok();}catch(e){}};
  try{if(navigator.clipboard&&window.isSecureContext)navigator.clipboard.writeText(t).then(ok,fb);else fb();}catch(e){fb();}}
function _pxAprovado(P){P.fim=1;_pxParar();_pxStat('ok');var cb=_pxEl('pxCopyBtn');if(cb)cb.disabled=true;
  var lp={};try{lp=JSON.parse(localStorage.getItem('sullab_last_purchase')||'{}')||{};}catch(e){}
  var its=(lp.ped===P.pedido&&lp.items)||[],v=Math.round((P.total||lp.v||0)*100)/100;
  _pxEv('pix_aprovado',{transaction_id:P.pedido,value:v,currency:'BRL',tentativa:P.tent});
  /* uma conversão por pedido: o obrigado.html não repete o que já foi enviado aqui (sullab_purchase_enviadas) */
  var env={};try{env=JSON.parse(localStorage.getItem('sullab_purchase_enviadas')||'{}')||{};}catch(e){}
  if(!env[P.pedido]){
    var gp={transaction_id:P.pedido,value:v,currency:'BRL',payment_type:'pix'};if(its.length)gp.items=its;if(lp.frete)gp.shipping=lp.frete;
    try{if(typeof gtag==='function'){gtag('event','purchase',gp);gtag('event','conversion',{send_to:'AW-11390766577/zT6SCKz-1KwdEPGbxbcq',value:v||1,currency:'BRL',transaction_id:P.pedido});}}catch(e){}
    try{if(typeof fbq==='function')fbq('track','Purchase',{value:v,currency:'BRL',content_type:'product',content_ids:its.map(function(x){return String(x.item_id);}),contents:its.map(function(x){return {id:String(x.item_id),quantity:x.quantity,item_price:x.price};}),num_items:its.reduce(function(s,x){return s+(x.quantity||1);},0)},{eventID:P.pedido});}catch(e){}
    try{if(window.clarity)clarity('event','purchase');}catch(e){}
    env[P.pedido]=Date.now();try{localStorage.setItem('sullab_purchase_enviadas',JSON.stringify(env));}catch(e){}
  }
  var u='/obrigado.html?pedido='+encodeURIComponent(P.pedido)+'&external_reference='+encodeURIComponent(P.pedido)+'&status=approved&payment_id='+encodeURIComponent(P.id)+'&metodo=pix'+(v?('&total='+v):'');
  setTimeout(function(){location.href=u;},900);}
document.addEventListener('visibilitychange',function(){try{if(!document.hidden&&_PX&&!_PX.fim&&_PX.tick){clearTimeout(_PX.timer);_pxStatus();}}catch(e){}});
function pagarMP(){
  var f=coletarFicha();
  if(soDig(f.tel).length<10)return ckFoco('ckTel'),ckErro('Informe um WhatsApp com DDD.');
  if(DOCT==='cnpj'?!cnpjValido(f.doc):!cpfValido(f.doc))return ckFoco('ckDoc'),ckErro(DOCT==='cnpj'?'Confira o CNPJ: são 14 caracteres (números, ou letras e números no CNPJ novo).':'Confira o CPF: são 11 números.');
  if(!f.nome)return ckFoco('ckNome'),ckErro(DOCT==='cpf'?'Informe seu nome completo.':'Informe a razão social da empresa.');
  if(!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(f.email))return ckFoco('ckEmail'),ckErro(PG==='pix'?'Informe um e-mail válido para gerar o Pix: é por ele que enviamos a confirmação e a NF-e.':'Informe um e-mail válido.');
  if(soDig(f.cep).length!==8)return ckFoco('ckCep'),ckErro('Informe o CEP com 8 números.');
  if(!f.log||!f.num)return ckFoco(f.log?'ckNum':'ckLog'),ckErro('Informe a rua e o número do endereço de entrega.');
  localStorage.setItem('sullab_ficha',JSON.stringify(f));
  if(!freteValido()){try{cotarFreteLoja();}catch(e){}return ckErro('Calcule o frete pelo CEP e escolha a transportadora antes de pagar.');}
  var items=[];
  CART.forEach(function(x){var fator=fatorPg(x.c)*(1-cupomPct);var b=precoBase(x);if(b<=0)return;var q=(x.kq&&x.kd)?Math.min(x.kq,x.qty):0;if(q)items.push({title:('KIT -'+Math.round(x.kd*100)+'% '+x.c+' '+x.n).slice(0,120),quantity:q,unit_price:Math.round(b*(1-x.kd)*fator*100)/100});if(x.qty-q>0)items.push({title:(x.c+' '+x.n).slice(0,120),quantity:x.qty-q,unit_price:Math.round(b*fator*100)/100});});
  if(freteSelLoja>0)items.push({id:'FRETE',title:'Frete'+(freteLabelLoja?(' ('+freteLabelLoja+')'):''),quantity:1,unit_price:Math.round(freteSelLoja*100)/100});
  if(faltaTubo()>0)return ckErro(msgMin()+' Faltam '+brl(faltaTubo())+' em produtos.');
  if(PG==='boleto'&&!boletoOk())return ckErro('Boleto disponível para pedidos a partir de R$ 400,00.');
  if(!items.length)return ckErro('Nenhum item com preço para pagar online. Equipamentos são sob consulta — use o WhatsApp.');
  var pedido='SLB-'+Date.now();window._pedAtual=pedido;
  try{var vtot=items.reduce(function(s,i){return s+i.unit_price*i.quantity;},0);
    localStorage.setItem('sullab_last_purchase',JSON.stringify({v:Math.round(vtot*100)/100,ped:pedido,ts:Date.now(),tel:f.tel||'',frete:freteSelLoja||0,
      items:CART.map(function(x){return {item_id:x.c,item_name:x.n,item_brand:x.m||'',quantity:x.qty,price:Math.round(precoItem(x)*fatorPg(x.c)*100)/100};})}));
  }catch(e){}
  try{var _o=window.SULLAB_ORIGEM||{};var _cm={action:'conv_meta',pedido:pedido,v:(function(){try{return JSON.parse(localStorage.getItem('sullab_last_purchase')||'{}').v||0;}catch(e){return 0;}})(),
      gclid:_o.gclid||'',gbraid:_o.gbraid||'',wbraid:_o.wbraid||'',utm_source:_o.utm_source||'',utm_campaign:_o.utm_campaign||'',cid:'',sid:''};
    var _ga=(document.cookie.match(/(?:^|;\s*)_ga=GA\d\.\d\.(\d+\.\d+)/)||[])[1];if(_ga)_cm.cid=_ga;
    var _gs=(document.cookie.match(/(?:^|;\s*)_ga_RK2PX868MS=GS\d\.\d\.s?(\d+)/)||[])[1];if(_gs)_cm.sid=_gs;
    _cm.t=SULLAB_EVT_TOKEN;var _cmb=JSON.stringify(_cm);
    if(!(navigator.sendBeacon&&navigator.sendBeacon(SHEET_ENDPOINT,new Blob([_cmb],{type:'text/plain;charset=utf-8'}))))fetch(SHEET_ENDPOINT,{method:'POST',mode:'no-cors',keepalive:true,headers:{'Content-Type':'text/plain;charset=utf-8'},body:_cmb});
  }catch(e){}
  dispararPedido('pedido_mp',PG,f,pedido);
  var endereco={cep:f.cep,logradouro:f.log,numero:f.num,complemento:f.compl,bairro:f.bairro,cidade:f.cidade,uf:f.uf};
  var corpo={pedido:pedido,items:items,method:PG,endereco:endereco,frete:{valor:Math.round((freteSelLoja||0)*100)/100,gratis:!(freteSelLoja>0),servico:freteSelId||'',nome:freteLabelLoja||'',cep:soDig(f.cep)},cliente:{nome:f.nome,doc:docParaMP(f.doc),docTipo:DOCT,tel:f.tel,email:f.email}};
  /* 31/10/2026: Pix transparente — o QR aparece aqui mesmo (Worker POST /pix); cartão e boleto seguem para o Mercado Pago */
  if(PG==='pix')return pixGerar(corpo,1);
  var btn=document.getElementById('ckPayBtn');var orig=btn.textContent;btn.disabled=true;btn.textContent='Abrindo Mercado Pago…';
  fetch(MP_WORKER,{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(corpo)})
   .then(function(r){return r.json();}).then(function(d){if(d&&d.init_point){window.location.href=d.init_point;}else{btn.disabled=false;btn.textContent=orig;ckErro('Não foi possível iniciar o pagamento: '+((d&&d.error)||'tente novamente.'));}})
   .catch(function(){btn.disabled=false;btn.textContent=orig;ckErro('Erro de conexão com o pagamento online. Obs.: na versão de teste local (preview) o pagamento só funciona com a loja publicada — você pode fechar pelo WhatsApp logo abaixo.');});
}

var FBCFG={apiKey:"AIzaSyBoIPsSsAAg0dPsd8rmwNmuXz7SQHwQw68",authDomain:"sullab.firebaseapp.com",projectId:"sullab",storageBucket:"sullab.firebasestorage.app",messagingSenderId:"882002573877",appId:"1:882002573877:web:2808e29ca74e05a5cf0f7c"};
var AUTH=null,DB=null,ACCDOC='cnpj';window.__user=null;window.__profile=null;
var _FB={st:0,cbs:[]};
function sullabFirebase(cb){if(cb)_FB.cbs.push(cb);if(_FB.st===2||_FB.st===3){_fbFim();return;}if(_FB.st===1)return;_FB.st=1;
  var V='https://www.gstatic.com/firebasejs/10.12.2/firebase-',ld=function(n){return new Promise(function(ok,er){var s=document.createElement('script');s.src=V+n+'-compat.js';s.async=true;s.onload=ok;s.onerror=er;document.head.appendChild(s);});};
  ld('app').then(function(){return Promise.all([ld('auth'),ld('firestore')]);}).then(function(){try{firebase.initializeApp(FBCFG);AUTH=firebase.auth();DB=firebase.firestore();AUTH.onAuthStateChanged(function(u){window.__user=u||null;try{if(u)localStorage.setItem('sullab_fb','1');else localStorage.removeItem('sullab_fb');}catch(_e){}if(u){CNPJ=true;DB.collection('clientes').doc(u.uid).get().then(function(d){if(d.exists){window.__profile=d.data();perfilParaFicha(d.data());}atualizarConta();}).catch(function(){});}else{window.__profile=null;}atualizarConta();try{render();atualizarCart();}catch(e){}});_FB.st=2;}catch(e){_FB.st=3;}_fbFim();}).catch(function(){_FB.st=3;_fbFim();});}
function _fbFim(){var a=_FB.cbs;_FB.cbs=[];a.forEach(function(f){try{f();}catch(e){}});}
function _fbTenta(fn){if(AUTH||_FB.st===3)return false;sullabFirebase(fn);return true;}
(function(){var go=function(){setTimeout(function(){sullabFirebase();},1500);},on=false;try{on=!!localStorage.getItem('sullab_fb');}catch(e){}
  var dep=function(){if(document.readyState==='complete')go();else window.addEventListener('load',go);};
  if(on)return dep();try{if(indexedDB&&indexedDB.databases)indexedDB.databases().then(function(l){if((l||[]).some(function(d){return d&&d.name==='firebaseLocalStorageDb';}))dep();}).catch(function(){});}catch(e){}})();
function fbErr(e){var c=((e&&e.code)||'')+'';if(c.indexOf('email-already')>=0)return 'Este e-mail já tem conta. Tente entrar.';if(c.indexOf('wrong-password')>=0||c.indexOf('invalid-credential')>=0)return 'E-mail ou senha incorretos.';if(c.indexOf('user-not-found')>=0)return 'Não encontramos uma conta com esse e-mail.';if(c.indexOf('weak-password')>=0)return 'A senha precisa de ao menos 6 caracteres.';if(c.indexOf('invalid-email')>=0)return 'E-mail inválido.';if(c.indexOf('too-many')>=0)return 'Muitas tentativas. Aguarde um pouco.';if(c.indexOf('unauthorized-domain')>=0||c.indexOf('network')>=0)return 'Login só funciona na loja publicada — no preview local o Firebase bloqueia o domínio.';return (e&&e.message)||'Não foi possível concluir agora.';}
function perfilParaFicha(p){try{var f=fichaSalva();f.nome=p.razao||f.nome;f.doc=p.cnpj||f.doc;f.doct=p.docTipo||f.doct;f.tel=p.telefone||f.tel;f.email=p.email||f.email;localStorage.setItem('sullab_ficha',JSON.stringify(f));}catch(e){}}
function abrirConta(tab){sullabFirebase(function(){if(window.__user)carregarMeusPedidos(false);});var s=document.getElementById('accSenha');if(s)s.style.display='none';atualizarConta();setAccTab(tab==='reg'?'reg':'login');document.getElementById('accErr').style.display='none';document.getElementById('acc').classList.add('on');if(window.__user)carregarMeusPedidos(false);}
function fecharConta(){document.getElementById('acc').classList.remove('on');}
function setAccTab(t){document.getElementById('tabLogin').classList.toggle('on',t==='login');document.getElementById('tabReg').classList.toggle('on',t==='reg');document.getElementById('paneLogin').style.display=t==='login'?'':'none';document.getElementById('paneReg').style.display=t==='reg'?'':'none';}
function setAccDoc(d){ACCDOC=d;document.getElementById('rgCnpj').classList.toggle('on',d==='cnpj');document.getElementById('rgCpf').classList.toggle('on',d==='cpf');document.getElementById('rgLbDoc').textContent=d==='cnpj'?'CNPJ':'CPF';document.getElementById('rgLbNome').textContent=d==='cnpj'?'Nome fantasia':'Nome completo';document.getElementById('rgDoc').placeholder=d==='cnpj'?'00.000.000/0000-00':'000.000.000-00';}
function accErro(m){var e=document.getElementById('accErr');e.textContent=m;e.style.display='block';}
function _primeiroNome(){return (window.__profile&&window.__profile.razao)?String(window.__profile.razao).split(' ')[0]:'minha conta';}
function atualizarConta(){var u=window.__user;var inb=document.getElementById('accIn'),outb=document.getElementById('accOut');var _ds=document.getElementById('accSenha');if(_ds&&_ds.style.display!=='none'){if(inb)inb.style.display='none';if(outb)outb.style.display='none';}else if(inb&&outb){if(u){inb.style.display='';outb.style.display='none';document.getElementById('accNome').textContent='Olá, '+((window.__profile&&window.__profile.razao)||(u.email||'').split('@')[0])+'!';document.getElementById('accEmail').textContent=u.email||'';}else{inb.style.display='none';outb.style.display='';}}
  var l=document.getElementById('accLbl');if(l)l.textContent=u?'conectado':'CNPJ';
  var ut=document.getElementById('accUtil');if(ut)ut.textContent=u?('Olá, '+_primeiroNome()):'Entrar / Cadastrar CNPJ';}
function _acPost(body){return fetch(SHEET_ENDPOINT,{method:'POST',headers:{'Content-Type':'text/plain;charset=utf-8'},body:JSON.stringify(body)}).then(function(r){return r.json();});}
function _acH(s){return String(s==null?'':s).replace(/[&<>"']/g,function(c){return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c];});}
function fbLogin(){var id=val('liEmail'),pass=document.getElementById('liPass').value;if(!id||!pass)return accErro('Informe e-mail (ou CPF/CNPJ) e senha.');if(!AUTH){if(_fbTenta(fbLogin))return accErro('Conectando…');return accErro('Login disponível na loja publicada.');}
  var entrar=function(email){return AUTH.signInWithEmailAndPassword(email,pass).then(function(){document.getElementById('accErr').style.display='none';atualizarConta();carregarMeusPedidos(true);}).catch(function(e){accErro(fbErr(e));});};
  if(id.indexOf('@')>=0)return entrar(id);
  var dig=soDig(id);if(dig.length!==11&&dig.length!==14)return accErro('Digite um e-mail ou um CPF/CNPJ válido.');
  accErro('Entrando…');
  _acPost({action:'loginDoc',doc:dig,senha:pass}).then(function(d){if(d&&d.ok&&d.email)return entrar(d.email);accErro((d&&d.erro)||'CPF/CNPJ ou senha incorretos.');}).catch(function(){accErro('Não foi possível entrar agora. Tente com o e-mail.');});}
function fbReset(){var email=val('liEmail');if(!/.+@.+\..+/.test(email))return accErro('Para receber o link, digite o seu e-mail (não o CPF/CNPJ) no campo acima.');if(!AUTH){if(_fbTenta(fbReset))return;return accErro('Disponível na loja publicada.');}AUTH.sendPasswordResetEmail(email).then(function(){accErro('Enviamos um link de redefinição para '+email+'.');}).catch(function(e){accErro(fbErr(e));});}
function fbLogout(){_MP=null;if(AUTH)AUTH.signOut().then(function(){atualizarConta();fecharConta();});}
function fbCadastro(){var razao=val('rgNome'),docv=val('rgDoc'),email=val('rgEmail'),tel=val('rgTel'),pass=document.getElementById('rgPass').value;
  if(!razao)return accErro('Informe o '+(ACCDOC==='cnpj'?'nome fantasia':'nome')+'.');
  if(soDig(docv).length<11)return accErro('Informe um '+(ACCDOC==='cnpj'?'CNPJ':'CPF')+' válido.');
  if(!/.+@.+\..+/.test(email))return accErro('E-mail inválido.');
  if(soDig(tel).length<10)return accErro('Telefone com DDD.');
  if(pass.length<6)return accErro('A senha precisa de ao menos 6 caracteres.');
  if(!AUTH||!DB){if(_fbTenta(fbCadastro))return accErro('Conectando…');return accErro('Cadastro disponível na loja publicada (o preview local não conecta o Firebase).');}
  AUTH.createUserWithEmailAndPassword(email,pass).then(function(cred){var u=cred.user;var prof={razao:razao,cnpj:docv,docTipo:ACCDOC,telefone:tel,email:email,criadoEm:Date.now()};window.__profile=prof;try{sullabEvent('conta_cadastro',{razao:razao,doc:docv,docTipo:ACCDOC,telefone:tel,email:email});}catch(_e){}perfilParaFicha(prof);return DB.collection('clientes').doc(u.uid).set(prof,{merge:true});}).then(function(){fecharConta();}).catch(function(e){accErro(fbErr(e));});}

var _MP=null;
function _etapaTxt(e,pago){e=String(e||'').toLowerCase();if(e.indexOf('entreg')>=0)return statusLabel('entregue');if(e.indexOf('post')>=0)return statusLabel('postado');if(e.indexOf('fatur')>=0)return statusLabel('faturado');if(e.indexOf('separ')>=0)return statusLabel('separado');if(e.indexOf('pago')>=0||pago)return statusLabel('pago');return statusLabel('recebido');}
function _rastLinha(p){if(!p.rastreio)return '';var u=String(p.rastreioUrl||'');if(!/^https:\/\//.test(u))u='https://www.melhorrastreio.com.br/rastreio/'+encodeURIComponent(p.rastreio);return '<div style="font-size:12.5px;margin-top:5px">🚚 '+(p.transportadora?_acH(p.transportadora)+' · ':'')+'Rastreio <b>'+_acH(p.rastreio)+'</b> · <a href="'+_acH(u)+'" target="_blank" rel="noopener" style="color:var(--navy-l);font-weight:700">acompanhar entrega →</a></div>';}
function _mpCard(p){var its=(p.itens||[]).slice(0,4).map(_acH).join('<br>')+((p.itens||[]).length>4?'<br>…':'');
  return '<div style="border:1px solid var(--line);border-radius:11px;padding:11px 12px;margin-bottom:9px">'+
    '<div style="display:flex;justify-content:space-between;align-items:center;gap:8px"><b style="font-size:13.5px;color:var(--navy)">'+_acH(p.pedido)+'</b><span style="font-size:11.5px;color:var(--muted)">'+_acH(p.data)+'</span></div>'+
    '<div style="font-size:12px;color:var(--muted);margin:4px 0 6px;line-height:1.45">'+its+(p.total?'<br><b style="color:var(--ink)">Total pago: '+_acH(p.total)+'</b>':'')+'</div>'+
    '<div style="font-size:12.5px;font-weight:800;color:var(--ink)">'+_etapaTxt(p.etapa,p.pago)+'</div>'+
    (p.nf?'<div style="font-size:12.5px;margin-top:5px">🧾 NF-e <b>'+_acH(p.nf)+'</b>'+(p.chave?'<div style="font-size:10.5px;color:var(--muted);word-break:break-all;margin-top:2px">Chave: '+_acH(p.chave)+'</div>':'')+'</div>':'')+
    (p.danfe?'<button class="ckpay" style="background:var(--navy);padding:10px;font-size:13px;margin-top:8px" onclick="baixarDanfe(\''+_acH(p.pedido)+'\',this)">Baixar nota fiscal (PDF)</button>':'')+
    _rastLinha(p)+'</div>';}
function carregarMeusPedidos(forcar){var el=document.getElementById('mpList');if(!el)return;var u=window.__user;if(!u){el.innerHTML='';return;}
  if(_MP&&!forcar){renderMP();return;}
  el.innerHTML='<div style="font-size:12.5px;color:var(--muted);padding:8px 2px">Carregando seus pedidos…</div>';
  u.getIdToken(true).then(function(tk){return _acPost({action:'meuspedidos',idToken:tk});}).then(function(d){_MP=d||{ok:false};renderMP();}).catch(function(){_MP=null;el.innerHTML='<div style="font-size:12.5px;color:var(--muted);padding:8px 2px">Não foi possível carregar agora. Toque em “Atualizar”.</div>';});}
function renderMP(){var el=document.getElementById('mpList');if(!el)return;var d=_MP||{};
  if(!d.ok){el.innerHTML='<div style="font-size:12.5px;color:var(--muted);padding:8px 2px">Não foi possível carregar agora. Toque em “Atualizar”.</div>';return;}
  if(d.verificar){el.innerHTML='<div style="font-size:12.5px;color:var(--muted);background:var(--bg);border-radius:10px;padding:12px;line-height:1.5">Para ver seus pedidos, confirme o seu e-mail.<br><span class="rm" style="color:var(--navy-l);font-weight:800;cursor:pointer" onclick="enviarVerificacao(this)">Enviar e-mail de confirmação →</span></div>';return;}
  var a=d.pedidos||[];if(!a.length){el.innerHTML='<div style="font-size:12.5px;color:var(--muted);background:var(--bg);border-radius:10px;padding:14px;text-align:center;line-height:1.5">Nenhum pedido pago encontrado para este e-mail ainda.<br>Os pedidos pagos no site aparecem aqui com nota fiscal e rastreio.</div>';return;}
  el.innerHTML=a.map(_mpCard).join('');}
function enviarVerificacao(b){var u=window.__user;if(!u)return;var ok=function(){if(b)b.textContent='Enviado por comercial@sullabrj.com.br! Confira sua caixa de entrada (e o Spam) e depois toque em “Atualizar”.';},er=function(){if(b)b.textContent='Não foi possível enviar agora. Tente mais tarde ou fale com a gente no WhatsApp.';};if(b)b.textContent='Enviando…';u.getIdToken(true).then(function(tk){return _acPost({action:'verificaremail',idToken:tk});}).then(function(d){if(d&&d.ok){ok();}else{throw 0;}}).catch(function(){er();});}
function baixarDanfe(ped,btn){var u=window.__user;if(!u)return;var t=btn?btn.textContent:'';if(btn){btn.disabled=true;btn.textContent='Baixando…';}
  u.getIdToken().then(function(tk){return _acPost({action:'danfe',idToken:tk,pedido:ped});}).then(function(d){
    if(!d||!d.ok||!d.b64)throw 0;var bin=atob(d.b64),n=bin.length,arr=new Uint8Array(n);for(var i=0;i<n;i++)arr[i]=bin.charCodeAt(i);
    var url=URL.createObjectURL(new Blob([arr],{type:'application/pdf'}));var a=document.createElement('a');a.href=url;a.download=String(d.nome||('DANFE-'+ped+'.pdf')).replace(/[^\w.\- ]/g,'');document.body.appendChild(a);a.click();setTimeout(function(){URL.revokeObjectURL(url);a.remove();},4000);
    if(btn){btn.disabled=false;btn.textContent=t;}
  }).catch(function(){if(btn){btn.disabled=false;btn.textContent='Não foi possível baixar agora — tente de novo';}});}
var _DS_TOKEN='';
function abrirDefinirSenha(tok){sullabFirebase();_DS_TOKEN=tok;document.getElementById('accIn').style.display='none';document.getElementById('accOut').style.display='none';document.getElementById('accSenha').style.display='';document.getElementById('dsErr').style.display='none';document.getElementById('acc').classList.add('on');}
function definirSenhaSite(){var p1=document.getElementById('dsPass').value,p2=document.getElementById('dsPass2').value,er=document.getElementById('dsErr');var msg=function(m){er.textContent=m;er.style.display='block';};
  if(p1.length<6)return msg('A senha precisa de ao menos 6 caracteres.');if(p1!==p2)return msg('As duas senhas não são iguais.');
  var b=document.getElementById('dsBtn');b.disabled=true;b.textContent='Salvando…';
  _acPost({action:'definirSenha',token:_DS_TOKEN,senha:p1}).then(function(d){
    if(!d||!d.ok){b.disabled=false;b.textContent='Salvar senha e entrar';return msg((d&&d.erro)||'Não foi possível salvar agora.');}
    try{history.replaceState(null,'',location.pathname+location.search);}catch(e){}
    if(!AUTH&&_FB.st===1){return new Promise(function(ok){sullabFirebase(ok);}).then(function(){if(!AUTH){b.disabled=false;b.textContent='Salvar senha e entrar';return msg('Senha criada! Entre com seu e-mail e a nova senha.');}return AUTH.signInWithEmailAndPassword(d.email,p1).then(function(){document.getElementById('accSenha').style.display='none';b.disabled=false;b.textContent='Salvar senha e entrar';atualizarConta();carregarMeusPedidos(true);});});}
    if(!AUTH){b.disabled=false;b.textContent='Salvar senha e entrar';return msg('Senha criada! Entre com seu e-mail e a nova senha.');}
    return AUTH.signInWithEmailAndPassword(d.email,p1).then(function(){document.getElementById('accSenha').style.display='none';b.disabled=false;b.textContent='Salvar senha e entrar';atualizarConta();carregarMeusPedidos(true);});
  }).catch(function(){b.disabled=false;b.textContent='Salvar senha e entrar';msg('Erro de conexão. Tente de novo.');});}
(function(){function h(){var m=/^#definir-senha=([a-f0-9]{40,80})$/i.exec(location.hash||'');if(m){abrirDefinirSenha(m[1]);return;}if(location.hash==='#conta'){try{history.replaceState(null,'',location.pathname+location.search);}catch(e){}setTimeout(function(){abrirConta();},600);}}
  window.addEventListener('DOMContentLoaded',h);window.addEventListener('hashchange',h);})();

function meusPedidos(){try{return JSON.parse(localStorage.getItem('sullab_meus_pedidos')||'[]');}catch(e){return [];}}
function registrarMeuPedido(o){try{var a=meusPedidos();if(a.some(function(x){return x.pedido===o.pedido;}))return;a.unshift(o);a=a.slice(0,20);localStorage.setItem('sullab_meus_pedidos',JSON.stringify(a));}catch(e){}}
function statusLabel(st){var m={recebido:'🟡 Recebido — em processamento',pago:'🟢 Pagamento aprovado',separado:'🔵 Em separação',faturado:'🧾 Faturado (NF-e)',postado:'🚚 Postado',entregue:'✅ Entregue'};return m[st]||m.recebido;}
var RAST_EP=SHEET_ENDPOINT;
function _jsonp(url,cb){var s=document.createElement('script');var name='__rcb'+Date.now()+Math.floor(Math.random()*1e4);var done=false;window[name]=function(d){done=true;try{cb(d);}catch(e){}try{delete window[name];}catch(_e){}if(s.parentNode)s.parentNode.removeChild(s);};s.onerror=function(){if(!done){cb(null);try{delete window[name];}catch(_e){}if(s.parentNode)s.parentNode.removeChild(s);}};s.src=url+(url.indexOf('?')>=0?'&':'?')+'callback='+name;document.body.appendChild(s);setTimeout(function(){if(!done){try{window[name]=function(){};}catch(_e){}cb(null);}},9000);}
function consultarStatus(num,chave,done){if(!num||!chave){done(null);return;}_jsonp(RAST_EP+'?action=rastreio&pedido='+encodeURIComponent(num)+'&chave='+encodeURIComponent(chave),done);}
function rastStatusTexto(d){var e=((d&&d.etapa)||'').toLowerCase();var pg=((d&&d.statusPagamento)||'').toLowerCase();
  if(e.indexOf('entreg')>=0)return statusLabel('entregue');
  if(e.indexOf('post')>=0)return statusLabel('postado');
  if(e.indexOf('fatur')>=0)return statusLabel('faturado');
  if(e.indexOf('separ')>=0)return statusLabel('separado');
  if(pg.indexOf('approv')>=0||pg.indexOf('aprov')>=0||pg.indexOf('pago')>=0)return statusLabel('pago');
  if(pg.indexOf('pend')>=0||pg.indexOf('aguard')>=0)return '🟡 Aguardando pagamento';
  return statusLabel('recebido');}
function updateSavedStatuses(){var ch=((fichaSalva().email)||'').trim();if(!ch)return;meusPedidos().forEach(function(o){consultarStatus(o.pedido,ch,function(d){if(!d||!d.ok||!d.found)return;var pid=String(o.pedido).replace(/[^A-Za-z0-9-]/g,'');var el=document.getElementById('rstat_'+pid);if(el)el.innerHTML=rastStatusTexto(d);});});}
function abrirRastreio(){renderRastreio();var ce=document.getElementById('rastChave');if(ce&&!ce.value)ce.value=(fichaSalva().email||'');document.getElementById('rastResult').innerHTML='';document.getElementById('rast').classList.add('on');updateSavedStatuses();}
function fecharRastreio(){document.getElementById('rast').classList.remove('on');}
function acompanharWhats(num){abrirWhats('Olá! Quero acompanhar o meu pedido '+num+'. Pode me passar o status?');}
function _rastBox(msg,num){return '<div style="border:1px solid var(--line);border-radius:11px;padding:12px;margin-top:8px;font-size:12.5px;color:var(--muted)">'+msg+'<br><span class="rm" style="display:inline-block;margin-top:7px;color:var(--green-d);font-weight:700;cursor:pointer" onclick="acompanharWhats(\''+(num||'')+'\')">💬 Acompanhar pelo WhatsApp →</span></div>';}
function lookupRastreio(){var n=(document.getElementById('rastNum').value||'').trim();var ch=(document.getElementById('rastChave').value||'').trim();var box=document.getElementById('rastResult');
  if(!n){box.innerHTML='';return;}
  if(!ch){box.innerHTML=_rastBox('Informe o e-mail usado no pedido para ver o status — ou fale com a equipe.',n);return;}
  box.innerHTML='<div style="font-size:12.5px;color:var(--muted);padding:10px 2px">Consultando…</div>';
  consultarStatus(n,ch,function(d){
    if(!d||!d.ok){box.innerHTML=_rastBox('Não foi possível consultar agora (disponível na loja publicada). Fale com a equipe pelo WhatsApp.',n);return;}
    if(!d.found){box.innerHTML=_rastBox('Não encontramos um pedido com esse número e e-mail. Confira os dados.',n);return;}
    var tot=d.total?(String(d.total).indexOf('R$')>=0?d.total:('R$ '+d.total)):'';
    box.innerHTML='<div style="border:1px solid var(--green);background:var(--green-soft);border-radius:11px;padding:12px 13px;margin-top:8px">'+
      '<div style="display:flex;justify-content:space-between;align-items:center"><b style="color:var(--navy)">'+d.pedido+'</b><span style="font-size:11.5px;color:var(--muted)">'+(d.data||'')+'</span></div>'+
      ((d.canal||tot)?'<div style="font-size:12px;color:var(--muted);margin:3px 0 5px">'+[d.canal,tot].filter(Boolean).join(' · ')+'</div>':'')+
      '<div style="font-size:13px;font-weight:800;color:var(--ink)">'+rastStatusTexto(d)+'</div>'+
      (d.nf?'<div style="font-size:12.5px;margin-top:5px">🧾 NF-e <b>'+_acH(d.nf)+'</b> · a nota fiscal (PDF) fica na sua <span class="rm" style="color:var(--navy-l);font-weight:700;cursor:pointer" onclick="fecharRastreio();abrirConta()">área do cliente</span></div>':'')+
      _rastLinha(d)+
      '<span class="rm" style="display:inline-block;margin-top:7px;color:var(--green-d);font-weight:700;cursor:pointer" onclick="acompanharWhats(\''+_acH(d.pedido)+'\')">💬 Falar com a equipe →</span>'+
    '</div>';
  });}
function renderRastreio(){var a=meusPedidos();var el=document.getElementById('rastList');
  if(!a.length){el.innerHTML='<div style="font-size:12.5px;color:var(--muted);background:var(--bg);border-radius:10px;padding:16px;text-align:center;line-height:1.5">Você ainda não fez pedidos por aqui.<br>Quando fizer, eles aparecem aqui com o número e o status — e você acompanha pelo WhatsApp.</div>';return;}
  el.innerHTML=a.map(function(o){var d=new Date(o.ts);var z=function(x){return ('0'+x).slice(-2);};var data=z(d.getDate())+'/'+z(d.getMonth()+1)+'/'+d.getFullYear();
    var its=(o.itens||[]).slice(0,3).map(function(x){return (x.q||1)+'x '+x.nome;}).join(', ')+(((o.itens||[]).length>3)?'…':'');
    var canal=(o.canal==='online')?'Pagamento online':'WhatsApp';
    return '<div style="border:1px solid var(--line);border-radius:11px;padding:12px 13px;margin-bottom:9px">'+
      '<div style="display:flex;justify-content:space-between;align-items:center"><b style="font-size:13.5px;color:var(--navy)">'+o.pedido+'</b><span style="font-size:11.5px;color:var(--muted)">'+data+' · '+canal+'</span></div>'+
      '<div style="font-size:12px;color:var(--muted);margin:4px 0 7px">'+its+' &nbsp;·&nbsp; <b style="color:var(--ink)">'+brl(o.total)+'</b></div>'+
      '<div id="rstat_'+String(o.pedido).replace(/[^A-Za-z0-9-]/g,'')+'" style="font-size:12.5px;font-weight:700;color:var(--ink)">'+statusLabel(o.status||'recebido')+'</div>'+
      '<span class="rm" style="display:inline-block;margin-top:7px;color:var(--green-d);font-weight:700;cursor:pointer" onclick="acompanharWhats(\''+o.pedido+'\')">💬 Acompanhar pelo WhatsApp →</span>'+
    '</div>';}).join('');}

var __pmL=[],__pmI=0;
function pmLista(p){var l=[p.img];[p.img2,'img/a/'+p.c+'.webp'].forEach(function(u){if(u&&l.indexOf(u)<0)l.push(u);});return l;}
function pmGo(k){if(!__pmL.length)return;__pmI=(k+__pmL.length)%__pmL.length;var m=document.getElementById('pmMain');if(m){m.src=__pmL[__pmI];m.classList.toggle('art',__pmI>0);}
  var th=document.querySelectorAll('#pmTh img');for(var i=0;i<th.length;i++)th[i].classList.toggle('on',i===__pmI);}
function pmNav(d){pmGo(__pmI+d);}
function pmTroca(u){var k=__pmL.indexOf(u);if(k>=0)pmGo(k);else{var m=document.getElementById('pmMain');if(m)m.src=u;}}
function pmSwipe(){var st=document.getElementById('pmStage');if(!st||st.__sw)return;st.__sw=1;var x0=null;
  st.addEventListener('touchstart',function(e){x0=e.touches[0].clientX;},{passive:true});
  st.addEventListener('touchend',function(e){if(x0===null)return;var dx=e.changedTouches[0].clientX-x0;x0=null;if(Math.abs(dx)>40)pmNav(dx<0?1:-1);},{passive:true});}
document.addEventListener('keydown',function(e){var m=document.getElementById('pmodal');if(!m||!m.classList.contains('on'))return;if(e.key==='ArrowRight')pmNav(1);else if(e.key==='ArrowLeft')pmNav(-1);});
function abrirProd(i){
  var p=CATALOG[i];
  var catNome=(DEPTS.find(function(d){return d.key===deptOf(p.k);})||{}).nome||'';
  var _prm=(window.PRECOS||{})[p.c];var precoHtml=(_prm&&_prm[1])?(((window.PIX3&&window.PIX3[p.c])?'<div style="display:inline-block;background:#1F4E79;color:#fff;font-size:12px;font-weight:800;padding:4px 10px;border-radius:999px;margin-top:8px">🏆 Tabela exclusiva do site em Vacuette</div>':'')+'<div style="margin-top:10px;line-height:1.45"><div style="font-size:26px;font-weight:800;color:#2f9e63">'+brl(_prm[1])+'</div>'+unitLn(p.c,_prm[1])+'<div style="font-size:13px;color:#3a4a63;font-weight:700">'+brl(Math.round(_prm[1]*(100-pixPct(p.c)*100))/100)+' no Pix</div><div class="pixl big">💚 Pague no Pix e ganhe <b>'+Math.round(pixPct(p.c)*100)+'% de desconto</b></div><div style="font-size:12px;color:#5f6b7c;margin-top:6px">Preço único · NF-e em todo pedido · frete calculado pelo CEP</div></div>'):('<div class="b2bsob" style="font-size:14px;margin-top:8px">Preço sob consulta — solicite o orçamento (NF-e · atacado)</div>');
  var acao='<div style="display:flex;gap:10px;align-items:center;margin-top:16px"><div class="stepper"><button onclick="step('+i+',-1,this)">−</button><span>1</span><button onclick="step('+i+',1,this)">+</button></div><button class="btn navy" style="flex:1" onclick="addCart('+i+',this)">🛒 Adicionar ao carrinho</button></div>';
  __pmL=pmLista(p);__pmI=0;
  document.getElementById('pmInner').innerHTML=
    '<div class="pmimg"><div class="pmstage" id="pmStage"><button class="pmar l" onclick="pmNav(-1)" aria-label="Foto anterior">&#8249;</button><img id="pmMain" width="320" height="320" src="'+__pmL[0]+'" onerror="this.removeAttribute(\'srcset\');this.src=\'/img/logo-sullab.png\';this.style.opacity=.4" alt="'+p.n+'"><button class="pmar r" onclick="pmNav(1)" aria-label="Próxima foto">&#8250;</button></div>'+(__pmL.length>1?'<div class="pmth" id="pmTh">'+__pmL.map(function(u,k){return '<img class="'+(k?'':'on')+'" width="58" height="58" src="'+u+'" onclick="pmGo('+k+')" alt="'+(k?'Informações técnicas':'Foto do produto')+'" onerror="this.remove();__pmL=__pmL.filter(function(x){return x!==this.getAttribute(\'src\')}.bind(this))">';}).join('')+'</div>':'')+'</div>'+
    '<div class="pmb"><button class="pmx" onclick="fecharProd()">×</button>'+
    '<span class="bc">'+p.m+' · cód. '+p.c+'</span><h3>'+p.n+'</h3>'+(catNome?'<div style="display:inline-block;font-size:11.5px;background:#eef2fb;color:var(--navy);padding:3px 10px;border-radius:8px;margin:2px 0 6px">🗂️ '+catNome+'</div>':'')+'<div id="pmFicha"></div>'+
    '<div class="spec">🏷️ Direto da distribuidora autorizada, sem taxa de marketplace.<br>🧾 NF-e em todo pedido · 📦 envio em 24h · 🛡️ produto com procedência.</div>'+
    precoHtml+
    '<div style="font-size:12px;color:var(--green-d);font-weight:700;margin-top:6px">'+(precoDe(p)>0?'✓ Preço de empresa (CNPJ) já aplicado':'')+'</div>'+
    acao+'</div>';
  document.getElementById('pmodal').classList.add('on');pmSwipe();
  var _fp=p;ensureFT(function(){var el=document.getElementById('pmFicha');if(el&&FTMAP&&FTMAP[_fp.c]){el.innerHTML='<div style="margin-top:10px;border:1px solid #e6ebf5;border-radius:10px;padding:10px 12px;background:#fafbff"><div style="font-weight:700;color:var(--navy);font-size:12.5px;margin-bottom:4px">🔬 Ficha técnica</div><div style="font-size:12.5px;color:#40506b;line-height:1.5">'+FTMAP[_fp.c].replace(/ · /g,'<br>')+'</div></div>';}});
  
}
function fecharProd(){document.getElementById('pmodal').classList.remove('on');}
window.addEventListener('mousedown',function(e){window.__mdT=e.target;},true);
window.addEventListener('load',function(){setTimeout(function(){ensureKw();},3000);setTimeout(function(){ensureFT();},3200);});
document.addEventListener('keydown',e=>{if(e.key==='Escape'){fecharProd();fecharCarrinho();}});

function carregarLive(){
  if(!/^https?:/.test(location.origin))return;
  fetch('/?_sullabcat='+Date.now(),{cache:'no-store'}).then(r=>r.text()).then(function(html){
    var m=html.match(/var\s+P\s*=\s*(\[[\s\S]*?\]);/);
    if(!m)return;
    var P; try{P=JSON.parse(m[1]);}catch(e){return;}
    var doc=new DOMParser().parseFromString(html,'text/html');
    var pm={};
    [...doc.querySelectorAll('.card')].forEach(function(c){
      var cod=((c.querySelector('.brandcod')||{}).textContent||'').replace(/·|cód\.?/gi,'').trim();
      var pub=parseFloat(((c.querySelector('.price')||{}).textContent||'').replace(/[^0-9,]/g,'').replace(',','.'))||0;
      var cnpj=parseFloat(((c.querySelector('.cnpjbox .val')||{}).textContent||'').replace(/[^0-9,]/g,'').replace(',','.'))||0;
      if(cod)pm[cod]={pub:pub,cnpj:cnpj};
    });
    var live=P.map(function(p){var pr=pm[p.cod]||{pub:0,cnpj:0};
      if(p.cod==='18150'||p.cod==='18153'){pr={pub:1098.90,cnpj:1000.00};}
      if(p.cod==='18151'){pr={pub:549.45,cnpj:500.00};}
      return {c:p.cod,n:p.nome,m:p.brand||'',k:p.cat||'',img:p.img||'/img/logo-sullab.png',pub:pr.pub,cnpj:pr.cnpj,selo:''};
    });
    if(live.length>20){CATALOG=live;boot();}
  }).catch(function(){ });
}

function fecharDeskNote(){var n=document.getElementById('deskNote');if(n)n.classList.remove('on');try{localStorage.setItem('sullab_desknote','1');}catch(e){}}
function maybeDeskNote(){
  try{if(localStorage.getItem('sullab_desknote'))return;}catch(e){}
  var mob=window.matchMedia('(max-width:760px)').matches||(('ontouchstart'in window)&&window.innerWidth<900);
  if(!mob)return;
  var n=document.getElementById('deskNote');if(n)setTimeout(function(){n.classList.add('on');},700);
}
function boot(){montarDeptNav();montarCatTiles();montarGreiner();montarOfertas();montarBrands();montarFiltros();render();atualizarCart();maybeDeskNote();}
try{boot();}catch(e){try{console.error(e);}catch(_){}}
(function(){
  try{
    var sp=new URLSearchParams(location.search);
    var q=(sp.get('q')||'').trim();
    var d=(sp.get('dept')||sp.get('cat')||'').trim();
    if(q){buscarTermo(q);}
    else if(d){setDept(d);}
  }catch(e){}
})();

/* ==== vendaJs ==== */
try{
(function(){
var REL={tubo:['agulha','curativo'],agulha:['tubo','curativo'],seringa:['agulha','curativo','luva'],scalp:['tubo','curativo','luva'],lanceta:['curativo','luva','tr'],tr:['lanceta','luva','curativo'],luva:['epi','curativo','plast'],curativo:['luva','agulha','epi'],epi:['luva','curativo'],lamina:['micro','meio','luva'],cubeta:['controle','bioq'],pipeta:['plast','luva'],meio:['micro','plast','lamina'],micro:['meio','lamina','luva'],bioq:['controle','cubeta','pipeta'],hemat:['controle','tubo','pipeta'],sorol:['tubo','controle','pipeta'],controle:['bioq','hemat','cubeta'],coletoram:[],plast:[],hosp:['luva','curativo','seringa']};
var RANK={top:0,hot:1};
var POOL={tubo:['450071','GRL36','188082','25492'],agulha:['GRL36','25492'],tr:['25492'],meio:['18248A','18286-10','PA285'],micro:['18248A','18286-10','PA285'],lanceta:['GRL36']};
var ITEM={'18248A':['18286-10','PA285'],'181401':['18286-10','PA285'],'18142E':['18286-10','PA285'],'18286-10':['18248A','PA285'],'18288-10':['18248A','PA285']};
function priced(p){var r=(window.PRECOS||{})[p.c];return r&&r[1]>0?r[1]:0;}
function famKey(p){var t=semAcento(p.n||'').replace(/\(.*?\)/g,' ').split(/ \u2014 | - /)[0];
  t=t.replace(/\b(bege|azul|branco|branca|rosa|verde|amarelo|amarela|vermelho|vermelha|preto|preta|laranja|roxo|lilas|cinza|incolor|transparente|kids|kid|infantil|slim|adulto|pequeno|medio|grande|neonatal|pediatrico)\b/g,' ').replace(/\b(c|cx|caixa|pacote|pct|com|un|unidades?)\b/g,' ').replace(/[^a-z]+/g,' ').trim();
  return t.split(' ').slice(0,5).join(' ')+'|'+semAcento(p.m||'');}
function relatedFor(codes,max){
  var inCart={};CART.forEach(function(x){inCart[x.c]=1;});codes.forEach(function(c){inCart[c]=1;});
  var byCode={};CATALOG.forEach(function(p){byCode[p.c]=p;});
  var seenC={},seenF={};
  Object.keys(inCart).forEach(function(c){seenC[c]=1;if(byCode[c])seenF[famKey(byCode[c])]=1;});
  var src=[];codes.forEach(function(c){var p=byCode[c];if(p)src.push(deptOf(p.k));});
  var out=[];
  function take(p){if(!p||out.length>=max||!priced(p)||!p.img)return;var f=famKey(p);if(seenC[p.c]||seenF[f])return;seenC[p.c]=1;seenF[f]=1;out.push(p);}
  codes.forEach(function(c){(ITEM[c]||[]).forEach(function(x){take(byCode[x]);});});
  src.forEach(function(d){(POOL[d]||[]).forEach(function(x){take(byCode[x]);});});
  var order=[];src.forEach(function(d){(REL[d]||[]).forEach(function(r){if(order.indexOf(r)<0&&src.indexOf(r)<0)order.push(r);});});
  var lists=order.map(function(d){return CATALOG.filter(function(p){return deptOf(p.k)===d&&priced(p)&&p.img&&!inCart[p.c];}).sort(function(a,b){var ra=RANK[a.selo]!=null?RANK[a.selo]:9,rb=RANK[b.selo]!=null?RANK[b.selo]:9;return ra-rb||priced(a)-priced(b);}).slice(0,8);});
  for(var k=0;k<8&&out.length<max;k++)lists.forEach(function(l){if(l[k])take(l[k]);});
  return out;
}
function rowHtml(p){return '<div class="rrow"><img '+imgMini(p,'46px')+' alt="" loading="lazy" width="46" height="46"><div class="rn">'+p.n+'<small>'+brl(priced(p))+'</small></div><button onclick="addRel(\''+p.c+'\',this)">+ Adicionar</button></div>';}
function relBlock(codes,title,max){var l=relatedFor(codes,max);if(!l.length)return '';return '<div class="relbox"><div class="rt">'+title+' <i>LEVE JUNTO</i></div>'+l.map(rowHtml).join('')+'</div>';}
window.addRel=function(c,btn){addCodigo(c,1);if(btn){btn.textContent='✓ Adicionado';}try{atualizarCart();}catch(e){}if(!document.getElementById('drawer').classList.contains('on'))abrirCarrinho();try{sullabEvent&&sullabEvent('cross_sell_add',{c:c});}catch(e){}};
var _ac=window.atualizarCart;
window.atualizarCart=function(){_ac.apply(this,arguments);try{var cr=document.getElementById('crel');if(!cr)return;if(!CART.length){var top=CATALOG.filter(function(p){return (p.selo==='top'||p.selo==='hot')&&priced(p)&&p.img;}).slice(0,6);cr.innerHTML=top.length?'<div class="relbox"><div class="rt">Mais vendidos <i>COMECE POR AQUI</i></div>'+top.map(rowHtml).join('')+'</div>':'';return;}cr.innerHTML=relBlock(CART.map(function(x){return x.c;}),'Complete seu pedido',6);}catch(e){}};
window.__sullabRel={rowHtml:rowHtml,priced:priced};
var _ap=window.abrirProd;
window.abrirProd=function(i){_ap.apply(this,arguments);try{var p=CATALOG[i],b=document.querySelector('#pmInner .pmb');if(b&&p)b.insertAdjacentHTML('beforeend',relBlock([p.c],'Quem leva este item costuma levar também',4));}catch(e){}};
window.fgConsulta=function(auto){
  var el=document.getElementById('fgCep'),out=document.getElementById('fgRes');if(!el||!out)return;
  var cep=(el.value||'').replace(/\D/g,'');
  if(cep.length!==8){if(!auto){out.className='fgr on';out.innerHTML='Informe o CEP com 8 números.';}return;}
  var code='18288-10',v=precoItem({c:code})||1.64;
  out.className='fgr on';out.innerHTML='Consultando…';
  try{var f=fichaSalva();f.cep=cep;localStorage.setItem('sullab_ficha',JSON.stringify(f));}catch(e){}try{document.getElementById('utilCep').innerHTML='📍 Entregar no CEP <b>'+cep.slice(0,5)+'-'+cep.slice(5)+'</b> · alterar';document.getElementById('fgx').classList.add('ok');}catch(e){}
  fetch(FRETE2,{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({cep:cep,itens:[{c:code,q:1,v:v}]})}).then(function(r){return r.json();}).then(function(d){
    var g=d&&d.gratis,c=cep.slice(0,5)+'-'+cep.slice(5);
    if(g&&g.falta>0){out.innerHTML='✅ CEP <b>'+c+'</b> salvo: <b>frete grátis disponível para a sua região</b>.<small>Adicione os produtos e veja no carrinho quanto falta para o frete grátis.</small>';}
    else if(g&&g.ativo){out.innerHTML='✅ Para o CEP <b>'+c+'</b>: o <b>frete é grátis</b> já nos pedidos pequenos.';}
    else{out.innerHTML='Para o CEP <b>'+c+'</b> o frete é calculado no carrinho ou confirmado no atendimento.';}
    try{sullabEvent&&sullabEvent('frete_gratis_consulta',{cep3:cep.slice(0,3)});}catch(e){}
  }).catch(function(){out.innerHTML='Não foi possível consultar agora. O frete aparece no carrinho.';});
};
try{var _fc=(fichaSalva()||{}).cep;if(_fc&&document.getElementById('fgCep')){document.getElementById('fgCep').value=String(_fc).replace(/\D/g,'').replace(/^(\d{5})(\d)/,'$1-$2');fgConsulta(true);}}catch(e){}
var CATPH={tubo:1,tr:1,meio:1,micro:1,bioq:1,hemat:1,curativo:1,coletoram:1};
window.montarCatTiles=function(){
  var el=document.getElementById('catTiles');if(!el)return;var h='';
  Object.keys(CATPH).forEach(function(k){var d=DEPTS.find(function(x){return x.key===k;});if(!d)return;var n=CATALOG.filter(function(p){return deptOf(p.k)===k;}).length;if(!n)return;
    h+='<div class="ctile cph" role="button" tabindex="0" onclick="setDept(\''+k+'\')" onkeydown="if(event.key===\'Enter\')setDept(\''+k+'\')"><div class="cimg"><picture><source type="image/webp" srcset="/img/cat/'+k+'-400.webp 400w, /img/cat/'+k+'.webp 800w" sizes="(max-width:700px) 33vw, (max-width:900px) 50vw, 160px"><img src="/img/cat/'+k+'-400.jpg" srcset="/img/cat/'+k+'-400.jpg 400w, /img/cat/'+k+'.jpg 800w" sizes="(max-width:700px) 33vw, (max-width:900px) 50vw, 160px" decoding="async" alt="'+d.nome+'" width="400" height="300" onerror="this.closest(\'.cimg\').innerHTML=\'<div style=&quot;font-size:42px;display:flex;align-items:center;justify-content:center;height:100%&quot;>'+d.icon+'</div>\'"></picture></div><div class="cb"><b>'+d.nome+'</b><small>'+n+' produto'+(n>1?'s':'')+'</small></div></div>';});
  el.innerHTML=h;
  var fc=document.getElementById('footCats');if(fc)fc.innerHTML=DEPTS.filter(function(d){return CATALOG.some(function(p){return deptOf(p.k)===d.key;});}).slice(0,6).map(function(d){return '<a href="'+catHref(d.key)+'" onclick="setDept(\''+d.key+'\');return false">'+d.nome+'</a>';}).join('');
};
try{montarCatTiles();}catch(e){}
})();
(function(){try{
  var q=new URLSearchParams(location.search).get('orcar');if(!q)return;
  try{history.replaceState(null,'',location.pathname+location.hash);}catch(e){}
  setTimeout(function(){try{
    if(q!=='duvida'){
      var p=CATALOG.find(function(x){return String(x.c)===q;})||SEED.find(function(x){return String(x.c)===q;});
      if(p&&!CART.some(function(x){return x.c===p.c;})){CART.push({c:p.c,n:p.n,m:p.m,img:p.img,pub:p.pub,cnpj:p.cnpj,qty:1});salvarCart();atualizarCart();}
    }
    abrirContatoWA(q==='duvida'?'duvida':undefined);
  }catch(e){}},900);
}catch(e){}})();
}catch(e){try{console.error(e);}catch(_){}}

/* ==== growthJs ==== */
try{
(function(){
try{var q=new URLSearchParams(location.search);
 var ref=(q.get('ref')||'').replace(/[^A-Za-z0-9_-]/g,'').slice(0,24);if(ref){localStorage.setItem('sullab_ref',ref);localStorage.setItem('sullab_ref_ts',String(Date.now()));}
 var rts=parseInt(localStorage.getItem('sullab_ref_ts')||'0',10);if(rts&&Date.now()-rts>5184000000){localStorage.removeItem('sullab_ref');localStorage.removeItem('sullab_ref_ts');}
}catch(e){}
var _se=window.sullabEvent;
window.sullabEvent=function(t,e){e=e||{};try{var r=localStorage.getItem('sullab_ref');if(r&&!e.ref)e.ref=r;}catch(_){}return _se.call(this,t,e);};
function aplicarUrl(){
  /* 31/10/2026: ?carrinho=COD:QTD,... substitui o carrinho (o robô do WhatsApp depende disso); com &add=1 SOMA ao carrinho
     ("Comprar agora" das páginas de produto e de categoria). &nf=COD1,COD2 = itens que a equipe vai confirmar.
     Dispara add_to_cart (GA4) e AddToCart (Meta) com os itens do link; avisa quando nenhum código do link existe. */
  try{var q=new URLSearchParams(location.search),c=q.get('carrinho'),soma=q.get('add')==='1',nf=q.get('nf'),did=false,falt=[];
   if(nf){var lnf=nf.split(',').map(function(s){return decodeURIComponent(s||'').trim().slice(0,60);}).filter(Boolean).slice(0,30);if(lnf.length){try{sessionStorage.setItem('sullab_nf',JSON.stringify(lnf));}catch(e){}window.__nfConfirmar=lnf;did=true;}}
   if(c){
    var novos=[];c.split(',').forEach(function(par){var a=par.split(':'),cod=decodeURIComponent(a[0]||'').trim(),n=Math.max(1,Math.min(9999,parseInt(a[1])||1));if(!cod)return;var p=null;for(var i=0;i<CATALOG.length;i++){if(CATALOG[i].c===cod){p=CATALOG[i];break;}}if(p){var ex=novos.find(function(x){return x.c===cod;});if(ex)ex.qty+=n;else novos.push({c:p.c,n:p.n,m:p.m,img:p.img,pub:p.pub,cnpj:p.cnpj,qty:n});}else falt.push(cod);});
    if(novos.length){
     if(!soma)CART.length=0;
     novos.forEach(function(x){var ex=soma&&CART.find(function(y){return y.c===x.c;});if(ex)ex.qty=Math.min(99999,ex.qty+x.qty);else CART.push(x);});
     salvarCart();atualizarCart();did=true;
     try{var its=novos.map(function(x){return {item_id:x.c,item_name:x.n,item_brand:x.m,quantity:x.qty,price:precoItem(x)||0};}),val=Math.round(its.reduce(function(s,x){return s+x.price*x.quantity;},0)*100)/100;
      if(typeof gtag==='function')gtag('event','add_to_cart',{currency:'BRL',value:val,items:its,origem:soma?'link_comprar':'link_carrinho'});
      if(typeof fbq==='function')fbq('track','AddToCart',{currency:'BRL',value:val,content_ids:its.map(function(x){return x.item_id;}),content_type:'product',num_items:its.reduce(function(s,x){return s+x.quantity;},0)});}catch(e){}}
    if(falt.length){window.__linkFaltou=falt;did=true;try{sullabEvent('carrinho_link_invalido',{codigos:falt.slice(0,20)});}catch(e){}}}
   if(did){history.replaceState(null,'',location.pathname);abrirCarrinho();try{if(c)sullabEvent('carrinho_por_link',{soma:soma?1:0});}catch(e){}}
  }catch(e){}
}
window.__aplicarCarrinhoUrl=function(){if(window.__carrinhoUrlFeito)return;window.__carrinhoUrlFeito=true;aplicarUrl();};
window.addEventListener('load',function(){window.__aplicarCarrinhoUrl();});

var _ac2=window.atualizarCart;
window.atualizarCart=function(){_ac2.apply(this,arguments);
  try{var df=document.getElementById('df');if(!df||!CART.length)return;
   var f={};try{f=fichaSalva();}catch(e){}
   var tel=(f&&f.tel)||'';
   var box=document.createElement('div');box.className='sv';box.id='svBox';
   box.innerHTML='<b>Não vai fechar agora?</b> Guardamos seu carrinho e avisamos se o preço mudar ou o estoque estiver acabando.'+(tel?'<div style="margin-top:6px">Aviso no WhatsApp ativo: <b>'+tel+'</b></div>':'<div class="svr"><input id="svTel" inputmode="tel" placeholder="Seu WhatsApp com DDD"><button onclick="salvarCarrinhoTel()">Guardar</button></div>')+'<span class="svlk" onclick="copiarLinkCarrinho()">🔗 Copiar link deste carrinho</span><span id="svMsg" style="display:block;margin-top:5px;font-weight:700"></span>';
   df.appendChild(box);
   var tp=document.createElement('div');tp.className='trustp';tp.innerHTML='<a href="/sobre.html">🧾 NF-e em todo pedido</a><a href="/sobre.html">🛡️ Registro ANVISA quando exigido</a><a href="/sobre.html">🏆 40 anos de mercado</a><a href="/politica-de-entrega.html">🚚 Frota própria no RJ</a>';df.appendChild(tp);
  }catch(e){}
};
window.salvarCarrinhoTel=function(){var el=document.getElementById('svTel'),m=document.getElementById('svMsg');if(!el)return;var t=el.value.replace(/\D/g,'');
  if(t.length<10){if(m)m.textContent='Informe o WhatsApp com DDD.';return;}
  try{var f=fichaSalva();f.tel=t;localStorage.setItem('sullab_ficha',JSON.stringify(f));}catch(e){}
  try{sullabEvent('carrinho_salvo',{tel:t,total:Math.round(totalCart()*100)/100,qtd:CART.reduce(function(s,x){return s+x.qty;},0),itens:CART.map(function(x){return {cod:x.c,nome:x.n,q:x.qty};}),link:linkCarrinho()});}catch(e){}
  try{if(typeof gtag==='function')gtag('event','carrinho_salvo',{value:totalCart(),currency:'BRL'});}catch(e){}
  atualizarCart();var m2=document.getElementById('svMsg');if(m2)m2.textContent='Pronto! Carrinho guardado.';};
function linkCarrinho(){return location.origin+'/?carrinho='+CART.map(function(x){return encodeURIComponent(x.c)+':'+x.qty;}).join(',');}
window.linkCarrinho=linkCarrinho;  
window.copiarLinkCarrinho=function(){var l=linkCarrinho(),m=document.getElementById('svMsg');
  function ok(){if(m)m.textContent='Link copiado! Cole no WhatsApp ou e-mail.';}
  try{navigator.clipboard.writeText(l).then(ok,function(){prompt('Copie o link:',l);});}catch(e){prompt('Copie o link:',l);}};

var PREV_VISIT=0;try{PREV_VISIT=parseInt(localStorage.getItem('sullab_last')||'0',10);}catch(e){}
function retorno(){try{
  if(!CART.length)return;var last=PREV_VISIT,now=Date.now();
  if(last&&now-last>1800000&&!sessionStorage.getItem('retShown')){
    var n=CART.reduce(function(s,x){return s+x.qty;},0);var b=document.createElement('div');b.id='retBar';b.className='on';
    b.innerHTML='<span>Você deixou <b>'+n+(n===1?' item':' itens')+'</b> no carrinho. Finalize com <b>desconto no Pix</b>.</span><button class="go" onclick="abrirCarrinho();this.parentNode.remove()">Ver carrinho</button><button class="x" onclick="this.parentNode.remove()" aria-label="Fechar">×</button>';
    document.body.appendChild(b);sessionStorage.setItem('retShown','1');try{sullabEvent('carrinho_retorno',{});}catch(e){}}
 }catch(e){}}
window.addEventListener('load',function(){setTimeout(retorno,1200);});
function marca(){try{localStorage.setItem('sullab_last',String(Date.now()));}catch(e){}}
marca();
document.addEventListener('visibilitychange',function(){
  if(document.visibilityState!=='hidden')return;marca();
  try{if(!CART.length||sessionStorage.getItem('abSent'))return;var f=fichaSalva(),t=(f&&f.tel)||'';if(!t)return;
    sessionStorage.setItem('abSent','1');sullabEvent('carrinho_abandonado',{tel:t,total:Math.round(totalCart()*100)/100,itens:CART.map(function(x){return {cod:x.c,nome:x.n,q:x.qty};}),link:linkCarrinho()});
    roboPost('/site/carrinho-abandonado',{tel:t,nome:(f&&f.nome)||'',itens:CART.map(function(x){return {cod:x.c,q:x.qty};})});}catch(e){}
});

var _ap3=window.abrirProd;
window.abrirProd=function(i){_ap3.apply(this,arguments);try{var b=document.querySelector('#pmInner .pmb');if(b&&!b.querySelector('.trustp'))b.insertAdjacentHTML('beforeend','<div class="trustp"><a href="/sobre.html">🧾 NF-e em todo pedido</a><a href="/sobre.html">🛡️ Registro ANVISA quando exigido</a><a href="/sobre.html">🏆 Distribuidora há 40 anos</a><a href="/politica-de-entrega.html">🚚 Entrega com frota própria no RJ</a></div>');}catch(e){}};
})();
}catch(e){try{console.error(e);}catch(_){}}

/* ==== pedidoDireto ==== */
try{
(function(){
var MOTIVO='';
var UNID='(?:x|cx|cxs|caixas?|un|und|unid|unidades?|pct|pcts|pc|pcs|pacotes?|frascos?|fr|kits?|racks?|rolos?|potes?|galao|galoes|litros?|testes?)';
var RX_QI=new RegExp('^\\s*(\\d{1,4})(?![\\d.,])\\s*'+UNID+'?\\.?\\s*(?:de\\s+|-\\s*|–\\s*|:\\s*)?([A-Za-zÀ-ú].+)$','i');
var RX_QF=new RegExp('^(.+?)\\s+(?:-|–|:|x|qtd\\.?|quantidade)?\\s*(\\d{1,5})\\s*'+UNID+'?\\.?\\s*$','i');
function _nrm(t){return semAcento(t).replace(/(\d),(\d)/g,'$1.$2').replace(/(\d)\s+(ml|l|mm|cm|g|mg|kg|ul|µl|un)\b/g,'$1$2');}
function _linhas(txt){
  return String(txt||'').split(/\n|;/).map(function(l){return l.replace(/^[\s•\-\*\d]+[\.\)]\s+/,'').trim();}).filter(function(l){return l.length>=2;}).slice(0,60).map(function(l){
    var q=1,t=l,m=l.match(RX_QI);
    if(m&&!/^\s*\d+[\.,]?\d*\s*(ml|l|mm|g|mg|cm|ul)\b/i.test(l)){q=parseInt(m[1],10);t=m[2];}
    else{m=l.match(RX_QF);if(m&&!/(\d)\s*(ml|l|mm|g|mg|cm)$/i.test(l)){t=m[1];q=parseInt(m[2],10);}}
    return {orig:l,termo:t.trim(),q:Math.max(1,Math.min(9999,q||1))};
  });
}
function _cands(termo){
  /* 31/10/2026: mesma busca da loja (sinônimos, plurais, código sem espaço/hífen, 1 erro de digitação) */
  var r=buscaPrep(String(termo||'').replace(/\b(x|cx|cxs|caixa|caixas|un|und|unid|pct|pc)\b|\bc\//gi,' '));
  if(!r.g.length)return [];
  var out=[];
  CATALOG.forEach(function(p){
    var F=_bCampos(p),nm=F.n+' '+F.m+' '+F.c,sc;
    if(/\d/.test(r.qc)&&r.qc.length>=3&&(F.cc===r.qc||F.cc.indexOf(r.qc)===0||r.g.some(function(g){return g.c===F.cc;})))sc=2;
    else{var hit=0;r.g.forEach(function(g){var h=_bTem(nm,g);if(h)hit+=h;else if(_bTem(F.kw,g))hit+=0.4;});sc=hit/r.g.length;}
    if(sc>=0.5){sc+=(precoDe(p)>0?0.05:0);out.push({p:p,s:sc});}
  });
  out.sort(function(a,b){return b.s-a.s||a.p.n.length-b.p.n.length;});
  return out.slice(0,4);
}
function _modal(){
  var m=document.getElementById('pdm');
  if(!m){m=document.createElement('div');m.className='cko';m.id='pdm';m.innerHTML='<div class="ckb"><button class="ckx" onclick="fecharPd()">&times;</button><div id="pdb"></div></div>';
    m.addEventListener('click',function(e){if(e.target===m)fecharPd();});document.body.appendChild(m);}
  return m;
}
window.fecharPd=function(){var m=document.getElementById('pdm');if(m)m.classList.remove('on');};
function _esc(s){return String(s).replace(/[&<>"]/g,function(c){return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c];});}
var _ult=[];
function mostrarLista(txt){
  ensureKw(function(){
    var ls=_linhas(txt);_ult=ls;
    var ach=0,h='<h3>Encontramos estes produtos</h3><div class="sub">Confira cada linha e ajuste o produto ou a quantidade. <b>Quantidade = nº de embalagens</b> (caixa, rack, frasco).</div>';
    ls.forEach(function(l,i){
      var c=_cands(l.termo);l.c=c;
      if(c.length){ach++;
        h+='<div class="pdl ok"><div class="pdq">Você escreveu: <b>'+_esc(l.orig)+'</b></div><div class="pdr"><select id="pds'+i+'">'+
          c.map(function(x,j){var pr=precoDe(x.p);return '<option value="'+j+'"'+(j===0&&x.s>=0.99?' selected':'')+'>'+_esc(x.p.n)+' · cód. '+_esc(x.p.c)+(pr?' · '+brl(pr):' · sob consulta')+'</option>';}).join('')+
          '<option value="-1"'+(c[0].s<0.99?' selected':'')+'>Nenhum destes</option></select><input id="pdq'+i+'" inputmode="numeric" value="'+l.q+'" aria-label="Quantidade"></div><div class="pdn" id="pdn'+i+'"></div></div>';
      }else{
        h+='<div class="pdl no"><div class="pdq">Você escreveu: <b>'+_esc(l.orig)+'</b></div><div class="pdno">Não temos esse item no site. <a onclick="fecharPd();buscarTermo(\''+_esc(l.termo).replace(/'/g,'')+'\')">Buscar com outro nome</a></div></div>';
      }
    });
    var falta=ls.length-ach;
    h+='<div class="pdtot">'+ach+' de '+ls.length+(ls.length===1?' linha encontrada':' linhas encontradas')+' no site.</div>'+
      '<button class="ckpay" onclick="pdAdicionar()">Adicionar ao carrinho e finalizar &rarr;</button>'+
      (falta?'<button class="ckwa" onclick="pdAvisarEquipe()">Preciso dos itens não encontrados: avisar a equipe</button>':'')+
      '<button class="ckwa" onclick="fecharPd();abrirListaOrcamento()">Voltar e editar a lista</button>';
    _modal();document.getElementById('pdb').innerHTML=h;document.getElementById('pdm').classList.add('on');
    ls.forEach(function(l,i){var s=document.getElementById('pds'+i);if(!s)return;var up=function(){var j=parseInt(s.value,10),d=document.getElementById('pdn'+i),x=l.c[j];if(d)d.innerHTML=x?('✔ '+_esc(x.p.n)+' <b>'+(precoDe(x.p)?brl(precoDe(x.p)):'sob consulta')+'</b>'):'Item fora do pedido';var b=s.closest('.pdl');if(b){b.className='pdl '+(x?'ok':'no');}};s.addEventListener('change',up);up();});
    try{if(typeof gtag==='function')gtag('event','lista_colada',{linhas:ls.length,encontradas:ach});}catch(e){}
    try{sullabEvent('lista_colada',{linhas:ls.length,encontradas:ach,lista:String(txt).slice(0,1500)});}catch(e){}
  });
}
window.pdAdicionar=function(){
  var n=0;
  _ult.forEach(function(l,i){var s=document.getElementById('pds'+i);if(!s||!l.c)return;var j=parseInt(s.value,10);if(j<0||!l.c[j])return;
    var q=parseInt(String((document.getElementById('pdq'+i)||{}).value||'1').replace(/\D/g,''),10)||1;addCodigo(l.c[j].p.c,Math.min(9999,q));n++;});
  fecharPd();
  if(!n){abrirCarrinho();return;}
  var semPreco=CART.some(function(x){return !precoItem(x);});
  if(!semPreco&&totalCart()>0)abrirCheckout();else abrirCarrinho();
};
window.pdAvisarEquipe=function(){
  var nao=_ult.filter(function(l,i){var s=document.getElementById('pds'+i);return !l.c||!l.c.length||(s&&s.value==='-1');}).map(function(l){return l.q+'x '+l.termo;});
  fecharPd();
  abrirContatoWA('equipe',nao.join('\n'));
};
function confirmacao(pid,f,txt){
  var h='<div class="pdok">✅</div><h3 style="text-align:center">Pedido '+pid+' recebido</h3>'+
    '<div class="sub" style="text-align:center;line-height:1.5">'+txt+'<br>Enviamos para o WhatsApp <b>'+_esc(f.tel||'')+'</b> e o e-mail <b>'+_esc(f.email||'')+'</b>, em horário comercial.</div>'+
    '<button class="ckpay" onclick="fecharPd()">Continuar comprando</button>';
  _modal();document.getElementById('pdb').innerHTML=h;document.getElementById('pdm').classList.add('on');
}
window.registrarPedidoEquipe=function(f,origem){
  var pid='SLB-'+Date.now();window._pedAtual=pid;
  f.lista=String(f.lista||'');
  var cb=function(fr){
    if(fr){freteSelLoja=fr.gratis?0:(parseFloat(fr.preco)||0);freteLabelLoja=fr.nome;freteSelPrazo=fr.prazo||0;freteMeta={pesoKg:fr.peso,pacotes:fr.pacotes};}
    var bak=CART;if(origem==='equipe'){CART=[];}
    try{dispararPedido('pedido_wa',origem||'site',f,pid);}finally{CART=bak;}
    try{fecharContatoWA();}catch(e){}try{fecharCheckout();}catch(e){}
    var txt=origem==='refrigerado'?'Vamos verificar uma entrega rápida para o produto refrigerado e mandar o <b>link de pagamento</b>.':origem==='cpf'?'Vamos conferir o pedido e mandar o <b>link de pagamento</b> com o frete.'
      :(origem==='equipe'?'Vamos procurar os itens e mandar o <b>link do carrinho pronto para pagar</b>.'
      :'Vamos confirmar os itens sob consulta e mandar o <b>link de pagamento</b> com o frete.');
    confirmacao(pid,f,txt);
  };
  if(origem==='equipe'){cb(null);return;}
  try{_freteEstimado(f.cep,cb);}catch(e){cb(null);}
};
var _abrir=window.abrirContatoWA;
window.abrirContatoWA=function(motivo,texto){
  MOTIVO=motivo||'';
  _abrir(motivo==='equipe'?undefined:motivo,texto);
  var t=function(id,v){var e=document.getElementById(id);if(e)e.innerHTML=v;};
  if(MOTIVO==='duvida'){
    t('waqTit','Falar com a SULLAB');t('waqSub','Dúvida técnica ou sobre um pedido? Mandamos sua mensagem pelo WhatsApp. <b>Para comprar</b>, use o carrinho ou cole sua lista: é mais rápido.');
    t('waListaLb','Sua mensagem');t('waqBtn','Enviar pelo WhatsApp &rarr;');
  }else if(MOTIVO==='equipe'){
    t('waqTit','Avisar a equipe');t('waqSub','Informe seus dados: procuramos os itens e mandamos o <b>link do carrinho pronto para pagar</b>.');
    t('waListaLb','Itens que você precisa');t('waqBtn','Enviar para a equipe &rarr;');
  }else{
    var vazio=!CART.length;
    t('waqTit',vazio?'Monte seu pedido':'Finalize seu pedido');
    t('waListaLb',vazio?'Sua lista de compras (um item por linha)':'Mais itens? Cole aqui (opcional)');
    t('waqBtn',vazio?'Montar meu carrinho &rarr;':'Continuar &rarr;');
  }
};
function _salvarParcial(){try{var f=fichaSalva(),m={nome:'waNome',tel:'waTel',cep:'waCep',doc:'waDoc',email:'waEmail',log:'waLog',num:'waNum',compl:'waCompl',bairro:'waBairro',cidade:'waCidade',uf:'waUf'},k;
  for(k in m){var v=val(m[k]);if(v)f[k]=(k==='uf'?v.toUpperCase():v);}f.doct=WA_DOCT;localStorage.setItem('sullab_ficha',JSON.stringify(f));}catch(e){}}
window.confirmarContatoWA=function(){
  if(MOTIVO==='duvida'){var f0=_waLer(false);if(f0)_enviarOrcamentoCom(f0,false);return;}
  if(MOTIVO==='equipe'){var fe=_waLer(false);if(fe)registrarPedidoEquipe(fe,'equipe');return;}
  var lista=val('waLista');
  if(lista.length>=3){_salvarParcial();fecharContatoWA();mostrarLista(lista);return;}
  if(!CART.length)return waqErro('Cole pelo menos um item da sua lista (um por linha).');
  var semPreco=CART.some(function(x){return !precoItem(x);});
  if(!semPreco&&totalCart()>0){_salvarParcial();fecharContatoWA();abrirCheckout();return;}
  var f=_waLer(false);if(f)registrarPedidoEquipe(f,'consulta');
};
window.enviarPedidoCPF=function(){
  var f=coletarFicha();
  if(soDig(f.doc).length!==11)return ckErro('Informe um CPF válido.');
  if(!f.nome)return ckErro('Informe seu nome completo.');
  if(!/.+@.+\..+/.test(f.email))return ckErro('Informe um e-mail válido.');
  if(soDig(f.tel).length<10)return ckErro('Informe um WhatsApp com DDD.');
  if(soDig(f.cep).length!==8||!f.num||!f.log||!f.cidade)return ckErro('Informe o endereço completo com CEP e número.');
  try{localStorage.setItem('sullab_ficha',JSON.stringify(f));}catch(e){}
  f.lista='';registrarPedidoEquipe(f,'cpf');
};
var _ck=window.ckModo;
window.ckModo=function(){var d=DOCT;DOCT='cnpj';try{_ck.apply(this,arguments);}finally{DOCT=d;}};
var _ac=window.atualizarCart;
window.atualizarCart=function(){_ac.apply(this,arguments);
  try{var a=document.querySelector('#df a.wbtn[onclick="enviarOrcamento()"]');if(!a)return;
    var semPreco=CART.some(function(x){return !precoItem(x);});
    if(semPreco){[].forEach.call(document.querySelectorAll('#df .note'),function(nt){if(/sob consulta/.test(nt.textContent))nt.textContent='Alguns itens são sob consulta: envie o pedido e mandamos o link de pagamento.';});}
    if(!semPreco&&totalCart()>0)a.remove();
    else{a.textContent='📄 Enviar pedido (itens sob consulta)';a.style.cssText='background:var(--navy,#1f3c73);color:#fff';}
  }catch(e){}
};
var _rd=window.render;
window.render=function(){_rd.apply(this,arguments);
  try{var e=document.querySelector('#grid .empty');if(e&&!e.classList.contains('bvz')&&/WhatsApp/i.test(e.innerHTML)){var q=(FILTRO&&FILTRO.busca)||'';
    e.innerHTML='Nenhum produto encontrado'+(q?' para “'+_esc(q)+'”':'')+'.<br>Tente outro termo ou <a class="lk" style="color:var(--navy-l);cursor:pointer" onclick="abrirContatoWA(\'equipe\','+JSON.stringify(q).replace(/"/g,'&quot;')+')">avise a equipe que você precisa</a>.';}}catch(x){}
};
var _cb=window._cartBuscarGo;
window._cartBuscarGo=function(){_cb.apply(this,arguments);
  setTimeout(function(){try{var n=document.querySelector('#cartRes .none');if(n&&/WhatsApp/i.test(n.innerHTML)){var q=val('cartSearch');
    n.innerHTML='Nenhum produto encontrado para “'+_esc(q)+'”.<br><a class="lk" style="color:var(--navy-l,#1f5fa8);cursor:pointer;font-weight:700" onclick="abrirContatoWA(\'equipe\','+JSON.stringify(q).replace(/"/g,'&quot;')+')">Avisar a equipe que preciso</a>';}}catch(x){}},400);
};
function _listaUrl(){try{var t=new URLSearchParams(location.search).get('lista');if(!t)return;
  history.replaceState(null,'',location.pathname);mostrarLista(_nrmMed(t));try{sullabEvent('lista_por_link',{lista:String(t).slice(0,500)});}catch(e){}}catch(e){}}
if(document.readyState==='complete')setTimeout(_listaUrl,600);else window.addEventListener('load',function(){setTimeout(_listaUrl,800);});
try{render();atualizarCart();}catch(e){}
})();
}catch(e){try{console.error(e);}catch(_){}}

/* ==== freteRefrigerado ==== */
try{
(function(){
var PRAZO_MAX=4;  
var UF_BLOQ=/^(AC|AL|AM|AP|MT|PA|PB|PI|RO|RR|SE|TO)$/;
function ufDoCep(c){c=parseInt(String(c||'').replace(/\D/g,'').slice(0,5),10);if(!c)return '';
  var T=[[1000,19999,'SP'],[20000,28999,'RJ'],[29000,29999,'ES'],[30000,39999,'MG'],[40000,48999,'BA'],[49000,49999,'SE'],[50000,56999,'PE'],[57000,57999,'AL'],[58000,58999,'PB'],[59000,59999,'RN'],[60000,63999,'CE'],[64000,64999,'PI'],[65000,65999,'MA'],[66000,68899,'PA'],[68900,68999,'AP'],[69000,69299,'AM'],[69300,69399,'RR'],[69400,69899,'AM'],[69900,69999,'AC'],[70000,72799,'DF'],[72800,72999,'GO'],[73000,73699,'DF'],[73700,76799,'GO'],[76800,76999,'RO'],[77000,77999,'TO'],[78000,78899,'MT'],[79000,79999,'MS'],[80000,87999,'PR'],[88000,89999,'SC'],[90000,99999,'RS']];
  for(var i=0;i<T.length;i++)if(c>=T[i][0]&&c<=T[i][1])return T[i][2];return '';}
var RX_SIM=/placa|biplaca|Ø\s?\d|cromo|caldo|[aá]gar|meio de|newp \d|plasma|egg yolk|gema|sangue de carneiro|suplemento vx|rugai|meio sim|urease|epm|mili|kit para (enterob|micob|confirma)|mini kit/i, RX_NAO=/cult pack|stuart|swab|colora|corante|gram|ziehl|papanicolau|lugol|tamp[aã]o|reativo|al[cç]a|agulha/i;
var EXTRA={'052000':1};
var EBRAM_AMB=/^(21910|21805|23805|23920|23930|23940|22805|740|741|742|EBIO.*|EB\d{4}|EBCOAG.*)$/;  
var ISOPOR=0;  
var NP_REF={"PA242":1,"PA246":1,"PA149":1,"PA150":1,"PA352":1,"PA151":1,"PA152":1,"PA153":1,"PA114":1,"PA121":1,"PA120":1,"PA384":1,"PA42":1,"PA43":1,"PA44":1,"PA45":1,"PA46":1,"PA47":1,"PA48":1,"PA49":1,"PA50":1,"PA18":1,"PA28":1,"PA312":1,"PA340":1,"PA347":1,"PA07":1,"PA13":1,"PA14":1,"PA16":1,"PA24":1,"PA25":1,"PA319":1,"PA321":1,"PA323":1,"PA325":1,"PA328":1,"PA329":1,"PA330":1,"PA331":1,"PA344":1,"PA37":1,"PA39":1,"PA02":1,"PA03":1,"PA406":1,"PA04":1,"PA06":1,"PA08":1,"PA09":1,"PA387":1,"PA10":1,"PA11":1,"PA345":1,"PA12":1,"PA15":1,"PA17":1,"PA19":1,"PA341":1,"PA20":1,"PA346":1,"PA22":1,"PA26":1,"PA23":1,"PA31":1,"PA27":1,"PA32":1,"PA29":1,"PA30":1,"PA380":1,"PA33":1,"PA34":1,"PA35":1,"PA36":1,"PA38":1,"PA40":1,"PA41":1,"PA395":1,"PA308":1,"PA318":1,"PA320":1,"PA322":1,"PA324":1,"PA348":1,"PA349":1,"PA350":1,"PA333":1,"PA334":1,"PA335":1,"PA338":1,"PA339":1,"PA313":1,"PA314":1,"PA315":1,"PA316":1,"PA54":1,"PA58":1,"PA60":1,"PA61":1,"PA63":1,"PA66":1,"PA69":1,"PA75":1,"PA89":1,"PA91":1,"PA94":1,"PA416":1,"PA355":1,"PA356":1,"PA363":1,"PA365":1,"PA368":1,"PA369":1,"PA407":1,"PA248":1,"PA249":1,"PA250":1,"PA251":1,"PA252":1,"PA253":1,"PA254":1,"PA255":1,"PA256":1,"PA257":1,"PA258":1,"PA259":1,"PA260":1,"PA261":1,"PA262":1,"PA263":1,"PA264":1,"PA265":1,"PA266":1,"PA231":1,"PA311":1,"PA394":1,"PA154":1,"PA155":1,"PA158":1,"PA159":1};
var NP_AMB={"PA377":1,"PA163":1,"PA164":1,"PA165":1,"PA166":1,"PA167":1,"PA168":1,"PA117":1,"PA124":1,"PA118":1,"PA122":1,"PA115":1,"PA116":1,"PA123":1,"PA100":1,"PA101":1,"PA102":1,"PA104":1,"PA106":1,"PA110":1,"PA112":1,"PA295":1,"PA109":1,"PA99":1,"PA411":1,"PA125":1,"PA126":1,"PA127":1,"PA128":1,"PA129":1,"PA130":1,"PA131":1,"PA132":1,"PA133":1,"PA134":1,"PA136":1,"PA137":1,"PA138":1,"PA139":1,"PA140":1,"PA141":1,"PA142":1,"PA143":1,"PA146":1,"PA147":1,"PA148":1,"PA374":1,"PA53":1,"PA55":1,"PA57":1,"PA64":1,"PA65":1,"PA67":1,"PA68":1,"PA70":1,"PA71":1,"PA72":1,"PA73":1,"PA76":1,"PA77":1,"PA78":1,"PA79":1,"PA80":1,"PA81":1,"PA82":1,"PA84":1,"PA85":1,"PA86":1,"PA87":1,"PA386":1,"PA88":1,"PA90":1,"PA93":1,"PA375":1,"PA52":1,"PA56":1,"PA59":1,"PA74":1,"PA83":1,"PA96":1,"PA92":1,"PA402":1,"PA410":1,"PA161":1,"PA354":1,"PA376":1,"PA382":1,"PA162":1,"PA353":1,"PA95":1};
var NP_TRANSP_AMB={"PA91":1,"PA315":1,"PA231":1};
function refrigCod(c){
  if(NP_TRANSP_AMB[c])return false;
  if(EXTRA[c])return true;
  if(NP_REF[c])return true;
  if(NP_AMB[c])return false;
  var p=null;for(var i=0;i<CATALOG.length;i++){if(CATALOG[i].c===c){p=CATALOG[i];break;}}
  if(!p)return false;
  if(/ebram/i.test(p.m||'')&&!EBRAM_AMB.test(c))return true;
  return /newprov/i.test(p.m||'')&&RX_SIM.test(p.n)&&!RX_NAO.test(p.n);
}
window.itemRefrigerado=refrigCod;
window.cartRefrigerado=function(){return CART.some(function(x){return refrigCod(String(x.c));});};
window._refrigSemOpcao=false;
var _f=window.fetch;
window.fetch=function(u,o){
  try{
    if(String(u).indexOf('/frete2')>=0&&o&&o.body){
      var b=JSON.parse(o.body),its=(b&&b.itens)||[],uf=ufDoCep(b&&b.cep);
      if(its.some(function(i){return refrigCod(String(i.c));})){
        return _f.apply(this,arguments).then(function(r){return r.json().then(function(d){
          d=d||{};var ops=UF_BLOQ.test(uf)?[]:(d.opcoes||[]).filter(function(x){return (parseInt(x.prazo)||99)<=PRAZO_MAX&&(uf==='RJ'||!/jet|j&t/i.test(String(x.nome||'')))&&!/latam/i.test(String(x.nome||'')); });
          if(!d.refrigSrv)ops=ops.map(function(x){var y=Object.assign({},x);if(y.gratis){y.preco=y.economia||0;delete y.gratis;delete y.economia;}y.preco=Math.round(((+y.preco||0)+ISOPOR)*100)/100;return y;});
          if(d.gratis&&!d.refrigSrv){d.gratis={ativo:false,falta:null,sugestoes:[]};}
          ops.sort(function(a,c){return (a.prazo-c.prazo)||(a.preco-c.preco);});
          d.opcoes=ops.slice(0,1);d.refrigerado=true;
          window._refrigSemOpcao=!d.opcoes.length;
          if(!d.opcoes.length&&d.gratis){d.gratis.ativo=false;d.gratis.falta=null;}
          return new Response(JSON.stringify(d),{status:200,headers:{'Content-Type':'application/json'}});
        });});
      }
    }
  }catch(e){}
  return _f.apply(this,arguments);
};
var AVISO='<div id="refrigAviso" style="background:#eef6ff;border:1px solid #c9ddf5;color:#1f3c73;border-radius:9px;padding:8px 10px;font-size:12px;margin:6px 0;line-height:1.4">❄️ <b>Produto refrigerado:</b> vai pela transportadora mais rápida, com entrega em até 3 dias úteis, e é postado no início da semana para não ficar parado no fim de semana.</div>';
function nomesRefrig(){return CART.filter(function(x){return refrigCod(String(x.c));}).map(function(x){return String(x.n||x.c).slice(0,60);});}
window.refrigSemMsg=function(){var n=nomesRefrig();
  return '<div style="background:#fff6e5;border:1px solid #f1d7a6;color:#7a5a12;border-radius:9px;padding:8px 10px;font-size:12px;line-height:1.45">❄️ <b>Não entregamos produto refrigerado neste CEP.</b><br>Placas e meios prontos precisam chegar refrigerados em até 3 dias úteis, e para a sua região o prazo de entrega passa disso.'+(n.length?'<br>Item refrigerado no carrinho: <b>'+n.join('</b>, <b>')+'</b>.':'')+'<br>Os demais produtos (não refrigerados) podemos enviar normalmente: é só remover o item refrigerado do carrinho.</div>';};
var SEM='<div id="refrigSem" style="margin:6px 0">'+'</div>';
function marcar(){
  try{
    var box=document.getElementById('freteBox');if(!box)return;
    var a=document.getElementById('refrigAviso'),s=document.getElementById('refrigSem');
    var bt0=document.getElementById('ckPayBtn');
    if(!cartRefrigerado()){if(a)a.remove();if(s)s.remove();if(bt0&&bt0.disabled&&/refrigerada/.test(bt0.textContent)){bt0.disabled=false;bt0.style.opacity='';bt0.textContent='Pagar agora →';}return;}
    if(!a)box.insertAdjacentHTML('afterbegin',AVISO);
    var opt=document.getElementById('freteOpts'),calc=opt&&/Informe o CEP|Calculando/.test(opt.innerText||'');
    var sem=window._refrigSemOpcao&&!calc&&!(opt&&opt.querySelector('label'));
    if(sem&&!s){box.insertAdjacentHTML('beforeend',SEM);s=document.getElementById('refrigSem');if(s)s.innerHTML=refrigSemMsg();}else if(!sem&&s)s.remove();
    if(sem&&opt){[].slice.call(opt.querySelectorAll('div')).forEach(function(d){if(/confirmado no checkout/.test(d.textContent))d.remove();});}
    var btn=document.getElementById('ckPayBtn');
    if(btn){if(sem){btn.disabled=true;btn.style.opacity='.5';btn.textContent='Sem entrega refrigerada para este CEP';}
      else if(btn.disabled&&/refrigerada/.test(btn.textContent)){btn.disabled=false;btn.style.opacity='';btn.textContent='Pagar agora →';}}
  }catch(e){}
}
setInterval(function(){var c=document.getElementById('cko');if(c&&c.classList.contains('on'))marcar();},600);
var _pg=window.pagarMP;
window.pagarMP=function(){
  if(cartRefrigerado()){
    if(window._refrigSemOpcao)return ckErro('Não entregamos produto refrigerado neste CEP: ele precisa chegar em até 3 dias úteis e, para a sua região, o prazo passa disso. Remova o item refrigerado para seguir com os demais.');
    if(!freteSelLoja&&!(freteMeta&&freteMeta.gratis))return ckErro('Produto refrigerado: calcule o frete pelo CEP antes de pagar.');
  }
  return _pg.apply(this,arguments);
};
})();
}catch(e){try{console.error(e);}catch(_){}}

/* ==== freteObrigatorio ==== */
try{
(function(){
var _pg=window.pagarMP;
window.pagarMP=function(){
  if(!freteValido()){
    if(soDig(val('ckCep')).length===8){try{cotarFreteLoja();}catch(e){}return ckErro('Calculando o frete para o seu CEP: escolha a transportadora e toque em pagar de novo.');}
    return ckErro('Informe o CEP para calcular o frete antes de pagar.');
  }
  return _pg.apply(this,arguments);
};
var _ult='';
function trava(){
  var b=document.getElementById('ckPayBtn');if(!b)return;
  var online=/pagarMP/.test(b.getAttribute('onclick')||'');
  if(!online||/refrigerada/.test(b.textContent)){if(b.dataset.fr){delete b.dataset.fr;b.disabled=false;b.style.opacity='';}return;}
  var ok=freteValido(),opt=document.getElementById('freteOpts'),calc=opt&&/Calculando/.test(opt.innerText||'');
  if(ok){if(b.dataset.fr){delete b.dataset.fr;b.disabled=false;b.style.opacity='';b.textContent='Pagar agora →';}return;}
  var t=calc?'Calculando o frete…':(soDig(val('ckCep')).length===8?'Escolha o frete para pagar':'Informe o CEP para calcular o frete');
  if(b.textContent==='Abrindo Mercado Pago…')return;
  b.dataset.fr='1';b.disabled=true;b.style.opacity='.55';if(b.textContent!==t)b.textContent=t;
}
window._travaFrete=trava;window._freteReset=function(){_ult='';};
setInterval(function(){try{var c=document.getElementById('cko');if(!c||!c.classList.contains('on')){_ult='';return;}var cep=soDig(val('ckCep'));
  var k=chaveFrete();
  if(cep.length===8&&k!==_ult&&document.getElementById('freteOpts')){_ult=k;if(!freteValido())cotarFreteLoja();}
  else if(cep.length!==8&&_freteOk){zerarFrete();ckTotais();var o=document.getElementById('freteOpts');if(o)o.innerHTML='';}
  trava();}catch(e){}},500);
})();
}catch(e){try{console.error(e);}catch(_){}}

/* ==== bloco ==== */
try{
try{if(window.__aplicarCarrinhoUrl)window.__aplicarCarrinhoUrl();}catch(e){}
}catch(e){try{console.error(e);}catch(_){}}

/* ==== bloco ==== */
try{
 
(function(){try{var q=new URLSearchParams(location.search),n=(q.get('pedido')||'').replace(/[^A-Za-z0-9-]/g,'').slice(0,40);if(!n)return;var em=(q.get('email')||'').trim().slice(0,120);
 try{history.replaceState(null,'',location.pathname);}catch(e){}
 abrirRastreio();var a=document.getElementById('rastNum');if(a)a.value=n;var b=document.getElementById('rastChave');if(b&&em)b.value=em;
 if(b&&b.value){lookupRastreio();}else if(b){setTimeout(function(){try{b.focus();}catch(e){}},300);}
}catch(e){}})();
}catch(e){try{console.error(e);}catch(_){}}

/* ==== bloco ==== */
try{
(function(){
 /* 30/10/2026 (PageSpeed: "reflow forçado"): medir tudo antes e só depois mexer no DOM */
 function medir(el){if(el.__hs||el.closest('.drawer,.pmodal,.cko,#retBar'))return null;
  var cs=getComputedStyle(el);if(!/(auto|scroll)/.test(cs.overflowX))return null;if(el.scrollWidth<=el.clientWidth+8)return null;
  return {el:el,m:cs.marginTop+' '+cs.marginRight+' '+cs.marginBottom+' '+cs.marginLeft,sm:el.clientHeight<60};}
 function setup(x){var el=x.el;if(el.__hs)return;
  el.__hs=1;var w=document.createElement('div');w.className='hsw';
  w.style.margin=x.m;el.style.margin='0';
  el.parentNode.insertBefore(w,el);w.appendChild(el);
  var sm=x.sm;
  var l=document.createElement('button'),r=document.createElement('button');
  l.type=r.type='button';l.className='hsA l off'+(sm?' sm':'');r.className='hsA r hint'+(sm?' sm':'');l.innerHTML='‹';r.innerHTML='›';
  l.setAttribute('aria-label','Rolar para a esquerda');r.setAttribute('aria-label','Rolar para a direita');
  l.onclick=function(){el.scrollBy({left:-el.clientWidth*.8,behavior:'smooth'});};
  r.onclick=function(){el.scrollBy({left:el.clientWidth*.8,behavior:'smooth'});};
  w.appendChild(l);w.appendChild(r);
  var _t=null;  /* altura das setas: mede uma vez só */
  function ler(){var x=el.scrollLeft,max=el.scrollWidth-el.clientWidth-4,t=_t;if(t===null){t=0;var im=el.querySelector('.ofi,.ph');if(im){var a=im.getBoundingClientRect(),b=w.getBoundingClientRect();if(a.height)t=Math.round(a.top-b.top+a.height/2);}if(t)_t=t;}
   return function(){l.classList.toggle('off',x<4);r.classList.toggle('off',x>=max);if(t>10&&_t!==-1){l.style.top=r.style.top=t+'px';_t=-1;}};}
  function upd(){ler()();}
  el.addEventListener('scroll',function(){requestAnimationFrame(upd);},{passive:true});
  return ler;
  el.addEventListener('touchstart',function(){w.classList.add('used');},{passive:true});
 }
 var SEL='.deptbar .wrap,.trust .wrap,.popq,.bsel,.ofgrid,.mRowS';  /* os únicos com overflow-x:auto no CSS fora de carrinho/modais */
 function scan(){try{
  /* 31/10/2026 (PageSpeed: TBT): não medir fileiras longe da tela — ler scrollWidth dentro de um .mRow com content-visibility:auto
     obriga o navegador a montar a fileira inteira (12 cards). Mede só o que está a até 600 px da tela; o resto entra quando se aproxima (IO abaixo). */
  var vh=window.innerHeight||800;
  var L=[].slice.call(document.querySelectorAll(SEL)).filter(function(el){if(!el.children.length||el.__hs)return false;
    var r=el.closest('.mRow');if(!r)return true;var b=r.getBoundingClientRect();return b.bottom>-200&&b.top<vh+600;});
  var X=L.map(medir).filter(Boolean);            /* só leituras */
  var F=X.map(setup);                            /* só escritas */
  function passo(){var E=F.map(function(f){return f();});E.forEach(function(e){e();});}  /* todas as leituras, depois todas as escritas */
  if(F.length)requestAnimationFrame(function(){passo();setTimeout(function(){requestAnimationFrame(passo);},800);});
 }catch(e){}}
 var _sT=null;function agenda(ms){clearTimeout(_sT);_sT=setTimeout(function(){(window.requestIdleCallback||function(f){setTimeout(f,1);})(scan,{timeout:800});},ms||0);}
 window.hsScan=function(){agenda(60);};
 window.addEventListener('load',function(){agenda(0);setTimeout(function(){agenda(0);},3500);});
 /* fileiras que se aproximam da tela ganham as setas na hora certa */
 try{if('IntersectionObserver' in window){var _io=new IntersectionObserver(function(es){var any=false;es.forEach(function(e){if(e.isIntersecting){any=true;_io.unobserve(e.target);}});if(any)agenda(60);},{rootMargin:'600px 0px'});
  var _obs=function(){[].slice.call(document.querySelectorAll('.mRow')).forEach(function(r){if(!r.__io){r.__io=1;_io.observe(r);}});};
  window.addEventListener('load',_obs);var _hs0=window.hsScan;window.hsScan=function(){try{_obs();}catch(e){}_hs0();};}}catch(e){}
 window.addEventListener('resize',function(){agenda(300);});
})();
(function(){var _ac=window.atualizarCart;window.atualizarCart=function(){_ac.apply(this,arguments);
 try{if(!matchMedia('(max-width:700px)').matches)return;var dl=document.querySelector('.drawer .dleft'),df=document.getElementById('df');if(!dl||!df)return;
  [].slice.call(dl.children).forEach(function(n){if(n.classList.contains('sv')||n.classList.contains('trustp'))n.remove();});
  df.querySelectorAll('.sv,.trustp').forEach(function(n){dl.appendChild(n);});
 }catch(e){}};})();
setInterval(function(){var b=document.getElementById('retBar');if(b&&!b.__t){b.__t=setTimeout(function(){if(b.parentNode)b.remove();},12000);}},1000);
}catch(e){try{console.error(e);}catch(_){}}

/* ==== bloco ==== */
try{
(function(){
 var ROWS=[
  ['Tubos de coleta a vácuo',['tubo'],'tubo'],
  ['Agulhas, lancetas e coleta',['agulha','lanceta','scalp','seringa'],'agulha'],
  ['Meios de cultura prontos em placa',['meio'],'meio',function(p){return /placa/i.test(p.n);}],
  ['Meios de cultura em frasco e tubo',['meio'],'meio',function(p){return !/placa/i.test(p.n);}],
  ['Microbiologia: discos e corantes',['micro'],'micro'],
  ['Coletores de amostra',['coletoram'],'coletoram'],
  ['Reagentes de bioquímica',['bioq'],'bioq'],
  ['Hematologia e coagulação',['hemat'],'hemat'],
  ['Sorologia, controles e calibradores',['sorol','controle'],'sorol'],
  ['Curativos, gaze e algodão',['curativo'],'curativo'],
  ['Luvas e EPI',['luva','epi'],'luva'],
  ['Lâminas, cubetas e pipetas',['lamina','cubeta','pipeta'],'lamina'],
  ['Descartáveis e plásticos',['plast','hosp'],'plast'],
  ['Equipamentos e acessórios',['equip'],'equip'],
  ['Vidraria de laboratório',['vidraria'],'vidraria']
 ];
 var MAX=12;
 function mob(){return matchMedia('(max-width:700px)').matches;}
 function semFiltro(){return !FILTRO.busca&&!FILTRO.dept&&!FILTRO.marca;}
 function build(){
  var g=document.getElementById('grid');if(!g)return;
  var box=document.getElementById('mRows');
  if(!box){box=document.createElement('div');box.id='mRows';box.className='mRows';g.parentNode.insertBefore(box,g);}
  if(!mob()||!semFiltro()||typeof _card!=='function'){document.body.classList.remove('mHome');box.innerHTML='';return;}
  var P=window.PRECOS||{},h='',H=[];
  ROWS.forEach(function(r){
   var arr=CATALOG.filter(function(p){return r[1].indexOf(deptOf(p.k))>-1&&(!r[3]||r[3](p));});
   if(!arr.length)return;
   arr=arr.slice().sort(function(a,b){var pa=(P[a.c]&&P[a.c][1])?1:0,pb=(P[b.c]&&P[b.c][1])?1:0;var sa=(window.PIX3&&window.PIX3[a.c])?1:0,sb=(window.PIX3&&window.PIX3[b.c])?1:0;return (pb-pa)||(sb-sa);});
   var mostra=arr.slice(0,MAX).map(_card).join('');
   var all='onclick="setDept(\''+r[2]+'\')"',lk='href="'+catHref(r[2])+'" onclick="setDept(\''+r[2]+'\');return false"';
   h='<section class="mRow"><div class="mRowH"><h3><a '+lk+'>'+r[0]+'</a></h3><a '+lk+'>Ver todos ('+arr.length+') →</a></div><div class="mRowS">'+mostra+(arr.length>MAX?'<div class="mAll" '+all+'><b>→</b>Ver todos os '+arr.length+' produtos</div>':'')+'</div></section>';H.push(h);
  });
  /* 30/10/2026 (PageSpeed: tarefas longas): as 3 primeiras fileiras na hora; as outras em lotes de 3 quando o navegador estiver livre */
  var gen=(build.__g=(build.__g||0)+1),ric=window.requestIdleCallback||function(f){return setTimeout(function(){f({timeRemaining:function(){return 8;}});},16);};
  box.innerHTML=H.slice(0,3).join('');document.body.classList.add('mHome');
  var k=3;function lote(){if(gen!==build.__g)return;if(k>=H.length){window.hsScan&&hsScan();return;}box.insertAdjacentHTML('beforeend',H.slice(k,k+3).join(''));k+=3;ric(lote,{timeout:600});}
  if(H.length>3)ric(lote,{timeout:600});else{window.hsScan&&hsScan();}
 }
 var _r=window.render;window.render=function(){_r.apply(this,arguments);try{build();}catch(e){}};
 window.addEventListener('load',function(){try{build();}catch(e){}});
 var _w=innerWidth;window.addEventListener('resize',function(){if(Math.abs(innerWidth-_w)>80){_w=innerWidth;try{build();}catch(e){}}});
})();
}catch(e){try{console.error(e);}catch(_){}}

/* ==== conversao (31/10/2026): selos de pedido mínimo, avisos do link do carrinho, barra fixa do celular, cliques sem ação ==== */
try{
(function(){
/* selo "Pedido mín." nos cards já desenhados antes de a lista de refrigerados existir, e nos destaques (Greiner/testes) */
function selosRefresh(){try{
  [].forEach.call(document.querySelectorAll('.prod[data-c]'),function(el){if(el.querySelector('.pmin'))return;var h=seloMinHtml(el.getAttribute('data-c'));if(!h)return;var px=el.querySelector('.pixl');if(px)px.insertAdjacentHTML('afterend',h);});
  [].forEach.call(document.querySelectorAll('.ofc'),function(el){if(el.querySelector('.pmin'))return;var m=(el.getAttribute('onclick')||'').match(/abrirProd\((\d+)\)/);var p=m&&CATALOG[+m[1]];if(!p)return;var h=seloMinHtml(p.c);if(!h)return;var b=el.querySelector('.ofb');if(b)b.insertAdjacentHTML('beforebegin',h);else el.insertAdjacentHTML('beforeend',h);});
}catch(e){}}
window.selosRefresh=selosRefresh;
var _rd=window.render;window.render=function(){var r=_rd.apply(this,arguments);selosRefresh();return r;};
['montarGreiner','montarOfertas'].forEach(function(n){var o=window[n];if(typeof o==='function')window[n]=function(){var r=o.apply(this,arguments);selosRefresh();return r;};});
/* selo no modal do produto */
var _apM=window.abrirProd;
window.abrirProd=function(i){var r=_apM.apply(this,arguments);try{var p=CATALOG[i],b=document.querySelector('#pmInner .pixl.big');if(p&&b&&!document.querySelector('#pmInner .pmin'))b.insertAdjacentHTML('afterend',seloMinHtml(p.c));}catch(e){}return r;};

/* avisos do link do carrinho: código inexistente e itens que a equipe vai confirmar (&nf=) */
function nfLista(){var l=window.__nfConfirmar;if(!l){try{l=JSON.parse(sessionStorage.getItem('sullab_nf')||'null');}catch(e){l=null;}}return (l&&l.length)?l:null;}
function nomeCod(c){for(var i=0;i<CATALOG.length;i++)if(CATALOG[i].c===c)return CATALOG[i].n+' (cód. '+c+')';return 'cód. '+c;}
function esc(s){return String(s).replace(/[&<>"]/g,function(c){return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c];});}
window.fecharAvisoLink=function(k){if(k==='nf'){window.__nfConfirmar=null;try{sessionStorage.removeItem('sullab_nf');}catch(e){}}else window.__linkFaltou=null;atualizarCart();};
window.__nfConfirmarLista=nfLista;
var _acL=window.atualizarCart;
window.atualizarCart=function(){var r=_acL.apply(this,arguments);try{
  var di=document.getElementById('ditems');if(di){var h='',fa=window.__linkFaltou,nf=nfLista();
    if(fa&&fa.length)h+='<div class="lkAviso warn" role="alert"><button type="button" class="x" aria-label="Fechar aviso" onclick="fecharAvisoLink(\'faltou\')">×</button>⚠️ <b>'+(CART.length?'Alguns códigos do link não estão no catálogo do site:':'Nenhum produto deste link foi encontrado no catálogo do site.')+'</b> '+esc(fa.slice(0,12).join(', '))+'<br>Busque o produto pelo nome acima ou <a class="lk" onclick="abrirContatoWA(\'duvida\',\'Link do carrinho com código não encontrado: '+esc(fa.slice(0,12).join(', ')).replace(/'/g,'')+'\')">fale com a gente</a>.</div>';
    if(nf)h+='<div class="lkAviso nf"><button type="button" class="x" aria-label="Fechar aviso" onclick="fecharAvisoLink(\'nf\')">×</button>📝 <b>Itens que a equipe vai confirmar</b> (disponibilidade e preço, pelo WhatsApp, depois do pedido):<ul>'+nf.map(function(c){return '<li>'+esc(nomeCod(c))+'</li>';}).join('')+'</ul></div>';
    if(h)di.insertAdjacentHTML('afterbegin',h);}
  mbarRender();
}catch(e){}return r;};
/* barra do frete grátis: atualiza a barra única quando a cotação do CEP chega */
var _gh=window._gratisHtml;if(typeof _gh==='function')window._gratisHtml=function(){var r=_gh.apply(this,arguments);setTimeout(progRefresh,0);return r;};

/* barra fixa do celular (home e catálogo): total + Finalizar */
function mbarRender(){try{
  var b=document.getElementById('mbar');
  if(!b){b=document.createElement('div');b.id='mbar';b.className='mbar';document.body.appendChild(b);}
  if(!CART.length){document.body.classList.remove('temCart');b.innerHTML='';return;}
  var n=CART.reduce(function(s,x){return s+x.qty;},0),sub=totalCart(),semP=CART.some(function(x){return !precoItem(x);}),f=faltaTubo();
  var btn=semP?'<button type="button" onclick="abrirCarrinho()">Ver carrinho</button>':(f>0?'<button type="button" class="falta" onclick="minimoBloqueado(\'barra_fixa\')">Faltam '+brl(f)+'</button>':'<button type="button" onclick="abrirCheckout()">Finalizar</button>');
  b.innerHTML='<button type="button" class="mbT" onclick="abrirCarrinho()" aria-label="Abrir carrinho"><small>🛒 '+n+(n===1?' item':' itens')+'</small><b>'+(sub>0?brl(sub):'Sob consulta')+'</b></button>'+btn;
  document.body.classList.add('temCart');
}catch(e){}}
window.mbarRender=mbarRender;

/* botões indisponíveis: aria-disabled + motivo ao clicar (o clique não some sem explicação) */
document.addEventListener('click',function(e){var el=e.target&&e.target.closest&&e.target.closest('[aria-disabled="true"]');if(!el)return;e.preventDefault();e.stopPropagation();slAviso(el.getAttribute('data-motivo')||'Opção indisponível no momento.');},true);

selosRefresh();mbarRender();
})();
}catch(e){try{console.error(e);}catch(_){}}

/* ==== fim: devolve os addEventListener originais e avisa o rastreio.js (GA4/Meta) que a loja está pronta ==== */
try{window.__lojaFimShim&&window.__lojaFimShim();}catch(e){}
window.__lojaPronta=true;
try{window.dispatchEvent(new Event('sullab:loja'));}catch(e){}
