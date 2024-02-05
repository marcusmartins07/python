# Utilizamos o bloco try / except para tratar erros que podem ocorrer no nosso código.
# Previnindo assim que o programa pare de funcionar e o usuário receba mensagem de erro inesperadas

try:
    len(5)
except:
    print('Deu algum problema')

try:
    len(5)
except TypeError as err:
    print(f'A aplicação gerou o seguinte erro: {err}')

# ignorando erro
def pega_valor(dicionario, chave):
    try:
        return dicionario[chave]
    except KeyError:
        return None
    except TypeError:
        return None

dic = {"nome": "Geek"}
print(pega_valor(dic, "game"))