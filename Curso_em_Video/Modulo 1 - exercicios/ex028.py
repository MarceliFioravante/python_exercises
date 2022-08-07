import random
from time import sleep
print("-=-" * 14)
print("Estou pensando em um número entre 0 e 5...")
print("-=-" * 14)
num = int(input("Voce consegue adivinhar qual é?! Digite um número:"))
sorteado = random.randrange(6) #numero que o computador pensou, posso usar from random import randit sorteado = randit(0, 5)
print("PROCESSANDO....")
sleep(2)
if num == sorteado:
    print("O número sorteado foi {}!".format(sorteado))
    print("PARABENS! Voce me VENCEU!!")
else:
    print("Voce PERDEU! O numero sorteado foi {}!".format(sorteado))
