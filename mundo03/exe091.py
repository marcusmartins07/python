from random import randint
from operator import itemgetter

jogo = {
  'jogadorA':randint(1, 6),
  'jogadorB':randint(1, 6),
  'jogadorC':randint(1, 6),
  'jogadorD':randint(1, 6)
}

ranking=list()

for k, v in jogo.items():
  print(f'{k} tirou {v} no dado.')
ranking=sorted(jogo.items(), key=itemgetter(1), reverse=True)
print(ranking)

for i, v in enumerate(ranking):
  print(f'{i+1}° lugar: {v[0]} com {v[1]}.')
  