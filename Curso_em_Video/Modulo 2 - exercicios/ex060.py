''''Faca um programa que leia um numero qualquer e mostre o seu fatorial'''
# !n = n * (n-1) * (n-2)....
num = int(input("Digite um valor: "))
diferenca = 0
fatorial = 1
resultado = 0
while num > 1:
    fatorial = fatorial * num
    num = num -1
    print(fatorial, end= " > ")
print("Fim")

'''num = int(input("Digite um valor: "))
resultado = 1
contagem = 1
while contagem <= num:
    resultado = contagem * resultado
    contagem = contagem + 1
    print("{}x{} = {} ->".format(num, contagem, resultado))'''""