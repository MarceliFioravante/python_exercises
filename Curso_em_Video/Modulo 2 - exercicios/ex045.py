import random
from time import sleep
print("=" * 25)
print(" ROCK - PAPER - SCISSORS  ")
print("=" * 25)
jogador = str(input("JOGADOR - escolha: 1 - pedra  2 - papel  3 - tesoura\n"))
computador = "pedra", "papel", "tesoura"
print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PO")
sleep(1)
computadorsorteou = random.choice(computador)
print("O computador jogou: {}!".format(computadorsorteou))
if jogador == "pedra" and computadorsorteou == "tesoura" or jogador == "papel" and computadorsorteou == "pedra" or jogador == "tesoura" and computadorsorteou == "papel":
    print("O jogador VENCEU!")
elif computadorsorteou == "papel" and jogador == "pedra" or computadorsorteou == "tesoura" and jogador == "papel" or computadorsorteou == "pedra" and jogador == "tesoura":
    print("O computador VENCEU!")
elif jogador == computadorsorteou:
    print("Empate!")





