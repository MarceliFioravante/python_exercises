cidade = str(input("Em qual cidade voce mora?")).strip()
#cidade = cidade.split()
#print("SANTO" in cidade[0])
# print("O nome da sua cidade comeca com SANTO ?", "SANTO" in cidade) #aqui o código so pega santo com todas upper
print(cidade[:5].upper() == "SANTO")
