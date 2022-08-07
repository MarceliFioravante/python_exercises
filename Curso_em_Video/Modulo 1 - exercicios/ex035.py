# ler o comprimento de 3 retas e falar para o usuario se elas podem ou nao formar um triangulo
l1 = int(input("Entre o comprimento de uma reta: "))
l2 = int(input("Entre o comprimento de outra reta: "))
l3 = int(input("Entre o comprimento de uma última reta: "))
if (l1 + l2) > l3 and (l1 + l3) > l2 and (l2 + l3) > l1:
    print("Essas retas podem formar um triangulo!")
else:
    print("Essas retas não podem formar um triangulo!")