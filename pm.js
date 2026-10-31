/* SULLAB — barra fixa de compra e ajustes de celular nas páginas de produto (26/10/2026) */
(function(){try{
  var buy=document.querySelector('a.btn-whats');if(!buy)return;
  var pr=document.querySelector('.preco>b');
  var href=buy.getAttribute('href')||'';
  /* 31/10/2026: "Comprar agora" soma ao carrinho (&add=1) em vez de substituir o que o cliente já tinha */
  if(/[?&]carrinho=/.test(href)&&!/[?&]add=1/.test(href)){href+='&add=1';buy.setAttribute('href',href);}
  var m=href.match(/carrinho=([^:&]+):(\d+)/);
  var precoTxt=pr?pr.textContent.trim():'';
  var v=precoTxt?parseFloat(precoTxt.replace(/[^\d,]/g,'').replace(',','.')):0;
  var brl=function(n){return 'R$ '+n.toFixed(2).replace('.',',').replace(/\B(?=(\d{3})+(?!\d))/g,'.');};
  /* preço no Pix: 5% off; 3% em tubos e agulhas Vacuette (mesma lista PIX3 da loja) — 31/10/2026 */
  var PIX3={"450071":1,"450072":1,"454036":1,"454087":1,"454921":1,"454235":1,"456211":1,"454071":1,"454482":1,"456071":1,"455071":1,"454092":1,"455092":1,"456001":1,"454327":1,"454085":1,"454091":1,"454030":1,"456080":1,"450539":1};
  var cod=m?decodeURIComponent(m[1]):'';var pct=PIX3[cod]?3:5;
  if(v>0&&m){var pb=document.querySelector('.preco');if(pb&&!pb.querySelector('.pmpix')){var px=document.createElement('span');px.className='pmpix';px.innerHTML='💚 '+brl(Math.round(v*(100-pct))/100)+' no Pix<span>'+pct+'% off</span>';pb.appendChild(px);}}
  var mob=window.matchMedia&&matchMedia('(max-width:700px)').matches;
  /* no celular o botão de compra fica logo abaixo do preço */
  if(mob){var ref=document.querySelector('.tb')||document.querySelector('.preco');if(ref&&ref.parentNode===buy.parentNode)ref.parentNode.insertBefore(buy,ref.nextSibling);}
  /* barra fixa embaixo: preço + quantidade + comprar */
  var bar=document.createElement('div');bar.id='pmBar';
  var q=1,lbl=(buy.textContent||'').replace(/^[^A-Za-zÀ-ú]+/,'').trim()||'Comprar';
  if(/comprar/i.test(lbl))lbl='Comprar';
  bar.innerHTML='<div class="pmP">'+(v>0?'<small>Preço (NF-e)</small><b>'+precoTxt+'</b>':'<small>SULLAB</small><b style="font-size:16px;color:#1f3a5f">Sob consulta</b>')+'</div>'+
    (m?'<div class="pmQ"><button type="button" aria-label="Diminuir">−</button><span>1</span><button type="button" aria-label="Aumentar">+</button></div>':'')+
    '<a class="pmB" href="'+href.replace(/"/g,'&quot;')+'">🛒 '+lbl+'</a>';
  document.body.appendChild(bar);
  var a=bar.querySelector('.pmB');
  if(m){var bs=bar.querySelectorAll('.pmQ button'),sp=bar.querySelector('.pmQ span');
    var up=function(){sp.textContent=q;var h=href.replace(/(carrinho=[^:&]+:)\d+/,'$1'+q);a.setAttribute('href',h);buy.setAttribute('href',h);
      var pp=bar.querySelector('.pmP b');if(v>0&&pp)pp.textContent=brl(Math.round(v*q*100)/100);var sm=bar.querySelector('.pmP small');if(sm)sm.textContent=q>1?(q+' × '+precoTxt):'Preço (NF-e)';};
    bs[0].onclick=function(){if(q>1){q--;up();}};bs[1].onclick=function(){if(q<999){q++;up();}};}
}catch(e){}})();

/* 27/10/2026: clique na foto (era o clique "morto" mais comum no Clarity) abre a foto grande; toque fora ou ✕ fecha */
(function(){try{
  var ph=document.getElementById('ph');if(!ph)return;
  ph.style.cursor='zoom-in';ph.setAttribute('role','button');ph.setAttribute('aria-label','Ampliar foto');ph.tabIndex=0;
  var abrir=function(){
    var m=(ph.style.backgroundImage||'').match(/url\(["']?([^"')]+)["']?\)/);if(!m)return;
    var o=document.createElement('div');o.id='pmZoom';
    o.setAttribute('style','position:fixed;inset:0;z-index:100001;background:rgba(10,20,35,.92);display:flex;align-items:center;justify-content:center;padding:16px;cursor:zoom-out');
    o.innerHTML='<img alt="Foto do produto ampliada" style="max-width:100%;max-height:100%;object-fit:contain;background:#fff;border-radius:12px;touch-action:pinch-zoom"><button type="button" aria-label="Fechar" style="position:absolute;top:12px;right:12px;width:46px;height:46px;border:0;border-radius:50%;background:#fff;font-size:22px;font-weight:800;color:#1f3a5f;cursor:pointer">✕</button>';
    o.querySelector('img').src=m[1];
    var fechar=function(){o.remove();document.removeEventListener('keydown',esc);};
    var esc=function(e){if(e.key==='Escape')fechar();};
    o.addEventListener('click',function(e){if(e.target.tagName!=='IMG')fechar();});
    document.addEventListener('keydown',esc);document.body.appendChild(o);
  };
  ph.addEventListener('click',abrir);
  ph.addEventListener('keydown',function(e){if(e.key==='Enter'||e.key===' '){e.preventDefault();abrir();}});
}catch(e){}})();
