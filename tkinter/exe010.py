from tkinter import *

menu_incial=Tk()
menu_incial.title('Label')
menu_incial.geometry('500x300')

label_a = Label(menu_incial, 
                text='Este é o label 1',
                bg='black',
                fg='yellow',
                font='Arial'
                )
label_a.pack()

label_b = Label(menu_incial, 
                text='Este é o label 2',
                font='Times 20 bold'
                )
label_b.pack()

label_c = Label(menu_incial, 
                text='Este é o label 3',
                font='Verdana 42 bold',
                fg='#aaaaaa')
label_c.pack()

menu_incial.mainloop()
    