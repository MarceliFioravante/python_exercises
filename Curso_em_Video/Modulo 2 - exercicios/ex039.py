from datetime import date
atual = date.today().year
sexo = str(input("Qual o seu sexo? ")).upper()
if sexo == "FEMININO":
    print("O alistamento militar não é obrigatório para pessoas do sexo feminino!")
elif sexo == "MASCULINO":
    ano = int(input("Em que ano voce nasceu? "))
    idade = date.today().year - ano
    print("Quem nasceu em {}, tem em {}, {} anos!".format(ano, atual, idade))
    if idade < 18:
        falta = 18 - idade
        if falta == 1:
            print("Ainda falta {} ano para você se alistar no exército!".format(falta))
            saldo = atual + falta
            print("Seu alistamento será em {}!".format(saldo))
        else:
            print("Ainda faltam {} anos para você se alistar no exército!".format(falta))
            saldo = atual + falta
            print("Seu alistamento será em {}!".format(saldo))
    elif idade == 18:
              print("Você já tem {} completos. É hora de se alistar no exército!".format(idade))
    else:
        passou = idade - 18
        if passou == 1:
            print("Você passou {} ano do prazo de alistamento no exército!".format(passou))
            saldo = atual - passou
            print("Seu alistamento será em {}!".format(saldo))
        else:
            print("Você passou {} anos do prazo de alistamento no exército!".format(passou))
            saldo = atual - passou
            print("Seu alistamento será em {}!".format(saldo))

