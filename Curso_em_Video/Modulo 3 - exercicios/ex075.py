'''Desenvolva um program que leia 4 valores e guarde eles em uma tupla. No final
mostre:
a) quantas vezes apareceu o valor 9
b) Em que posição foi digitado o primeiro valor 3
c) Quais foram os números pares'''
v1 = int(input("Digite um valor: "))
v2 = int(input("Digite outro valor: "))
v3 = int(input("Digite outro valor: "))
v4 = int(input("Digite um último valor: "))
valores = (v1, v2, v3, v4)
nove = 0
c = 0
compar = True
print(f"Você digitou os valores {valores}.")
for c in range(0, len(valores)):
    if valores[c] == 9:
        nove += 1
print(f"O valor 9 apareceu {nove} vezes.")
if 3 in (valores):
    print(f"O valor 3 apareceu na {valores.index(3) + 1}º posição.")
if 3 not in (valores):
    print("O valor 3 não foi digitado.")
for c in range(0, len(valores)):
    if valores[c] % 2 == 0:
        if compar:
            print(f"Os valores pares digitados foram ", end="")
        print(valores[c]," ", end="")
        compar = False
if compar:
    print("Não foram digitados valores pares.")





