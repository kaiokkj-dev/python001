from random import randint
from time import sleep

# computador escolhe um número
numero = randint(0, 5)

print("-=" * 20)
print("Vou pensar em um número entre 0 e 5. Tente adivinhar...")
print("-=" * 20)

# jogador tenta adivinhar
palpite = int(input("Em que número eu pensei? "))

print("PROCESSANDO...")
sleep(2)

# comparação
if palpite == numero:
    print("PARABÉNS! Você conseguiu me vencer!")
else:
    print(f"GANHEI! Eu pensei no número {numero} e não no {palpite}")
