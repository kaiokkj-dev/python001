nome = str(input("Qual e o seu nome? ")).strip().lower()
if nome == "Kaio":
    print("Que lindo nome!")
elif nome in ["Gustavo", "Pedro","Lucas"]:
    print("Nome bem generico, parabens!")
elif nome in ["yasmim", "emily"]:
    print("Lindo nome, o Kaio gosta muito dele por algum motivokkkkkkk")
else:
    print("Seu nome e bem comum.")
print(f"Tenha um bom dia, {nome.title()}!")