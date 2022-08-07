'''Crie um programa que leia nome, ano de nascimentos e carteria de trabalho e cadastre-os
com idade, num dict. Se por acaso a CTPS for diferente de ZERO, o dicionario tambem receberá
o ano de contratacao e o salario. Calcule e acrescente, alem da idade com quantos anos essa pessoa ira se aposentar (35
anos de contribuicao).'''
from datetime import date
atual = date.today().year
geral = {}
geral['Nome'] = str(input('Digite seu nome: '))
Nascimento = int(input('Ano de nascimento: '))
geral['Idade'] = atual - Nascimento
geral['CTPS'] = int(input('Carteira de trabalho (0 - não tem): '))
if geral['CTPS'] != 0:
    geral['Contratacao'] = int(input('Ano de contratação: '))
    geral['Salário'] = float(input('Salário (R$): '))
    geral['Aposentadoria'] = (geral['Contratacao'] + 35) - Nascimento
print('-=' * 30)
for k, v in geral.items():
    print(f' - {k} tem o valor {v}.')
