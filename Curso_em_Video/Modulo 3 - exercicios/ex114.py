'''Crie um código em Python que teste se o site Pudim esta acessivel pelo
computador usado.'''
import webbrowser as wb
import requests
def main():
    url = 'http://pudim.com.br/'
    try:
        req = requests.get(url, timeout=3)
        wb.open(url)
        print('Consegui acessar o site Pudim com sucesso')
    except requests.ConnectionError:
        print('Nao foi possivel abrir o site Pudim no momento.')


main()