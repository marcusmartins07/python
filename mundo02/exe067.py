n=c=1

while n>0:
  n=int(input('Quer ver a tabuada de qual valor? '))
  if n>0:
    c=1
    while c<11:
      print(f'{n} X {c} = {n*c}')
      c+=1
  else:
    break
print('FIM')