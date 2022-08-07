'''Crie um programa que tenha a funcao leiaInt(), que vai funcionar de forma semelhante a
funcao input() do Python, so que fazendo a validacao para aceitar apenas um valor numerico.
ex n=leiaInt('Digite um numero: ')'''
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)


def leiaInt(num):
    n = str(input(num))
    if n.isnumeric():
        n = int(n)
        return n
    while True:
        if n.strip() == "" or len(n) == 0 or type(num) != int:
            print(Back.RED + 'ERRO! Digite um numero inteiro valido.')
            n = (str(input(num)))
        if n.isnumeric():
            n = int(n)
            return n


n = leiaInt('Digite um numero: ')
print(f'Voce acabou de digitar o numero {n}.')