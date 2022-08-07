v = int(input("Digite um número para ver sua tabuada: "))
print("-" * 12)
for c in range(1, 11):
    print("{} X {} = {}".format(v, c, v * c))
print("-" * 12)