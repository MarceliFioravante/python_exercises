resp = "S"
soma = cont = med = maior = menor = 0
while resp in "Ss":
    num = int(input("Digiter um número: "))
    soma += num
    cont += 1
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input("Quer continuar? [S/N] ")).upper().strip()
med = soma / cont
print("Você digitou {} números e a média foi {:.0f}.".format(cont, med))
print("O maior valor foi {} e o menor valor foi {}.".format(maior, menor))
