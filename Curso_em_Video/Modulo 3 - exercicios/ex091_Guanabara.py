from random import randint
from time import sleep
from operator import itemgetter
jogos = { 'Jogador 1': randint(1,6),
          'Jogador 2': randint(1,6),
          'Jogador 3': randint(1,6),
          'Jogador 4': randint(1,6)}
ranking = list() # depois que der o sorted ele vai ser apresentado como uma lista
print('Valores sorteados:')
for k, v in jogos.items():
    print(f'{k} tirou o valor {v} no dado.')
    sleep(0.5)
ranking = sorted(jogos.items(), key=itemgetter(1), reverse=True)
print('-=' * 15)
print(' == RANKING DOS JOGADORES == ')
for i, v in enumerate(ranking):
    print(f'    {i+1}º lugar: {v[0]} com {v[1]}.')
    sleep(0.5)
