from tkinter import *

#Tamanhos de tela

menu_inicial = Tk() # recebe o metodo tk
menu_inicial.title('Primeiro App') # nome que vai na janela da aplicação

menu_inicial.geometry('500x250+200+200') # ('tamanho x tamanho+ posição + posição')
#menu_inicial.resizable(False, False) # ou (1, 0) não permite redimensionar a tela
#menu_inicial.minsize(500, 250) # tamanho minimo 
#menu_inicial.maxsize(700, 400) # tamanho maximo
menu_inicial.state('zoomed') # inicia com a tela cheia
#menu_inicial.state('iconic') # inicia minimizado 
menu_inicial.iconbitmap('C://Users/Marcus Martins/Documents/Estudos/python publico/python/tkinter/images/icone.ico')

menu_inicial.mainloop() # deixa o programa rodando em loop   