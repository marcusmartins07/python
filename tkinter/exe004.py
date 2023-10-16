from tkinter import *

menu_inicial = Tk()

menu_inicial.title('exe004')

menu_inicial['bg'] = 'blue'

# botao
btn = Button(menu_inicial, text='Executar')
btn.pack()

menu_inicial = mainloop()

# Para saber todos os metodos
# terminal
# from tkinter import *
# dir(Tk)