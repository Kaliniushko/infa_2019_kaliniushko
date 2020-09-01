from tkinter import *
from random import randint, choice


class Ball:
    def __init__(self):
        self.R = randint(30, 60)
        self.x = randint(self.R, WIDTH - self.R)
        self.y = randint((self.R + 50), HEIGHT - self.R)
        self.colors = ['red', 'orange', 'yellow', 'green', 'blue']
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


def ball_move():
    ball1.move()
    ball1.show()
    ball2.move()
    ball2.show()
    root.after(20, ball_move)


def new_score(event):
    global global_score, ball1, ball2
    goal = ((event.x - ball1.x) ** 2 + (event.y - ball1.y) ** 2) ** 0.5
    if goal <= ball1.R:
        score_label['text'] = 'Total score: ' + str(global_score)
        global_score += 1
        canv.delete(ball1.ball_id)
        ball1 = Ball()
    goal = ((event.x - ball2.x) ** 2 + (event.y - ball2.y) ** 2) ** 0.5
    if goal <= ball2.R:
        score_label['text'] = 'Total score: ' + str(global_score)
        global_score += 1
        canv.delete(ball2.ball_id)
        ball2 = Ball()


def main():
    global root, canv, WIDTH, HEIGHT, score_label, global_score, ball1, ball2
    root = Tk()
    WIDTH = 800
    HEIGHT = 600
    global_score = 1
    root.geometry(str(WIDTH) + 'x' + str(HEIGHT) + '+500+50')
    root.title('Catch the ball')

    canv = Canvas(root, bg='white')
    canv.pack(fill=BOTH, expand=1)
    score_label = Label(canv, text='Total score: 0', font='Arial 20', bg='blue', fg='white', width=90, bd=5)
    score_label.pack()

    ball1 = Ball()
    ball2 = Ball()

    ball_move()

    canv.bind('<Button-1>', new_score)
    root.mainloop()


if __name__ == '__main__':
    main()
