from tkinter import *
from random import randint, choice


class Ball:
    def __init__(self):
        self.R = randint(35, 45)
        self.x = randint(self.R, WIDTH - self.R)
        self.y = randint((self.R + 50), HEIGHT - self.R)
        self.colors = ['red', 'orange', 'darkcyan', 'green', 'blue', 'indigo', 'darkmagenta']
        self.dx, self.dy = +4, +5
        self.ball_id = canv.create_oval(self.x - self.R, self.y - self.R,
                                        self.x + self.R, self.y + self.R,
                                        fill=choice(self.colors), width=0)

    def move(self):
        self.x += self.dx
        self.y += self.dy
        if self.x + self.R > WIDTH or self.x - self.R <= 0:
            self.dx = -self.dx
        if self.y + self.R > HEIGHT or (self.y - self.R - 50) <= 0:
            self.dy = -self.dy

    def show(self):
        canv.move(self.ball_id, self.dx, self.dy)


class Rhombus:
    def __init__(self):
        self.R = randint(20, 30)
        self.x = randint(self.R, WIDTH - self.R)
        self.y = randint((self.R + 50), HEIGHT - self.R)
        self.dx, self.dy = +4, +5
        self.romb_id = canv.create_polygon(self.x, self.y - self.R, self.x + self.R, self.y,
                                           self.x, self.y + self.R, self.x - self.R, self.y,
                                           fill='yellow', width=0)

    def move(self):
        self.x += self.dx
        self.y += self.dy
        if self.x + self.R > WIDTH or self.x - self.R <= 0:
            self.dx = -self.dx
        if self.y + self.R > HEIGHT or (self.y - self.R - 50) <= 0:
            self.dy = -self.dy

    def show(self):
        canv.move(self.romb_id, self.dx, self.dy)


def ball_move():
    ball1.move()
    ball1.show()
    ball2.move()
    ball2.show()
    root.after(20, ball_move)


def romb_move():
    romb1.move()
    romb1.show()
    root.after(20, romb_move)


def inRhombus(x, y, xp, yp):
    c = 0
    for i in range(len(xp)):
        if (((yp[i] <= y and y < yp[i - 1]) or (yp[i - 1] <= y and y < yp[i])) and \
                (x > (xp[i - 1] - xp[i]) * (y - yp[i]) / (yp[i - 1] - yp[i]) + xp[i])): c = 1 - c
    return c


def new_score(event):
    global global_score, ball1, ball2, romb1
    goal = ((event.x - ball1.x) ** 2 + (event.y - ball1.y) ** 2) ** 0.5
    if goal <= ball1.R:
        score_label['text'] = 'Total score: ' + str(global_score + 1)
        global_score += 1
        canv.delete(ball1.ball_id)
        ball1 = Ball()
    goal = ((event.x - ball2.x) ** 2 + (event.y - ball2.y) ** 2) ** 0.5
    if goal <= ball2.R:
        score_label['text'] = 'Total score: ' + str(global_score + 1)
        global_score += 1
        canv.delete(ball2.ball_id)
        ball2 = Ball()
    ok = inRhombus(event.x, event.y, (romb1.x, romb1.x + romb1.R, romb1.x, romb1.x - romb1.R),
                   (romb1.y - romb1.R, romb1.y, romb1.y + romb1.R, romb1.y))
    if ok == 1:
        score_label['text'] = 'Total score: ' + str(global_score + 2)
        global_score += 2
        canv.delete(romb1.romb_id)
        romb1 = Rhombus()


def main():
    global root, canv, WIDTH, HEIGHT, score_label, global_score, ball1, ball2, romb1
    root = Tk()
    WIDTH = 800
    HEIGHT = 600
    global_score = 0
    root.geometry(str(WIDTH) + 'x' + str(HEIGHT) + '+500+50')
    root.title('Catch the ball')

    canv = Canvas(root, bg='white')
    canv.pack(fill=BOTH, expand=1)
    score_label = Label(canv, text='Total score: 0', font='Arial 20', bg='darkslategrey', fg='white', width=90, bd=5)
    score_label.pack()

    ball1 = Ball()
    ball2 = Ball()
    ball_move()

    romb1 = Rhombus()
    romb_move()

    canv.bind('<Button-1>', new_score)
    root.mainloop()


if __name__ == '__main__':
    main()
