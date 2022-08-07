'''Crie um programa que tenha uma funcao chamada voto() que vai receber como parametro
o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem
voto NEGADO, OPCONAL ou OBR na eleicoes.
> 18 - Voto negado
<= 18 - Voto obr
<65 - voto opcional'''
def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return print(f"Com {idade} anos: VOTO NEGADO.")
    elif 16 <= idade < 18 or idade > 65:
        return print(f'Com {idade} anos: VOTO OPCIONAL.')
    else:
        return print(f'Com {idade} anos: VOTO OBRIGATÓRIO.')


print('-' * 30)
ano = int(input('Em que ano voce nasceu? '))
voto(ano)
