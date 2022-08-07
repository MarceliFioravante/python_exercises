'''1- Perguntar qual cacactere o jogador deseja ter
2 - setar o caractere para o computaador
3- Perguntar qual local da matriz o jogador quer fazer a jogada, mostrar a matriz
4 - fazer a jogada
5 - Jogada do computador
6 - quem completar primeiro uma linha ganha. 3 horizontais, 3 verticais e duas diagonais'''
# Matriz ========== 86/87
'''dados = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0,3):
    for c in range(0,3):
       # dados.append((int(input(f"Digite um valor para [{c, d}]: "))))
        dados[l][c] = int(input(f"Digite um valor para [{l, c}]: "))
print("-="* 30)
#print(dados)
for x in range(0,3):
    for y in range(0,3):
        print(f"[{dados[x][y]:^5}]", end="")
    print()'''
caracter = str(input('Qual caracter deseja escolher [X/0]: '))
jogador = caracter
computador = str
while True:
    dados = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    for x in range(0, 3):
        for y in range(0, 3):
            print(f"[{dados[x][y]:^5}]", end="")
        print()
    jogada = str(input('EScolha onde quer jogar: '))
    if dados[] === jogada:
        substituir o numero pelo simbolo