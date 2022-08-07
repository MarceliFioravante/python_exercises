# ler o ano de nascimento de 7 pessoas. No final mostrar quantas ainda nao atingiram a maioridade (21 anos) e quantas ja.
from datetime import date
m = 0
maior = 0
for c in range (1, 8):
    ano = int(input("Em que ano a {}. pessoa nasceu: ".format(c)))
    idade = date.today().year - ano
    if idade < 21:
        m += 1
    else:
        maior += 1
print("{} pessoas já atingiram a maioridade.".format(maior))
print("{} pessoas ainda são menores de idade.".format(m))
