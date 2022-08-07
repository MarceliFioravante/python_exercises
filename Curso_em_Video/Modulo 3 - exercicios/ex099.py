'''DESEMPACOTAMENTO DE PARAMETROS
Faca um programa que tenha uma função chaamda maior(), que receberá varios parametros
com valores inteiros. Seu programa deve analisar todos os valores e dizer qual é o maior.  '''
def maior(*num):
    print('Analisando os valores passados...')
    if len(num) == 0:
        print(f'Foram informados 0 valores ao todo.')
        print('Nao existe maior valor.')
    else:
        print(f'{num}...Foram informados {len(num)} valores ao todo.')
        maior = num[0]
        for c in range(1, len(num)):
            if num[c] > maior:
                maior = num[c]
        print(f'O maior valor informado foi {maior}.')
        print('-=' * 30)


maior(9, 90, 3, 5)
maior(1, 115, 6, 8, 79)
maior(10, 245, 99, 115)
maior()