'''Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
Seu aplicativo deverá analisar se a expressão digitada está com os parênteses abertos e fechados na ordem correta.
* Sua expressão é válida.
* Sua expressão está errada'''
aberto = 0
fechado = 0
expressao = list(str(input("Escreva sua expressão: ")))
for c in range(0, len(expressao)):
    if expressao[c] == "(":
        aberto += 1
    if expressao[c] == ")":
        fechado += 1
#print(f" parenteses abertos: {aberto}.")
#print(f"parenteses fechados: {fechado}.")
if aberto == fechado:
    print("Sua expressão é valida!")
else:
    print("Sua expressão é inválida!")


