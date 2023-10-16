from tkinter import *

menu_inicial = Tk()
menu_inicial.title('Exercício 15')
menu_inicial.geometry("500x500")

label_a = Label(menu_inicial, 
                text='frase de teste',
                font='Arial 20',
                bd=1,
                relief='solid',
).pack()   

label_b = Label(menu_inicial)
label_b['text'] = 'texto da label'
label_b['font'] = 'Arial 20'
label_b['bd'] = 1
label_b['relief'] = 'solid'
label_b.pack()  

label_b['text'] = 'novo texto'
for item in label_b.keys():#tudo que pode ser alterado
    print(item, " : ", label_b[item])

menu_inicial = mainloop()