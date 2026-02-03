k = str(input('Digite uma frase: ')).strip()
print('A letra A aparece {} vezes  na frase.'.format(k.upper().count('A'))) # count conta quantas vezes aparece a letra
print('A primeira letra A aparece na posicao {}'.format(k.upper().find('A') + 1)) # find procura a primeira ocorrencia da letra
print('A ultima letra A aparece na posicao {}'.format(k.upper().rfind('A') + 1)) # rfind procura da direita para a esquerda