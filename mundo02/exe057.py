sexo=str(input('Informe seu sexo: ')).strip().upper()
while sexo not in 'MmFf':
    sexo=str(input('Dados inválidos. Por favor, informe seu sexo: ')).strip().upper()
print('Sexo {} registrado com sucesso'. format(sexo))