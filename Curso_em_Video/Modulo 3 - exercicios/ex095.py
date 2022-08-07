'''Aprimore o ex093 para que ele funcione com varios jogadores, incluindo um sistema de
vizualizacao de detalhes do aproveitamento de cada jogador.'''
jogador = dict()
partidas = list()
time = list()
while True:
    jogador.clear()
    jogador['Nome'] = str(input(("Nome do jogador: ")))
    tot = int(input(f"Quantidade de Partidas que {jogador['Nome']} jogou? "))
    partidas.clear()
    for c in range (0, tot):
        partidas.append(int(input(f'Gols na {c+1}. partida: ')))
    jogador['Gols'] = partidas[:]
    jogador['Total de gols'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()
        if resp in "SN":
            break
        print('ERRO! Rsponda somente S ou N.')
    if resp == "N":
        break
print('-=' * 30)
print('Cód.', end=" ")
for i in jogador.keys():
    print(f'{i:<12}', end=" ")
print()
print('-' * 40)
for k, v in enumerate(time):
    print(f'{k:>3} ', end=" ")
    for d in v.values():
        print(f'{str(d):<15}', end=" ") # printou os dados em forma de strin para nao aparecerem os { } []
    print()
print('-' * 40)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar): '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não existem jogador com código {busca}.')
    else:
        print(f" -- LEVANTAMENTO DO JOGADOR {time[busca]['Nome']}.")
        for i, g in enumerate(time[busca]['Gols']):
            print(f'   No jogo {i+1} fez {g} gols.')
    print('-' * 40)
print(' << VOLTE SEMPRE >>')

