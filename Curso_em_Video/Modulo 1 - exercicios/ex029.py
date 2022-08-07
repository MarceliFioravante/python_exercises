v = float(input("Digite a velocidade de um carro: "))
vmais = (80 - v) * -1
multa = ((80 - v) * -1) * 7
if v > 80:
    print("Sua velocidade ultrapassou {}km/h da velocidade permitida\nE voce foi multado em R${:.2f}!".format(vmais,multa))
print("Tenha um bom dia! Dirija com seguranca!")

