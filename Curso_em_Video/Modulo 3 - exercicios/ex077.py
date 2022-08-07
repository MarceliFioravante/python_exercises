'''Crie um programa que tenha uma tupla com várias palavras (não usar acentos)
Depois disso voce deve mostrar, para cada palavra, quais são as suas vogais.'''
palavras = ("Python", "Computador", "Aprender", "Programacao", "Biblioteca", "Aprendizado", "Estudo", "Teclado", "Jupiter", "Escola")
'''caracter = "AEIOUaeiou"
for c in range (0, len(palavras)):
    print(f"\nNa palavra {palavras[c]}, temos as vogais: ", end=" ")
    for i in palavras[c]:
        if i in "AEIOUaeiou":
            print(i, end="")'''
for p in palavras:
    print(f"\nNa palavra {p.upper()} temos as vogais", end=" ")
    for letra in p:
        if letra.lower() in "aeiou":
            print(letra, end= " ")