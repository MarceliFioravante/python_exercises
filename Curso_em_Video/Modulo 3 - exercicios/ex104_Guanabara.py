import colorama
from colorama import Back
colorama.init(autoreset=True)


def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print(Back.RED + 'ERRO! Digite um número inteiro válido.')
        if ok:
            break
    return valor


#Programa principal
n = leiaInt('Digite um numero: ')
print(f'Voce acabou de digitar o número {n}.')