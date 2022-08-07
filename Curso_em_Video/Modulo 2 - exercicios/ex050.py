s = 0
co = 0
for c in range(1,7):
    n = int(input("Digite o {}. valor: ".format(c)))
    if n % 2 == 0:
        s += n
        co = co + 1
print("Voce informou {} valores pares. A soma de todos os valores pares é {}.".format(co, s))
