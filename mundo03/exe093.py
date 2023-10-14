jogador=dict()
gol=list()

jogador['nome']=str(input('Nome do jogador: '))
n=int(input(f'Quantas partidas {jogador["nome"]} jogou: '))

for c in range(0, n):
  gol.append(int(input(f'Quantos gols na partida {c+1}: ')))
jogador['gols']=gol
jogador['total']=sum(gol)
print(jogador)

for k, v in jogador.items():
  print(f'O campo {k} tem o valor {v}')

print(f'O jogador {jogador["nome"]} jogou {len(gol)} partidas')
for i, v in enumerate(jogador['gols']):
  print(f'Na partida {i+1}, fez {v}')
print(f'Foi um total de {sum(gol)} gols')
