''''Faca um programa que leia o sexo de uma pessoa, mas só aceite M ou F. Caso esteja errado, peca a digitacao novamente
ate ter um valor correto'''
'''sexo = " "
while sexo != "M" != "F":  # while sexo not in "MmFf":
    sexo = str(input("Informe o seu sexo [M/F]: ")).upper().strip()[0]
    if sexo == "M" or sexo == "F":
        print("A informação do seu sexo foi computada!")
        break
    else:
        print("Resposta dada de forma incorreta. Tente novamente!")'''

sexo = str(input("Digite seu sexo: [M/F] ")).strip().upper()[0]
while sexo not in "MmFf":
    sexo = str(input("Dados invalidos. Por favor, informe seu sexo: ")).strip().upper()[0]
print("Sexo {} computado com sucesso.".format(sexo))