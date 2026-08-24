l = str(input(''))
s = str(input(''))
c = len(s)
p = c - 11
po = 0
print('Byte irá julgar a sua senha.')

if  not s.isupper() and not s.islower() and s.lower() != s.upper():
    po += 5

if p > 0:
    po += p

if '@' in s:
    po += 1
if '_' in s:
    po += 1
if '&' in s:
    po += 1
if '%' in s:
    po += 1
if '#' in s:
    po += 1


if c < 8  or " " in s or s.isnumeric() or (not '0' in s and not '1' in s and not '2' in s and not '3' in s and not '4' in s and not '5' in s and not '6' in s and not '7' in s and not '8' in s and not '9' in s and not '@' in s and not '_' in s and not '&' in s and not '%' in s and not '#' in s):
    print('Essa senha nem chega perto do que eu aceito. Tente de novo.')
else:
    print('Vamos fazer a contagem dos pontos.')

    if c > 14:
        print('Que senha grande! Não seria difícil esquecer dela.')

    if l.upper() in s.upper():
        print('Olha o que eu encontrei aqui, não deixarei isso passar tão fácil.')
        po -= 10

    faltam = 1 - po

    if po < 1:
        print('Infelizmente terá que mudar sua senha, é para o seu bem.')
        print(f'Melhore sua senha em {faltam} ponto(s) e ela será suficiente.')

    if 11 > po > 0:
        print('Pode manter a sua senha, ela parece adequada.')

    if po > 10:
        print('Parabéns! Nem o maior hacker do mundo encontraria uma senha assim.')