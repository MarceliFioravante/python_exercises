'''Faco um programa que ajude um jogador da Mega Sena a criar palpites.
O programa vai perguntar quantos jogos serao gerados e vai sortear 6 numeros
entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.'''
from random import randint
from time import sleep
print("-" * 30)
print("{:^30}".format("JOGA NA MEGA SENA"))
print("-" * 30)
quantidade = int(input("Quantos jogos voce quer que eu sorteie? "))
total = 1
print("-=" * 5, f"SORTEANDO {quantidade} JOGOS ", "-=" * 5)
jogadas = list()
lista = list()
while total <= quantidade:
    cont = 0
    while True:
        num = randint(1,60)
        if num not in jogadas:
            jogadas.append(num)
            cont +=1
        if cont >= 6:
            break
    jogadas.sort()
    lista.append(jogadas[:])
    jogadas.clear()
    total += 1
for i, l in enumerate(lista):
    print(f"Jogo {i+1}: {l}.")
    sleep(0.5)
print("-=" * 5, "< BOA SORTE! >", "-=" * 5)


# Minha solucao funciona, mas coloca numeros repetidos dentro de um mesmo jogo ex: [3, 35, 3, 8, 18, 50]
'''for c in range(1, jogos + 1):
    for i in range(0,6):
        x = randint(1,60)
        jogadas.append(x)
    print(f"Jogada {c}: {jogadas}")
    sleep(0.5)
    jogadas.clear()'''