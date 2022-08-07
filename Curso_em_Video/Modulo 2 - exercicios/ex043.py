peso = float(input("Qual o seu peso (Kg): "))
altura = float(input("Qual a sua altura (m): "))
IMC = peso / (altura ** 2)
if IMC < 18.5:
    print("Seu IMC é {:.1f}  - ABAIXO DO PESO.".format(IMC))
elif IMC >= 18.5 and IMC < 25:
    print("Seu IMC é {:.1f} - PESO IDEAL.".format(IMC))
elif IMC >= 25 and IMC < 30:
    print("Seu IMC é {:.1f} - SOBREPESO.".format(IMC))
elif IMC >= 30 and IMC < 40:
    print("Seu IMC é {:.1f} - OBESIDADE.".format(IMC))
else:
    print("Seu IMC é {:.1f} - OBESIDADE MÓRBIDA.".format(IMC))