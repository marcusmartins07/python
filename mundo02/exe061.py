print('='*25)
print('   10 TERMOS DE UMA PA')
print('='*25)

termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
final = termo + (10-1) * razao

while termo<=final:
  print(termo, end=' ')
  print('->', end=' ')
  termo+=razao
print('FIM')