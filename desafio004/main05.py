import random 
k = input('Primeiro aluno:')
y = input('Segundo aluno:')
z = input('Terceiro aluno:')
x = input('Quarto aluno:')
print('A ordem de apresentacao sera:')
print(random.sample([k, y, z, x], k=4))