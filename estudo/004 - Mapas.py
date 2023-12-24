receita = {'jan': 100, 'fev': 250, 'mar': 400}
print(receita)

print(receita.keys())

for chave in receita.keys():
    print (receita[chave])

print(sum(receita.values()))