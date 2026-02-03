k = str(input('Digite seu nome completo: ')).strip() 
print('Muito prazer em te conhecer!')
print('Seu primeiro nome e {}'.format(k.split()[0]))
print('Seu ultimo nome e {}'.format(k.split()[-1]))