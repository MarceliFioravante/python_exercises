nome = str(input("Escreva seu nome completo: ")).strip()
print("Analisando seu nome...")
print("Seu nome em maiusculas é:", nome.upper())
print("Seu nome em minusculas é:", nome.lower())
print("Seu nome tem ao todo {} letras".format(len(nome) - nome.count(" ")))
separa = nome.split()
print("Seu primeiro nome é {} e ele tem {} letras".format(separa[0], len(separa[0])))