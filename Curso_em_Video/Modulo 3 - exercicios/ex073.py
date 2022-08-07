'''Crie uma tupla com os 20 primeiros colocados da Tabela do Campeonato Brasileiro, na
ordem de colocação. Depois mostre
a) Apenas os 5 primeiros coolocados
b) Os ultimos 4 colocados da tabela
c) Um lista com os times em ordem alfabética
d) Em que posição da tabela está o time Chapecoense.'''
campeonato = ("Atletico Mineiro", "Flamengo", "Palmeiras", "Fortaleza", "Corinthians",
              "Bragantino", "Fluminense", "America", "Atletico Goiania", "Santos", "Ceara",
              "Internacional", "Sao Paulo", "Atletico PR", "Cuiaba", "Juventude", "Gremio",
              "Bahia", "Sport Recife", "Chapecoense")
for t in campeonato:
    print(t)
print("-=" * 35)
print(f"Lista dos times do Brasileirão 2021: {campeonato}")
print("-=" * 35)
print(f"Os cinco primeiros colocados são: {(campeonato[0:5])}")
print("-=" * 35)
print(f"Os quatro últimos são: {(campeonato[-4:])}")
print("-=" * 35)
print(f"Times em ordem alfabética: {sorted(campeonato)}.")
print("-=" * 35)
print(f"O Chapecoense está na {campeonato.index('Chapecoense') + 1}º posição.")
