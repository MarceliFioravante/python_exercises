import random
a1 = input("Aluno 1: ")
a2 = input("Aluno 2: ")
a3 = input("Aluno 3: ")
a4 = input("Aluno 4: ")
#TA = [a1, a2, a3, a4]
TA = a1, a2, a3, a4
print("O aluno escolhido pelo professor é {}!".format(random.choice(TA)))
