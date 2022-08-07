import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print(Fore.RED + 'ERRO! Por favor, digite um numero inteiro válido.')
            continue
        except KeyboardInterrupt:
            print(Fore.RED + 'O usuario preferiu nao informar os dados.')
            return 0
        else:
            return n


def linha(tam = 42):
    return '-' * tam

def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabecalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(Fore.GREEN + f'{c} - ' + Fore.BLUE + f'{item}')
        c += 1
    print(linha())
    opc = leiaInt('Sua opcao: ')
    return opc