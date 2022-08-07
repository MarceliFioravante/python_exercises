'''Reescreva a funcao leiaInt() do exercicio 104, incluindo agora a possibilidade
de digitacao de um numero inválido. Aproveite e crie tambem uma funcao leiaFloat()
com a mesma funcionalidade.'''
#Nao aceitara: vazio, varios espacos, letras e interromper pelo keyboard.
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except KeyboardInterrupt:
            print(Fore.RED + 'O usuario preferiu nao informar os dados.')
            return 0
        except (ValueError, TypeError):
            print(Fore.RED + 'ERRO! Por favor, digite um numero inteiro válido.')
            continue
        else:
            return n


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except KeyboardInterrupt:
            print(Fore.RED + 'O usuario preferiu nao informar os dados.')
            return 0
        except (ValueError, TypeError):
            print(Fore.RED + 'ERRO! Por favor, digite um numero real válido.')
            continue
        else:
            return n


n = leiaInt('Digite um numero inteiro: ')
num = leiaFloat('Digite um numero real: ')
print(f'O valor inteiro digitado foi {n} e o valor real foi {num}.')