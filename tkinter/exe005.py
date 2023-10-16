from tkinter import *

menu_inicial = Tk()
menu_inicial.title('Exercio 05')
menu_inicial.geometry('500x300')

# botao


def btnClick():
    print('Ola, mundo!')

def btnMensagem(mensagem):
    print(mensagem)


btn = Button(menu_inicial, text='Executar', command=btnClick)
btn.pack()

btn = Button(menu_inicial, text='Mensagem', command=lambda: btnMensagem('Nova mensagem'))
btn.pack()

btn = Button(menu_inicial, text='Sem função', command=lambda: print('Também Funciona'))
btn.pack()


menu_inicial.mainloop()
