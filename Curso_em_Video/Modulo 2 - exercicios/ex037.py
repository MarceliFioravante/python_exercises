num = int(input("Digite um número inteiro: "))
base = input('''Escolha uma base para conversão:
[ 1 ] Binário
[ 2 ] Octal
[ 3 ] Hexadecimal''')
escolha = int(input("Sua escolha: "))
if escolha == 1:
    print("O número {} convertido para binário é {}.".format(num, bin(num)[2:]))
elif escolha == 2:
    print("O número {} convertido para octal é {}.".format(num, oct(num)[2:]))
elif escolha == 3:
    print("O número {} convertido para hexadecimal é {}.".format(num, hex(num)[2:]))
else:
    print("Opção inválida. Tente novamente!")



