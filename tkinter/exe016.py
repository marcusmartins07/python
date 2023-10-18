from tkinter import *

menu_inicial = Tk()
menu_inicial.title('Exercício 16')
menu_inicial.geometry("500x500")

texto = StringVar()
texto.set('Novo Texto')

label_a = Label(menu_inicial, 
                font='Arial 20',
                bg='red',
                fg='white',
                textvariable=texto
)

label_b = Label(menu_inicial, 
                font='Arial 20',
                bg='red',
                fg='white',
                textvariable=texto
)

label_c = Label(menu_inicial, 
                font='Arial 20',
                bg='red',
                fg='white',
                textvariable=texto
)

label_d = Label(menu_inicial, 
                font='Arial 20',
                bg='red',
                fg='white',
                textvariable=texto
)

label_a.pack()   
label_b.pack()
label_c.pack()
label_d.pack()

texto.set('Defino todos os textos')

menu_inicial = mainloop()