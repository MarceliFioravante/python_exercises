salario = float(input("Qual o valor do seu salário? R$ "))
if salario > 1250.00:
    aum1 = 10 * salario / 100 + salario
    print("Voce ganhava {} e com um aumento de 10% passará a ganhar {}!".format(salario, aum1))
else:
    aum2 = 15 * salario / 100 + salario
    print("Voce ganhava {} e com um aumento de 15% passará a ganhar {}!".format(salario, aum2))