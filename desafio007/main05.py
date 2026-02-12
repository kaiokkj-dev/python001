from datetime import date
ano = int(input("Ano de Nascimento: "))
ano_atual = date.today().year
idade = ano_atual - ano
print(f"O atleta tem {idade} anos.")
if idade < 9:
    print("Classicacao: MIRIM")
elif idade < 14:
    print("Classicacao: INFANTIL")
elif idade < 19:
    print("Classicacao: JÚNIOR")
elif idade < 25:
    print("Classicacao: SÊNIOR")
else:
    print("Classicacao: MASTER")