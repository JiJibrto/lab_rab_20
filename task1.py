# !/usr/bin/env python3
# -*- coding: utf-8 -*-

from tkinter import *

# напишите программу, состоящую из двух списков Listbox . В первом будет,
# например, перечень товаров, заданный программно. Второй изначально пуст, пусть это
# будет перечень покупок. При клике на одну кнопку товар должен переходить из одного
# списка в другой. При клике на вторую кнопку – возвращаться (человек передумал покупать).
# Предусмотрите возможность множественного выбора элементов списка и их перемещения.


class Main_prog():
    def __init__(self, master):
        self.btn_1 = Button(text=">>", width=10)
        self.btn_2 = Button(text="<<", width=10)
        self.lst_1 = Listbox()
        self.lst_2 = Listbox()

        self.btn_1.bind('<Button-1>', self.lst_1_move)
        self.btn_2.bind('<Button-1>', self.lst_2_move)

        self.lst_1.grid(row=0, column=0, rowspan=4)
        self.lst_2.grid(row=0, column=2, rowspan=4)
        self.btn_1.grid(row=1, column=1, sticky=S)
        self.btn_2.grid(row=2, column=1, sticky=N)

        for i in ['ammo', 'shotgun', 'shield', 'sword', 'frog', 'tank', 'lasergun']:
            self.lst_1.insert(END, i)

    def lst_1_move(self, event):
        temp = list(self.lst_1.curselection())
        temp.reverse()
        for i in temp:
            self.lst_2.insert(0, self.lst_1.get(i))
            print(i)
            self.lst_1.delete(i)

    def lst_2_move(self, event):
        temp = list(self.lst_2.curselection())
        temp.reverse()
        for i in temp:
            self.lst_1.insert(0, self.lst_2.get(i))
            self.lst_2.delete(i)

root = Tk()
main_prog = Main_prog(root)
root.mainloop()
