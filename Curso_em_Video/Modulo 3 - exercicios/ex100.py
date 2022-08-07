"""FACA um programa que tenha uma lista chamada numeros e duas funcoes
chamadas sorteio() e somaPar().
A primeira funcao vai srotear 5 numeros e vai coloca-los dentro da lista.
A segunda funcao vai mostrar a soma entre todos os valores pares sorteados pela funcao anterior."""
from random import randint

def sorteio():
    numeros = list()
    print(f'Os numeros sorteados sao:', end=" ")
    for c in range(1, 6):
        num = randint(1, 10)
        numeros.append(num)
        print(f'{num}', end=" ")
    print('PRONTO!')
    return numeros

def somaPar(somalista):
    soma = 0
    for valor in somalista:
        if valor % 2 == 0:
            soma += valor
    print(f'A soma dos valores pares é {soma}.')


numeros = sorteio()
#print(f'Os números sorteados sao: {numeros}')
somaPar(numeros)


