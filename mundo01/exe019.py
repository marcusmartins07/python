import random
a1 = str(input('Digite o nome do primeiro aluno: '))
a2 = str(input('Digite o nome do segundo aluno: '))
a3 = str(input('Digite o nome do terceiro aluno: '))
a4 = str(input('Digite o nome do quarto aluno: '))
alunos = [a1, a2, a3, a4]
escolhido = random.choice(alunos)

print('O aluno escolhido é {}'.format(escolhido))