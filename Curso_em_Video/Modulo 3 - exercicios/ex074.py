'''Crie um programa que vai gerar 5 números aleatórios e colocar em uma tupla.
Depois disso mostre a listagem dos numeros gerados e tambem indique o menor e o maior valor que
estão na tupla'''
from random import sample
from random import randint   # Guanabara
valores = (randint(1, 10), randint(1,10), randint(1,10), randint(1,10), randint(1,10))
#print(valores)
#valores = (sample(range(1, 10), 5))
#print(valores)
#tupla = valores
#max = max(tupla)
#min = min(tupla)
print(f"Os valores gerados foram {valores}.")
print(f"O maior valor sorteado foi {max(valores)}.")
print(f"O menor valor sorteado foi {min(valores)}.")

#Os valores sorteados foram:
#O maior valor sorteado foi:
#O menor valor sorteado foi: