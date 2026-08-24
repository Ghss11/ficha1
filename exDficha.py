chuva = str(input(''))
temperatura = int(input(''))
energia = int(input(''))
if chuva == 'S':
    if energia > 3:
        print('Brincar de bolinha no laboratório')
    if energia <= 3:
        print('Soneca na caminha do CIn')
if chuva == 'N':
    if temperatura > 30:
        if energia > 3:
            print('Nadar no lago da UFPE')
        if energia <= 3:
            print('Descansar na sombra da árvore')
    if 15 <= temperatura <= 30:
        if energia > 2:
            print('Longo passeio no parque')
        if energia <= 2:
            print('Passeio curto no quarteirão')
if temperatura < 15:
    print('Passeio com roupinha de frio')