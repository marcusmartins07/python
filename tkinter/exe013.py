from tkinter import *

menu_inicial = Tk()
menu_inicial.geometry('500x300')
menu_inicial.title('Exercicio 11')

label_a = Label(menu_inicial, 
                text='0123456789',
                font='Arial 20',
                bd=1,
                relief='solid',
                width=25,
                height=2,
                anchor=N
).pack()

label_a = Label(menu_inicial, 
                text='0123456789',
                font='Arial 20',
                bd=1,
                relief='solid',
                width=25,
                height=2,
                anchor=E
).pack()

label_a = Label(menu_inicial, 
                text='0123456789',
                font='Arial 20',
                bd=1,
                relief='solid',
                width=25,
                height=2,
                anchor=S
).pack()

label_a = Label(menu_inicial, 
                text='0123456789',
                font='Arial 20',
                bd=1,
                relief='solid',
                width=25,
                height=2,
                anchor=W
).pack()

menu_inicial = mainloop()