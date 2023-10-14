print('='*25)
print('   10 TERMOS DE UMA PA')
print('='*25)

termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
final = termo + (10-1) * razao

for c in range(termo, final+razao, razao):
  print(c, end=' ')
  print('->', end=' ')
print('Acabou')