'''
Copyright (c) 2012-2024 Scott Chacon and others

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
'''

from arquivos import Arquivo
from tkinter import *
from tkinter import filedialog
from typing import Any
from tkinter import ttk
import json

class App():
    def __init__(self) -> None:
        self.root = Tk()
        self.entries = 5
        self.root.title("Organizador")
        self.root.geometry("540x320")
        self.root.resizable(True,True)
        background_image = PhotoImage(file="fundo.png")
        background_label = Label(self.root,image=background_image,anchor='nw')
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        my_button = Button(self.root,text="Me clique para organizar", padx=20, command=self.myclick,bg='#4DB22F',fg='white').place(x=190,y=150)
        
        menubar = Menu(self.root)
        filemenu = Menu(menubar)
        filemenu.add_command(label="Open configuration",command=self.open_file_config)
        filemenu.add_command(label="Exit",command=self.root.quit)

        menubar.add_cascade(label="File", menu=filemenu)

        self.root.config(menu=menubar)
        
        self.root.mainloop()
    
    def remove(self):
        try:
            del self.medium_dict[self.entries_list[0].get()]
            self.tview.delete(*self.tview.get_children())
            self.insert_starters()
            self.save_medium_json(quit=False)
        except Exception as e:
            print(e)
            pass
    def add(self):
            
        self.medium_dict[f'{self.entries_list[0].get()}'] = [i.get() for i in self.entries_list[1:] if i.get()!='']

        self.tview.insert('', "end", text=self.entries_list[0].get(), values=tuple([i.get() for i in self.entries_list[1:] if i.get()!='']))


    def open_file_config(self):
        self.get_last_json_config()
        self.new_window = Toplevel(self.root)
        Label(self.new_window,text='Nome da Pasta').grid(row=0)
        for i in range(1,self.entries):
            Label(self.new_window, text=f'Extensão {i}').grid(row=i)
        
        columns = ('Nome da Pasta',*tuple([f'Final do Arquivo {i}' for i in range(self.entries-2)]))
        self.tview = ttk.Treeview(self.new_window, columns=columns)
        self.tview.grid(row=self.entries, column=0, columnspan=10)
        self.tview.heading(f'#0', text="Pasta de entrada")

        for i in range(1,self.entries):
            self.tview.heading(f'#{i}', text=f"Final do arquivo {i}")

        self.insert_starters()

        self.entries_list = []    
        for i in range(self.entries):
            self.entries_list.append(Entry(self.new_window, width="30"))
            self.entries_list[-1].grid(row=i, column=1, pady=10)
        
        
        b1 = Button(self.new_window, text="Add", width="25",command=self.add)
        b1.grid(row=self.entries+1, column=1, pady=10)
        b2 = Button(self.new_window ,text="Delete", width="25",command=self.remove)
        b2.grid(row = self.entries+3, column=1, pady=10)
        b3 = Button(self.new_window,text="save",width=25,command=self.save_medium_json)
        b3.grid(row = self.entries+4,column=1,pady=10)

    def myclick(self):
        e = filedialog.askdirectory()
        self.get_last_json_config()
        table_val = Arquivo(path_to_organize=e,type_table=self.medium_dict).run()
        mylabel = Label(text='organizado',bg='#4DB22F',fg='white').pack()

    def insert_starters(self):
        for key in self.medium_dict.keys():
            self.tview.insert('',"end",text=f'{key}',values=tuple(self.medium_dict[key]))
    def get_last_json_config(self):
        with open('config.json','r',encoding='utf-8') as fr:
            self.medium_dict =  json.load(fr)
            print(self.medium_dict)
    def save_medium_json(self,quit  = True):
        with open('config.json','w',encoding='utf-8')as f:
            json.dump(self.medium_dict,f)
            if quit:
                self.new_window.destroy()

if __name__=='__main__':
    app = App()
