import PySimpleGUI as sg
from validaCPF import *

# 08768529406

# Defina o layout da janela
layout = [
    [sg.Text('Digite seu CPF:')],
    [sg.Input(size=(20,1), key='cpfSujo')],
    [sg.Button('Verifica', key='verifica')],
    [sg.Text('', size=(20,1), key='saida')]
]

# Crie a janela
window = sg.Window('Validador de CPF', layout)

# Loop de eventos
while True:
    event, values = window.read()
    
    cpfSujo=values['cpfSujo']
    cpfMultiplicado=multiplicaCpf(cpfSujo)
    print(type(cpfMultiplicado))
    print(len(cpfMultiplicado))

    # Se o usuário fechar a janela, saia do loop
    if event == sg.WIN_CLOSED:
        break
    
    # Se o botão for pressionado, atualize a saída
    if event == 'verifica':
        window['saida'].update(cpfMultiplicado)
        
# Feche a janela ao sair do loop
window.close()
