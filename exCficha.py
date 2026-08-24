D = str(input(''))
C = int(input(''))
F = int(input(''))
T = int(input(''))
if D == 'Tsinghua':
    if C >= 90:
        if F > T:
            print('Todos os torcedores do Santa Cruz passam a ter acesso ao intercâmbio para a Tsinghua University.')
        else:
            print('Os chineses gostam do Santa Cruz, mas preferem tênis de mesa e solicitam a criação do Santa Cruz Tênis de Mesa China.')
    if C < 90:
        print('Byte consegue fazer amigos na universidade, mas a paixão pelo Santa Cruz fica para a próxima.')
elif D == 'Shenzhen':
    if F >= 80:
        if C == 100:
            print('Todos os chineses passam a torcer para o Santa Cruz.')
        if C < 100:
            print('O Santa Cruz ganha um patrocínio de uma gigante de tecnologia de Shenzhen!')
    else: 
        print('Byte falha em converter os chineses ao Santa Cruz, mas aproveita a viagem visitando Shenzhen.')
else:
    print('Passaporte invalido. Byte deve retornar a Recife.')
