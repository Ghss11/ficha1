l = str(input(''))
p = str(input(''))
s = str(input(''))
a = str(input(''))

print('Um bom faro nunca falha! E o meu tá apontando pra uma covardia: sumiram TODOS os monitores! Eu passo o dia perseguindo o próprio rabo, mas juro que hoje acho eles mais rápido que isso!')

if l == 'Grad 5':
    print('O laboratório mais movimentado do CIn... e nenhum sinal de monitor por aqui.')

if l == 'Kaonelle':
    print('Byte farejou cada mesa da Kaonelle em busca de pistas.')

if l == 'DA':
    print('A sala de convivência estava vazia. Até as bolinhas de ping pong sumiram.')

if l == 'Feirinha do CIn':
    print('No meio da Feirinha, muita gente, mas nenhum monitor à vista.')

if p == 'nota fiscal': 
    if l == 'Kaonelle':
        print('A nota fiscal é de uma compra de 350 cãoxinhas. Alguém está planejando alimentar um exército — ou uma festa e tanto.')
    else:
        print('Uma nota fiscal misteriosa, mas as informações estão meio apagadas.')

if p == 'boné':
    print('Um boné caído no chão. Alguém saiu correndo e esqueceu a cabeça descoberta.')

if p == 'balão':
    print('Um balão murcho no chão... isso aqui cheira a comemoração.')

if p == 'passagem para Catende':
    print('Uma passagem de ônibus para Catende. Alguém tem raízes por lá.')

if s == 'Ricardo Maneiro' or s == 'Fernanda Arvore' or s == 'Marciano' or s == 'Amanda da Arte' or s == 'Yoda':
    if (p == 'balão' or (p == 'nota fiscal' and l == 'Kaonelle')):
        print(f'{s} alega o álibi: {a}. Diz estar ocupado com os preparativos de algo... mas não entrega do que se trata.')
    else:
        print(f'{s} alega o álibi: {a}. Diz só estar corrigindo provas atrasadas. Nada a ver com o caso.')

if s == 'Jaobé':
    if p == 'passagem para Catende':
        print(f'Diante da pista encontrada, Jaobé gagueja e alega o álibi: {a}. A coincidência é grande demais.')
    else:
        print(f'Jaobé alega o álibi: {a}. Sem essa pista específica, nada o liga ao caso.')

if s == 'Jorge Arthur':
    if p == 'boné':
        print(f'Jorge Arthur alega o álibi: {a}... mas, estranhamente, está sem boné pela primeira vez na vida. Algo não bate.')
    else:
        print(f'Jorge Arthur alega o álibi: {a}. Sem essa pista específica, nada o liga ao caso.')

if (s == 'Ricardo Maneiro' or s == 'Fernanda Arvore' or s == 'Marciano' or s == 'Amanda da Arte' or s == 'Yoda') and (p == 'balão' or (p == 'nota fiscal' and l == a)):
    print('CASO ENCERRADO: Não houve crime algum! Os monitores, emocionados com a volta de Byte, prepararam uma festa surpresa, com direito a muita cãoxinha e bolinho de ração pra ele. O banquete foi ótimo... pelo menos pra quem é cachorro.')

elif (s == 'Jaobé' and p == 'passagem para Catende' and l == a) or (s == 'Jorge Arthur' and p == 'boné' and l == a):
    print('CASO ENCERRADO: Jaobé e Jorge Arthur, enfurecidos por não terem honra o suficiente para serem conselheiros, sequestraram todos os monitores e só os libertariam em troca dos cargos. Byte percebe que o álibi contado bate exatamente com o lugar onde a pista foi encontrada, o flagrante perfeito! Byte morde a canela dos dois e resgata a equipe. Os culpados levam um puxão de orelha e são exilados da monitoria.')

else:
    print('CASO EM ABERTO: Byte se distraiu perseguindo um esquilo no meio do pátio e esqueceu completamente onde tinha parado a investigação. Sem solução dessa vez.')