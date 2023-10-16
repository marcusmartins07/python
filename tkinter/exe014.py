from tkinter import *

menu_inicial = Tk()
menu_inicial.title('Exercício 14')
menu_inicial.geometry("500x500")

label_a = Label(menu_inicial, 
                text='frase de teste\nmais teste',
                font='Arial 20',
                bd=1,
                relief='solid',
                width=30,
                height=5,
                justify=LEFT,
                anchor=W
).pack()

label_a = Label(menu_inicial, 
                text='frase de teste\nmais teste\nteste',
                font='Arial 10',
                bd=1,
                relief='solid',
                padx=50,
                pady=20,
                justify=RIGHT
).pack()

menu_inicial = mainloop()