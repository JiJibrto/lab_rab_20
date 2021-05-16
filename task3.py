# !/usr/bin/env python3
# -*- coding: utf-8 -*-

from tkinter import *

# Размеры многострочного текстового
# поля определяются значениями, введенными в однострочные текстовые поля. Изменение
# размера происходит при нажатии мышью на кнопку, а также при нажатии клавиши Enter.
# Цвет фона экземпляра Text светлосерый ( lightgrey ), когда поле не в фокусе, и белый,
# когда имеет фокус.

class Main_prog:
    def __init__(self, master):
        self.header = LabelFrame(master, text="Menu")
        self.ent_1 = Entry(self.header)
        self.ent_2 = Entry(self.header)
        self.btn_1 = Button(self.header, text="Изменить", width=10)
        self.txt_1 = Text(width=25, height=25, bg='lightgrey')

        self.btn_1.bind('<Button-1>', self.btn_clck_ev)
        self.ent_1.bind('<Return>', self.btn_clck_ev)
        self.ent_2.bind('<Return>', self.btn_clck_ev)
        self.btn_1.bind('<Return>', self.btn_clck_ev)
        self.txt_1.bind('<Return>', self.btn_clck_ev)
        self.txt_1.bind('<FocusIn>', lambda temp, clr="white": self.clr_change(temp, clr))
        self.txt_1.bind('<FocusOut>', lambda temp, clr="lightgrey": self.clr_change(temp, clr))

        self.header.pack()
        self.ent_1.pack(side=TOP)
        self.ent_2.pack(side=TOP)
        self.btn_1.pack(side=TOP)
        self.txt_1.pack()

    def btn_clck_ev(self, event):
        self.txt_1['width'] = self.ent_1.get()
        self.txt_1['height'] = self.ent_2.get()

    def clr_change(self, event, clr):
        self.txt_1['bg'] = clr

root = Tk()
main_prog = Main_prog(root)
root.mainloop()
