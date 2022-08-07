''''Melhore o jogo do ex028 onde o computador vai pensar e mum numero entre 0 e 10. So que agora o jogador vai
 tentar adivinhar ate acertar, mostrando no final quantos palpites foram necessarios para vencer'''
from random import randint
computador = randint(0, 10)
print("Sou seu computador...Acabei de pensar num número entre 0 e 10.")
print("Será que você consegue adivinhar qual foi? ")
acertou = False
palpites = 0
while not acertou:
    jogador = int(input("Qual é o seu palpite? "))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print("Mais..tenta mais uma vez!")
        elif jogador > computador:
            print("Menos...tente mais uma vez")
print("Você acertou com {} tentativas! Parabéns!".format(palpites))
