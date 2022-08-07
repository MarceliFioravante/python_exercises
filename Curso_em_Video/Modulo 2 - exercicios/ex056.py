# ler o nome, idade e sexo de 4 pessoas. Mostrar no final:
# a media de idade do grupo
# qual é o nome do homem mais velho
# quantas mulheres tem menos de 20 anos
idades = 0
menor20 = 0
maioridade = 0
# nomemaisvelho = ""
for c in range(1,5):
    print("----- {}. PESSOA -----".format(c))
    nomes = str(input("Nome: ")).strip()
    idade = int(input("Idade: "))
    sexo = str(input("SEXO [M/F]: ")).strip()
    idades = idades + idade
    if idade > maioridade:
        maioridade = idade
        nomemaior = nomes
    if sexo == "F" and idade < 20:
        menor20 = menor20 + 1
media = idades / 4
print("A média de idade do grupo é {:.1f} anos.".format(media))
print("O total de mulheres com menos de 20 anos é de {}.".format(menor20))
print("A pessoa com maior idade, {} anos, se chama {}.".format(maioridade, nomemaior))
