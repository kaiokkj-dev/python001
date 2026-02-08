k = float(input('digite  a primeira nota: '))
y = float(input('digite  a segunda nota: '))
m = (k + y)/2
print('A dua media foi {:.1f}'.format(m))
if m >= 6.0:
    print ('Parabens pela nota, otimo desempenho!')
else:
    print('Sua nota pode melhorar, se esforce mais!')