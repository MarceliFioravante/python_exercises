'''Crie um programa onde o usuário possa digitar 5 valores numéricos e
cadastre-os em uma lista, já na posição correta de inserção(sem usar o sort()).
No final mostre a lista ordenada na tela.
Digite um valor: 7
Adicionado ao final da lista...
Valor: 3
Adicionado na posição 0 da lista...
Os valores digitados em ordem foram: '''
valor = 0
num = []
if len(num) == 0:
    num.append(int(input("Digite um valor: ")))
    print("Valor adicionado a lista.")
for cont in range(0, 4):
    print(num)
    valor = int(input("Digite um valor: "))
    for c in range(0, len(num)):
        print(c)
        if valor > num[c] and valor < num[-1]:
            num.insert(num[-2], valor)
            print("Valor adicionado no final da lista.")
            break
        if valor > num[c]:
            num.insert(num[-1], valor)
            print("Valor adicionado no final da lista.")
            break
        if valor < num[c]:
            num.insert(c, valor)
            print("valor adicionado no começo da lista. ")
            break
print(num)





