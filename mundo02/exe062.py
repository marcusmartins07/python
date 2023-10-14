print('='*25)
print('   10 TERMOS DE UMA PA')
print('='*25)

primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
termo = primeiro
count=1
total=0
mais=10

while mais!=0:
  total+=mais
  while count<=total:
    print('{} -> '.format(termo), end=' ')
    termo+=razao
    count+=1
  print('Pausa')
  mais=int(input('Quantos termos você quer mostar a mais? '))
print('Progressão finalizada com {} termos mostrados'.format(total))
