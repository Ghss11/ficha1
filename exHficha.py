f1 = str(input(''))
td = len(f1) * 5
np = 0
td2 = 0
PORTAL = False
DIAMANTE = False
FERRO = False
OURO = False
C = False
M = False
Q = False
V = False
CD = False
MF = False
FF = False

DIS = False
ENTR = False
MAI = False
CTEND = False
USC = False
APNS = False
ALFL = False
DNI = False
D = False
TROIA = False

CO = True
CTENDMORTO = False




if f1.isupper():
    np += 30
else:
    np += 10

if 'MONSTROS' in f1.upper():
    M = True
    np += 25
    td += 20
    if '4' in f1:
        Q = True
        np *= 2


if 'FERRO' in f1.upper():
    FERRO = True
    np -= 15
    td += 5

if 'DIAMANTE' in f1.upper():
    if 'FERRO' in f1.upper():
        np -= 40
        DIAMANTE = True
    else:
        td += 15

if 'OURO' in f1.upper():
    if 'FERRO' in f1.upper():
        OURO = True
        td += 10
    else:
        td += 5

if 'ESTRUTURA' in f1.upper():
    e = str(input(''))
    if 'VILA' in e.upper():
        V = True
        C = True
        td += 10
    if 'PORTAL' in e.upper():
        PORTAL = True
    if 'TEMPLO' in e.upper():
        np += 100
    if 'MANSAO' in e.upper():
        if np > 100:
            MF = True
        np -= 150
        td += 40
    if 'CAMARA' in e.upper():
        CD = True
        td += 60
        np += 50

td2 = td
if np <= 100:
    FF = True
    if np < 0:
        np = 0
    np += 30
    if PORTAL == False:
        td += 5

    n1 = float(input())
    n2 = float(input())

    if (n1 + n2) % 1 != 0:
        if OURO == True:
            np += 10
        else:
            np += 20
            td += 30

    rb = str(input(''))
    if rb.isnumeric() and 1 <= int(rb) <= 12:
         td += 20
    elif rb.isnumeric() and int(rb) > 12:
            td += 10
    else:
        td += 30
        np += 40
    if np <= 100:
        CTEND = True
        if np < 0:
            np = 0
        np -= 20

        x = int(input(''))
        z = int(input(''))
        d = int(((100 - x)**2 + (200 - z)**2)**0.5)
        DIS = True
        td += d*2
        np += 30
        if np > 100:
            CTEND_MORTO = True
            CO = False
        if td > 300:
            MAI = True
            TROIA = True
            CO = False

        elif C == True:
            np -= 30

        elif 180 <= td <= 300:
            ENTR = True
            TROIA = True
            np += 10
            if np > 100:
                CTENDMORTO = True
                CO = False
            nfl = int(input(''))
            nal = int(input(''))
            if nal == 1:
                APNS = True
            if nal == 1 and nfl == 1:
                ALFL = True 
            if (nfl / nal) % 1 == 0 and (nfl / nal) > 0:
                td += 10
                D = True
            else:
                DNI = True
                td += 20
                CO = False
        elif td < 180:
            D = True
            td += 5
        if np > 100:
            CO = False
    if CTEND == False:
        CO = False
if FF == False:
    CO = False
if np < 0:
    np = 0


print('Byte: Au! Vou conseguir esse ovo!!')
if M == True:
    print('Você não pode dormir agora, há monstros por perto.')
if FERRO == True:
    print('Byte desbloqueou a conquista: [A Idade do Ferro]')
if DIAMANTE == True:
    print('Byte desbloqueou a conquista: [Diamantes!]')
if Q == True:
    print('Byte desbloqueou a conquista: [Caçador de Monstros]')
if V == True:
    print('Byte desbloqueou a conquista: [Negócio Fechado!]')
if CD == True:
    print('Byte desbloqueou a conquista: [Minecraft: Jogos Vorazes]')
if MF == True:
    print('Byte desbloqueou a conquista: [À beira da Morte]')
if FF == True:
    print(f'Byte: Ufa, finalmente acabei, demorei apenas {td2} minutos, vamos ao Nether!')


if PORTAL == False and FF == True:
    print('Byte desbloqueou a conquista: [Entrando numa fria]')
if FF == True:
    print('Byte desbloqueou a conquista: [O buraco é mais embaixo]')
if OURO == True and FF == True:
    print('Byte desbloqueou a conquista: [Meu precioso!]')

if DIS == True and CTEND == True:
    print(f'Byte: Estou a {d} blocos da Stronghold!')
if ENTR == True and CTEND == True:
    print('Troia desbloqueou a conquista: [É o fim?]')
if MAI == True and CTEND == True:
    print('Troia desbloqueou a conquista: [Liberte o End]')
if CTEND == True:
    print('Byte desbloqueou a conquista: [É o fim?]')
if C == True and CTEND == True and MAI == False:
    print('Byte: Como eu amo o [Design Intencional do Jogo]!')
if APNS == True and CTEND == True and ALFL == False:
    print('Byte: Troia já destruiu todos os cristais, agora é só o Dragão...')
if ALFL == True and CTEND == True:
    print('Byte: Uma flecha, Uma chance.')
if DNI == True and CTEND == True:
    print('Byte: Droga! Não tenha flechas suficientes, Troia vai ganhar...')
if D == True and CTEND == True:
    print('Byte desbloqueou a conquista: [Liberte o End]')

if CO == True:
        print('Byte desbloqueou a conquista: [A nova geração]')
        print('Byte: Aauauau! O ovo é meu! que rolem os créditos!')

if CO == False:
        
    if FF == False or CTEND == False or CTENDMORTO:
        print('Byte foi morto.')
    print('Byte: auu.... Não consegui pegar o ovo...')

print()
print('🚨Avaliação de nível de perigo:', end=' ')
if np == 100 or TROIA == True:
    print('Odisseia de Byte.')
elif np < 30:
    print('Passeio no Parque.')
elif 70 > np >= 30:
    print('Jornada Complicada.')
elif 100 > np >=70:
    print('Aventura Perigosa.')
elif np > 100:
    print('Letal.')
print()
hora = td // 60
min = td % 60
print(f'Timer: {int(hora)} h e {int(min)} minutos')