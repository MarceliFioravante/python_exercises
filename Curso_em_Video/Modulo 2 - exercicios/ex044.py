#print("{}".format("LOJAS GUANABARA"))
preco = float(input("Informe o preço do produto: R$ "))
print("Escolha abaixo a opção de pagamento:")
print('''[ 1 ] - À vista - dinhero ou cheque (10% de desconto)
[ 2 ] - À vista no cartão (5% de desconto)
[ 3 ] - Em até 2x no cartão
[ 4 ]- 3x ou mais no cartão (20% de juros)''')
pagamento = int(input("Qual é a opção? "))
if pagamento == 1:
    vista = preco - (preco * 10 / 100)
    print("O valor a pagar será de R${:.2f}.".format(vista))
elif pagamento == 2:
    cartao = preco - (preco * 5 / 100)
    print("O valor a pagar será de R${:.2f}.".format(cartao))
elif pagamento == 3:
    parcela = preco / 2
    print("Sua compra será parcelada em 2x de R${:.2f}.".format(parcela))
    print("O valor a pagar será de R${:.2f}.".format(preco))
elif pagamento == 4:
    maisparcelas = preco + (preco * 20 / 100)
    parcela = int(input("Quantas parcelas? "))
    totparcelas = maisparcelas / parcela
    print("Sua compra será parcelada em {}x vezes de R${:.2f} COM JUROS.".format(parcela, totparcelas))
    print("O valor a ser pago será de R${:.2f}.".format(maisparcelas))
else:
    print("Opção INVÁLIDA!")
