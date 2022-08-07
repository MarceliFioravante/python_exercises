'''Crie um programa que vai ler vários números e colocá-los numa lista. (continuar? s/n)
Depois disso, crie duas listas extras, uma para os valores pares digitados e outra para os
valores ímpares.
Ao final mostre o conteúdo das 3 listas geradas.'''
valores = list()
pares = list()
impares = list()
while True:
    valores.append(int(input("Digite um valor: ")))
    resp = str(input("Deseja continuar? [S/N] "))
    if resp in "N":
        break
for c in range(0, len(valores)):
    if valores[c] % 2 == 0:
        pares.append(valores[c])
    if valores[c] % 2 == 1:
        impares.append(valores[c])
print(f"Os valores digitados foram {valores}.")
print(f"os valores pares digitados foram {pares}.")
print(f"Os valores impares digitados foram {impares}.")
