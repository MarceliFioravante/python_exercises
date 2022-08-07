'''Crie um programa que tenha uma funcao fatorial() que receba dois parametros: o primeiro que indique
o numero a calcular e o outro chamado show, que sera um valor logico opcional indicando se sera mostrado
ou nao na tela o processo de calculo do fatorial.'''
def fatorial(num, show=False):
    """
    -> Calcula o valor de um fatorial
    :param num: o numero a ser calculado
    :param show: (opcional), mostrar ou nao a conta
    :return: o valor do Fatorial
    """
    print('-' * 30)
    f = 1
    for c in range(num, 0, -1):
        if show:
            print(f'{c}', end=" ")
            if c > 1:
                print('x', end=' ')
            else:
                print('=', end=' ')
        f *= c
    return f


#programa principal
print(fatorial(1, show=True))
help(fatorial)