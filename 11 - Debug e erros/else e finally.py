# else = executa somente se não ocorrer erro
# Finally - Sempre vai ser executado

try:
    num = int(input('Informe um número: '))
except ValueError:
    print('Valor incorreto')
else:
    print(f'Você digitou {num}')
finally:
    print('Executando o finally')

def dividir(a, b):
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError) as err:
        return f'Ocorreu um problema {err}'

num1 = input('Informe o primeiro número: ')
num2 = input('Informe o segundo número: ')

print(dividir(num1, num2))

