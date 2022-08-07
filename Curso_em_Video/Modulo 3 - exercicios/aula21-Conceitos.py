# Interactive Help
#help(print)
#print(input.__doc__)
def contador(i, f, p):
    # DOCSTRINGS
    """
    -> Faz uma contagem e mostra na tela
    :param i: inicio da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    Funcao criada por Gustavo Guanabara do canal CursoemVideo.
    """
    c = i
    while c <= f:
        print(f'{c}', end=" ")
        c += p
    print('FIM!')


contador(2, 10, 2)
help(contador)

def somar(a=0, b=0, c=0):
    """
    -> Soma tres valores e mostra o resultado na tela.
    :param a: primeiro valor
    :param b: segundo valor
    :param c: terceiro valor
    """
    s= a+b+c
    print(f'A soma é {s}.')


somar(2, 8, 9)
somar()
somar(b=4, c=2)

# <<<<<< ESCOPO DE VARIÁVES >>>>>>>
def teste():
    x = 8   # x tem escopo local (nao foi declarada fora do teste()), ou seja, so funciona dentro da funcao.
    print(f'Na funcao teste, n vale {n}.')
    print(f'Na funcao teste, x vale {x}.')

# Programa principal
n = 2  # variavel global, funciona dentro e fora da funcao
print(f'No programa principal n vale {n}.')
teste()
print(f'No programa principal, x vale {x}')

# <<< ESCOPO DE VARIAVEIS COM GLOBAL >>>
def teste(b):
    global a
    a = 8
    b += 4
    c = 2
    print(f'A dentro vale {a}.')
    print(f'B dentro vale {b}.')
    print(f'C dentro vale {c}.')


a = 5
teste(a)
print(f'A fora vale {a}.')

#  <<<< RETORNANDO VALORES - return() >>>>
def somar(a=0, b=0, c=0):
    s = a+b+c
    #print(f'A soma é {s}.')
    return s

r1 = somar(3, 2, 5)
r2 = somar(2, 4, 6)
r3 = somar(15, 67)
print(f'{r1}')
print(f'A soma dos calculos foram: {r1}, {r2} e {r3}.')