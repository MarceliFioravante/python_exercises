def soma(a,b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma de A + B é: {s}')


# Programa principal
soma(8, 9)  # soma(a=8, b= 9) ou soma(b = 9, a= 7)
soma(3, 4)
soma(9, 5)

# DesEmpacotamento
def contador(*num): # o * informa pro Python que não existe uma quantidade fixa de valores que irão entrar
    # print(num)  # o resultado sai em forma de tupla()
   # for valor in num:
    #    print(f"{valor}", end=' ')
    #print('FIM')
    tam = len(num)
    print(f'Recebi os valores {num} e são ao todo {tam} números.')
contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)
def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *=2
        pos += 1


valores = [4, 6, 7, 2, 1]
dobra(valores)
print(valores)


def soma(* valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos a soma {s}.')

soma(5, 2)
soma(10,16)