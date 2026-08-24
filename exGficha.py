c1= str(input('')).strip()
v1 = str(input('')).strip().upper()
c2 = str(input('')).strip()
v2 = str(input('')).strip().upper()
vc = 0
g = 0
ng = 0
print('Depois que a Série A e a Libertadores ficaram só no sonho do Santa, Byte pendura a chuteira de ídolo tricolor e parte pro interior: começa a Excursão Interiorana em busca do time da sua vida!')

if 'Catende' in c1:
    print('Catende!!! Aqui já rodou a maior usina de açúcar e álcool da América Latina, Byte sente o orgulho no ar.')

if 'Palmares' in c1:
    print('Palmares, a Terra dos Poetas! Berço de nomes como Ascenso Ferreira, aqui até o futebol merece um verso.')

if 'Carcará' in c1:
    vc += 1
    print('Carcará no peito! Essa é terra de Salgueiro, o primeiro clube do interior a ser campeão pernambucano, Byte sente o chamado do Sertão!')

if 'Patativa' in c1:
    vc += 1
    print('Show da Patativa! Caruaru e o Central esperam Byte de braços abertos, direto da maior feira a céu aberto do mundo!')

if 'Azulão' in c1:
    vc += 1
    print('Ar puro de serra! O Azulão de Bonito, sensação recente do Pernambucano, pode ser o novo lar de Byte!')

if 'fruticultura' in c1:
    print('Margens do Velho Chico! Petrolina, a maior cidade do interior, com direito a manga, uva e muita irrigação, chama Byte pro time!')
    vc += 1

if 'Pássaro Preto' in c1:
    print('Pertinho de casa! O Pássaro Preto, orgulhosamente um dos times mais folclóricos do planeta, também está de olho em Byte!')
    vc += 1

if 'GOSTOU' in v1 and not 'NÃO GOSTOU' in v1:
    print('Aquele cheirinho de interior fisgou o faro do Byte! Visita gostosa, mas ele quer conhecer mais um pouco antes de assinar.')
    g += 1

if 'NÃO GOSTOU' in v1:
    print('Byte torceu o focinho dessa vez... não rolou clima pra ficar por aqui.')
    ng += 1


if 'Catende' in c2:
    print('Catende!!! Aqui já rodou a maior usina de açúcar e álcool da América Latina, Byte sente o orgulho no ar.')

if 'Palmares' in c2:
    print('Palmares, a Terra dos Poetas! Berço de nomes como Ascenso Ferreira, aqui até o futebol merece um verso.')

if 'Carcará' in c2:
    vc += 1
    print('Carcará no peito! Essa é terra de Salgueiro, o primeiro clube do interior a ser campeão pernambucano, Byte sente o chamado do Sertão!')

if 'Patativa' in c2:
    vc += 1
    print('Show da Patativa! Caruaru e o Central esperam Byte de braços abertos, direto da maior feira a céu aberto do mundo!')

if 'Azulão' in c2:
    vc += 1
    print('Ar puro de serra! O Azulão de Bonito, sensação recente do Pernambucano, pode ser o novo lar de Byte!')

if 'fruticultura' in c2:
    print('Margens do Velho Chico! Petrolina, a maior cidade do interior, com direito a manga, uva e muita irrigação, chama Byte pro time!')
    vc += 1

if 'Pássaro Preto' in c2:
    print('Pertinho de casa! O Pássaro Preto, orgulhosamente um dos times mais folclóricos do planeta, também está de olho em Byte!')
    vc += 1

if 'GOSTOU' in v2 and not 'NÃO GOSTOU' in v2:
    print('Aquele cheirinho de interior fisgou o faro do Byte! Visita gostosa, mas ele quer conhecer mais um pouco antes de assinar.')
    g += 1

if 'NÃO GOSTOU' in v2:
    print('Byte torceu o focinho dessa vez... não rolou clima pra ficar por aqui.')
    ng += 1

if ("Catende" in c1 and "Palmares" in c2) or ("Palmares" in c1 and "Catende" in c2):
    print('Catende e Palmares na excursão? Aí sim Byte tá garimpando ouro puro da Zona da Mata Sul! Pena que acabou por aqui.')

print()
print('RELATÓRIO DA EXCURSÃO SERTANEJA DO BYTE:')
print(f'- Visitas que contaram: {vc}')
print(f'- Gostou: {g}')
print(f'- Não gostou: {ng}')
print()
print('E assim termina a Excursão Interiorana de Byte em Pernambuco. Anotar tudo isso na unha, sem laço nem lista, dá um trabalhão! Nas próximas férias, Byte espera que a molecada já saiba de laços, listas e funções pra dar conta do recado com estilo :)')
