from tkinter import *
from random import randrange as rnd, choice

root = Tk()
root.geometry('800x600+500+50')

canv = Canvas(root, bg='white')
canv.pack(fill=BOTH, expand=1)

colors = ['red', 'orange', 'yellow', 'green', 'blue']
global_score = 1


def new_ball():
    global x, y, r
    canv.delete(ALL)
    x = rnd(100, 700)
    y = rnd(100, 500)
    r = rnd(30, 50)
    canv.create_oval(x - r, y - r, x + r, y + r, fill=choice(colors), width=0)
    root.after(1000, new_ball)


def new_score(event):
    global global_score
    k = event.x
    z = event.y
    goal = ((k - x) ** 2 + (z - y) ** 2) ** 0.5
    if goal <= r:
        print(global_score)
        global_score += 1


new_ball()
canv.bind('<Button-1>', new_score)

mainloop()
