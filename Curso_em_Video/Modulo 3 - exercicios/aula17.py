num = list()
num = [2, 5, 9, 1]
print(num)
num[2] = 3
print(num)
num.append(7)
num.sort()
num.sort(reverse=True)
num.insert(2, 0)
# num.pop()
num.pop(2) # ese é o index, não o valor
num.remove(2)  # vai procurar na lista a primeira ocorrência desse valor e elimina o mesmo
if 5 in num:
    num.remove(5)
else:
    print("xxx")
print(num)
print(f"Esa lista tem {len(num)} elementos.")
valores = []
valores.append(5)
valores.append(9)
valores.append(4)
#for v in valores:
 #   print(f"{v}...", end="")

for c, v in enumerate(valores):
    print(f"Na posição {c} encontrei o valor {v}.")
print("Cheguei ao final da lista.")

valores = list()
for cont in range(0,5):
    valores.append(int(input("Digite um valor: ")))

a = [2, 3, 4, 7]
b = a              # quando igualamos uma lista a outra, elas ficam ligadas e toda alteração feita em uma vale para a outra também!
b = a[:]           # aqui foi feita uma cópia de A, então as listas não possuem ligação.
b[2] = 8
print(f"Lista A: {a}")
print(f"Lista B: {b}")
lista = [0, 1, 2, 3]
print(lista)
lista.insert(2, 5)
print(lista)