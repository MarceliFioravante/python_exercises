'''Crie um programa que leia varios numeros inteiros pelo teclado. Condicao de parada: quando o usuário
digita 999.
No final mostre quantos numeros foram digitados e qual a soma deles, desconsiderando o flag.'''
soma = contador = 0
while True: # sempre vai ser verdadeiro até o momento que o flag for estabelecido!
    num = int(input("Digite um valor [999 para sair]: "))
    if num == 999:
        break
    contador += 1
    soma += num
print(f"Foram digitados {contador} números e a soma deles é {soma}.")