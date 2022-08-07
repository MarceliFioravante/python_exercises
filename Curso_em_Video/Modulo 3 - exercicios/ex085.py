'''Crie um programa onde o usuário possa digitar sete valores numéricos e
cadastre-os em uma lista unica, que mantenha separado os valores pares dos impares.
No final mostre os valores pares e impares em ordem crescente cada uma na sua lista.
1lista unica com duas dentro.'''
'''pares = list()
impares = list()
valores = [pares, impares]
numero = list()
for c in range(1, 8):
    numero.append(int(input(f"Digite o {c}o. valor: ")))
    for p in numero:
            if p % 2 == 0:
                pares.append(numero[:])
                numero.clear()
            else:
                impares.append(numero[:])
                numero.clear()
print(f"Voce digitou os valores: {valores}.")
valores[0].sort()
valores[1].sort()
print(f"Os valores pares sao: {valores[0]}.")
print(f"Os valores impares sao: {valores[1]}.")'''

# GUANABARA
num = [[],[]]
valor = 0
for c in range(1,8):
    valor = int(input(f"Digite o {c}. valor: "))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
print("-=" * 30)
print(f"Os valores digitados foram: {num}")
num[0].sort()
num[1].sort()
print(f"Os valores pares digitados foram: {num[0]}.")
print(f"Os valores impares digitados foram: {num[1]}.")

