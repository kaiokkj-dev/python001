nota1 = float(input("Primeira nota: "))
nota2 = float(input("Segunda nota: "))
media = (nota1 + nota2) / 2
print(f"Tirando {nota1} e {nota2}, a media do aluno e {media}")
if 7 > media >= 5:
    print("Voce esta de recuperacao, MELHORE!")
elif media < 5:
    print("Voce foi reprovado, TE ESPERO NA PROXIMA CHANCE!")
else:
    print("Voce foi aprovado, PARABENS DESEMPENHO INCRIVEL!")
