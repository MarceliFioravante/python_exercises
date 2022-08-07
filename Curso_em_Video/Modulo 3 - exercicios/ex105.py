''''FAca uma programa que tenha uma funcao chamada notas() que pode receber varias notas de alunos e vai
retornar um dicionario com as seguintes informacoes:
a) Quantidade de notas
b) A maior nota
c) A menor nota
d) A media da turma
e) A situacao

Adicione tambem as docstrings da funcao.'''
def notas(*n, sit=False):
    """
    -> Funcao para analizar notas e situacoes de varios alunos
    :param n: lista de notas dos alunos
    :param sit: (opcional) mostra a situacao: boa, razoavel ou ruim dependendo da media
    :return: retorna os valores para um dicionario
    """
    print('-' * 30)
    '''somanotas = 0
    resp = dict()
    resp['Total de notas'] = len(n)
    for c in range(0, len(n)):
        maior = n[0]
        menor = n[0]
        somanotas += n[c]
        media = somanotas / len(n)
        resp['Média'] = media
        if n[c] >= maior:
            maior = n[c]
            resp['Maior'] = maior
        if n[c] <= menor:
            menor = n[c]
            resp['Menor'] = menor
    if sit:
        if media <= 5:
            resp['Situacao'] = "Ruim"
            return resp
        elif media >= 7:
            resp['Situacao'] = "Boa"
            return resp
        elif media > 5 and media < 7:
            resp['Situacao'] = "Razoável"
            return resp
    else:
        return resp'''
    r = dict()
    r['Total'] = len(n)
    r['Maior'] = max(n)
    r['Menor'] = min(n)
    r['Média'] = sum(n)/len(n)
    if sit:
        if r['Média'] >= 7:
            r['Situacao'] = "BOA"
        elif r['Média'] >= 5:
            r['Situacao'] = "RAZOÁVEL"
        else:
            r['Situacao'] = "RUIM"
    return r

# Programa principal
resp = notas(5.5, 6, 6, 6.5, 9, sit=True)
print(resp)
#help(notas)
