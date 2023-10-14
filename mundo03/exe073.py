tabBrasileirao = ('Fortaleza', 'Athletico-PR', 'Atlético-GO', 'Bragantino',
                      'Bahia', 'Fluminense', 'Palmeiras', 'Flamengo', 'Atlético-MG',
                      'Corinthians', 'Ceará SC', 'Santos', 'Cuiabá', 'Sport Recife',
                      'São Paulo', 'Juventude', 'Internacional', 'Grêmio', 'América-MG',
                      'Chapecoense')

print(f'Lista de times do Brasileirão: {tabBrasileirao}')
print(f'Os 5 primeiros são {tabBrasileirao[:5]}')
print(f'Os 4 ultimos são : {tabBrasileirao[-4:]}')
print(f'Times em ordem alfabética: ', sorted(tabBrasileirao))
print(f'A Flamengo esta na {tabBrasileirao.index("Flamengo")+1}° posição')