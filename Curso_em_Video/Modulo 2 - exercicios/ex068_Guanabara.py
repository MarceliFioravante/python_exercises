from random import randint
v = 0
while True:
    jogador = int(input("Digite um valor: "))
    computador = randint(0,10)
    total = jogador + computador
    tipo = " "
    while tipo not in "PI":
        tipo = str(input("PAR ou IMPAR? [P/I] ")).strip().upper()[0] # [0] - # pega somente a primeira letra
    print(f"Voce jogou {jogador} e o computador jogou {computador}. Total de {total}. ", end= "")
    print("Deu PAR" if total % 2 == 0 else "Deu IMPAR")
    if tipo == "P":
        if total % 2 == 0:
            print("Você VENCEU!")
            v += 1
        else:
            print("Você PERDEU!")
            break
    elif tipo == "I":
        if total % 2 == 1:
            print("Você VENCEU!")
            v += 1
        else:
            print("Você PERDEU!")
            break
    print("Vamos joga novamente...")
print(f"Game OVER! Você venceu {v} vezes!")
