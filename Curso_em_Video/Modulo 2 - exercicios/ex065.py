'''Crie um programa que leia varios numeros inteiros pelo teclado.
No final da execucao, mostre a media entre todos os valores e qual foi o maior e menor valor lido.
O programa deve perguntar ao usuario se ele quer continuar ou nao a digitar valores.
FLAG - NAO QUERO DIGITAR MAIS'''
soma = 0
maior = 0
media = 0
menor = 0
valores = 1
c = 0
while valores != 0:
    valores = int(input("Digite um número: "))
    soma += valores
    maior = valores
    menor = valores
    if valores > maior:
        maior = valores
    if valores < menor:
        menor = valores
    c += 1
    media = soma / c
    more = str(input("Digitar mais valores?\n[1] - Continuar\n[2] - Nao quero digitar mais\n")).upper()
    if more == "2":
        print("A média dos valores digitados foi {}.\nO menor valor digitado foi {} e o maior {}.".format(media, maior, menor))
        break
    if more == "1":
        continue
