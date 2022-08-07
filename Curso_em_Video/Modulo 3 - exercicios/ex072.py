'''Crie um programa que tenha uma tupla completamente preenchida, com uma contagem
por extenso, de 0 até 20. Seu programa deverá ler um número pelo teclado entre 0 e 20 e mostrá-lo
 por extenso.'''
contagem = ("zero", "um", "dois", "tres", "quatro",
            "cinco", "seis", "sete", "oito", "nove",
            "dez", "onze", "doze", "treza", "quatorze",
            "quinze", "dezesseis", "dezessete", "dezoito",
            "dezenove", "vinte")
while True:
    num = int(input("Digite um número entre 0 e 20: "))
    if num >= 0 and num <= 20: # if 0 <= num <= 20:
        break
    print("Tente novamente. Digite um número: ")
'''for pos, numeros in enumerate(contagem):
    if num == pos:
        pos = contagem[pos]
        print(f"Você digitou o número {pos}.")'''
print(f"Voce digitou o número {contagem[num]}.")
