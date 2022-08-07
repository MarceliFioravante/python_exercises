'''Crie um programa que leia 2 valores e mostre um menu na tela
1 - somar/2 - multiplicar/3 - maior/4 - novos numeros/5 - sair do programa
Seu programa devera realizar a operacao solicitada em cada caso'''
valor = 0
soma = 0
multiplica = 0
multiplica1 = 0
multiplica2 = 0
maior = 0
novos = 0
for c in range(1,3):
    valor = int(input("Digite o {}. valor: ".format(c)))
    soma += valor
    if valor > maior:
        maior = valor
    if multiplica1 == 0:
        multiplica1 = valor
    if valor == multiplica1 or valor != multiplica1:
        multiplica2 = valor
    multiplica = multiplica1 * multiplica2
print("-" * 24)
print("--------- MENU ---------")
print('''ESCOLHA A OPÇÃO DESEJADA:
[1] - SOMAR
[2] - MULTIPLICAR
[3] - MAIOR
[4] - NOVOS NÚMEROS
[5] - SAIR DO PROGRAMA''')
print("-" * 24)
operacao = str(input("Qual operação deseja realizar: "))
while operacao != "5":
    if operacao == "1":
        print("A soma dos valores informados é {}.".format(soma))
        break
    if operacao == "3":
        print("O maior valor informado é {}.".format(maior))
        break
    if operacao == "4":
        for c in range(1, 3):
            valor = int(input("Digite o {}. valor: ".format(c)))
            soma += valor
            if valor > maior:
                maior = valor
            if multiplica1 == 0:
                multiplica1 = valor
            if valor == multiplica1 or valor != multiplica1:
                multiplica2 = valor
            multiplica = multiplica1 * multiplica2
        print("-" * 24)
        print("--------- MENU ---------")
        print('''ESCOLHA A OPÇÃO DESEJADA:
        [1] - SOMAR
        [2] - MULTIPLICAR
        [3] - MAIOR
        [4] - NOVOS NÚMEROS
        [5] - SAIR DO PROGRAMA''')
        print("-" * 24)
        operacao = str(input("Qual operação deseja realizar: "))
        while operacao != "5":
            if operacao == "1":
                print("A soma dos valores informados é {}.".format(soma))
                break
            if operacao == "3":
                print("O maior valor informado é {}.".format(maior))
                break
            if operacao == "2":
                print("O resultado da multiplicação dos dois valores é {}.".format(multiplica))
                break
            if operacao == "5":
                print("Saindo do programa!")
                continue
    if operacao == "2":
        print("O resultado da multiplicação dos dois valores é {}.".format(multiplica))
        break
if operacao == "5":
    print("Saindo do programa!")




