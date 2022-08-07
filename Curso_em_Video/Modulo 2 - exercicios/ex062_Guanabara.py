n1 = int(input("Digite o primeiro termo da P.A.: "))
r = int(input("Entre a razão da P.A.: "))
termo = n1
c = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while c <= total:
        print(termo, end= " -> ")
        termo += r
        c += 1
    print("PAUSA!")
    mais = int(input("Quantos termos voce quer mostrar a mais? "))
print("Progressão finalizada com {} termos mostrados.".format(total))

