import math
k = float(input('Comprimento do cateto oposto: '))
y = float(input('Comprimento do cateto adjacente: '))
print('A hipotenusa vai medir {:.2f}'.format(math.hypot(k, y)))