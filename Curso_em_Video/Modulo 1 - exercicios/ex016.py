from math import floor, trunc
num = float(input("Escreva um número: "))
print("O número {} tem a parte inteira {}.".format(num, floor(num)))
print("O número {} tem a parte inteira {}.".format(num, trunc(num)))

# outra opcao é usar .format(num, int(num) - para mostrar somente a parte inteira do numero.