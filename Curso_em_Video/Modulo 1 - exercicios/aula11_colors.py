'''i = int(input("Início: "))
f = int(input("Fim: "))
p = int(input("Passo: "))
for c in range (i, f + 1, p ):
    print(c)
print("FIM")'''
s = 0
for c in range (0, 5):
    n = int(input("Digite um valor: "))
    # s = s + n
    s += n
print("O valor da somatória é {}.".format(s))