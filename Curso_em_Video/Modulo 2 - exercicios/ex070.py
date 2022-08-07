'''Crie um programa que leia o nome e o preco de vários produtos.
O programa deverá perguntar se o usuário quer continuar. No final mostrar:
a) Qual é o total gasto na compra
b) Quantos produtos custam mais de 1000 reais
c) Qual é o nome do produto mais barato'''
total = mil = 0
resp = "S"
barato = 0
nomebarato = ""
print("-" * 20)
print(" Lojas AMERICANAS ")
print("-" * 20)
while resp in "S":
    produto = str(input("Nome do produto: "))
    preco = float(input("Preço do produto: "))
    total += preco
    if preco >= 1000:
        mil += 1
    if barato == 0:
        barato = preco
        nomebarato = produto
    elif preco < barato:
        barato = preco
        nomebarato = produto
    resp = " "
    while resp not in "SN":
        resp = str(input("Deseja acrescentar mais produtos? [S/N] ")).upper().strip()[0]
        if resp == "N":
            print("Compra finalizada!")
            break
print("-" * 20)
print("Dados da compra: ")
print(f"O total gasto na compra foi de R$ {total:.2f}.")
print(f"Dos produtos comprados, {mil} custam mais de R$ 1000,00.")
print("O produto mais barato comprado foi {}.".format(nomebarato))
