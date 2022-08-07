'''Modifique as funcoes que foram criadas no exercicio 107 para que elas aceitem um parametro a mais,
informando se o valor retornado por elas vai ser formatado pela funcao moeda() do ex 108.'''
from ex109 import moeda

p = float(input('Digite o preco (R$): '))
print(f'A metade de {moeda.moeda(p)} é igual {moeda.metade(p, True)}.')
print(f'O dobro de {moeda.moeda(p)} é igual {moeda.dobro(p, True)}.')
print(f'Aumentando 10%, temos {moeda.aumentar(p, 10, True)}.')
print(f'Reduzindo 13%. temos {moeda.diminuir(p, 13, True)}.')