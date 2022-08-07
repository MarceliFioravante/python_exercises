'''Crie um modulo chamado moeda.py que tenha as funcoes incorporadas:
aumentar()
diminuir()
dobro()
metade(). FAca um prgrama que importe esse modulo e use essas funcoes.'''
import moeda

p = float(input('Digite o preco (R$): '))
print(f'A metade de {p} é igual {moeda.metade(p)}.')
print(f'O dobro de {p} é igual {moeda.dobro(p)}.')
print(f'Aumentando 10%, temos {moeda.aumentar(p, 10)}.')
print(f'Reduzindo 13%, temos {moeda.diminuir(p, 13)}.')


