'''Crie um programa que leia o nome e duas notas de vários alunos a guarde tudo em uma lista composta.
No final, mostre um boletim contendo a média de cada um e permita que o usuario possa mostrar as notas de cada
aluno individualmente.
3 niveis de lista
No final: Mostrar notas de qual aluno? (puxar pelo index) (999 interrompe)'''
geral = list()
informacoes = list()
aluno = list()
notas = list()
medias = list()
while True:
    aluno.append(str(input("Nome do aluno: ")))
    notas.append(float(input("1a nota: ")))
    notas.append(float(input("2a nota: ")))
    informacoes.append(aluno[:])
    informacoes.append(notas[:])
    geral.append(informacoes[:])
    aluno.clear()
    notas.clear()
    informacoes.clear()
    resp = (str(input("Deseja continuar? [S/N] ")))
    if resp in "Nn":
        break
soma = 0
media = 0
for n in geral:
    soma = n[1][0] + n[1][1]
    media = soma / 2
    medias.append(media)
print("=-" * 30)
print("No.    NOME       MÉDIA")
print("-" * 25)
for a, n, in enumerate(geral):
    print(f"{a:<7}{n[0][0]:^5}{medias[a]:>11.2f}")
print("-" * 25)
while True:
    resp = int(input("Mostrar nota de qual aluno? (999 interrompe): "))
    for a, n, in enumerate(geral):
        if resp == a:
            print(f"Notas da {geral[a][0]} são {n[1]}.")
            print("-" * 25)
    if resp == 999:
        break
print("Finalizando...")
