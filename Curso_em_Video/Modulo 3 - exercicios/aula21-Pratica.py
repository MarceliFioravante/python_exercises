def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f


n = int(input('Digite um numero: '))
print(fatorial(n))
f1 = fatorial(5)
f2 = fatorial(100)
f3 = fatorial()
print(f'O fatorial de {5} é {fatorial(5)}, o fatorial de {100} é {fatorial(100)}, o fatorial de 0 é {fatorial()}.')

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

def par(num=0):
    if num % 2 ==0:
        return True
    else:
        return False


num = int(input('Digite um valor: '))
if par(num):
    print('É par!')
else:
    print('Nao é par!')