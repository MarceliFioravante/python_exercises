'''In this problem you have to read an integer value and calculate the smallest
possible number of banknotes in which the value may be decomposed.
The possible banknotes are 100, 50, 20, 10, 5, 2 e 1. Print the read value and the list of banknotes.
Input
The input file contains an integer value N (0 < N < 1000000).'''
N = int(input())
print(N)
cem = N/100
print(f'{int(cem)} nota(s) de R$ 100,00')
cinq = (N%100) / 50
print(f'{int(cinq)} nota(s) de R$ 50,00')
vinte = ((N%100) % 50) / 20
print(f'{int(vinte)} nota(s) de R$ 20,00')
dez = (((N%100) % 50)%20) / 10
print(f'{int(dez)} nota(s) de R$ 10,00')
cinco = ((((N%100) % 50)%20)%10) / 5
print(f'{int(cinco)} nota(s) de R$ 5,00')
dois = (((((N%100) % 50)%20)%10)%5) / 2
print(f'{int(dois)} nota(s) de R$ 2,00')
um = ((((((N%100) % 50)%20)%10)%5)%2) / 1
print(f'{int(um)} nota(s) de R$ 1,00')
