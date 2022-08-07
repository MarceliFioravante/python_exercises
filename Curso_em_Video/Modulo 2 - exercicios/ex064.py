'''Crie um programa que leia varios numeros inteiros pelo teclado
O programa só vai parar quando o usuario digitar 999, que é a condicao de parada
No final mostre quantos numeros foram digitados e qual foi a soma entre eles (desconsiderando o flag)'''
soma = 0
contador = 0
numeros = 0
# soma = contador = numeros = 0
numeros = int(input("Digite um número [999 para parar]: "))
while numeros != 999:
    soma += numeros
    contador += 1
    numeros = int(input("Digite um número [999 para parar]: "))
print("Foram digitados {} números e a soma entre eles é de {}.".format(contador, soma))
# if c == 999:
    # break
