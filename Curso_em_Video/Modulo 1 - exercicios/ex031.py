dis = int(input("Digite a distância da sua viagem em km: "))
# preco = dis * 0.50 if dis <= 200 else dis * 0.45
if dis <= 200:
    dis1 = dis * 0.50
    print("Sua viagem tem menos de 200km e a passagem custará {:.2f}.".format(dis1))
else:
    dis2 = dis * 0.45
    print("Sua viagem tem mais de 200km e a passagem custará {:.2f}.".format(dis2))
