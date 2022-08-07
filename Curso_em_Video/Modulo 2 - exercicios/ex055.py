# ler o peso de 5 pessoas e no final mostrar qual foi o maior peso e o menor peso.
maior = 0
menor = 0
for c in range (0,5):
    peso_atual = float(input("Entre um valor de peso (Kg): "))
    if c == 0:
        maior = peso_atual
        menor = peso_atual
    else:
        if peso_atual > maior:
            maior = peso_atual
        if peso_atual < menor:
            menor = peso_atual
print("O menor peso é {:.1f}Kg.".format(menor))
print("O maior peso é {:.1f}Kg.".format(maior))