# !/usr/bin/env python3
# -*- coding: utf-8 -*-

from tkinter import *
import math

# Изучите приведенную программу и самостоятельно запрограммируйте постепенное
# движение фигуры в ту точку холста, где пользователь кликает левой кнопкой мыши.
# Координаты события хранятся в его атрибутах x и y ( event.x , event.y ).

class Game:
    def __init__(self, width=1000, height=1000):
        self.vx = 1
        self.vy = 1
        self.t = 0
        self.dt = 1
        self.i = 0
        self.height = height
        self.width = width
        self.c = Canvas(root, width=self.width, height=self.height, bg="white")
        self.c.pack()
        self.rad = 20
        self.ball = self.c.create_oval(self.width // 2 - self.rad, self.height // 2 - self.rad,
                                       self.width // 2 + self.rad, self.height // 2 + self.rad, fill='green')

        self.c.bind('<Button-1>', self.onclick)
        root.after(10, self.onframe)

    def onclick(self, event):
        self.p = self.c.coords(self.ball)
        self.dx = event.x - self.p[0]
        self.dy = event.y - self.p[1]

        self.r = math.sqrt(self.dx ** 2 + self.dy ** 2)

        self.vx = self.dx / self.r
        self.vy = self.dy / self.r

        self.t += self.dt
        self.p[0] += self.vx + 10
        self.p[1] += self.vy + 10

        if 200 > self.dx >= 100 or 200 > self.dy >= 100 or -200 < self.dx <= -100 or -200 < self.dy <= -100:
            self.dt = 2
        elif 300 > self.dx >= 200 or 300 > self.dy >= 200 or -300 < self.dx <= -200 or -300 < self.dy <= -200:
            self.dt = 4
        elif 500 > self.dx >= 300 or 500 > self.dy >= 300 or -500 < self.dx <= -300 or -500 < self.dy <= -300:
            self.dt = 7
        elif self.dx >= 500 or self.dy >= 500 or self.dx <= -500 or self.dy <= -500:
            self.dt = 10
        else:
            self.dt = 1
        print(self.dx, self.dy, self.dt)

    def onframe(self):
        self.c.move(self.ball, self.dt * self.vx, self.dt * self.vy)
        self.p = self.c.coords(self.ball)

        if self.p[1] < 0 or self.p[1] > self.height - 2 * self.rad:
            self.vy = -self.vy

        if self.p[0] < 0 or self.p[0] > self.width - 2 * self.rad:
            self.vx = -self.vx

        root.after(10, self.onframe)

root = Tk()
root.resizable(False, False)
Game()
root.mainloop()
