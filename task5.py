# !/usr/bin/env python3
# -*- coding: utf-8 -*-

from tkinter import *
import math

# Изучите приведенную программу и самостоятельно запрограммируйте постепенное
# движение фигуры в ту точку холста, где пользователь кликает левой кнопкой мыши.
# Координаты события хранятся в его атрибутах x и y ( event.x , event.y ).

class Main_prog:
    def __init__(self, master, width=600, height=600):
        self.vect_x = 1
        self.vect_y = 1
        self.path = 0
        self.center_x = 0
        self.center_y = 0
        self.move_x = 0
        self.move_y = 0
        self.clck_x = 0
        self.clck_y = 0
        self.height = height
        self.width = width
        self.main_canv = Canvas(master, width=self.width, height=self.height, bg='black')
        self.rad = 10
        self.ball = self.main_canv.create_oval(self.width // 2 - self.rad + 100, self.height // 2 - self.rad + 100,
                                                self.width // 2 + self.rad + 100, self.height // 2 + self.rad + 100,
                                               fill='white')
        self.line =self.main_canv.create_line(self.width // 2, self.height / 2 - 200,
                                              self.width // 2, self.height / 2 + 200, fill='white')
        self.main_canv.pack()
        self.main_canv.bind('<Button-1>', self.clck_move)
        root.after(10, self.move_ball)

    def clck_move(self, event):
        self.ball_coords = self.main_canv.coords(self.ball)
        self.center_x = (self.ball_coords[0] + self.ball_coords[2]) / 2
        self.center_y = (self.ball_coords[1] + self.ball_coords[3]) / 2
        self.clck_x = event.x
        self.clck_y = event.y

        self.vect_x = self.clck_x - self.center_x
        self.vect_y = self.clck_y - self.center_y
        self.path = math.sqrt(self.vect_x ** 2 + self.vect_y ** 2)

        self.move_x = self.vect_x / self.path
        self.move_y = self.vect_y / self.path

    def move_ball(self):
        self.main_canv.move(self.ball, self.move_x * 6, self.move_y * 6)
        self.ball_coords = self.main_canv.coords(self.ball)

        if self.ball_coords[0] < 0 or self.ball_coords[2] > self.width:
            self.move_x = -self.move_x
        if self.ball_coords[1] < 0 or self.ball_coords[3] > self.height:
            self.move_y = -self.move_y
        if self.ball_coords[0] < self.width // 2 and self.height / 2 + 200 > self.ball_coords[1] > self.height / 2 - 200 and self.ball_coords[2] > self.width // 2:
                self.move_x = -self.move_x

        root.after(10, self.move_ball)

root = Tk()
game = Main_prog(root)
root.mainloop()
