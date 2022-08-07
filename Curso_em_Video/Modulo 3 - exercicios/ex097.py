'''Faca um programa que tenha uma função chamada escreva(), que receba um texto qualquer como
parametro e mostre uma mensagem com tamanho adaptável.'''
def escreva(msg):
    tam = len(msg) + 4
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)


escreva('Marceli Borges Fioravante')
escreva("Lara")
escreva('Curso de Python')
str = str(input("Digite um texto: "))
escreva(str)
