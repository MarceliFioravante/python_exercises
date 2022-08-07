# ler uma frase qualquer e dizer se ela é um plindromo, desconsiderando os espacos.
# ex: APOS A SOPA // A SACADA DA CASA // A TORRE DA DERROTA // O LOBO AMA BOLO // ANOTARAM A DATA DA MARATONA
frase = str(input("Digite uma frase: ")).upper().strip()
palavras = frase.split()
junto = "".join(palavras)
inverso = ""
# inverso: junto[::-1] e nao é preciso usar o for!
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print("O inverso de {} é {}.".format(junto, inverso))
if inverso == junto:
    print("Essa frase é um PALÍNDROMO!")
else:
    print("ESSA FRASE NAO É UM PALÍNDROMO!")


