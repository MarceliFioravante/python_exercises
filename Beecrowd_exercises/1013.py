'''Make a program that reads 3 integer values and present the greatest one followed by the message
"eh o maior". Use the following formula:
Input
The input file contains 3 integer values.
Output
Print the greatest of these three values followed by a space and the message “eh o maior”.'''
valor = input().split(" ")
A, B, C = valor
maiorAB = (int(A)+int(B)+(abs(int(A)-int(B)))) / 2
resultado = (int(maiorAB)+int(C)+(abs(int(maiorAB)-int(C)))) / 2
print(f'{resultado} eh o maior')
