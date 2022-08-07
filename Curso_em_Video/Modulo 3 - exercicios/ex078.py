'''Faça um programa que leia 5 valores numéricos pelo teclado e guarde-os numa lista.
No final mostre qual foi o menor e o maior valor digitado e suas respectivas posições na lista.
Se um número apareceu mais de uma vez ,devem ser informadas todas as posições em que ele apareceu.'''
valores = list()
repetido = 0
posicoes = list()
for cont in range(0,5):
    valores.append(int(input("Digite um valor: ")))
print(f"Você digitou os valores {valores}.")
print(f"O menor número digitado foi {min(valores)} na posicao {valores.index(min(valores))}.")
print(f"O maior número digitado foi {max(valores)} na posicao {valores.index(max(valores))}.")
for c in range(0, len(valores)):
    if valores.count(valores[c]) > 1:
        repetido = valores[c]
        posicoes.append(c)
        #print(f"O valor {valores[c]} apareceu nas posições ", end="")
        #print(f"{c}.")
print(f"O valor {repetido} apareceu nas posições {posicoes}.")

