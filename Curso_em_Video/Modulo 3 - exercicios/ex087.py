'''Aprimore o desafio anterior, mostrando no final:
a) a soma de todos os valores pares digitados
b) A soma dos valores da terceira coluna
c) O maior valor da segunda linha'''
somapares = somacoluna = maiorvalor = 0
dados = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for c in range(0,3):
    for d in range(0,3):
       # dados.append((int(input(f"Digite um valor para [{c, d}]: "))))
        dados[c][d] = int(input(f"Digite um valor para [{c, d}]: "))
        if dados[c][d] % 2 == 0:
            somapares += dados[c][d]
        somacoluna += dados[c][2]
print("-="* 30)
for x in range(0,3):
    for y in range(0,3):
        print(f"[{dados[x][y]:^5}]", end="")
    print()
print("-=" * 30)
print(f"A soma de todos os valores pares é: {somapares}.")
print(f"A soma dos valores da terceira coluna é: {somacoluna}")
for c in range(0,3):
    if c == 0:
        maiorvalor = dados[1][c]
    elif dados[1][c] > maiorvalor:
        maiorvalor = dados[1][c]
print(f"O maior valor segunda linha é: {maiorvalor}.")