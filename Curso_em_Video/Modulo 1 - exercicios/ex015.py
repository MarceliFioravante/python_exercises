d = int(input("Quantos dias alugado? "))
km = float(input("Quantos kilometros rodados? "))
aluguel = (d * 60) + (km * 0.15)
print("O valor a pagar pelo aluguel é R${:.2f}".format(aluguel))