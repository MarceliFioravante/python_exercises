''''Melhore o jogo do ex028 onde o computador vai pensar e mum numero entre 0 e 10. So que agora o jogador vai
 tentar adivinhar ate acertar, mostrando no final quantos palpites foram necessarios para vencer'''
import random
from time import sleep
print("---" * 14)
print("Estou pensando em um número entre 0 e 5...")
print("---" * 14)
num = 0
tentativas = 0
sorteado = random.randrange(6) #numero que o computador pensou, posso usar from random import randit sorteado = randit(0, 5)
while num != sorteado:
    num = int(input("Voce consegue adivinhar qual é?! Digite um número:"))
    print("PROCESSANDO....")
    sleep(0.5)
    tentativas += 1
    if num != sorteado:
        print("O número que pensei foi {}!".format(sorteado))
        print("Vamos tentar de novo?!")
    else:
        print("O número que pensei foi {}!".format(sorteado))
        if tentativas == 1:
            print("Voce acertou! E precisou de apenas {} tentativa até acertar!".format(tentativas))
        else:
            print("Voce acertou! Mas precisou de {} tentativas para acertar!".format(tentativas))
