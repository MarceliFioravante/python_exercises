frase = str(input("Digite uma frase:")).upper().strip()
print("A letra A aparece {} vezes nessa frase.".format(frase.count("A")))
print("A letra A apareçe primeiro na posiçao {}.".format(frase.find("A")+1))
print("A letra a aparece por último na posiçao {}.".format(frase.rfind("A")+1))
