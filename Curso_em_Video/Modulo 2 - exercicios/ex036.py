valorcasa = float(input("Informe o valor da casa que voce quer comprar: "))
salario = float(input("Informe o seu salário: "))
parcelas = int(input("Informe em quantos anos deseja parcelar a divida: "))
partesalario = 30 * salario /100
prestacao = valorcasa / (parcelas * 12)
if prestacao > partesalario:
    print("A prestacao da casa no valor de {:.2f} excede 30% do seu salario, que é {:.2f}.\nSeu empréstimo foi NEGADO!".format(prestacao, partesalario))
else:
    print("A prestacao da casa no valor de {:.2f} é compativel com 30% do seu salario que é {:.2f}.\nSeu empréstimo foi ACEITO!".format(prestacao, partesalario))
