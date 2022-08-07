from ex115.lib.interface import *
from ex115.lib.arquivo import *
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do sistema'])
    if resposta == 1:
        lerArquivo(arq)
    elif resposta == 2:
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabecalho('Saindo do Sistema...')
        break
    else:
        print(Fore.RED + 'ERRO! Digite uma opcao valida')