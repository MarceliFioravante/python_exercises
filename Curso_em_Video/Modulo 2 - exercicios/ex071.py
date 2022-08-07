'''Crie um programa que simule o funcionamento de um caixa eletronico.
No inicio pergunte ao usuário qual o valor que será sacado (numero inteiro) e o
programa vai informar quantas cédulas de cada valor serão entregues
considere que o caixa eletronico possui cédulas de 1, 10, 20 e 50 reais.'''
print("-" * 30)
print("{:-^30}".format("CAIXA ELETRÔNICO"))
print("-" * 30)
valor = int(input("Qual valor será sacado? R$ "))
total = valor
cedula = 50
totalcedula = 0
while True:
    if total >= cedula:
        total -= cedula
        totalcedula += 1
    else:
        if totalcedula > 0:
            print(f"Total de {totalcedula} cédulas de {cedula} reais!")
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        totalcedula = 0
        if total == 0:
            break
print("=" * 30)

print("Volte sempre ao banco! Tenha um bom dia!")