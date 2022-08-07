ficha = []
while True:
    nome = str(input("Nome: "))
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resp = (str(input("Deseja continuar? [S/N] ")))
    if resp in "Nn":
        break
print("=-" * 30)
print(f'{"No":<4}{"Nome":<10}{"Média":>8}')
print("-" * 26)
for i, a in enumerate(ficha):
    print(f"{i:<4}{a[0]:<10}{a[2]:>8.1f}")
while True:
    print("=-" * 30)
    resp = int(input("Mostrar nota de qual aluno? (999 interrompe): "))
    if resp == 999:
        print("Finalizando...")
        break
    if resp <= len(ficha) - 1:
        print(f"Notas da {ficha[resp][0]} são {ficha[resp][1]}.")99
print("VOLTE SEMPRE...")

