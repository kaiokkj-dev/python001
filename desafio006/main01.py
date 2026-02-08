k = int(input('Qual e a velociade atual do carro?'))
if k > 80:
    multa = (k - 80) * 7
    print ('MULTADO! Voce excedeu o limite permitido que e de 80km/h')
    print (f'Voce deve pagar uma de R${multa:.2f}')
else:
    print ('Tenha um bom dia, dirija com seguranca.')