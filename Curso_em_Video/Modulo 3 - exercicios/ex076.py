'''Crie um programa que tenha uma tupla única  com nomes de produtos e seus respectivos preços, na sequência.
No final, mostre uma listagem de preços, organizando os dados em forma tabular.'''
precosprodutos = ("Geladeira", 4500.99, "Lavadora", 3000.89, "Secadora", 5000, "Cama", 2500, "Roupeiro", 3000)
print("-" * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print("-" * 40)
for c in range(0, len(precosprodutos), 2):
    #print("{:<10}{:>5}{:>5}".format(precosprodutos[c],"................. R$", precosprodutos[c + 1]))
    print(f"{precosprodutos[c]:.<29}R$ {precosprodutos[c + 1]:>5.2f}")
print("-" * 40)




