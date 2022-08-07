# ler o primero termo e a razao de uma PA. No final mostrar os primeros 10 termos dessa progressao.
n1 = int(input("Digite o primeiro termo da P.A.: "))
r = int(input("Entre a razão da P.A.: "))
pa = n1 + r
# decimo = n1 + (10-1) * r
for c in range (1, 11): # outra forma: for c in range(n1, decimo, r)
    print(pa, end=' -> ')
    pa += r
print("ACABOU!")
