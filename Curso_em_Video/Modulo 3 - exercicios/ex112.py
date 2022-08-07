'''Dentro do pacote utilidade do ex 111, temos um modulo chamado Dado. Crie uma funcao chamada
leiadinheiro() que seja capaz de funcionar como uma funcao input(), mas com validadacao de dados para
aceitar apenas valores que sejam monetarios.'''
from UtilidadesCeV import dado, moeda

p = dado.leiaDinheiro('Digite o preco: R$ ')
moeda.resumo(p, 35)