'''teste = list()
teste.append("Gustavo")
teste.append(22)
galera = list()
galera.append(teste[:]) #cópia da lista teste
teste[0] = "Maria"
teste[1] = 22
galera.append(teste[:])
print(galera)

galera = [["João", 19], ["Ana", 33], ["Joaquim", 13], ["Maria", 44]]
print(galera)
print(galera[0][0])
print(galera[2][1])
for p in galera:
    # print(p[0]) #para pegar apenas os nomes
    print(f"{p[0]} tem {p[1]} anos de idade.")'''

galera = list()
dado = list()
maior = menor = 0
for c in range(0, 3):
    dado.append(str(input("Nome: ")))
    dado.append(int(input("Idade: ")))
    galera.append(dado[:]) #uma cópia da lista Dado
    dado.clear()
print(galera[1])
for p in galera:
    if p[1] >= 21:
        print(f"{p[0]} é maior de idade.")
        maior += 1
        print(p[1])
    else:
        print(f"{p[0]} é menor de idade.")
        menor += 1
print(f"Temos {maior} maiores e {menor} menores de idade.")
