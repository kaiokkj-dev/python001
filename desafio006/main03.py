k = float(input('Qual e a distancia da sua viagem? '))
print('Voce esta prestes a comecar uma viagem de {}Km'.format(k))
if k <= 200:
    preco = k * 0.50
else:
    preco = k * 0.45
print('E o preco da sua passagem sera de R${:.2f}'.format(preco))