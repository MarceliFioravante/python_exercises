'''Escreva um programa que leia um numero n inteiro qualquer e mostre na tela os n primeiros elementos
  de uma sequencia de Fibonacci'''
# 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987,
'''n = int(input("Entre quantos elementos da sequencia de Fibonacci quer ver: "))
n1 = 0
n2 = 1
soma = 0
contador = 1
while contador <= n:
    print(soma, end= " ")
    contador += 1
    n1 = n2
    n2 = soma
    soma = n1 + n2'''

# RESOLUÇÃO GUANABARA
print("-" * 30)
print(" SEQUÊNCIA DE FIBONACCI")
print("-" * 30)
n = int(input("Quantos termos você quer mostrar? "))
print("~" * 30)
t1 = 0
t2 = 1
print("{} -> {}".format(t1, t2), end= " ")
cont = 3
while cont <= n:
    t3 = t1 + t2
    print("-> {} ".format(t3), end= " ")
    t1 = t2
    t2 = t3
    cont += 1
print("Fim!")





