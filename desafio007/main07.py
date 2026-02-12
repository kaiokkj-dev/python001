peso = float(input("Qual e seu peso? (Kg) "))
altura = float(input("Qual a sua altura? (m) "))
imc = peso / (altura ** 2)
print(f"O IMC dessa pessoa e de {imc:.2f}")
if imc < 18.5:
    print("Abaixo do Peso")
elif imc < 25:
    print("Peso Ideal")
elif imc < 30:
    print("Sobrepeso")
elif imc < 40:
    print("Obesidade")
else:
    print("Obesidade Mórbida")

