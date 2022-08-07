nota1 = float(input("Digite sua primeira nota: "))
nota2 = float(input("Digite sua segunda nota: "))
M = (nota1 + nota2) / 2
# if M >= 5 and media < 7
# if > 7 media <= 5
if M >= 7:
    print("Sua média foi {:.2f} e você está APROVADO!".format(M))
elif M < 5:
    print("Sua média foi {:.2f} e você está REPROVADO!".format(M))
else:
    print("Sua média foi {:.2f} e você está de recuperação!".format(M))
