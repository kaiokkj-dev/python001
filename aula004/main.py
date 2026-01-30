import math
k = int(input("Digite um número: "))
raiz = math.sqrt(k)
print("A raiz quadrada de", k, "é", raiz.format(k, math.ceil(raiz)))