from datetime import date
nascimento = int(input("Ano de nascimento: "))
ano_atual = date.today().year
idade = ano_atual - nascimento

print(f"Quem nasceu em {nascimento} tem {idade} em {date.today().year}.")
if idade < 18:
    faltam = 18 - idade
    ano_alistamento = ano_atual + faltam
    print(f"Ainda faltam {faltam} anos para o alistamento.")
elif idade == 18:
    print("Você tem 18 anos.")
    print("Este é o ano do seu alistamento!")
else:
    atraso = idade - 18
    ano_alistamento = ano_atual - atraso
    print(f"Você deveria ter se alistado há {atraso} anos.")
    print(f"Seu alistamento foi em {ano_alistamento}.")