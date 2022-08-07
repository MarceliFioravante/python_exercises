'''Faca um mini sistema que utilize o iteractive Help do Python.
O usuario vai digitar o comando e o manual vai aparecer.
Quando o usuario digitar a palavra 'FIM', o programa se encerrara'''
from time import sleep
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)


def minisistem():
    while True:
        msg = str('SISTEMA DE AJUDA PyHELP')
        tam = len(msg) + 4
        print(Back.GREEN + '~' * tam)
        print(Back.GREEN + f'  {msg}  ')
        print(Back.GREEN + '~' * tam)
        escolha = str(input('Funcao ou Biblioteca > '))
        if escolha.upper() in "FIM":
            sleep(1)
            mens = str('ATÉ LOGO!')
            tamanhomsg = len(mens) + 4
            print(Back.RED + '~' * tamanhomsg)
            print(Back.RED + f'  {mens}  ')
            print(Back.RED + '~' * tamanhomsg)
            break
        mensagem = str(f'Acessando o manual do comando "{escolha}"')
        tamanho = len(mensagem) + 4
        print(Back.BLUE + '~' * tamanho)
        print(Back.BLUE + f'  {mensagem}  ')
        print(Back.BLUE + '~' * tamanho)
        sleep(1)
        help(escolha)


minisistem()


# Fore: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
# Back: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
# Style: DIM, NORMAL, BRIGHT, RESET_ALL
# print(Fore.BLACK + Back.GREEN + Style.BRIGHT)