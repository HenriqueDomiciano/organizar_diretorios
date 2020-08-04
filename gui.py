import arquivos
from tkinter import *
from tkinter import filedialog
from typing import Any

root = Tk()


def myclick():
    e = filedialog.askdirectory()
    arquivos.organize_files(e)
    mylabel = Label(root, text='organizado',bg='#4DB22F',fg='white').pack()


root.title("Organizador")
root.iconbitmap(r'book.ico')
root.geometry('543x340')
root.resizable(True,True)
background_image = PhotoImage(file="fundo.png")
background_label = Label(root, image=background_image,anchor='nw')
background_label.place(x=0, y=0, relwidth=1, relheight=1)
my_button = Button(root, text="Me clique para organizar", padx=20, command=myclick,bg='#4DB22F',fg='white').place(x=190,y=150)

root.mainloop()
