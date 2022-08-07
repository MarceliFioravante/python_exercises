n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))
n3 = int(input("Digite outro número: "))
'''menor = min(n1, n2, n3)
maior = max(n1, n2, n3)
print(menor, maior)'''
if (n1 > n2) and (n1 > n3):
    print("O número {} é o maior número de todos!".format(n1))
    print("O menor número é o número {}!".format(min(n2,n3)))
elif (n2 > n1) and (n2 > n3):
    print("O número {} é o maior número de todos!".format(n2))
    print("O menor número é o número {}!".format(min(n1,n3)))
else:
    print("O número {} é o maior número de todos!".format(n3))
    print("O menor número é o número {}!".format(min(n1, n2)))
