''''Faca um programa que tenha uma funcao chamada ficha(), que receba dois parametros adicionais:
o nome de um jogador e quantos gols ele marcou.
O programa devera ser capaz de mostrar a ficha do jogador, mesmo que algum dado nao tenha
sido informado corretamente.'''
def ficha(n='<desconhecido>', g=0):
    print('-' * 30)
    print(f'O jogador {n} fez {g} gol(s) no campeonato.')


nome = str(input('Nome do Jogador: '))
gols = str(input('Número de gols: '))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if nome.strip() == "":
    ficha(g=gols)
else:
    ficha(nome, gols)

