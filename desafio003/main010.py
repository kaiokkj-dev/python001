k = float(input('O Video custa R$: '))
print(f'Um video que custava R${k}, a vista ele tem um desconto de 10%, vai custar R$:{k - (k * 0.1) :.2f}.')
y = float(input('Quantas vezes voce quer parcelar? '))
print(f'Sendo parcelado em {y}x, o valor total vai ser R$:{k + (k * 0.2) :.2f} e cada parcela vai custar R$:{(k + (k * 0.2)) / y :.2f} .')