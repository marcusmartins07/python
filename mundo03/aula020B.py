
def dobra(lst):
  pos=0
  while pos < len(lst):
    lst[pos]*=2
    pos+=1

def soma(*valores):
  s=0
  for num in valores:
    s+=num
  print(f'Somando os valores {valores} temos {s}')

valores=[7, 2, 5, 0, 4]
print(valores)
dobra(valores)
print(valores)

soma(5,2)
soma(2, 9, 4)


