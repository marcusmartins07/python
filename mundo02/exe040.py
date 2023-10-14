n1=float(input('Primeira nota: '))
n2=float(input('Segunda nota: '))
media=(n1+n2)/2

if(media<5):
    print('O aluno está reprovado')
elif(media>=5)and(media<=6.9):
    print('O aluno está em recuperação')
else:
    print('O aluno está aprovado')

print('Tirando {} e {} a média do aluno é {}'.format(n1, n2, media))