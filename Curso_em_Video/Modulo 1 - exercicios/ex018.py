import math
ang = float(input("Informe o valor do angulo: "))
rad = ang * math.pi / 180
seno = math.sin(rad)
cos = math.cos(rad)
tan = math.tan(rad)
print("O angulo {}, tem seno {:.2f}, cosseno {:.2f} e tangente {:.2f}.".format(ang, seno, cos, tan))