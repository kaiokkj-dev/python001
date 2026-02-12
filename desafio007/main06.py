print('\033[0;30;31mAnalisador de Triangulos!\033[m')
k1 = float(input('Primeiro segmento: '))
y2 = float(input('Segundo segmento: '))
f3 = float(input('Terceiro segmento: '))
if k1 < y2 + f3 and y2 < k1 + f3 and f3 < k1 + y2:
    print('Os segmento acima PODEM FORMAR um TRIANGULO ')
    if k1 == y2 == f3:
        print("EQUILATERO")
    if k1 != y2 != f3:
        print("ESCALENO")
    else:
        print("ISOSCELES")
else: 
    print('Os segmentos acimas nao pode formar um TRIANGULO')