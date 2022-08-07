p = float(input("Qual é o preço do produto? R$"))
desc = p - ((p * 5) / 100)
print("O produto que custava R${}, na promoção com desconto de 5% vai custar R${:.2f}".format(p, desc))