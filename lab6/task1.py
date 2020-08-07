from tkinter import *
from random import randrange as rnd, choice

root = Tk()
root.geometry('800x600+500+50')
root.title('Catch the ball')

canv = Canvas(root, bg='white')
canv.pack(fill=BOTH, expand=1)
score_label = Label(canv, text='Total score: 0', font='Arial 20', bg='blue', fg='white', width=90)
score_label.pack()

colors = ['red', 'orange', 'yellow', 'green', 'blue']
x, y, r, i = 0, 0, 0, 0
global_score = 1
ball_id = None


def new_ball():
    global x, y, r, i
    canv.delete(ALL)
    x = rnd(100, 700)
    y = rnd(100, 500)
    r = rnd(30, 50)
    new_ball_id = canv.create_oval(x - r, y - r, x + r, y + r, fill=choice(colors), width=0)
    i = 0
    return new_ball_id


def ball_move():
    global x, y, r, i, ball_id
    if ball_id == None:
        ball_id = new_ball()
    if i >= 10:
        ball_id = new_ball()
    canv.move(ball_id, 10, 0)
    x += 10
    i += 1
    root.after(100, ball_move)


def new_score(event):
    global global_score, x, y
    k = event.x
    z = event.y
    goal = ((k - x) ** 2 + (z - y) ** 2) ** 0.5
    if goal <= r:
        score_label['text'] = 'Total score: ' + str(global_score)
        global_score += 1


canv.bind('<Button-1>', new_score)
ball_move()

mainloop()
