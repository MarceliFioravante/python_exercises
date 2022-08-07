'''Refaca o desafio 51, lendo o primero termo e a razao de uma PA, mostrando os 10
primeiros termos da progressao usando a estrutura while'''
n1 = int(input("Digite o primeiro termo da P.A.: "))
r = int(input("Entre a razão da P.A.: "))
termo = n1
c = 1
# decimo = n1 + (10-1) * r
'''for c in range (1, 11): # outra forma: for c in range(n1, decimo, r)
    print(pa, end=' -> ')
    pa += r
print("ACABOU!")'''
while c <= 10:
    print(termo, end= " -> ")
    termo += r
    c += 1
print("Acabou!")

