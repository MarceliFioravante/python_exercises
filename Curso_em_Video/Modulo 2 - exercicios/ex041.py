from datetime import date
print("-=-" * 11)
print("CONFEDERAÇÃO NACIONAL DE NATAÇÃO")
print("  ---CADASTRO DE NADADORES---")
print("-=-" * 11)
ano = int(input("Entre o ano de nascimento do atleta: "))
idade = date.today().year - ano
if idade <= 9:
    print("Idade do atleta: {} - CATEGORIA: MIRIM.".format(idade))
elif idade <= 14:
    print("Idade do atleta: {} - CATEGORIA: INFANTIL.".format(idade))
elif idade <= 19:
    print("Idade do atleta: {} - CATEGORIA: JUNIOR.".format(idade))
elif idade <= 25:
    print("Idade do atleta: {} - CATEGORIA: SÊNIOR.".format(idade))
else:
    print("Idade do atleta: {} - CATEGORIA: MASTER.".format(idade))