'''Crie um programa que gerencie o aproveitamento de um jogador de futebol.
O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de
gols feitos em cada partida. No final tudo isso será guardado em um dict, incluindo o total de gols feitos durante o
campeonato.'''
aprov = dict()
gols = list()
aprov['Nome'] = str(input(("Nome do jogador: ")))
Partidas = int(input(f"Quantidade de Partidas que {aprov['Nome']} jogou: "))
for c in range (0, Partidas):
    Gols = int(input(f'Gols na {c}. partida: '))
    gols.append(Gols)
    aprov['Gols'] = gols[:]
    aprov['Total de gols'] = sum(gols)
print('-=' * 25)
print(aprov)
print('-=' * 25)
for k, v in aprov.items():
    print(f'O campo {k} tem valor: {v}')
print('-=' * 25)
print(f'O jogador {aprov["Nome"]} jogou {Partidas} partidas.')
for c in range(0, Partidas):
    print(' ' * 3, f"=> Na partida {c}, fez {aprov['Gols'][c]} gols.")
print(f'Foi um total de {aprov["Total de gols"]} gols.')

