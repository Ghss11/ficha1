e = int(input(''))
qp = int(input(''))
qa = int(input(''))
b = int(input(''))
gps = str(input(''))
bolinha = str(input(''))
chuva = str(input(''))
t = int(input(''))
i = int(input(''))
p = 0 
print('Byte recebeu um novo chamado! Preparando-se para a aventura...')

if e >= 70:
    p += 2
    print('Byte está cheio de energia!')
if e < 30:
    p -= 2
    print('Byte está muito cansado... A missão ficou mais difícil.')

if qp >= 2 and qa >= 1:
    p += 2
    print('Suprimentos preparados!')

if b >= 50 and gps == 'sim':
    p += 2
    print('Coleira tecnológica preparada!')

if b <= 20:
    p -= 1
    print('A bateria da coleira está crítica! Isso pode atrapalhar a missão.')

if bolinha == 'sim' or qp >= 4:
    p += 1
    print('Byte está ainda mais animado para a aventura!')

if chuva == 'sim' or  t > 32:
    p -= 2
    print('O clima não está ajudando... Isso vai dificultar a missão.')

if i >= 70:
    p += 1
    print('O sinal está forte! Há algo estranho por perto...')

print()

print(f'Nível de preparo: {p}')

if p >= 5:
    print('Byte está pronto! A nova aventura começa agora!')
else:
    print('Byte ainda não está pronto. Melhor se preparar um pouco mais!')

