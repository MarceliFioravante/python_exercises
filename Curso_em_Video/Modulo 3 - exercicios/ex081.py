'''Crie um programa que vai ler vários números e colocá-los numa lista.
Depois disso mostre:
a)Quantos números foram digitados
b)A lista de valores ordenada de forma decrescente
c)Se o valor 5 foi digitado e  está ou não na lista'''
valores = list()
while True:
    valores.append(int(input("Digite um valor: ")))
    resp = str(input("Quer continuar? [S/N] ")).upper().strip()[0]
    if resp in "Nn":
        break
print(f"Foram digitados {len(valores)} números.")
valores.sort(reverse=True)
print(f"Os valores em ordem decrescente são: {valores}")
if 5 not in valores:
    print("O valor 5 não foi digitado!")
else:
    print(f"O valor 5 apareceu nas posições ", end="")
for c, v in enumerate(valores):
    if v == 5:
        print(f"{c}", end= " ")
