# soma entre os numeros impares
# que sao multiplos de 3
# que estao entre 1 e 500
s = 0
cont = 0
for c in range (1, 501):
  if c % 3 == 0 and c % 2 == 1:
      s += c
      cont = cont + 1
      # print(c," ", end="")
print("O valor da somatória dos {} número ímpares, multiplos de 3 entre 1 e 500 é: {}.".format(cont, s))
