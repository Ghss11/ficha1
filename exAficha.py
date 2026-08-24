g = int(input(''))
print('Nossa, que lindo cavalo! Mas deixe-me verificar apenas uma coisa...')
if g == 0:
    print('ENTRADA LIBERADA')
if g != 0:
    print('ARMADILHA')
    if (g % 2) == 0:
        qntd_duplas = g // 2
        print(f'OS GUERREIROS FORMARAM {qntd_duplas} DUPLAS')
    if (g % 2) != 0:
        qntd_duplas = g // 2
        print(f'OS GUERREIROS FORMARAM {qntd_duplas} DUPLAS E UM GUERREIRO FICOU SOZINHO')