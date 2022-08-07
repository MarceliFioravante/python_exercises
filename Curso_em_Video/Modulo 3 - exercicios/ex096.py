'''Crie um programa que tenha uma função chamada área, que receba as dimensões de um terreno retangular
(largura x comprimento) e mostre a área do terreno.'''
def area(l,c):
    area = l * c
    print(f'A área de um terreno de {l:.1f}x{c:.1f}m é {area:.1f}m².')


print('Controle de Terrenos')
print('-' * 20)
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
area(l, c)
