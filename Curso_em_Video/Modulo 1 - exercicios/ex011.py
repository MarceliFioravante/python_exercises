l = float(input("Qual é a largura da sua parede: "))
a = float(input("Qual é a altura da sua parede: "))
ar = l * a
print("Sua parede tem a dimensão de {}x{} e sua área é de {}m2".format(l, a, ar))
print("Para pintar essa parede, voce precisará de {} litros de tinta".format(ar / 2))

