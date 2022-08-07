def metade(p=0):
    m = p / 2
    return m


def dobro(p=0):
    d = 2 * p
    return d


def aumentar(p=0, taxa=0):
    a = p + ((taxa * p) / 100)
    return a


def diminuir(p=0, taxa=0):
    d = p - ((taxa * p)/ 100)
    return d


def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:>.2f}'.replace('.', ',')
