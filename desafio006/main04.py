from datetime import date
k = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual: '))
if k == 0:
    k = date.today().year
if k % 4 == 0 and k % 100 != 0 or k % 400 == 0:
    print('O ano {} e BISSEXTO'.format(k))
else:
    print('O ano {} nao e BISSEXTO'.format(k))