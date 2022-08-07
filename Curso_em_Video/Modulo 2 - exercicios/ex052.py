# ler um numero inteiro e dizer se ele é ou nao primo. divisivel por 1 e por ele mesmo.
numero = int(input("Digite um número: "))
d = 0
#for c in range (0,10):
if numero > 1 and numero % 2 == 0 or numero % 3 == 0 or numero % 5 == 0:
    if numero == 2 or numero == 3 or numero == 5:
        print("Esse número é PRIMO!")
    else:
        print("Esse número não é PRIMO!")
else:
    print("Esse número é primo!")

