k = int(input('Quanto dinheiro você tem na carteira? R$'))
print(f'Com R${k} você pode comprar U${k / 5.20 :.2f}.')
print(f'Se voce juntar {k} por mais {k:.2f} meses, você terá U${(k * k + k) / 5.20 :.2f}.')