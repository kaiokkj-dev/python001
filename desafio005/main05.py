k = str(input('Digite seu nome completo: ')).strip() 
print('Muito prazer em te conhecer!')
print('Seu primeiro nome e {}'.format(k.split()[0])) # split() divide a string em uma lista
print('Seu ultimo nome e {}'.format(k.split()[-1])) # -1 pega a ultima posicao da lista