print("\033[0;30;32m======== LOJAS KA1OKKJ ======== \033[m")  
preco = float(input("Preco das compras: R$ "))
print("FORMAS DE PAGAMENTO")
print("[ 1 ] à vista dinheiro/cheque")
print("[ 2 ] à vista no cartão")
print("[ 3 ] em até 2x no cartão")
print("[ 4 ] 3x ou mais no cartão")
opcao = int(input("Qual e a sua opcao? "))

if opcao == 1:
    preco_final = preco * 0.90
    print("Sua compra sera à vista dinheiro/cheque")
    print(f"Sua compra de R${preco:.2f} vai custar R${preco_final:.2f} no final.")
elif opcao == 2:
    preco_final = preco * 0.95
    print("à vista no cartão")
    print(f"Sua compra de R${preco:.2f} vai custar R${preco_final:.2f} no final.")
elif opcao == 3:
    print("em até 2x no cartão")
    print(f"Sua compra vai custar R${preco:.2f}.")
elif opcao == 4:
    preco_final = preco * 1.20
    print(f"Sua compra de R${preco:.2f} vai custar R${preco_final:.2f} no final.")
else:
    print("Opcao invalida. Tente novamente.")