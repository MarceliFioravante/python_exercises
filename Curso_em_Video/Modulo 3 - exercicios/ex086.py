''''Crie um programa que crie uma matriz 3x3 e preencha com valores lidos pelo teclado.
No final mostre a matriz na tela com a formatacao correta.'''
dados = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0,3):
    for c in range(0,3):
       # dados.append((int(input(f"Digite um valor para [{c, d}]: "))))
        dados[l][c] = int(input(f"Digite um valor para [{l, c}]: "))
print("-="* 30)
#print(dados)
for x in range(0,3):
    for y in range(0,3):
        print(f"[{dados[x][y]:^5}]", end="")
    print()