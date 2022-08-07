'''Melhore o desafio 61 perguntando para o usuario se ele quer mostrar mais alguns termos .
O programa encerra quando ele disser que quer mostrar 0 termos.'''
n1 = int(input("Digite o primeiro termo da P.A.: "))
r = int(input("Entre a razão da P.A.: "))
pa = n1 + r
c = 0
print(n1, end= " -> ")
while c != 9:
    print(pa, end= " -> ")
    pa += r
    c += 1
print("PAUSA!")
maistermos = int(input("\nGostaria de mostrar mais quantos termos? "))
if maistermos == 0:
    print("Fim da progressão!")
if maistermos >= 1:
    for c in range (0, maistermos):
        print(pa, end=" -> ")
        pa += r
        c += 9
print("Fim da progressão!")