l1 = int(input("Digite o comprimento de uma reta: "))
l2 = int(input("Digite o comprimento de outra reta: "))
l3 = int(input("Digite o comprimento de uma outra reta: "))
if (l1 + l2) > l3 and (l1 + l3) > l2 and (l2 + l3) > l1:
    print("Essas retas podem formar um triangulo!")
    if l1 == l2 == l3:
        print("Tipo de triângulo: EQUILÁTERO")
    elif l1 == l2 or l2 == l3 or l1 == l3:
        print("Tipo de triângulo: ISÓCELES")
    else:
        print("Tipo de triângulo: ESCALENO")
else:
    print("Essas retas não podem formar um triangulo!")
