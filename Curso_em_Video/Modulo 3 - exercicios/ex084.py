'''Crie um programa que leia o nome e o peso de várias pessoas guardando tudo em uma lista (Continuar S/N?).
No final, mostrar:
a) Quantas pessoas foram cadastradas
b) Uma lista com as pessoas mais pesadas
c) Uma listagem com as pessoas mais leves.'''
dados = []
informacoes = []
leves = []
pesadas = []
nomes = 0
maior = menor = 0
while True:
    dados.append(str(input("Digite seu nome: ")))
    nomes += 1
    dados.append(int(input("Digite seu peso (Kg): ")))
    informacoes.append(dados[:])
    dados.clear()
    resp = (str(input("Deseja continuar? [S/N] ")))
    if resp in "Nn":
        break
for c in informacoes:
    if c[1] >= maior:
        maior = c[1]
        pesadas.append(c[0])
    if c[1] < maior: # ERRO AQUI
        menor = c[1]
        leves.append(c[0])
print("-=" * 30)
print("Cadastro finalizado...")
#print(informacoes)
print("-=" * 30)
print(f"Foram cadastradas {nomes} pessoas.")
print(f"As pessoas mais com maior peso {maior}Kg, sao: {pesadas}.")
#leves.sort()
print(f"As pessoas com menor peso {menor}Kg, sao: {leves}.")

