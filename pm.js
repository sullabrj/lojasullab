/* SULLAB — barra fixa de compra e ajustes de celular nas páginas de produto (26/10/2026) */
(function(){try{
  var buy=document.querySelector('a.btn-whats');if(!buy)return;
  var pr=document.querySelector('.preco>b');
  var href=buy.getAttribute('href')||'';
  var m=href.match(/carrinho=([^:&]+):(\d+)/);
  var precoTxt=pr?pr.textContent.trim():'';
  var v=precoTxt?parseFloat(precoTxt.replace(/[^\d,]/g,'').replace(',','.')):0;
  var brl=function(n){return 'R$ '+n.toFixed(2).replace('.',',').replace(/\B(?=(\d{3})+(?!\d))/g,'.');};
  /* preço no Pix (5% off, igual à loja) */
  if(v>0&&m){var pb=document.querySelector('.preco');if(pb&&!pb.querySelector('.pmpix')){var px=document.createElement('span');px.className='pmpix';px.innerHTML='💚 '+brl(Math.round(v*95)/100)+' no Pix<span>5% off</span>';pb.appendChild(px);}}
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
