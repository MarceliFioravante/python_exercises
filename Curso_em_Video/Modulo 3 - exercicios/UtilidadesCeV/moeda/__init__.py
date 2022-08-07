def metade(p=0, show=False):
    m = p / 2
    return m if show is False else moeda(m)


def dobro(p=0, show=False):
    d = 2 * p
    return d if show is False else moeda(d)

def aumentar(p=0, taxa=0, show=False):
    a = p + ((taxa * p) / 100)
    return a if show is False else moeda(a)


def diminuir(p=0, taxa=0, show=False):
    d = p - ((taxa * p)/ 100)
    return d if show is False else moeda(d)


def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:>.2f}'.replace('.', ',')

def resumo(p=0, a=10, r=5):
    print('-' * 30)
    print(f'RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preco analisado: \t{moeda(p)}')
    print(f'Dobro do preco: \t{dobro(p, True)}')
    print(f'Metade do preco: \t{metade(p, True)}')
    print(f'{a}% de aumento: \t{aumentar(p, a, True)}')
    print(f'{r}% de reducao: \t{diminuir(p, r, True)}')
    print('-' * 30)
