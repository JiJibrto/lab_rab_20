# !/usr/bin/env python3
# -*- coding: utf-8 -*-

from tkinter import *

# Создайте на холсте подобное изображение

class Main_image:
    def __init__(self, master):
        self.main_canv = Canvas(master, width=800, height=800, bg='white')

        self.main_canv.pack()

        self.main_canv.create_polygon(400, 100, 100, 300, 700, 300, fill='lightblue', outline='lightblue')
        self.main_canv.create_rectangle(200, 300, 600, 700, fill='lightblue', outline='lightblue')
        self.main_canv.create_oval(650, 50, 750, 150, fill='yellow', outline='yellow')

        self.ind = 0
        while self.ind < 1000:
            self.main_canv.create_arc(self.ind, 675, self.ind+25, 930,
                 start=180, extent=-100,
                 style=ARC, outline='darkgreen',
                 width=3)
            self.ind += 25


root = Tk()
main_image = Main_image(root)
root.mainloop()