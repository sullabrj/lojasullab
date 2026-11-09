#!/usr/bin/env python3
"""Gera guias de SEO em /guia/ a partir do molde de guia/meio-stuart-x-cary-blair.html (09/11/2026).
Idempotente. Uso: python3 _ferramentas/gerar_guias_seo.py
Não mexe em preço nem em páginas de produto; só cria guia/*.html e ajusta sitemap-paginas.xml.
"""
import html, json, os, re, sys
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/'
SITE = 'https://lojasullabrj.com.br'
MOLDE = R + 'guia/meio-stuart-x-cary-blair.html'
DATA = '2026-11-09'

def P(slug):  # confere se a página de produto existe
    assert os.path.exists(R + 'p/' + slug + '.html'), slug
    return '/p/' + slug + '.html'

GUIAS = [
 dict(
  slug='agar-sangue-de-carneiro-para-que-serve',
  title='Ágar sangue de carneiro: para que serve e qual base | SULLAB',
  h1='Ágar sangue de carneiro: para que serve e qual base escolher',
  desc='Ágar sangue de carneiro: para que serve, como ler a hemólise (alfa, beta e gama) e qual base escolher (Columbia, TSA, triptose). Preço CNPJ e NF-e.',
  lead='O ágar sangue de carneiro é o meio de cultura de uso geral mais comum na rotina de microbiologia clínica. Ele é enriquecido com sangue, por isso cresce a maior parte das bactérias exigentes, e ainda mostra o padrão de <strong>hemólise</strong> de cada colônia — uma pista importante na identificação.',
  cta=('Ver o ágar sangue de carneiro Columbia (caixa c/ 10 placas)', 'agar-sangue-de-carneiro-base-columbia-9015-mm-caixa-c-10-placas-pa27'),
  body='''
  <h2>Para que serve</h2>
  <p>É usado no isolamento primário de amostras clínicas, como <strong>urina, secreção de orofaringe, feridas, escarro e hemocultura repicada</strong>. Por ser um meio nutritivo e não seletivo, permite o crescimento de bactérias Gram-positivas e Gram-negativas, inclusive as mais exigentes, como <em>Streptococcus</em>. Para separar bacilos Gram-negativos entéricos, ele costuma ser usado junto com o <a href="/guia/agar-macconkey-para-que-serve.html">ágar MacConkey</a>.</p>

  <h2>Como ler a hemólise</h2>
  <table>
    <tr><th>Padrão</th><th>Aspecto ao redor da colônia</th><th>O que significa</th></tr>
    <tr><td>Beta (β)</td><td>Halo transparente</td><td>Destruição completa das hemácias</td></tr>
    <tr><td>Alfa (α)</td><td>Halo esverdeado ou escurecido</td><td>Destruição parcial das hemácias</td></tr>
    <tr><td>Gama (γ)</td><td>Sem halo</td><td>Não há hemólise</td></tr>
  </table>
  <p>A hemólise sozinha não identifica a bactéria: ela orienta os próximos testes, como a coloração de Gram, a catalase e a <a href="/guia/plasma-de-coelho-prova-da-coagulase.html">prova da coagulase</a>.</p>

  <h2>Qual base escolher: Columbia, TSA ou triptose</h2>
  <p>A base é o meio nutritivo que recebe o sangue. Todas servem para a rotina geral. A escolha costuma seguir o protocolo do laboratório e a preferência de quem lê as placas:</p>
  <ul>
    <li><a href="%(columbia)s">Base Columbia</a> — muito usada como padrão em microbiologia clínica.</li>
    <li><a href="%(tsa)s">Base TSA (caseína-soja)</a> — meio de uso geral bastante difundido.</li>
    <li><a href="%(triptose)s">Base triptose</a> — alternativa de uso geral, em placa de 90 mm.</li>
  </ul>
  <p>Para antibiograma de bactérias exigentes, o laboratório usa uma base diferente: o <a href="/guia/agar-mueller-hinton-antibiograma.html">ágar Mueller-Hinton</a>, que também existe com sangue (<a href="%(mhs90)s">placa de 90 mm</a> e <a href="%(mhs140)s">placa de 140 mm</a>).</p>

  <h2>Quando preparar em casa e quando comprar a placa pronta</h2>
  <p>Preparar a placa exige base desidratada, esterilização, sangue desfibrinado e câmara de fluxo. Para laboratórios que fazem isso, a SULLAB tem o <a href="/p/sangue-de-carneiro-desfibrinado-frasco-c-50-ml-pa158.html">sangue de carneiro desfibrinado (frasco de 50 mL)</a>. Para quem quer padrão e menos trabalho, a placa pronta é a opção mais prática.</p>

  <h2>Armazenamento</h2>
  <p>Placas com sangue são produto refrigerado e a validade vem no rótulo de cada lote. Evite deixar as caixas fora da geladeira por muito tempo, para não ressecar nem desnaturar o meio. A SULLAB envia produto refrigerado com isopor e gelo; veja o pedido mínimo e o prazo na página do produto.</p>
  <a class="cta" href="%(columbia)s">Ver ágar sangue de carneiro na loja →</a>
''',
  faq=[('O que é hemólise beta, alfa e gama?', 'São os três padrões de ação sobre as hemácias no ágar sangue: beta é a destruição completa (halo transparente), alfa é a parcial (halo esverdeado) e gama é a ausência de hemólise.'),
       ('Posso usar ágar sangue de carneiro para antibiograma?', 'O antibiograma de rotina usa o ágar Mueller-Hinton. Para bactérias exigentes, existem versões do Mueller-Hinton com sangue. Siga o protocolo e o documento de referência que o laboratório adota.'),
       ('O ágar sangue é seletivo?', 'Não. É um meio enriquecido, de uso geral, que permite o crescimento de muitas bactérias. Meios seletivos, como o MacConkey, são usados junto com ele para separar grupos específicos.'),
       ('Placa de ágar sangue precisa de geladeira?', 'Sim. As placas com sangue devem ser armazenadas sob refrigeração, conforme o rótulo do lote.')],
  links={'columbia':'agar-sangue-de-carneiro-base-columbia-9015-mm-caixa-c-10-placas-pa27','tsa':'agar-sangue-de-carneiro-base-tsa-9015-mm-caixa-c-10-placas-pa31','triptose':'agar-sangue-de-carneiro-base-triptose-9015-mm-caixa-c-10-placas-pa30','mhs90':'agar-sangue-de-carneiro-base-mueller-hinton-9015-mm-caixa-c-10-placas-pa29','mhs140':'agar-sangue-de-carneiro-base-mueller-hinton-14015-mm-caixa-c-10-placas-pa28'},
 ),
 dict(
  slug='agar-mueller-hinton-antibiograma',
  title='Ágar Mueller-Hinton: antibiograma e qual usar | SULLAB',
  h1='Ágar Mueller-Hinton: para que serve no antibiograma e qual usar',
  desc='Ágar Mueller-Hinton: para que serve no antibiograma por disco-difusão, diferença para o Mueller-Hinton com sangue e MH-F, e onde comprar com NF-e.',
  lead='O Mueller-Hinton é o meio padrão do antibiograma por disco-difusão (método de Kirby-Bauer). Ele foi escolhido por ter boa reprodutibilidade e pouca interferência nos antibióticos testados. Aqui você vê as variações do meio e quando cada uma é usada.',
  cta=('Ver o ágar Mueller-Hinton (placas de 90 mm)', 'agar-mueller-hinton-9015-mm-caixa-c-10-placas-pa19'),
  body='''
  <h2>Para que serve</h2>
  <p>É usado para testar a sensibilidade de bactérias a antimicrobianos em placa. Discos com antibióticos são colocados sobre a placa semeada com a bactéria, e o tamanho do halo de inibição ao redor de cada disco é medido e interpretado de acordo com o documento de referência que o laboratório adota (CLSI ou BrCAST/EUCAST).</p>

  <h2>Pontos que mais interferem no resultado</h2>
  <ul>
    <li><strong>Espessura do ágar:</strong> a referência é de cerca de 4 mm na placa. Camada mais fina ou mais grossa altera o tamanho dos halos.</li>
    <li><strong>Inóculo:</strong> suspensão padronizada em 0,5 da escala de McFarland.</li>
    <li><strong>Incubação:</strong> geralmente 35 °C por 16 a 18 horas, conforme o protocolo adotado.</li>
    <li><strong>Armazenamento:</strong> placa fora da validade ou ressecada muda o resultado.</li>
  </ul>

  <h2>Tipos de Mueller-Hinton</h2>
  <table>
    <tr><th>Meio</th><th>Quando é usado</th></tr>
    <tr><td>Mueller-Hinton simples</td><td>Bactérias de crescimento fácil, como enterobactérias, <em>Pseudomonas</em> e <em>Staphylococcus</em></td></tr>
    <tr><td>Mueller-Hinton com sangue de carneiro</td><td>Bactérias exigentes, como estreptococos, no protocolo CLSI</td></tr>
    <tr><td>Mueller-Hinton fastidioso (MH-F)</td><td>Bactérias exigentes no protocolo EUCAST/BrCAST: base com sangue de cavalo e NAD</td></tr>
  </table>

  <h2>Onde escolher na SULLAB</h2>
  <ul>
    <li>Placas prontas simples: <a href="%(p90)s">90 mm</a> e <a href="%(p140)s">140 mm</a>.</li>
    <li>Com sangue de carneiro: <a href="/p/agar-sangue-de-carneiro-base-mueller-hinton-9015-mm-caixa-c-10-placas-pa29.html">90 mm</a> e <a href="/p/agar-sangue-de-carneiro-base-mueller-hinton-14015-mm-caixa-c-10-placas-pa28.html">140 mm</a>.</li>
    <li>MH-F com sangue de cavalo: <a href="/p/agar-mh-f-sangue-de-cavalo-base-mueller-hinton-9015-mm-caixa-c-10-placas-pa341.html">90 mm</a> e <a href="/p/agar-mh-f-sangue-de-cavalo-base-mueller-hinton-14015-mm-caixa-c-10-placas-pa340.html">140 mm</a>.</li>
    <li>Base desidratada (para o laboratório preparar): <a href="/p/agar-mueller-hinton-100grs-200046.html">100 g</a>, <a href="/p/agar-mueller-hinton-250grs-200152.html">250 g</a> ou <a href="/p/agar-mueller-hinton-500grs-bio-200035.html">500 g</a>.</li>
  </ul>
  <p>Para o isolamento da bactéria antes do antibiograma, veja também o <a href="/guia/agar-sangue-de-carneiro-para-que-serve.html">ágar sangue de carneiro</a> e o <a href="/guia/agar-macconkey-para-que-serve.html">ágar MacConkey</a>.</p>
  <a class="cta" href="%(p90)s">Ver Mueller-Hinton na loja →</a>
''',
  faq=[('Qual é a espessura correta do ágar Mueller-Hinton no antibiograma?', 'A referência é de cerca de 4 mm. A placa pronta já vem padronizada; ao preparar em casa, o volume por placa deve ser calculado para chegar a essa espessura.'),
       ('Qual a diferença entre Mueller-Hinton com sangue e MH-F?', 'O Mueller-Hinton com sangue de carneiro é a versão do protocolo CLSI para bactérias exigentes. O MH-F usa sangue de cavalo e NAD e é a versão do protocolo EUCAST/BrCAST.'),
       ('Posso usar a mesma placa para todas as bactérias?', 'Não. Bactérias exigentes, como estreptococos e Haemophilus, precisam de versões enriquecidas do meio. Siga o documento de referência adotado pelo laboratório.'),
       ('Mueller-Hinton precisa ficar na geladeira?', 'As placas prontas devem ser armazenadas conforme o rótulo do lote, normalmente sob refrigeração. A base em pó é guardada seca e fechada.')],
  links={'p90':'agar-mueller-hinton-9015-mm-caixa-c-10-placas-pa19','p140':'agar-mueller-hinton-14015-mm-caixa-c-10-placas-pa18'},
 ),
 dict(
  slug='agar-macconkey-para-que-serve',
  title='Ágar MacConkey: para que serve e como ler as colônias | SULLAB',
  h1='Ágar MacConkey: para que serve e como ler as colônias',
  desc='Ágar MacConkey: meio seletivo e diferencial para bacilos Gram-negativos. Veja como ler colônias lactose positivas e negativas e onde comprar com NF-e.',
  lead='O ágar MacConkey é um meio <strong>seletivo e diferencial</strong>. Ele só deixa crescer bacilos Gram-negativos e, ao mesmo tempo, mostra pela cor da colônia se a bactéria fermenta a lactose. É um dos meios mais usados em culturas de urina e fezes.',
  cta=('Ver o ágar MacConkey (caixa c/ 10 placas)', 'agar-macconkey-9015-mm-caixa-c-10-placas-pa15'),
  body='''
  <h2>Como ele funciona</h2>
  <p>Os sais biliares e o cristal violeta do meio inibem a maioria das bactérias Gram-positivas. A lactose e o indicador de pH deixam visível quem a fermenta: a fermentação produz ácido e a colônia fica rosa ou vermelha.</p>

  <h2>Como ler as colônias</h2>
  <table>
    <tr><th>Aspecto</th><th>Significado</th><th>Exemplos comuns</th></tr>
    <tr><td>Rosa ou vermelha</td><td>Fermenta a lactose</td><td><em>E. coli</em>, <em>Klebsiella</em>, <em>Enterobacter</em></td></tr>
    <tr><td>Incolor ou transparente</td><td>Não fermenta a lactose</td><td><em>Salmonella</em>, <em>Shigella</em>, <em>Pseudomonas</em>, <em>Proteus</em></td></tr>
  </table>
  <p>A cor orienta a triagem, mas a identificação depende de outros testes, como as provas bioquímicas (veja o <a href="/guia/meios-de-cultura-tsi-tioglicolato-stuart-mrvp.html">guia sobre TSI e outros meios</a>) ou outros métodos que o laboratório utilize.</p>

  <h2>Variações do MacConkey</h2>
  <ul>
    <li><strong>MacConkey sorbitol:</strong> troca a lactose por sorbitol e é usado na triagem de <em>E. coli</em> O157, que não fermenta o sorbitol. Veja o <a href="/p/agar-macconkey-sorbitol-500grs-200415.html">MacConkey sorbitol 500 g</a>.</li>
    <li><strong>Triplaca com sangue, chocolate e MacConkey:</strong> três meios na mesma placa, que economiza espaço e tempo de leitura. Veja a <a href="/p/agar-sangue-chocolate-mac-conkey-9015-mm-caixa-c-10-triplacas-pa334.html">triplaca (caixa c/ 10)</a>.</li>
  </ul>

  <h2>Onde comprar</h2>
  <ul>
    <li>Placas prontas: <a href="%(p90)s">90 mm (caixa c/ 10)</a> e <a href="%(p60)s">60 mm (caixa c/ 8)</a>.</li>
    <li>Base desidratada para preparo: <a href="/p/agar-macconkey-100grs-bio-200058.html">100 g</a>, <a href="/p/agar-macconkey-250grs-200304.html">250 g</a> ou <a href="/p/agar-macconkey-500grs-bio-200037.html">500 g</a>.</li>
  </ul>
  <p>Na rotina, o MacConkey costuma ser semeado junto com o <a href="/guia/agar-sangue-de-carneiro-para-que-serve.html">ágar sangue de carneiro</a>, que cresce as bactérias Gram-positivas e as exigentes.</p>
  <a class="cta" href="%(p90)s">Ver ágar MacConkey na loja →</a>
''',
  faq=[('O ágar MacConkey cresce bactérias Gram-positivas?', 'Em geral não. Os sais biliares e o cristal violeta inibem a maioria das Gram-positivas. Por isso ele é seletivo para bacilos Gram-negativos.'),
       ('O que significa colônia rosa no MacConkey?', 'Significa que a bactéria fermentou a lactose e produziu ácido. É o caso típico de E. coli e Klebsiella. A identificação final depende de outros testes.'),
       ('Qual a diferença entre MacConkey e MacConkey sorbitol?', 'O MacConkey sorbitol usa sorbitol no lugar da lactose e é usado na triagem de E. coli O157, que não fermenta o sorbitol.'),
       ('Placa de MacConkey precisa de geladeira?', 'Siga o rótulo do lote. As placas prontas são, em geral, armazenadas sob refrigeração. A base em pó é guardada seca e fechada.')],
  links={'p90':'agar-macconkey-9015-mm-caixa-c-10-placas-pa15','p60':'agar-macconkey-6010-mm-caixa-c-8-placas-pa14'},
 ),
 dict(
  slug='plasma-de-coelho-prova-da-coagulase',
  title='Plasma de coelho: prova da coagulase passo a passo | SULLAB',
  h1='Plasma de coelho liofilizado: como fazer a prova da coagulase',
  desc='Prova da coagulase com plasma de coelho liofilizado: para que serve, passo a passo em tubo, como ler o coágulo e onde comprar com NF-e.',
  lead='A prova da coagulase separa o <em>Staphylococcus aureus</em> dos outros estafilococos. Ela usa plasma de coelho: se a bactéria produz coagulase, o plasma forma um coágulo. É um teste simples e muito usado na rotina de microbiologia.',
  cta=('Ver o plasma de coelho liofilizado (frasco com 3 mL)', 'plasma-de-coelho-liofilizado-frasco-c-3-ml-apos-reconstituicao-pa231'),
  body='''
  <h2>Para que serve</h2>
  <p>Estafilococos aparecem como cocos Gram-positivos em cachos e são catalase positivos. Para saber se é <em>S. aureus</em> (coagulase positivo) ou outro estafilococo (em geral coagulase negativo), faz-se a prova da coagulase. Alguns outros estafilococos, como os do grupo <em>S. intermedius</em>, também podem dar resultado positivo, e o laboratório considera isso na identificação.</p>

  <h2>Passo a passo (prova em tubo)</h2>
  <ol>
    <li>Reconstitua o plasma liofilizado conforme a instrução do frasco.</li>
    <li>Coloque um pequeno volume do plasma em um tubo limpo.</li>
    <li>Adicione colônia isolada da bactéria (ou cultura em caldo) e misture suavemente.</li>
    <li>Incube a 35–37 °C e observe após 4 horas.</li>
    <li>Se ainda não houver coágulo, deixe até 24 horas antes de dar como negativo.</li>
  </ol>
  <p>Faça sempre os controles positivo e negativo da rotina do laboratório. Siga o protocolo e o documento de referência que você adota.</p>

  <h2>Como ler</h2>
  <table>
    <tr><th>Resultado</th><th>O que se vê</th></tr>
    <tr><td>Positivo</td><td>Coágulo firme no tubo, que não se desfaz ao inclinar</td></tr>
    <tr><td>Negativo</td><td>Plasma líquido, sem coágulo</td></tr>
  </table>

  <h2>Onde comprar na SULLAB</h2>
  <ul>
    <li><a href="%(pa231)s">Plasma de coelho liofilizado, frasco para 3 mL após reconstituição</a>.</li>
    <li><a href="/p/biocoagulase-teste-plasma-coelho-liofilizado-5-x-3ml-052000.html">Biocoagulase: plasma de coelho liofilizado, 5 frascos de 3 mL</a>.</li>
  </ul>
  <p>As colônias para o teste costumam sair do <a href="/guia/agar-sangue-de-carneiro-para-que-serve.html">ágar sangue de carneiro</a>. Veja também o <a href="/categoria/meios-de-cultura.html">catálogo de meios de cultura</a>.</p>
  <a class="cta" href="%(pa231)s">Ver plasma de coelho na loja →</a>
''',
  faq=[('Qual a diferença entre a prova da coagulase em tubo e em lâmina?', 'A prova em tubo detecta a coagulase livre e é a mais confiável. A prova em lâmina detecta a coagulase ligada à bactéria e dá o resultado em segundos, mas pode precisar de confirmação em tubo.'),
       ('Quanto tempo esperar para ler a prova da coagulase em tubo?', 'A leitura é feita após 4 horas. Se for negativa, o tubo costuma ser mantido até 24 horas antes de se dar o resultado final.'),
       ('Que plasma é usado na prova da coagulase?', 'Plasma de coelho, que é o recomendado para essa prova. Ele pode ser vendido liofilizado e precisa ser reconstituído antes do uso.'),
       ('Como guardar o plasma liofilizado?', 'Siga as instruções do rótulo do fabricante quanto à temperatura e ao tempo de uso depois da reconstituição.')],
  links={'pa231':'plasma-de-coelho-liofilizado-frasco-c-3-ml-apos-reconstituicao-pa231'},
 ),
]

def montar(g, molde):
    url = f"{SITE}/guia/{g['slug']}.html"
    links = {k: P(v) for k, v in g['links'].items()}
    cta_txt, cta_slug = g['cta']; links_cta = P(cta_slug)
    body = g['body'] % links
    faq_html = '<div class="faq">' + ''.join(f'<details><summary>{html.escape(q)}</summary><p>{html.escape(a)}</p></details>' for q, a in g['faq']) + '</div>'
    main = (f'<main class="wrap">\n  <h1>{html.escape(g["h1"])}</h1>\n  <p class="lead">{g["lead"]}</p>\n  \n'
            f'  <p style="margin-top:14px"><a class="cta" href="{links_cta}">🛒 {html.escape(cta_txt)} →</a></p>\n{body}\n'
            f'  <h2>Perguntas frequentes</h2>\n  {faq_html}\n</main>')
    h = molde
    t = html.escape(g['title']); d = html.escape(g['desc'], quote=True)
    h = re.sub(r'<title>.*?</title>', f'<title>{t}</title>', h, count=1, flags=re.S)
    h = re.sub(r'(<meta name="description" content=")[^"]*(")', lambda m: m.group(1) + d + m.group(2), h, count=1)
    h = re.sub(r'(<link rel="canonical" href=")[^"]*(")', lambda m: m.group(1) + url + m.group(2), h, count=1)
    h = re.sub(r'(<meta property="og:title" content=")[^"]*(")', lambda m: m.group(1) + t + m.group(2), h, count=1)
    h = re.sub(r'(<meta property="og:description" content=")[^"]*(")', lambda m: m.group(1) + d + m.group(2), h, count=1)
    h = re.sub(r'(<meta property="og:url" content=")[^"]*(")', lambda m: m.group(1) + url + m.group(2), h, count=1)
    art = {"@context": "https://schema.org", "@type": "Article", "headline": g['title'].replace(' | SULLAB', ''), "description": g['desc'],
           "author": {"@type": "Organization", "name": "SULLAB"}, "publisher": {"@type": "Organization", "name": "SULLAB"},
           "datePublished": DATA, "dateModified": DATA, "mainEntityOfPage": url}
    faq = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in g['faq']]}
    bc = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Início", "item": SITE + "/"},
        {"@type": "ListItem", "position": 2, "name": "Guias", "item": SITE + "/"},
        {"@type": "ListItem", "position": 3, "name": g['title'].replace(' | SULLAB', '')}]}
    blocos = iter([art, faq, bc])
    h = re.sub(r'<script type="application/ld\+json">.*?</script>', lambda m: '<script type="application/ld+json">' + json.dumps(next(blocos), ensure_ascii=False) + '</script>', h, count=3, flags=re.S)
    i, j = h.find('<main class="wrap">'), h.find('</main>') + len('</main>')
    return h[:i] + main + h[j:]

def main():
    molde = open(MOLDE, encoding='utf8').read()
    novos = []
    for g in GUIAS:
        open(R + f"guia/{g['slug']}.html", 'w', encoding='utf8').write(montar(g, molde))
        novos.append(f"{SITE}/guia/{g['slug']}.html")
    sm = open(R + 'sitemap-paginas.xml', encoding='utf8').read()
    for u in novos:
        if u not in sm:
            sm = sm.replace('</urlset>', f'<url><loc>{u}</loc><lastmod>{DATA}</lastmod><changefreq>monthly</changefreq></url>\n</urlset>')
    open(R + 'sitemap-paginas.xml', 'w', encoding='utf8').write(sm)
    print('guias:', len(novos))

if __name__ == '__main__':
    main()
