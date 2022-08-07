'''Adapte o codigo do desafio 107 criando uma funcao adicional chamada moeda() que
consiga mostrar os valores como uma valor monetário formatado.'''
from ex108 import moeda

p = float(input('Digite o preco (R$): '))
print(f'A metade de {moeda.moeda(p)} é igual {moeda.moeda(moeda.metade(p))}.')
print(f'O dobro de {moeda.moeda(p)} é igual {moeda.moeda(moeda.dobro(p))}.')
print(f'Aumentando 10%, temos {moeda.moeda(moeda.aumentar(p, 10))}.')
print(f'Reduzindo 13%. temos {moeda.moeda(moeda.diminuir(p, 13))}.')