from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')

print("\033[1;35m JOKENPô")
print("\033[1;35m JOGADOR VS MÁQUINA")
print("\033[1;31m [0] PEDRA")
print("\033[1;31m [1] PAPEL")
print("\033[1;31m [2] TESOURA")

joga1 = int(input("\033[1;37m JOGADOR1: "))
maquina = randint(0,2)
if 0 < joga1 <=2:
    print('\033[1;35m JO')
    sleep(1)
    print("KEN")
    sleep(1)
    print("PO!!! \033[m")

    print('==========================================')
    print(f"\033[1;33m MÁQUINA: {itens[maquina]}")
    print(f'\033[1;31m JOGADOR: {itens[joga1]}')
    print("\033[1;36m ===========")
    print("\033[1;36m RESULTADO")
    print("\033[1;36m ===========")


    if joga1 == maquina:
        print("\033[1;34m EMPATE")
    elif joga1 == 0 and maquina == 2 or joga1 == 1 and maquina == 0:
        print("\033[1;34m VC GANHOU, PARABÉNS!")
    elif joga1 == 2 and maquina == 1:
        print("\033[1;34m VC GANHOU, PARABÉNS!")
    elif maquina == 0 and joga1 == 2 or maquina == 1 and joga1 ==0:
        print("\033[1;34m VC PERDEU!")
    elif maquina == 2 and joga1 == 1:
        print("\033[1;34m VC PERDEU!")

else:
    print("\033[1;31m JOGADA INVÁLIDA ")