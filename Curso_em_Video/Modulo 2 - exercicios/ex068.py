from random import randint
'''Faca um programa que jogue par ou impar com o computador
O jogo só será interrompido quando o jogador perder
Mostrando o total de vitorias consecutivas que ele conquistou no final do jogo.'''
print("=-" * 13)
print("VAMOS JOGAR PAR OU ÍMPAR? ")
print("=-" * 13)
computador = randint(0, 10)
total = 0
contador = 0
while True:
    num = int(input("Diga um valor? "))
    escolha = str(input("PAR ou ÍMPAR? [P/I] ")).upper()
    total = num + computador
    print(f"Voce jogou {num} e o computador jogou {computador}. Total de {total}")
    print("--" * 13)
    if total % 2 == 0:
        print("Deu PAR!")
        print("--" * 13)
        if escolha == "P":
            print("Você GANHOU!\nVamos jogar novamente...")
            print("=-" * 13)
            contador += 1
        if escolha == "I":
            print("Você PERDEU!")
            print("--" * 13)
            break
    else:
        print("Deu IMPAR!")
        print("--" * 13)
        if escolha == "P":
            print("Você PERDEU!")
            print("--" * 13)
            break
        if escolha == "I":
            print("Você GANHOU!\nVamos jogar novamente...")
            print("=-" * 13)
            contador += 1
print(f"GAME OVER!. Você venceu {contador} vezes!")

