nome = str(input("Digite seu nome completo: ")).strip()
primeiro = nome.split()
print("Primeiro nome: ", primeiro[0])
print("Ultimo nome: {}".format(primeiro[len(primeiro)-1]))
