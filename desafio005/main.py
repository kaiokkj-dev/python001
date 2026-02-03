k = str(input('Digite seu nome completo: ')).strip() # strip() remove espaços desnecessários
print('Analisando seu nome...')
print('Seu nome em maiúsculas é {}'.format(k.upper())) # Maiúsculas
print('Seu nome em minusculos é {}'.format(k.lower())) # Minúsculas
print('Seu nome tem ao todo {} letras'.format(len(k) - k.count(' '))) # Quantidade de letras sem espaços
print('Seu primeiro tem {} letras'.format(k.find(' '))) # Quantidade de letras