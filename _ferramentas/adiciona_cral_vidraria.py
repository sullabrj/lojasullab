# -*- coding: utf-8 -*-
"""Cadastra no site a linha de VIDRARIA e MICROSCÓPIOS da CRAL (30/10/2026).

Entrada: /home/claude/cral_portal_30-10-2026.txt (campos do portal da CRAL)
Preço: microscópios = portal x 1,50; vidraria = portal x 1,40.
Gera/atualiza: index.html (SEED, PRECOS, QTD, DEPTS, fileiras do celular, rodapé),
kw.json, ft.json, p/*.html, categoria/vidraria-de-laboratorio.html (nova),
categoria/equipamentos-e-acessorios.html, marca/cral.html, catalogo.html,
catalogo/index.html, sitemap-produtos.xml, sitemap-categorias.xml, feed-google.xml,
rodapé (lista de categorias) de todas as páginas e o CSV de frete.
Uso: python3 _ferramentas/adiciona_cral_vidraria.py
"""
import re, json, html, math, os, glob, unicodedata, csv
from decimal import Decimal, ROUND_HALF_UP

R = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/'
DADOS = '/home/claude/cral_portal_30-10-2026.txt'
CSV_FRETE = '/home/claude/frete_novos_cral_30-10-2026.csv'
SITE = 'https://lojasullabrj.com.br'
HOJE = '2026-10-30'
IMG_CRAL = 'https://storage.googleapis.com/cv-pub-cloud/cral/imagens/produtos/%s.jpg'
LOGO = SITE + '/img/logo-sullab.png'
# fotos inexistentes no portal: mesma carcaça/linha do modelo irmão (mesmo EAN no portal)
FOTO_IRMA = {'MICB100-INF': 'MICB-10', 'MICB200-INF': 'MICB-20', 'MICBTRI100-INF': 'MICBTRI10'}
SEM_FOTO = {'SISERLEN1000', 'SISERLEN250', 'SISERLEN500'}

CAT_VID = ('vidraria', 'Vidraria de laboratório', 'vidraria-de-laboratorio')
CAT_EQP = ('equip', 'Equipamentos e acessórios', 'equipamentos-e-acessorios')


def brl(v):
    return 'R$ ' + f'{v:,.2f}'.replace(',', 'X').replace('.', ',').replace('X', '.')


def r2(x):
    return float(Decimal(str(x)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP))


def num(s):
    return float(s.replace(',', '.')) if s else 0.0


def sem_acento(s):
    return unicodedata.normalize('NFKD', s).encode('ascii', 'ignore').decode()


def slugify(nome, cod):
    base = re.split(r' — (?:caixa|pacote|rack) c/', nome)[0]
    t = sem_acento(base).lower().replace('×', '')
    t = re.sub(r'[^a-z0-9]+', '-', t).strip('-')
    return t + '-' + re.sub(r'[^a-z0-9]+', '-', cod.lower()).strip('-')


def cap(v):
    v = int(v)
    return f'{v} mL'

# ---------------------------------------------------------------- grupos
# nome(param) -> (nome, qtd_caixa ou None);  base = linhas fixas da ficha;  sobre = parágrafo
G = {}


def grp(k, nome, base, sobre, kw, cat=CAT_VID):
    G[k] = dict(nome=nome, base=base, sobre=sobre, kw=kw, cat=cat)


MICN = {
    'MICB-10': 'Microscópio biológico binocular acromático — óptica finita, LED, bivolt',
    'MICB-20': 'Microscópio biológico binocular planacromático com contraste de fase — óptica finita, bivolt',
    'MICBTRI10': 'Microscópio biológico trinocular planacromático — óptica finita, LED, bivolt',
    'MICB100-INF': 'Microscópio biológico binocular planacromático — óptica infinita, LED, bivolt',
    'MIBEST': 'Microscópio estereoscópio binocular (lupa) 20X a 80X — LED, bivolt',
    'MICB200-INF': 'Microscópio biológico binocular planacromático — óptica infinita, campo 22 mm, LED, bivolt',
    'MICBTRI100-INF': 'Microscópio biológico trinocular planacromático — óptica infinita, LED, bivolt',
}
grp('MIC', lambda p: (MICN[p], None),
    ['Uso profissional em laboratórios clínicos, patologia, veterinária, ensino, pesquisa e controle de qualidade'],
    lambda it: ('O {n} é indicado para a rotina de laboratórios clínicos, centros de patologia, clínicas veterinárias, '
                'universidades e indústrias. {extra}Acompanha o conjunto óptico descrito na ficha técnica e opera em rede '
                'bivolt. Venda para empresas (CNPJ) com NF-e; consulte nossa equipe técnica para instalação e suporte.').format(
        n=it['nome'].split(' — ')[0].lower().replace('microscópio', 'microscópio', 1),
        extra=('Ideal para inspeção visual de amostras, peças e materiais com grande profundidade de foco. ' if it['cod'] == 'MIBEST'
               else 'A câmera pode ser acoplada à saída trinocular para documentação e ensino. ' if 'TRI' in it['cod']
               else 'Permite observar microrganismos e células vivas sem coloração, além do campo claro. ' if it['cod'] == 'MICB-20'
               else 'O sistema de óptica infinita oferece imagens nítidas e permite acoplar acessórios ópticos. ' if 'INF' in it['cod']
               else 'Configuração de campo claro de excelente custo-benefício para a rotina. ')),
    'microscopio microscopia optico optica lente objetiva ocular led bivolt laboratorio biologico equipamento', CAT_EQP)

grp('PASTEUR', lambda p: (f'Pipeta Pasteur de vidro {p} mm — caixa c/ 250 un', 250),
    ['Pipeta tipo conta-gotas em vidro soda, para transferência de pequenos volumes sem exigência de alta precisão',
     'Diâmetro da ponta: 1,91 mm; diâmetro da boca: 7,17 mm', 'Uso com pera/pipetador manual',
     'Embalagem: caixa com 250 un (não embaladas individualmente)'],
    lambda it: 'A pipeta Pasteur de vidro é usada na transferência de líquidos em pequenos volumes em rotinas de laboratório, ensaios químicos e manuseio de soluções e amostras. Utilize com pera ou pipetador manual. Não indicada para medições volumétricas rigorosas.',
    'pipeta pasteur vidro conta gotas transferencia liquidos laboratorio')
grp('KLINE', lambda p: ('Placa de Kline de vidro com 12 escavações 6×8 cm (VDRL)', None),
    ['Suporte para o teste VDRL (floculação), triagem laboratorial da sífilis em soro ou líquor',
     'Vidro óptico especial de alta transparência', '12 cavidades: Ø 16 mm, profundidade 1,75 mm',
     'Dimensões da placa: 80 × 60 × 5 mm', 'Reutilizável: lavar e descontaminar após cada uso'],
    lambda it: 'A placa de Kline é o suporte padrão para o teste VDRL, com 12 escavações uniformes para conter amostra e reagente, adequada tanto à leitura macroscópica quanto à leitura ao microscópio. Armazene em local limpo e seco, manuseie com cuidado e faça a limpeza e descontaminação após cada uso.',
    'placa kline vdrl sifilis escavacoes vidro floculacao sorologia')
grp('BEFA', lambda p: (f'Copo Becker forma alta (Berzelius) borossilicato 3.3 graduado {cap(p)}', None),
    ['Vidro borossilicato 3.3, alta resistência térmica, química e a choques térmicos', 'Forma alta (tipo Berzelius), graduado, com bico vertedor', 'Conforme ISO 3819'],
    lambda it: f'O copo Becker forma alta de {cap(it["p"])} é indicado para reações químicas, dissolução de substâncias, aquecimento de líquidos e mistura de soluções. O formato alto (Berzelius) reduz respingos e facilita titulações e o uso em banho-maria.',
    'becker bequer copo forma alta berzelius vidro borossilicato boro 3.3 graduado vidraria laboratorio')
grp('BEFB', lambda p: (f'Copo Becker forma baixa (Griffin) borossilicato 3.3 graduado {cap(p)}', None),
    ['Vidro borossilicato 3.3, alta resistência térmica, química e a choques térmicos', 'Forma baixa (tipo Griffin), graduado, com bico vertedor', 'Conforme ISO 3819'],
    lambda it: f'O copo Becker forma baixa de {cap(it["p"])} é a vidraria de uso geral do laboratório: reações químicas, dissolução, aquecimento e mistura de soluções, com graduação para leitura aproximada de volume.',
    'becker bequer copo forma baixa griffin vidro borossilicato boro 3.3 graduado vidraria laboratorio')
grp('PROBPH', lambda p: (f'Proveta graduada de vidro borossilicato 3.3 com base hexagonal plástica {cap(p)}', None),
    ['Corpo em vidro borossilicato 3.3; base hexagonal em polipropileno, resistente a impactos',
     'Graduação permanente em toda a extensão do corpo', 'Bico vertedor'],
    lambda it: f'A proveta de {cap(it["p"])} mede volumes de líquidos com rapidez em procedimentos que não exigem alta precisão volumétrica. Use em superfície plana e faça a leitura do menisco na altura dos olhos.',
    'proveta cilindro graduado medicao volume vidro borossilicato boro 3.3 base plastica hexagonal vidraria')
grp('ERLBL', lambda p: (f'Frasco Erlenmeyer boca larga borossilicato 3.3 graduado {cap(p)}', None),
    ['Vidro borossilicato 3.3, alta resistência térmica e química', 'Boca larga e fundo plano; graduação aproximada'],
    lambda it: f'O Erlenmeyer de boca larga ({cap(it["p"])}) facilita a introdução de sólidos, a pipetagem, a retirada de amostras e a limpeza. Indicado para preparo de soluções, cultivo de microrganismos, titulações e reações em geral.',
    'erlenmeyer frasco conico boca larga vidro borossilicato boro 3.3 graduado vidraria laboratorio')
grp('ERLBE', lambda p: (f'Frasco Erlenmeyer boca estreita borossilicato 3.3 graduado {cap(p)}', None),
    ['Vidro borossilicato 3.3, alta resistência térmica e química', 'Boca estreita e fundo plano; graduação aproximada', 'Compatível com agitação magnética'],
    lambda it: f'O Erlenmeyer de boca estreita ({cap(it["p"])}) é indicado para preparo de soluções, titulações, cultivo de microrganismos e reações químicas; a boca estreita reduz a evaporação e facilita o manuseio de líquidos voláteis.',
    'erlenmeyer frasco conico boca estreita vidro borossilicato boro 3.3 graduado vidraria laboratorio')
grp('SISF', lambda p: (f'Sistema de filtração a vácuo em vidro borossilicato 3.3 com garra de alumínio — Erlenmeyer {cap(p)}', None),
    ['Frasco Erlenmeyer com junta esmerilhada e graduação', 'Funil de filtração com filtro de vidro sinterizado (Ø aprox. 40,5 mm) e conexão para vácuo (Ø externo 9 mm)',
     'Copo coletor de 300 mL com tampa de vedação', 'Garra de fixação em alumínio anodizado',
     'Membrana filtrante não inclusa (recomendada Ø 47 a 50 mm)', 'Temperatura máxima de operação: 200 °C; autoclavável'],
    lambda it: f'Conjunto completo para filtração a vácuo com Erlenmeyer de {cap(it["p"])}: separação e purificação de componentes em suspensão, retenção de partículas e ensaios de limite microbiano em água purificada. Conecte o sistema a uma bomba de vácuo e utilize a membrana adequada ao ensaio.',
    'sistema filtracao vacuo kitasato erlenmeyer funil membrana garra aluminio vidro borossilicato boro 3.3 vidraria')
grp('BLFD', lambda p: (f'Balão de destilação fundo redondo com saída lateral borossilicato 3.3 {cap(p)}', None),
    ['Vidro borossilicato 3.3, autoclavável a 121 °C', 'Saída lateral para condensador', 'Gravação permanente em tinta cerâmica branca com área para marcação',
     'Parede uniforme para aquecimento homogêneo (recomendado aquecimento lento)'],
    lambda it: f'O balão de destilação de {cap(it["p"])} é indicado para destilação, aquecimento e reações químicas; a geometria esférica distribui o calor de forma uniforme e a saída lateral permite a ligação direta ao condensador.',
    'balao destilacao fundo redondo saida lateral vidro borossilicato boro 3.3 vidraria')
grp('BFC', lambda p: (f'Balão de fundo chato borossilicato 3.3 gargalo longo com orla {cap(p)}', None),
    ['Vidro borossilicato 3.3, autoclavável a 121 °C', 'Gargalo longo com orla, sem junta esmerilhada', 'Base plana para apoio direto em bancada',
     'Gravação permanente em tinta cerâmica branca com área para marcação'],
    lambda it: f'O balão de fundo chato de {cap(it["p"])} é usado em aquecimentos, destilações, refluxo e reações com desprendimento gasoso. Utilize até a metade da capacidade durante ebulição e prefira aquecimento lento.',
    'balao fundo chato gargalo longo orla vidro borossilicato boro 3.3 vidraria')
grp('BRF', lambda p: (f'Balão de fundo redondo borossilicato 3.3 gargalo longo com orla {cap(p)}', None),
    ['Vidro borossilicato 3.3, autoclavável a 121 °C', 'Gargalo longo com orla, sem junta esmerilhada',
     'Compatível com mantas de aquecimento, bico de Bunsen e banhos termostáticos', 'Gravação permanente em tinta cerâmica branca com área para marcação'],
    lambda it: f'O balão de fundo redondo de {cap(it["p"])} é o recipiente principal em destilações e reações que liberam gases, com aquecimento uniforme. Apoie em suporte adequado, use até a metade da capacidade e aqueça lentamente.',
    'balao fundo redondo gargalo longo orla destilacao vidro borossilicato boro 3.3 vidraria')
grp('BVCA', lambda p: (f'Balão volumétrico classe A borossilicato 3.3 com rolha plástica {cap(p)}', None),
    ['Classe A (alta precisão), marca única de aferição calibrada a 20 °C', 'Vidro borossilicato 3.3; rolha de polietileno; junta esmerilhada',
     'Graduação permanente gravada em branco', 'Conforme ISO 1042', 'Não aquecer; não acompanha certificado individual de calibração'],
    lambda it: f'O balão volumétrico classe A de {cap(it["p"])} é usado no preparo preciso de soluções e diluições em laboratórios analíticos e de controle de qualidade. Não deve ser aquecido para não alterar o volume calibrado.',
    'balao volumetrico classe a aferido rolha vidro borossilicato boro 3.3 solucao padrao vidraria')
grp('BVAB', lambda p: (f'Balão volumétrico classe A âmbar borossilicato 3.3 com rolha plástica {cap(p)}', None),
    ['Classe A (alta precisão), marca única de aferição calibrada a 20 °C', 'Vidro borossilicato 3.3 âmbar (proteção contra luz); rolha de polietileno; junta esmerilhada',
     'Graduação permanente gravada em branco', 'Conforme ISO 1042', 'Não aquecer; não acompanha certificado individual de calibração'],
    lambda it: f'O balão volumétrico âmbar classe A de {cap(it["p"])} é indicado para o preparo preciso de soluções fotossensíveis. Não deve ser aquecido para não alterar o volume calibrado.',
    'balao volumetrico ambar classe a aferido rolha vidro borossilicato boro 3.3 fotossensivel vidraria')
grp('FUHC', lambda p: (f'Funil analítico liso de vidro haste curta Ø {p.split("/")[0]} mm — {p.split("/")[1]} mL', None),
    ['Vidro neutro resistente a agentes químicos', 'Haste curta, ângulo do cone de 60° (compatível com papéis de filtro circulares dobrados)', 'Ponta chanfrada para escoamento sem refluxo'],
    lambda it: 'Funil analítico para filtração gravitacional e separação sólido-líquido com papel de filtro, também útil na transferência de líquidos em rotinas de laboratório.',
    'funil analitico liso haste curta filtracao papel filtro vidro vidraria')
grp('FUHL', lambda p: (f'Funil analítico liso de vidro haste longa Ø {p.split("/")[0]} mm — {p.split("/")[1]} mL', None),
    ['Vidro neutro resistente a agentes químicos', 'Haste longa, ângulo do cone de 60° (compatível com papéis de filtro circulares dobrados)', 'Ponta chanfrada para escoamento sem refluxo'],
    lambda it: 'Funil analítico de haste longa para filtração gravitacional com papel de filtro; a haste longa otimiza o fluxo do filtrado e preserva a integridade da amostra.',
    'funil analitico liso haste longa filtracao papel filtro vidro vidraria')
grp('FUTP', lambda p: (f'Funil de separação tipo pera (Squibb) borossilicato 3.3 com torneira de PTFE {cap(p)}', None),
    ['Vidro borossilicato 3.3, elevada resistência térmica e química', 'Torneira de PTFE (Teflon®) e rolha superior de polietileno', 'Formato de pera alongada (Squibb), desmontável para limpeza'],
    lambda it: f'O funil de separação de {cap(it["p"])} (também chamado funil de decantação ou de bromo) é usado na separação de líquidos imiscíveis, extrações líquido-líquido e decantação, com escoamento controlado da fase inferior.',
    'funil separacao decantacao bromo pera squibb torneira teflon ptfe vidro borossilicato boro 3.3 vidraria')
grp('TUBO', lambda p: (f'Tubo de ensaio de vidro borossilicato {p.split("/")[0]} mm — caixa c/ {p.split("/")[1]} un', int(p.split('/')[1])),
    ['Vidro borossilicato, fundo redondo, sem orla', 'Parede de aprox. 1 mm', 'Autoclavável; resistência térmica de -10 °C a 160 °C', 'Não estéril'],
    lambda it: 'Tubo de ensaio de vidro para armazenamento de material biológico e ensaios bioquímicos, sorológicos e imunoensaios. Reutilizável e compatível com esterilização em autoclave.',
    'tubo ensaio vidro borossilicato fundo redondo sem orla sorologia autoclavavel vidraria')
grp('TUBOB', lambda p: (f'Tubo de ensaio de vidro borossilicato {p.split("/")[0]} mm com tampa de rosca de baquelite — caixa c/ {p.split("/")[1]} un', int(p.split('/')[1])),
    ['Vidro borossilicato, parede de aprox. 1 mm; resistência de -30 °C a 160 °C', 'Tampa de rosca em baquelite com batoque de silicone para vedação',
     'Autoclavável e compatível com calor seco', 'Reutilizável'],
    lambda it: 'Tubo de vidro com tampa de rosca para armazenamento e processamento de amostras líquidas em cultura celular, microbiologia e análises clínicas, com excelente vedação e resistência a variações térmicas.',
    'tubo ensaio vidro tampa rosca baquelite batoque silicone borossilicato microbiologia meio cultura autoclavavel vidraria')
grp('PSORO', lambda p: (f'Pipeta sorológica de vidro {p.split("/")[0]} mL — graduada {p.split("/", 1)[1]} — caixa c/ 10 un', 10),
    ['Vidro soda, não estéril, autoclavável (121 °C por 15 min)', 'Bocal e bico temperados; esgotamento total; gravação permanente',
     'Conforme ISO 835', 'Compatível com a maioria dos pipetadores', 'Embalagem: caixa com 10 un'],
    lambda it: 'Pipeta sorológica graduada de vidro para transferência e medição de volumes de líquidos em sorologia, bioquímica e rotinas gerais de laboratório. Reutilizável após limpeza e esterilização.',
    'pipeta sorologica graduada vidro reutilizavel transferencia volume vidraria')
grp('FRABLRV', lambda p: (f'Frasco reagente âmbar boca larga com rolha de vidro {cap(p)}', None),
    ['Vidro neutro âmbar (proteção contra a luz)', 'Boca larga com rolha de vidro', 'Autoclavável'],
    lambda it: f'Frasco reagente âmbar de {cap(it["p"])} para armazenamento e manuseio seguro de reagentes, soluções e substâncias sólidas ou líquidas fotossensíveis.',
    'frasco reagente ambar boca larga rolha vidro armazenamento fotossensivel vidraria')
grp('PETRI', lambda p: (f'Placa de Petri de vidro borossilicato 3.3 {p.split("/")[0]} mm — caixa c/ {p.split("/")[1]} un', int(p.split('/')[1])),
    ['Vidro borossilicato 3.3 (tampa + base), resistente a variações térmicas', 'Autoclavável a 121 °C por 15 min, reutilizável',
     'Superfície lisa e bordas lapidadas para manuseio seguro'],
    lambda it: 'Placa de Petri de vidro para cultivo e identificação de microrganismos em microbiologia e bacteriologia, reutilizável após esterilização em autoclave.',
    'placa petri vidro borossilicato boro 3.3 microbiologia cultura autoclavavel reutilizavel vidraria')
grp('VIDRL', lambda p: (f'Vidro de relógio lapidado Ø {p} mm', None),
    ['Vidro neutro de boa resistência química', 'Bordas lapidadas e arredondadas; formato côncavo', 'Reutilizável; não autoclavável'],
    lambda it: 'O vidro de relógio serve de suporte para pesagens em balança analítica, evaporação de líquidos e pequenas reações, e como cobertura de béqueres para reduzir contaminação e evaporação.',
    'vidro relogio lapidado pesagem evaporacao cobertura becker vidraria')
grp('KITA', lambda p: (f'Frasco Kitasato com saída superior borossilicato 3.3 {cap(p)}', None),
    ['Vidro borossilicato 3.3 de parede espessa, próprio para vácuo', 'Saída lateral superior para mangueira de látex ou silicone', 'Graduado; autoclavável'],
    lambda it: f'O frasco Kitasato de {cap(it["p"])} é usado em filtrações a vácuo, em conjunto com funil de Büchner e membranas filtrantes. Manuseie com suporte e controle de pressão adequados e inspecione o vidro antes do uso.',
    'kitasato kitazato frasco vacuo filtracao buchner saida lateral vidro borossilicato boro 3.3 vidraria')
grp('FRITR', lambda p: (f'Frasco reagente borossilicato 3.3 incolor com tampa de rosca azul GL 45 graduado {cap(p)}', None),
    ['Vidro borossilicato 3.3; graduação permanente', 'Tampa de rosca azul em polipropileno com anel de vedação (anti-gotas), padrão GL 45',
     'Conforme ISO 4796; autoclavável'],
    lambda it: f'O frasco reagente de {cap(it["p"])} armazena e transporta reagentes, soluções, meios de cultura e amostras, com vedação segura e excelente visibilidade do conteúdo.',
    'frasco reagente schott tampa rosca azul gl45 graduado incolor vidro borossilicato boro 3.3 meio cultura vidraria')
grp('BURE', lambda p: (f'Bureta graduada classe A com torneira de PTFE {cap(p)}', None),
    ['Classe A (alta precisão), vidro borossilicato 3.3', 'Torneira de PTFE (Teflon®)', 'Totalmente graduada', 'Não acompanha certificado individual de calibração'],
    lambda it: f'A bureta de {cap(it["p"])} faz a dosagem controlada de líquidos em titulações e análises volumétricas. Use na vertical, fixada em suporte universal com garra.',
    'bureta classe a titulacao torneira teflon ptfe vidro borossilicato volumetrica vidraria')
grp('PVO', lambda p: (f'Pipeta volumétrica classe A de esgotamento total (1 traço) {cap(p)}', None),
    ['Classe A (alta precisão), vidro borossilicato 3.3', 'Marca única de calibração, esgotamento total', 'Marcação permanente em âmbar',
     'Usar com pipetador; não acompanha certificado individual de calibração'],
    lambda it: f'A pipeta volumétrica de {cap(it["p"])} mede e transfere com exatidão um volume fixo de líquido em procedimentos analíticos e de preparo de soluções.',
    'pipeta volumetrica classe a esgotamento total um traco aferida vidro borossilicato vidraria')
grp('FRATR', lambda p: (f'Frasco reagente âmbar com tampa de rosca azul graduado {cap(p)}', None),
    ['Vidro neutro âmbar (proteção contra a luz)', 'Tampa de rosca azul em polipropileno com anel de vedação (anti-gotas)', 'Graduado; autoclavável'],
    lambda it: f'Frasco reagente âmbar de {cap(it["p"])} para armazenar substâncias químicas, soluções, meios de cultura e amostras fotossensíveis com vedação segura.',
    'frasco reagente ambar tampa rosca azul graduado vidro fotossensivel vidraria')
grp('DV', lambda p: (f'Dessecador de vidro com tampa, torneira e disco de porcelana Ø {p} mm', None),
    ['Vidro borossilicato espesso', 'Tampa com vedação hermética e torneira para bomba de vácuo', 'Disco de porcelana perfurado para apoio dos recipientes',
     'Usar com agente dessecante (sílica gel, cloreto de cálcio etc.)'],
    lambda it: 'O dessecador preserva substâncias e materiais sensíveis à umidade em ambiente seco, com dessecante e, quando necessário, vácuo. Garanta o assentamento correto da tampa para a vedação.',
    'dessecador vidro vacuo torneira disco porcelana silica umidade vidraria')

# ---------------------------------------------------------------- leitura
itens = []
for ln in open(DADOS, encoding='utf-8'):
    if not ln.startswith(tuple('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ')):
        continue
    f = ln.rstrip('\n').split('|')
    cod, g, p, preco, est, un, ean, pb, a, l, cp, specs = f
    gd = G[g]
    nome, qtd = gd['nome'](p if g != 'MIC' else cod)
    custo = float(preco)
    fator = 1.5 if g == 'MIC' else 1.4
    venda = float((Decimal(preco) * Decimal(str(fator))).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP))
    fic = [gd['base'][0]] if g != 'MIC' else []
    if g == 'MIC':
        fic = [s for s in specs.split(';') if s] + gd['base']
    else:
        if g not in ('KLINE', 'PASTEUR', 'TUBO', 'TUBOB', 'PSORO', 'PETRI', 'SISF', 'FUHC', 'FUHL', 'VIDRL', 'DV'):
            fic.append('Capacidade: ' + cap(p))
        if g in ('FUHC', 'FUHL'):
            d, v = p.split('/')
            fic.append(f'Diâmetro externo: {d} mm; capacidade: {v} mL')
        if g == 'VIDRL':
            fic.append(f'Diâmetro externo: {p} mm')
        if g == 'DV':
            fic.append(f'Diâmetro externo: {p} mm')
        if g in ('TUBO', 'TUBOB'):
            fic.append('Dimensões: ' + p.split('/')[0] + ' mm (diâmetro × altura)')
        if g == 'PETRI':
            fic.append('Medidas aproximadas: ' + p.split('/')[0] + ' mm (diâmetro × altura, tampa + base)')
        fic += [s for s in specs.split(';') if s]
        fic += gd['base'][1:]
    if qtd and not any(x.startswith('Embalagem') for x in fic):
        fic.append(f'Embalagem: caixa com {qtd} un')
    fic.append('Marca: CRAL')
    it = dict(cod=cod, g=g, p=p, nome=nome, qtd=qtd, custo=custo, venda=venda, est=int(est or 0),
              pb=num(pb), a=num(a), l=num(l), cp=num(cp), ficha=fic, cat=gd['cat'])
    foto = None if cod in SEM_FOTO else IMG_CRAL % FOTO_IRMA.get(cod, cod)
    it['img'] = foto or LOGO
    it['sobre'] = gd['sobre'](it)
    it['slug'] = slugify(nome, cod)
    it['url'] = f'{SITE}/p/{it["slug"]}.html'
    itens.append(it)

print('itens lidos:', len(itens))

# ---------------------------------------------------------------- checagens
idx_path = R + 'index.html'
idx = open(idx_path, encoding='utf-8').read()
dec = json.JSONDecoder()
i0 = idx.find('var SEED=') + len('var SEED=')
seed, fim = dec.raw_decode(idx[i0:])
ja = {o['c'].upper() for o in seed}
novos = [it for it in itens if it['cod'].upper() not in ja]
pulados = [it['cod'] for it in itens if it['cod'].upper() in ja]
if pulados:
    print('JÁ EXISTEM (não mexo):', pulados)
itens = novos
for it in itens:
    assert not os.path.exists(R + 'p/' + it['slug'] + '.html'), it['slug']

# ---------------------------------------------------------------- frete (CSV + proposta Worker)


def frete(it):
    vidro = it['g'] != 'MIC'
    kg = max(0.1, it['pb'] * 1.15) + (0.1 if vidro else 0)
    kg = math.ceil(kg * 100 - 1e-9) / 100
    dims = [max(2, math.ceil(x * 100 * 1.15 - 1e-9)) for x in (it['a'], it['l'], it['cp'])]
    return [kg] + dims


with open(CSV_FRETE, 'w', newline='', encoding='utf-8') as fh:
    w = csv.writer(fh)
    w.writerow(['codigo', 'kg', 'altura', 'largura', 'comprimento', 'preco', 'custo'])
    w.writerow(['EV21', 0.4, 8, 15, 20, '29.23', '20.88'])
    for it in itens:
        k, a, l, c = frete(it)
        w.writerow([it['cod'], k, a, l, c, f'{it["venda"]:.2f}', f'{it["custo"]:.2f}'])

# ---------------------------------------------------------------- index.html
seed_new = [{'c': it['cod'], 'n': it['nome'], 'm': 'CRAL', 'k': it['cat'][0], 'img': it['img']} for it in itens]
seed_txt = idx[i0:i0 + fim]
assert seed_txt.endswith('}]')
novo_seed = seed_txt[:-1] + ',' + ','.join(json.dumps(o, ensure_ascii=False, separators=(',', ':')) for o in seed_new) + ']'
idx = idx[:i0] + novo_seed + idx[i0 + fim:]

j0 = idx.find('window.PRECOS=') + len('window.PRECOS=')
pre, pfim = dec.raw_decode(idx[j0:])
ptxt = idx[j0:j0 + pfim]
assert ptxt.endswith('}')
adic = ', '.join(f'"{it["cod"]}": [{it["venda"]:.2f}, {it["venda"]:.2f}, null]' for it in itens)
idx = idx[:j0] + ptxt[:-1] + ', ' + adic + '}' + idx[j0 + pfim:]

q0 = idx.find('window.QTD=') + len('window.QTD=')
qd, qfim = dec.raw_decode(idx[q0:])
qtxt = idx[q0:q0 + qfim]
adq = ','.join(f'"{it["cod"]}":[{it["qtd"]},"unidade","caixa"]' for it in itens if it['qtd'])
idx = idx[:q0] + qtxt[:-1] + ',' + adq + '}' + idx[q0 + qfim:]

dep_old = "  {key:'equip', nome:'Equipamentos e acessórios', icon:'🖥️', cats:['equip']}\n];"
assert dep_old in idx
idx = idx.replace(dep_old, "  {key:'equip', nome:'Equipamentos e acessórios', icon:'🖥️', cats:['equip']},\n  {key:'vidraria', nome:'Vidraria de laboratório', icon:'⚗️', cats:['vidraria']}\n];", 1)
row_old = "  ['Equipamentos e acessórios',['equip'],'equip']\n ];"
assert row_old in idx
idx = idx.replace(row_old, "  ['Equipamentos e acessórios',['equip'],'equip'],\n  ['Vidraria de laboratório',['vidraria'],'vidraria']\n ];", 1)
tub = '<a href="/categoria/tubos-a-vacuo.html">Tubos a vácuo</a>'
assert idx.count(tub) == 1
idx = idx.replace(tub, tub + '<a href="/categoria/vidraria-de-laboratorio.html">Vidraria de laboratório</a>', 1)
open(idx_path, 'w', encoding='utf-8').write(idx)

# ---------------------------------------------------------------- kw.json / ft.json
STOP = {'de', 'do', 'da', 'com', 'e', 'para', 'p', 'c', 'un', 'em', 'o', 'a', 'mm', 'ml'}


def kw_de(it):
    t = sem_acento((it['nome'] + ' ' + G[it['g']]['kw'] + ' cral').lower())
    t = t.replace('×', 'x')
    toks = set(x.strip('.,/') for x in re.split(r'[^a-z0-9.,/]+', t))
    toks = set(x for x in toks if x and x not in STOP and x != 'c/')
    toks |= {x.replace('.', '') for x in toks if '.' in x}
    m = re.search(r'(\d+) ml', sem_acento(it['nome'].lower()))
    if m:
        toks.add(m.group(1) + 'ml')
    c = it['cod'].lower()
    extra = [c]
    m2 = re.match(r'^([a-z]+)(\d.*)$', c)
    if m2:
        extra.append(m2.group(1) + '-' + m2.group(2))
    if '-' in c:
        extra.append(c.replace('-', ''))
    return ' '.join(sorted(toks - set(extra))) + ' ' + ' '.join(dict.fromkeys(extra))


kw = json.load(open(R + 'kw.json', encoding='utf-8'))
ft = json.load(open(R + 'ft.json', encoding='utf-8'))
for it in itens:
    kw[it['cod']] = kw_de(it)
    ft[it['cod']] = ' · '.join(x.rstrip('.') + '.' for x in it['ficha'])
json.dump(kw, open(R + 'kw.json', 'w', encoding='utf-8'), ensure_ascii=False, separators=(',', ':'))
json.dump(ft, open(R + 'ft.json', 'w', encoding='utf-8'), ensure_ascii=False, separators=(',', ':'))

# ---------------------------------------------------------------- páginas de produto
tpl = open(R + 'p/escalpe-para-coleta-de-sangue-a-vacuo-21g-com-tubo-de-7-ev21.html', encoding='utf-8').read()
STYLE = tpl[tpl.find('<style>'):tpl.find('</head>')]
STYLE = STYLE.replace("item_id:'EV21'", "item_id:'%COD%'")
STYLE = STYLE.replace('</style>', 'table.fam{width:100%;border-collapse:collapse;background:#fff;border-radius:10px;overflow:hidden;box-shadow:0 4px 16px rgba(20,40,70,.06);font-size:13px;margin:8px 0 4px}\ntable.fam th{background:#f5f8fc;color:#1f3a5f;text-align:left;padding:8px 10px;font-size:12px}\ntable.fam td{padding:8px 10px;border-top:1px solid #eef2f7}\ntable.fam tr.cur{background:#eef7f1;font-weight:700}\ntable.fam a{color:#1f3a5f;text-decoration:none;font-weight:700}</style>', 1)
FOOT = tpl[tpl.find('<footer class="siteftr">'):]
RETURN = {"@type": "MerchantReturnPolicy", "applicableCountry": "BR", "returnPolicyCategory": "https://schema.org/MerchantReturnFiniteReturnWindow", "merchantReturnDays": 7, "returnMethod": "https://schema.org/ReturnByMail", "returnFees": "https://schema.org/FreeReturn", "refundType": "https://schema.org/FullRefund", "merchantReturnLink": SITE + "/trocas-e-devolucoes.html"}
por_grupo = {}
for it in itens:
    por_grupo.setdefault(it['g'], []).append(it)


def emb_txt(it):
    return f'caixa c/ {it["qtd"]} un' if it['qtd'] else 'unidade'


def card(o):
    n = html.escape(o['nome'])
    return f'<a class="rc" href="{o["url"]}"><img src="{o["img"]}" alt="{n}" loading="lazy" width="160" height="160"><span class="rn">{n}</span><b class="rp">{brl(o["venda"])}</b><span class="rv">Ver produto</span></a>'


def pagina(it):
    cod, n = it['cod'], it['nome']
    ne = html.escape(n)
    curto = re.split(r' — (?:caixa|pacote|rack) c/', n)[0]
    titulo = f'{curto} CRAL | SULLAB'
    catk, catn, cats = it['cat']
    v = it['venda']
    if it['qtd']:
        un = v / it['qtd']
        un_txt = brl(un) if un >= 0.01 else 'R$ ' + f'{un:.4f}'.replace('.', ',')
        desc = f'{n} CRAL: {emb_txt(it)}. por {brl(v)} ({un_txt} por unidade) no CNPJ, com NF-e e entrega para todo o Brasil. Compre no site com desconto no Pix.'
        pfx = f'por {emb_txt(it)}. · <b>{un_txt} por unidade</b> · empresas (CNPJ), com NF-e'
    else:
        desc = f'{n} CRAL: unidade por {brl(v)} no CNPJ, com NF-e e entrega para todo o Brasil. Compre no site com desconto no Pix.'
        pfx = 'por unidade · empresas (CNPJ), com NF-e'
    de = html.escape(desc)
    fdesc = ' · '.join(x.rstrip('.') + '.' for x in it['ficha'])
    prod = {"@context": "https://schema.org/", "@type": "Product", "name": n, "sku": cod, "category": catn, "description": fdesc,
            "brand": {"@type": "Brand", "name": "CRAL"},
            "offers": {"@type": "Offer", "priceCurrency": "BRL", "price": f'{v:.2f}', "availability": "https://schema.org/InStock", "url": it['url'],
                       "itemCondition": "https://schema.org/NewCondition", "seller": {"@type": "Organization", "name": "SULLAB"}, "hasMerchantReturnPolicy": RETURN},
            "image": it['img'], "mpn": cod}
    bc = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Início", "item": SITE + "/"},
        {"@type": "ListItem", "position": 2, "name": catn, "item": f'{SITE}/categoria/{cats}.html'},
        {"@type": "ListItem", "position": 3, "name": n, "item": it['url']}]}
    img = it['img']
    gal = (f'<div class="gal"><div class="ph" id="ph" style="background-image:url(\'{img}\')"></div><div class="th"><button type="button" class="on" aria-label="Foto do produto" '
           f'onclick="var p=document.getElementById(\'ph\');p.style.backgroundImage=&quot;url(\'{img}\')&quot;;var b=this.parentNode.children;for(var i=0;i<b.length;i++)b[i].className=\'\';this.className=\'on\'">'
           f'<img src="{img}" alt="Foto do produto" loading="lazy" width="800" height="800"></button></div></div>')
    ficha = '<br>'.join(html.escape(x.rstrip('.') + '.') for x in it['ficha'])
    irm = por_grupo[it['g']]
    fam = ''
    if len(irm) > 1:
        linhas = ''.join(
            (f'<tr class="cur"><td>{html.escape(o["nome"])}</td><td>{"—" if not o["qtd"] else emb_txt(o)}</td><td>{brl(o["venda"])}</td><td>Você está aqui</td></tr>' if o is it else
             f'<tr><td>{html.escape(o["nome"])}</td><td>{"—" if not o["qtd"] else emb_txt(o)}</td><td>{brl(o["venda"])}</td><td><a href="{o["url"]}">Ver opção →</a></td></tr>')
            for o in irm)
        fam = f'<h2>Outras opções desta linha</h2><table class="fam"><thead><tr><th>Variante</th><th>Embalagem</th><th>Preço CNPJ</th><th></th></tr></thead><tbody>{linhas}</tbody></table>'
    k = irm.index(it)
    viz = [o for o in irm if o is not it]
    viz.sort(key=lambda o: abs(irm.index(o) - k))
    rel = viz[:6]
    if len(rel) < 6:
        outros = [o for o in itens if o['g'] != it['g'] and o['cat'] == it['cat']]
        rel += outros[:6 - len(rel)]
    rel_html = '\n'.join(card(o) for o in rel)
    return f'''<!DOCTYPE html><html lang="pt-BR"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(titulo)}</title>
<meta name="description" content="{de}">
<link rel="canonical" href="{it['url']}">
<meta name="robots" content="index,follow">
<meta property="og:type" content="product"><meta property="og:title" content="{html.escape(titulo)}">
<meta property="og:description" content="{de}">
<meta property="og:image" content="{img}">
<meta property="og:url" content="{it['url']}">

<script type="application/ld+json">{json.dumps(prod, ensure_ascii=False)}</script>
<script type="application/ld+json">{json.dumps(bc, ensure_ascii=False)}</script>
{STYLE.replace('%COD%', cod)}</head><body>
<div class="wrap">
<div class="top"><img src="{SITE}/og-sullab.png" alt="SULLAB" width="65" height="34"><a href="{SITE}/">SULLAB</a></div>
<div class="crumb"><a href="{SITE}/">Início</a> › <a href="{SITE}/categoria/{cats}.html">{catn}</a> › {ne}</div>
<div class="card">
{gal}
<div>
<h1>{ne}</h1>
<div class="brand"><b>Marca:</b> CRAL · <b>Código:</b> {cod}</div><div class="preco" style="margin:10px 0;padding:10px 12px;background:#f4f7fb;border-radius:8px;font-size:15px">💰 <b>{brl(v)}</b> <span class="pfx" style="color:#5a6472;font-weight:400;font-size:13px">{pfx}</span><br><span class="pfx" style="color:#5a6472;font-weight:400;font-size:13px">Frete calculado pelo CEP na loja; grátis automático em pedidos que atingem o valor mínimo.</span></div><div class="tb"><span>🧾 NF-e em todo pedido</span><span>🚚 Envio em 24h</span></div><a class="trocaslk" href="{SITE}/trocas-e-devolucoes.html">Ver política de trocas e devoluções</a><div class="ficha">🔬 <b>Ficha técnica</b><br>{ficha}</div>
<a class="btn-whats" style="background:#2f9e63" href="{SITE}/?carrinho={cod}:1">🛒 Comprar agora</a><a class="btn" href="{SITE}/?q={cod}">Ver na loja →</a>
<div>
<a class="btn2" href="{SITE}/categoria/{cats}.html">Ver {catn}</a>
<a class="btn2" href="{SITE}/marca/cral.html">Ver produtos CRAL</a>
</div>

</div></div>
<h2>Sobre o produto</h2><p class="lead">{html.escape(it['sobre'])}</p>
{fam}<h2>Produtos relacionados</h2><div class="rel rcards">
{rel_html}
</div>
{FOOT}'''


for it in itens:
    open(R + 'p/' + it['slug'] + '.html', 'w', encoding='utf-8').write(pagina(it))

# ---------------------------------------------------------------- categorias
vid = [it for it in itens if it['cat'] == CAT_VID]
mic = [it for it in itens if it['cat'] == CAT_EQP]


def grid_a(it):
    return f'<a href="{it["url"]}"><span class="nm">{html.escape(it["nome"][:70].rstrip())}</span><span class="pr">{brl(it["venda"])} <small>CNPJ</small></span><span class="cs">cód. {it["cod"]}</span></a>'


# equipamentos: acrescenta os microscópios
ep = R + 'categoria/equipamentos-e-acessorios.html'
e = open(ep, encoding='utf-8').read()
n_old = e.count('<div class="grid">\n') and len(re.findall(r'<a href="[^"]+"><span class="nm">', e))
n_new = n_old + len(mic)
e = e.replace(f'{n_old} itens em estoque', f'{n_new} itens em estoque')
e = e.replace(f'Produtos de Equipamentos e acessórios ({n_old})', f'Produtos de Equipamentos e acessórios ({n_new})')
m = re.search(r'("@type": "ItemList", "itemListElement": )(\[.*?\])(\})', e)
lst = json.loads(m.group(2))
for it in mic:
    lst.append({"@type": "ListItem", "position": len(lst) + 1, "url": it['url'], "name": it['nome']})
e = e[:m.start(2)] + json.dumps(lst, ensure_ascii=False) + e[m.end(2):]
gi = e.find('<div class="grid">\n')
ge = e.find('</div>', gi)
e = e[:ge] + '\n'.join(grid_a(it) for it in mic) + '\n' + e[ge:]
e = e.replace('<p>Categoria de equipamentos e acessórios de bancada — da câmara de Neubauer (contagem manual de células) a soluções',
              '<p>Categoria de equipamentos e acessórios de bancada — de microscópios biológicos e estereoscópios à câmara de Neubauer (contagem manual de células) e soluções', 1)
cmp_old = '</tbody></table></div><h2>Produtos de Equipamentos'
mic_rows = ''.join(f'<tr><td><b>{html.escape(it["nome"].split(" — ")[0])}</b></td><td>{"Inspeção com aumento de 20X a 80X" if it["cod"] == "MIBEST" else "Microscopia de campo claro" + (" e contraste de fase" if it["cod"] == "MICB-20" else "")}</td><td>unidade</td><td><a href="{it["url"]}">Ver produto →</a></td></tr>' for it in mic)
assert cmp_old in e
e = e.replace(cmp_old, mic_rows + cmp_old, 1)
open(ep, 'w', encoding='utf-8').write(e)

# vidraria: página nova a partir do modelo de equipamentos
cp_ = R + 'categoria/vidraria-de-laboratorio.html'
assert not os.path.exists(cp_)
e0 = open(R + 'categoria/equipamentos-e-acessorios.html', encoding='utf-8').read()
head_style = e0[e0.find('<style>'):e0.find('</head>')]
foot = e0[e0.find('<footer class="siteftr">'):]
URLC = SITE + '/categoria/vidraria-de-laboratorio.html'
nV = len(vid)
DESC_C = f'Vidraria de laboratório em vidro borossilicato 3.3: béqueres, provetas, Erlenmeyer, balões, pipetas, buretas, funis, frascos reagente, tubos e placas de Petri. Preço CNPJ, NF-e e entrega para todo o Brasil. {nV} itens em estoque.'
faq = [("Qual a diferença entre vidro borossilicato 3.3 e vidro neutro/soda?", "O borossilicato 3.3 tem baixo coeficiente de dilatação, por isso resiste melhor a choques térmicos, aquecimento e autoclave, além de ter alta resistência química. O vidro neutro ou soda atende bem a usos sem aquecimento intenso, como funis, vidros de relógio e pipetas sorológicas."),
       ("Vidraria classe A acompanha certificado de calibração?", "Os balões volumétricos, buretas e pipetas volumétricas classe A seguem as tolerâncias da norma, mas não acompanham certificado individual de calibração. Recomenda-se a calibração periódica conforme o controle de qualidade do laboratório."),
       ("Posso aquecer balão volumétrico ou proveta?", "Não. Vidraria volumétrica de medição (balão volumétrico, pipeta, bureta e proveta) não deve ser aquecida, pois o calor pode alterar o volume calibrado. Para aquecer, use béquer, Erlenmeyer ou balão de fundo redondo/chato."),
       ("A vidraria é vendida por unidade?", "Sim. Béqueres, provetas, Erlenmeyer, balões, funis, frascos, buretas e pipetas volumétricas são vendidos por unidade. Tubos de ensaio, pipetas Pasteur, pipetas sorológicas e placas de Petri de vidro são vendidos por caixa, com a quantidade indicada em cada produto.")]
faq_ld = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faq]}
bc_ld = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [{"@type": "ListItem", "position": 1, "name": "Início", "item": SITE + "/"}, {"@type": "ListItem", "position": 2, "name": "Vidraria de laboratório", "item": URLC}]}
il_ld = {"@context": "https://schema.org", "@type": "ItemList", "itemListElement": [{"@type": "ListItem", "position": i + 1, "url": it['url'], "name": it['nome']} for i, it in enumerate(vid)]}
tipos = [('BEFB', 'Copo Becker forma baixa (Griffin)', 'Reações, dissolução, aquecimento e mistura'), ('BEFA', 'Copo Becker forma alta (Berzelius)', 'Titulações e aquecimento com menos respingos'),
         ('PROBPH', 'Proveta graduada', 'Medição rápida de volumes'), ('ERLBE', 'Erlenmeyer boca estreita', 'Preparo de soluções e titulações'), ('ERLBL', 'Erlenmeyer boca larga', 'Cultivo e adição de sólidos'),
         ('BVCA', 'Balão volumétrico classe A', 'Preparo preciso de soluções'), ('PVO', 'Pipeta volumétrica classe A', 'Transferência exata de volume fixo'), ('BURE', 'Bureta classe A', 'Titulação'),
         ('KITA', 'Frasco Kitasato', 'Filtração a vácuo'), ('FUTP', 'Funil de separação', 'Extração líquido-líquido'), ('TUBO', 'Tubo de ensaio de vidro', 'Ensaios, sorologia e armazenamento'),
         ('PETRI', 'Placa de Petri de vidro', 'Microbiologia (reutilizável)')]
cmp_rows = ''
for g, t, u in tipos:
    o = por_grupo.get(g)
    if o:
        cmp_rows += f'<tr><td><b>{t}</b></td><td>{u}</td><td>{"caixa" if o[0]["qtd"] else "unidade"}</td><td><a href="{o[0]["url"]}">Ver opções →</a></td></tr>'
corpo = f'''<!DOCTYPE html><html lang="pt-BR"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Vidraria de laboratório: preço CNPJ e NF-e | SULLAB</title>
<meta name="description" content="{html.escape(DESC_C)}">
<link rel="canonical" href="{URLC}">
<meta name="robots" content="index,follow">
<meta property="og:type" content="website"><meta property="og:title" content="Vidraria de laboratório: preço CNPJ e NF-e | SULLAB">
<meta property="og:description" content="{html.escape(DESC_C)}">
<meta property="og:url" content="{URLC}">

<script type="application/ld+json">{json.dumps(bc_ld, ensure_ascii=False)}</script>
<script type="application/ld+json">{json.dumps(faq_ld, ensure_ascii=False)}</script>
<script type="application/ld+json">{json.dumps(il_ld, ensure_ascii=False)}</script>
{head_style}</head><body>
<div class="wrap">
<div class="top"><img src="{SITE}/og-sullab.png" alt="SULLAB" width="65" height="34"><a href="{SITE}/">SULLAB</a></div>
<div class="crumb"><a href="{SITE}/">Início</a> › Vidraria de laboratório</div>
<h1>Vidraria de laboratório</h1>
<p class="lead">Vidraria de laboratório CRAL em vidro borossilicato 3.3 e vidro neutro: béqueres, provetas, Erlenmeyer, balões volumétricos e de destilação, pipetas, buretas, funis, frascos reagente, Kitasato, dessecadores, tubos de ensaio e placas de Petri. A SULLAB é distribuidora de produtos para laboratório e diagnóstico clínico, com preço para CNPJ, nota fiscal (NF-e) e entrega para todo o Brasil. Veja abaixo os itens de <b>vidraria de laboratório</b> disponíveis.</p>
<a class="btn" href="{SITE}/?cat=vidraria">Ver na loja e montar orçamento →</a><div class="tb"><span>🧾 NF-e</span><span>💰 Preço CNPJ</span><span>🚚 Envio 24h</span><span>🏭 Sem taxa de marketplace</span></div><div id="b3categoria" class="b3cat"><p>Vidraria para rotina analítica, microbiologia, bioquímica e ensino. Para aquecimento, autoclave e choques térmicos, prefira as peças em <b>borossilicato 3.3</b>; para medições exatas, use a vidraria volumétrica <b>classe A</b> (balão volumétrico, pipeta volumétrica e bureta), que não deve ser aquecida. Provetas e béqueres graduados servem para medições aproximadas.</p><table class="cmp"><thead><tr><th>Tipo</th><th>Para que serve</th><th>Embalagem</th><th>Link</th></tr></thead><tbody>{cmp_rows}</tbody></table></div><h2>Produtos de Vidraria de laboratório ({nV})</h2>
<div class="grid">
{chr(10).join(grid_a(it) for it in vid)}
</div>
<h2>Perguntas frequentes</h2><div class="faq">{''.join(f'<details><summary>{html.escape(q)}</summary><p>{html.escape(a)}</p></details>' for q, a in faq)}</div>
{foot}'''
open(cp_, 'w', encoding='utf-8').write(corpo)

# ---------------------------------------------------------------- marca/cral.html
mp = R + 'marca/cral.html'
mk = open(mp, encoding='utf-8').read()
mm = re.search(r'<h2>Itens CRAL \((\d+)\)</h2>\n<div class="grid">\n(.*?)\n</div>', mk, re.S)
n0 = int(mm.group(1))
linhas = mm.group(2).split('\n')


def nome_l(l):
    return html.unescape(re.sub('<[^>]+>', '', l))


# a lista existente é só parcialmente ordenada: insere cada item novo antes do primeiro nome maior, sem reordenar os existentes
for it in sorted(itens, key=lambda o: o['nome']):
    nm = it['nome'] if len(it['nome']) <= 90 else it['nome'][:70]
    novo = f'<a href="{it["url"]}">{html.escape(nm)}</a>'
    pos = next((k for k, l in enumerate(linhas) if l.strip() and nome_l(l) > it['nome']), len(linhas))
    linhas.insert(pos, novo)
n1 = n0 + len(itens)
mk = mk[:mm.start()] + f'<h2>Itens CRAL ({n1})</h2>\n<div class="grid">\n' + '\n'.join(linhas) + '\n</div>' + mk[mm.end():]
mk = mk.replace(f'SULLAB: {n0} itens com preço', f'SULLAB: {n1} itens com preço').replace(f'São {n0} itens disponíveis', f'São {n1} itens disponíveis')
open(mp, 'w', encoding='utf-8').write(mk)

# ---------------------------------------------------------------- catálogo
for cpath in (R + 'catalogo.html', R + 'catalogo/index.html'):
    c = open(cpath, encoding='utf-8').read()
    i = c.find('<h2 id="cral">')
    j = c.find('<h2 id="cecon">')
    sec = c[i:j]
    m1 = re.search(r'<b>(\d+) itens</b> neste catálogo · linha completa com <b>(\d+) itens</b> no site', sec)
    nc, ns = int(m1.group(1)), int(m1.group(2))
    sec = sec.replace(m1.group(0), f'<b>{nc + len(itens)} itens</b> neste catálogo · linha completa com <b>{ns + len(itens)} itens</b> no site', 1)
    sec = sec.replace('Reagentes, corantes e soluções para laboratório clínico.', 'Reagentes, corantes e soluções para laboratório clínico, vidraria em borossilicato 3.3 e microscópios.', 1)
    gi = sec.find('<div class="grid">')
    ge = sec.find('</div><div class="notaimg">', gi)
    if ge < 0:
        ge = sec.find('</a></div>', gi) + 4
    itm = ''.join(f'<a class="item" target="_blank" rel="noopener" href="{SITE}/?q={it["cod"]}"><div class="ph"><img loading="lazy" src="{it["img"]}" alt="{html.escape(it["nome"])}"></div><div class="cod">cód. {it["cod"]} · CRAL</div><div class="nm">{html.escape(it["nome"])}</div><div class="pr">{brl(it["venda"])}<small>preço CNPJ, por embalagem</small></div></a>' for it in mic)
    sec = sec[:ge] + itm + sec[ge:]
    te = sec.rfind('</tbody></table></div>')
    rows = ''.join(f'<tr><td class="c">cód. {it["cod"]} · CRAL</td><td><a href="{SITE}/?q={it["cod"]}" target="_blank" rel="noopener">{html.escape(it["nome"])}</a></td><td class="p">{brl(it["venda"])}<small>preço CNPJ</small></td></tr>' for it in vid)
    sec = sec[:te] + rows + sec[te:]
    c = c[:i] + sec + c[j:]
    tot = re.search(r'(\d+) itens de 8 marcas', c).group(1)
    c = c.replace(f'{tot} itens de 8 marcas', f'{int(tot) + len(itens)} itens de 8 marcas')
    open(cpath, 'w', encoding='utf-8').write(c)

# ---------------------------------------------------------------- sitemaps
sp = R + 'sitemap-produtos.xml'
s = open(sp, encoding='utf-8').read()
s = s.replace('</urlset>', ''.join(f'<url><loc>{it["url"]}</loc><lastmod>{HOJE}</lastmod><changefreq>weekly</changefreq></url>\n' for it in itens) + '</urlset>', 1)
open(sp, 'w', encoding='utf-8').write(s)
sc = R + 'sitemap-categorias.xml'
s = open(sc, encoding='utf-8').read()
ant = '<url><loc>https://lojasullabrj.com.br/categoria/tubos-a-vacuo.html</loc>'
k = s.find(ant)
k2 = s.find('</url>', k) + len('</url>\n')
s = s[:k2] + f'<url><loc>{URLC}</loc><lastmod>{HOJE}</lastmod><changefreq>weekly</changefreq></url>\n' + s[k2:]
open(sc, 'w', encoding='utf-8').write(s)

# ---------------------------------------------------------------- feed Google
fp = R + 'feed-google.xml'
s = open(fp, encoding='utf-8').read()
x = html.escape
blocos = []
for it in itens:
    d = f'{it["nome"]}. Marca CRAL. Código {it["cod"]}. ' + ' '.join(y.rstrip('.') + '.' for y in it['ficha'][:-1]) + ' Produto para laboratório. Venda para empresas (CNPJ) com NF-e e entrega para todo o Brasil.'
    gcat = 'Business &amp; Industrial &gt; Science &amp; Laboratory &gt; Laboratory Equipment &gt; Microscopes' if it['g'] == 'MIC' else 'Business &amp; Industrial &gt; Science &amp; Laboratory &gt; Laboratory Supplies'
    blocos.append(f'''<item>
<g:id>{x(it["cod"])}</g:id>
<g:title>{x(it["nome"])} — CRAL</g:title>
<g:description>{x(d)}</g:description>
<g:link>{it["url"]}</g:link>
<g:image_link>{it["img"]}</g:image_link>
<g:condition>new</g:condition>
<g:availability>in_stock</g:availability>
<g:price>{it["venda"]:.2f} BRL</g:price>
<g:brand>CRAL</g:brand>
<g:mpn>{x(it["cod"])}</g:mpn>
<g:identifier_exists>no</g:identifier_exists>
<g:google_product_category>{gcat}</g:google_product_category>
<g:product_type>{x(it["cat"][1])}</g:product_type>
</item>
''')
s = s.replace('</channel>', ''.join(blocos) + '</channel>', 1)
open(fp, 'w', encoding='utf-8').write(s)

# ---------------------------------------------------------------- rodapé: link da nova categoria em todas as páginas
LINK = 'categoria/equipamentos-e-acessorios.html">Equipamentos e acessórios</a>'
alt = 0
for f in glob.glob(R + '**/*.html', recursive=True):
    if f.endswith('/index.html') and os.path.dirname(f) == R.rstrip('/'):
        continue
    t = open(f, encoding='utf-8').read()
    a = t.find('<footer class="siteftr">')
    if a < 0:
        continue
    b = t.find('</footer>', a)
    ft_ = t[a:b]
    if 'vidraria-de-laboratorio.html' in ft_ or LINK not in ft_:
        continue
    m = re.search(r'<a href="([^"]*)' + re.escape(LINK), ft_)
    pref = m.group(1)
    ft2 = ft_.replace(LINK, LINK + f'<a href="{pref}categoria/vidraria-de-laboratorio.html">Vidraria de laboratório</a>', 1)
    open(f, 'w', encoding='utf-8').write(t[:a] + ft2 + t[b:])
    alt += 1
print('rodapés atualizados:', alt)
print('novos:', len(itens), '| vidraria:', len(vid), '| microscópios:', len(mic))
