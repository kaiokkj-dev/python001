valor = int(input("Valor da casa: R$"))
salario = float(input("Salario do comprador: R$"))
financiamento = int(input("Quantos anos de financiamento? "))
prestacao = valor / (financiamento * 12)
print(f"Para pagar uma casa de R${valor:.2f} em {financiamento} anos a prestacao sera de {prestacao:.2f}")
if prestacao <= salario *0.3:
     print("Emprestimo pode ser CONCEDIDO!")
else:
    print("Emprestimo NEGADO!")