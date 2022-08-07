maiores = homens = mulheres = 0
resp = "S"
while resp in "S":
    print("-" * 20)
    str(print("CADASTRO DE PESSOAS")).center(15)
    print("-" * 20)
    idade = int(input("Idade: "))
    sexo = " "
    while sexo not in "MF":
        sexo = str(input("Sexo: [M/F] ")).upper().strip()[0]
    if idade >= 18:
        maiores += 1
    elif sexo == "M":
        homens += 1
    elif sexo == "F" and idade <= 20:
        mulheres += 1
    resp = " "
    while resp not in "SN":
        resp = str(input("Quer continuar? [S/N] ")).upper().strip()[0]
        if resp == "N":
            print("Cadastro finalizado!")
            break
print("-" * 20)
print(f"No total {maiores} pessoas tem mais de 18 anos.")
if homens == 1:
    print(f"Foi cadastrada {homens} pessoa do sexo masculino.")
elif homens > 1:
    print(f"Foram cadastradas {homens} pessoas do sexo masculino.")
print(f"Das mulheres cadastradas, {mulheres} tem menos de 20 anos.")

'''Crie um programa que leia a idade e o sexo de várias pessoas.
A cada pessoa cadastrada o programa deverá perguntar ao usuário se ele quer continuar ou nao.
No final mostre:
a) Quantas pessoas tem mais de 18 anos
b) Quantos homens foram cadastrados
c) Quantas mulheres tem menos de 20 anos'''
