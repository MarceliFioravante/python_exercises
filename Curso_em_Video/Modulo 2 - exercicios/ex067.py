'''Faca um programa que mostre a tabuada de vários numeros, um de cada vez, para cada
valor digitado pelo usuario. O programa será interrompido quando o valor digitado for negativo.
quer ver a tubuada de qual valor?
PROGRAMA TABUADA ENCERRADO. VOLTE SEMPRE!'''
while True:
    num = int(input("Quer ver a tabuada de qual valor? "))
    if num == -abs(num):  # simplesmente usar if num < 0:
        break
    print("-" * 20)
    for c in range (1, 11):
        print(f"{num} x {c} = {num * c}")
    print("-" * 20)
print("PROGRAMA TABUADA ENCERRADO. VOLTE SEMPRE!")
print("-" * 20)
