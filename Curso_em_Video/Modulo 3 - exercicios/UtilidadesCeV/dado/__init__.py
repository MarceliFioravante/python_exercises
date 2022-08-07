import colorama
from colorama import Back, Fore
colorama.init(autoreset=True)


def leiaDinheiro(msg):
    ok = False
    while not ok:
        n = str(input(msg)).replace(',', '.').strip()
        if n.isalpha() or n == "":
            print(Fore.RED + f'ERRO! "{n}" é um preco inválido.')
        else:
            ok = True
            return float(n)

