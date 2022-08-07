import math
co = float(input("Informe o comprimento do cateto oposto: "))
ca = float(input("Informe o comprimento do cateto adjacente: "))
com_hp = math.hypot(co, ca)
print("O comprimento da hipotenusa é {:.2f}.".format(com_hp))