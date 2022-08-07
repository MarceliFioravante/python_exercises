# todos os numeros pares que estao entre 1 e 50
print("Todos os números pares que estão entre 1 e 50: ")
for c in range (2, 51): # minha resolucao
    if c % 2 == 0:
        print(c," ", end= "")

for c in range (2, 51, 2): # resolucao Guanabara
    print(c, end= " ")
