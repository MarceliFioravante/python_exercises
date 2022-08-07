num1 = int(input("Entre um número inteiro: "))
num2 = int(input("Entre outro número inteiro: "))
if num1 > num2:
    print("O primeiro valor é maior: {}.".format(num1))
elif num2 > num1:
    print("O segundo valor é maior: {}.".format(num2))
else:
    print("Não existe valor maior, os dois são iguais!")
