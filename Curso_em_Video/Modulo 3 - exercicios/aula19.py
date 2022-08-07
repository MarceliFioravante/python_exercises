pessoas = {'nome': 'Marceli', 'idade': 30, 'sexo': 'F'}
print(f"A {pessoas['nome']} tem {pessoas['idade']} anos.")
print(pessoas.keys()) # mostra dict_keys(['nome', 'idade', 'sexo'])
print(pessoas.values()) # mostra dict_values(['Marceli', 30, 'F'])
print(pessoas.items()) # mostra dict_items([('nome', 'Marceli'), ('idade', 30), ('sexo', 'F')])
for k in pessoas.keys():
    print(k)
for k in pessoas.values():
    print(k)
for k, v in pessoas.items():
    print(f'{k} = {v}')
# del pessoas['sexo']
pessoas['nome'] = 'Leandro' # para mudar um elemento
pessoas['peso'] = 98.5 # para adicionar um nome index + elemento no dict

# ======== DICT DENTRO DE LISTA ========
brasil = list() #lista com dict dentro
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'Sao Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil[0]['uf']) # printa sem chaves ou colchetes'''
estado = dict()
brasil = []
for c in range(0,3):
    estado['uf'] = str(input('Unidade Federatva: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy()) #nao da pra usar o [:] das listas
print(brasil)
for e in brasil:  # loop para a lista
    #for k, v in e.items():
     #   print(f'O campo {k} tem valor {v}.')
     for v in e.values(): # loop para o dict
         print(v)