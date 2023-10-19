from tkinter import *

#Meu Widget

class FrameNome(Frame):
    def __init__(self, meuMaster):
        super().__init__()
        self['height'] = 150
        self['width'] = 200
        self['bd'] = 2
        self['relief'] = SOLID

        label_nome = Label(self, text='Nome')
        text_nome = Entry(self)
        label_nome.grid(row=0, column=0)
        text_nome.grid(row=0, column=1)

root = Tk()
root.title('Constructor Function')

frame_nome_a = FrameNome(root).grid()
frame_nome_b = FrameNome(root).grid()
frame_nome_c = FrameNome(root).grid()
frame_nome_d  = FrameNome(root).grid()

root.mainloop()