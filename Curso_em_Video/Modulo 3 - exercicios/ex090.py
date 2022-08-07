'''Faca um programa que leia nome e media de um aluno, guardando tambem a situacao em um dicionario.
No final mostre o conteudo da estrutura na tela.
Nome:
Média de ...:
Nome =
Media =
Situacao = Aprovado ou Reprovado '''
aluno = dict()
aluno['Nome'] = str(input('Nome do aluno: '))
aluno['Média'] = float(input(f'Média de {aluno["Nome"]}: '))
if (aluno['Média']) >= 7:
    aluno['Situacao'] = 'Aprovado'
elif (aluno['Média']) <= 5:
    aluno['Situacao'] = 'Reprovado'
else:
    aluno['Situacao'] = 'Recuperacao'
print('-=' * 20)
for k, v in aluno.items():
    print(f'- {k} é igual a {v}.')
print('-=' * 20)