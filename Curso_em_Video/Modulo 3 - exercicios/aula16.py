lanche = "Hamburguer", "suco", "pizza", "pudim"
print(lanche[-2])
print(lanche[:2])
print(lanche[-3:])
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a
print(c)
# print(c.count(5)) >>> conta quantas vezes um item aparece na tupla
# print(c.index(8)) >> em qual index está o valor 8
print(c.index(5, 1)) # >> procura o index do valor 5 contando a partir do index 1

# print(sorted(lanche)) >>>> mostra os itens ordenados

#for comida in lanche:
#   print(comida)

#for cont in range(0, len(lanche)):        >>> consigo acessar a posição
#    print(cont)

# for cont in range(0, len(lanche)):
#    print(lanche[cont])

#for pos, comida in enumerate(lanche):
#   print(f"Eu vou comer {comida} na posição {pos}")