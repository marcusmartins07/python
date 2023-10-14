contIdade=0
mNome=''
mIdade=0
medIdade=0
mediaIdade=0

n=int(input('Numero de pessoas que será analisado: '))
print('----- 1° PESSOA -----')
nome=str(input('Nome: '))
idade=int(input('Idade: '))
s=str(input('Sexo [M/F]: ')).upper()

if s == 'F':
        if idade < 20:
            contIdade+=1
elif s == 'M':
    if idade > mIdade:
        mNome=nome
        mIdade=idade
medIdade+=idade

for c in range (2, n+1):
    
    print('----- {}° PESSOA -----'.format(c))
    nome=str(input('Nome: '))
    idade=int(input('Idade: '))
    s=str(input('Sexo [M/F]: ')).upper()
    
    medIdade+=idade
    
    if s == 'F':
        if idade < 20:
            contIdade+=1
    elif s == 'M':
        if idade > mIdade:
            mNome=nome
            mIdade=idade

mediaIdade=medIdade/n
print('A média de idade do grupo é de {:.2f}'.format(mediaIdade))

if mNome=='' and mIdade==0:
    print('Não possui nenhum homem')
else:
    print('O homem mais velho tem {} anos e se chama {}'.format(mIdade, mNome))

if contIdade==0:
    print('Não possui nenhuma mulher com menos de 20 anos')
elif contIdade<2:
    print('Ao todo é {} mulher com menos de 20 anos'.format(contIdade))
else:
    print('Ao todo são {} mulheres com menos de 20 anos'.format(contIdade))