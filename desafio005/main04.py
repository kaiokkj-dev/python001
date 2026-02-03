k = str(input('Digite uma frase: ')).strip()
print('A letra A aparece {} vezes  na frase.'.format(k.upper().count('A')))
print('A primeira letra A aparece na posicao {}'.format(k.upper().find('A') + 1))
print('A ultima letra A aparece na posicao {}'.format(k.upper().rfind('A') + 1))