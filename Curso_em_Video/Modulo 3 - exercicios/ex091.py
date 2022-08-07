'''Crie um programa onde 4 jogadores joge um dado e tenha resultados aleatorios.
Guarde esses resultados em um dict. No final coloque esse dicionario em ordem, sabendo que o
vencedor tirou o maior número no dado.
valores sorteados:
Ranking dos jogadores'''
from random import randint
from time import sleep
Jogadas = {}
geral =[]
print('Valores sorteados: ')
for c in range(0,4):
    dado = randint(1, 6)
    print(f'Jogador {c}: {dado} ')
    Jogadas['Jogador'] = c
    Jogadas['dado'] = dado
    geral.append(Jogadas.copy())
print(geral)
#print('Ranking dos jogadores')
ranking = [0, 0, 0, 0]
maior = menor = 0
for e in geral:
    for v in (e.values()):
        print(e.values(), '*')
        print(e['dado'])





