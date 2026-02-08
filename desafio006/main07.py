print('\033[0;30;31mAnalisador de Triangulos!\033[m')
k = float(input('Primeiro segmento: '))
y = float(input('Segundo segmento: '))
f = float(input('Terceiro segmento: '))
if k < y + f and y < k + f and f < k + y:
    print('Os segmento acima podem formar um TRIANGULO')
else: 
    print('Os segmentos acimas nao pode formar um TRIANGULO')
