'''Faca um programa que tenha uma funcao chamada contador(),
que receba 3 parametros: inicio, fim e passo e realize a contagem.
Seu programa tem que ralizar 3 contagens atraves dafuncao criada:
a) de 1 ate 20 de 1 em 1
b) De 10 ate 0, de 2 em 2
c) Uma contagem personalizada. (deve aceitar -1, e 0 conta como 1)'''
from time import sleep
def contador(i, f, p):
    print('-=' * 30)
    if p < 0:
        p *= -1
    if p < 0:
        p *= -1
    print(f'Contando de {i} ate {f}, de {p} em {p}')
    if f > i:
        for c in range(i, f+1, p):
            print(c, end=' ')
            #sleep(0.5)
        print('FIM!')
    if f < i:
        for c in range(i, f, -p):
            print(c, end=' ')
            #sleep(0.5)
        print('FIM!')


contador(1, 10, 1)
contador(10, 0, 2)
print('-=' * 30)
print('Agora é a sua vez de personalizar a contagem: ')
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
contador(i, f, p)