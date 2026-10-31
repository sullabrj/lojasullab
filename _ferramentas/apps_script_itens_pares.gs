/**
 * SULLAB — robô do carrinho, camada 2 ("quem compra X leva Y")
 * Trecho para o Apps Script que já lança o pedido pago na planilha "Controle de Pedidos SULLAB".
 * Chamar gravarItensPedido(controle, cliente, itens) logo depois de criar a linha na aba Pedidos.
 *   itens = [{c:'PA03', n:'Agar batata dextrose...', q:1, sai:'Estoque'|'Encomenda'}, ...]
 * Grava 1 linha por item na aba "Itens" (Controle, Cliente, Código, Produto, Qtd, Sai de, Fornecedor, Situação do item).
 * A estatística de pares é recalculada por fora (_ferramentas/pares.py) e publicada em data/pares.json.
 */
function gravarItensPedido(controle, cliente, itens) {
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  var ws = ss.getSheetByName('Itens');
  if (!ws || !itens || !itens.length) return;
  var rows = itens.map(function (it) {
    return [controle, cliente, String(it.c || ''), String(it.n || ''), Number(it.q || 1), it.sai || 'A conferir', '', 'A conferir'];
  });
  ws.getRange(ws.getLastRow() + 1, 1, rows.length, rows[0].length).setValues(rows);
}
