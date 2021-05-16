# !/usr/bin/env python3
# -*- coding: utf-8 -*-

from tkinter import *

# напишите программу по следующему описанию. Нажатие Enter в
# однострочном текстовом поле приводит к перемещению текста из него в список (экземпляр
# Listbox ). При двойном клике ( <Double-Button-1> ) по элементу-строке списка, она должна
# копироваться в текстовое поле.

class Main_prog:
    def __init__(self, master):
        self.ent_1 = Entry(master)
        self.lst_1 = Listbox(master)

        self.ent_1.bind('<Return>', lambda temp: self.lst_1.insert(0, self.ent_1.get()))
        self.lst_1.bind('<Double-Button-1>', lambda temp: self.ent_1.insert(0, self.lst_1.get(self.lst_1.curselection())))

        self.ent_1.pack(side=LEFT)
        self.lst_1.pack(side=LEFT)


root = Tk()
main_prog = Main_prog(root)
root.mainloop()
