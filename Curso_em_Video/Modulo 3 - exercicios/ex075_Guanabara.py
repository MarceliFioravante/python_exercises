num = (int(input("Digite um número: ",)),
       int(input("Digite outro número: ",)),
        int(input("Digite outro número: ",)),
         int(input("Digite mais um número: ")))
print(f"Você digitou os números: {num}")
print(f"O valor 9 apareceu {num.count(9)} vezes.")
if 3 in num:
    print(f"O valor 3 apareceu na {num.index(3) + 1}º posição.")
else:
    print("O valor 3 não foi digitado en nenhuma posição.")
print(f"Os valores pares digitados foram: ", end="")
for n in num:
    if n % 2 == 0:
        print(n, end=" ")
