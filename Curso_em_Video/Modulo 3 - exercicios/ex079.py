'''Crie um programa onde o usuário possa digitar vários valores numéricos e
cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado.
No final serão exibidos todos os valores únicos digitados em ordem crescente.'''
valores = list()
while True:
    valor = int(input("Digite um valor: "))
    '''if len(valores) == 0:
        valores.append(valor)
        print("Valor adicionado com sucesso...")''' # desnecessário
    if valor not in valores:
        valores.append(valor)
        print("Valor adicionado com sucesso...")
    else:
        print("Valor duplicado! Não adicionado na lista.")
    resp = str(input("Quer continuar? [S/N] "))
    if resp == "Nn":
        break
valores.sort()
print(f"Os valores digitados foram: {valores}")
