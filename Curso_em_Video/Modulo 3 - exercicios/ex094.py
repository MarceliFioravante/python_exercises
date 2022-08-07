'''Crie um programa que leia nome, idade, sexo de varias pessoas.
Guardando os dados de cada pessoa em um dicionario e todos os dicionarios em uma lista.
No final mostre:
a) Quantas pessoas foram cadastradas
b) A media de idade do grupo.
c) Uma lista com todas as mulheres.
d) Uma lista com todas as pessoas com idade acima da media. '''
geral = list()
cadastro = dict()
totidade = m = 0
while True:
    cadastro['Nome'] = str(input('Nome: '))
    while True:
        cadastro['Sexo'] = str(input('Sexo [M/F]: ')).upper()
        if cadastro['Sexo'] in "MF":
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    cadastro['Idade'] = int(input('Idade: '))
    totidade += cadastro['Idade']
    geral.append(cadastro.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()
        if resp in "SN":
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == "N":
        break
print('-=' * 30)
# print(geral)
print(f'A) Ao todo temos {len(geral)} pessoas cadastradas.')
m = totidade / len(geral)
print(f'B) A média de idade é de {m:.2f} anos.')
print(f'C) As mulheres cadastradas foram: ', end="")
for p in geral:
    if p['Sexo'] == "F":
        print(p['Nome'], end=" ")
print('\nD) Lista das pessoas que estão acima da média: ')
for v in geral:
    if v['Idade'] >= m:
        print(f'    nome = {v["Nome"]}; sexo = {v["Sexo"]}; idade = {v["Idade"]};')
print(" << ENCERRADO >> ")
