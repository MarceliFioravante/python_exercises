temp = []
principal = []
maior = menor = 0
while True:
    temp.append(str(input("Nome: ")))
    temp.append(float(input("Peso (Kg): ")))
    if len(principal) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]
    principal.append(temp[:])
    temp.clear()
    resp = str(input("Quer continua? [S/N] "))
    if resp in "Nn":
        break
print(f"Os dados cadastrados foram: {principal}")
print(f"Voce cadastrou {len(principal)} pessoas.")
print(f"O maior peso foi de {maior}Kg.Peso de ", end="")
for p in principal:
    if p[1] == maior:
        print(f"{[p[0]]} ", end=" ")
print()
print(f"O menor peso foi de {menor}Kg. Peso de ", end="")
for p in principal:
    if p[1] == menor:
        print(f"{[p[0]]} ", end=" ")
print()