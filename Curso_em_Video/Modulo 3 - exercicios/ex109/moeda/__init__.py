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
