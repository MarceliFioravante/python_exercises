'''Crie um pacote interno chamado utilidadesCeV que tenha dois modulos internos chamados moeda e dado.
Transfira todas as funcoes usadas nos exercicios 107, 108 e 109 para o primeiro pacote e mantenha tudo funcionando'''

from UtilidadesCeV import moeda

p = float(input('Digite o preco: R$ '))
moeda.resumo(p, 35)