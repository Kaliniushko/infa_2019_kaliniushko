from graph import *
from math import sin, cos, pi

window = mainWindow()
window.geometry('600x600+350+70')
canvasSize(510, 600)


def ellipse(x1, y1, x2, y2, vertex_count=36):
    """
    This function draw an ellipse.
    It is necessary because the 'graph' module does not have the function to draw an ellipse.
    """
    (x1, x2) = (min(x1, x2), max(x1, x2))
    (y1, y2) = (min(y1, y2), max(y1, y2))
    a = (x2 - x1) / 2
    b = (y2 - y1) / 2
    VERTEX = [(a * cos(i * 2 * pi / vertex_count) + (x1 + x2) / 2, \
               b * sin(i * 2 * pi / vertex_count) + (y1 + y2) / 2) \
              for i in range(vertex_count)]
    mypol = polygon(VERTEX)
    return mypol


def bear_fishing(x0, y0, size=1, mirror_xcoord=False, mirror_ycoord=False):
    """
    This function draw a bear fishing: a hole, a fishing rod, and a bear, which consist of primitives.
    Parameters x0, y0 - it's the starting point of each primitive.
    Parameter size - it's the coefficient for increasing each primitive in the x, y direction.
    Parameters mirror_xcoord, mirror_ycoord - mirror the primitives along the x-axis and/or y-axis.
    """
    xcoord = 1
    ycoord = 1
    if mirror_xcoord:
        xcoord *= -1
    if mirror_ycoord:
        ycoord *= -1
    # Draw a hole
    penColor('black')
    brushColor(76, 76, 76)
    ellipse(x0 + 244 * xcoord * size, y0 + 265 * ycoord * size, x0 + 399 * xcoord * size, y0 + 315 * ycoord * size, vertex_count=36)
    brushColor(15, 79, 66)
    ellipse(x0 + 259 * xcoord * size, y0 + 280 * ycoord * size, x0 + 384 * xcoord * size, y0 + 315 * ycoord * size, vertex_count=36)

    # Draw a fishing rod
    penColor('black')
    penSize(2)
    line(x0 + 144 * xcoord * size, y0 + 217 * ycoord * size, x0 + 155 * xcoord * size, y0 + 171 * ycoord * size)
    line(x0 + 155 * xcoord * size, y0 + 171 * ycoord * size, x0 + 334 * xcoord * size, y0 + 0 * ycoord * size)
    penSize(1)
    line(x0 + 334 * xcoord * size, y0 + 0 * ycoord * size, x0 + 334 * xcoord * size, y0 + 300 * ycoord * size)

    # Draw a bear:
    # a head
    penColor('black')
    brushColor(231, 231, 231)
    ellipse(x0 + 69 * xcoord * size, y0 + 71 * ycoord * size, x0 + 161 * xcoord * size, y0 + 118 * ycoord * size, vertex_count=36)
    circle(x0 + 82 * xcoord * size, y0 + 81 * ycoord * size, 8 * size)
    brushColor('black')
    circle(x0 + 109 * xcoord * size, y0 + 85 * ycoord * size, 2.6 * size)
    circle(x0 + 161 * xcoord * size, y0 + 91 * ycoord * size, 2.6 * size)
    line(x0 + 104 * xcoord * size, y0 + 106 * ycoord * size, x0 + 134 * xcoord * size, y0 + 106 * ycoord * size)
    line(x0 + 134 * xcoord * size, y0 + 106 * ycoord * size, x0 + 157 * xcoord * size, y0 + 104 * ycoord * size)

    # a torso
    brushColor(231, 231, 231)
    ellipse(x0 + 0 * xcoord * size, y0 + 105 * ycoord * size, x0 + 140 * xcoord * size, y0 + 355 * ycoord * size, vertex_count=36)
    ellipse(x0 + 74 * xcoord * size, y0 + 285 * ycoord * size, x0 + 179 * xcoord * size, y0 + 365 * ycoord * size, vertex_count=36)
    ellipse(x0 + 139 * xcoord * size, y0 + 345 * ycoord * size, x0 + 219 * xcoord * size, y0 + 373 * ycoord * size, vertex_count=36)
    ellipse(x0 + 116 * xcoord * size, y0 + 159 * ycoord * size, x0 + 173 * xcoord * size, y0 + 185 * ycoord * size, vertex_count=36)


def fish(x0, y0, size=1, mirror_xcoord=False, mirror_ycoord=False):
    """
    This function draw a fish: a torso, a a tail, a fins and an eye, which consist of primitives.
    Parameters x0, y0 - it's the starting point of each primitive.
    Parameter size - it's the coefficient for increasing each primitive in the x, y direction.
    Parameters mirror_xcoord, mirror_ycoord - mirror the primitives along the x-axis and/or y-axis.
    """
    xcoord = 1
    ycoord = 1
    if mirror_xcoord:
        xcoord *= -1
    if mirror_ycoord:
        ycoord *= -1
    # a torso
    brushColor(193, 204, 202)
    torso = polygon([(x0 + 30 * xcoord * size, y0 + 34 * ycoord * size),
             (x0 + 40 * xcoord * size, y0 + 24 * ycoord * size),
             (x0 + 50 * xcoord * size, y0 + 17 * ycoord * size),
             (x0 + 60 * xcoord * size, y0 + 13 * ycoord * size),
             (x0 + 70 * xcoord * size, y0 + 10 * ycoord * size),
             (x0 + 80 * xcoord * size, y0 + 10 * ycoord * size),
             (x0 + 90 * xcoord * size, y0 + 11 * ycoord * size),
             (x0 + 100 * xcoord * size, y0 + 13 * ycoord * size),
             (x0 + 110 * xcoord * size, y0 + 16 * ycoord * size),
             (x0 + 100 * xcoord * size, y0 + 25 * ycoord * size),
             (x0 + 90 * xcoord * size, y0 + 31 * ycoord * size),
             (x0 + 80 * xcoord * size, y0 + 34 * ycoord * size),
             (x0 + 70 * xcoord * size, y0 + 36 * ycoord * size),
             (x0 + 60 * xcoord * size, y0 + 37 * ycoord * size),
             (x0 + 50 * xcoord * size, y0 + 37 * ycoord * size),
             (x0 + 40 * xcoord * size, y0 + 36 * ycoord * size),
             (x0 + 30 * xcoord * size, y0 + 34 * ycoord * size)])

    # a tail
    tail = polygon([(x0 + 10 * xcoord * size, y0 + 59 * ycoord * size),
             (x0 + 0 * xcoord * size, y0 + 39 * ycoord * size),
             (x0 + 10 * xcoord * size, y0 + 39 * ycoord * size),
             (x0 + 20 * xcoord * size, y0 + 38 * ycoord * size),
             (x0 + 30 * xcoord * size, y0 + 34 * ycoord * size)])

    # a fins
    brushColor(222, 167, 167)
    fin1 = polygon([(x0 + 60 * xcoord * size, y0 + 13 * ycoord * size),
             (x0 + 55 * xcoord * size, y0 + 10 * ycoord * size),
             (x0 + 50 * xcoord * size, y0 + 7 * ycoord * size),
             (x0 + 40 * xcoord * size, y0 + 4 * ycoord * size),
             (x0 + 80 * xcoord * size, y0 + 0 * ycoord * size),
             (x0 + 83 * xcoord * size, y0 + 5 * ycoord * size),
             (x0 + 80 * xcoord * size, y0 + 10 * ycoord * size),
             (x0 + 70 * xcoord * size, y0 + 10 * ycoord * size)])

    fin2 = polygon([(x0 + 89 * xcoord * size, y0 + 32 * ycoord * size),
             (x0 + 94 * xcoord * size, y0 + 36 * ycoord * size),
             (x0 + 99 * xcoord * size, y0 + 36 * ycoord * size),
             (x0 + 87 * xcoord * size, y0 + 44 * ycoord * size),
             (x0 + 84 * xcoord * size, y0 + 42 * ycoord * size),
             (x0 + 82 * xcoord * size, y0 + 39 * ycoord * size),
             (x0 + 80 * xcoord * size, y0 + 34 * ycoord * size)])

    fin3 = polygon([(x0 + 50 * xcoord * size, y0 + 37 * ycoord * size),
             (x0 + 49 * xcoord * size, y0 + 40 * ycoord * size),
             (x0 + 46 * xcoord * size, y0 + 45 * ycoord * size),
             (x0 + 42 * xcoord * size, y0 + 47 * ycoord * size),
             (x0 + 59 * xcoord * size, y0 + 47 * ycoord * size),
             (x0 + 61 * xcoord * size, y0 + 43 * ycoord * size),
             (x0 + 59 * xcoord * size, y0 + 37 * ycoord * size)])

    # an eye
    brushColor(121, 121, 243)
    eye = circle(x0 + 92 * xcoord * size, y0 + 20 * ycoord * size, 5 * size)
    brushColor(127, 133, 141)
    eye_apple1 = circle(x0 + 93 * xcoord * size, y0 + 21 * ycoord * size, 2 * size)
    penColor(219, 219, 36)
    brushColor(219, 219, 36)
    eye_apple2 = ellipse(x0 + 89 * xcoord * size, y0 + 19 * ycoord * size, x0 + 91 * xcoord * size, y0 + 21 * ycoord * size, vertex_count=36)
    penColor('black')
    penSize(1)

    # return a list of the fishes parts(primitives)
    parts_of_the_fish = [torso, tail, fin1, fin2, fin3, eye, eye_apple1, eye_apple2]
    return parts_of_the_fish


# Draw a background
penColor('cyan')
brushColor('cyan')
rectangle(90, 0, 510, 600)
penColor(231, 231, 231)
brushColor(231, 231, 231)
rectangle(90, 340, 510, 600)
penColor('black')
line(90, 340, 510, 340)

# Draw a sun
penColor(161, 249, 228)
brushColor(161, 249, 228)
ellipse(196, - 33, 489, 243, vertex_count=36)

penColor('cyan')
brushColor('cyan')
circle(343, 103, 118)

penColor(161, 249, 228)
brushColor(161, 249, 228)
polygon([(334, - 30), (354, - 30), (347, 243), (328, 242)])
polygon([(194, 95), (490, 100), (490, 120), (194, 115)])

brushColor(221, 247, 219)
polygon([(328, 242), (328, 220), (349, 220), (349, 243)])
polygon([(196, 95), (226, 95), (226, 117), (196, 117)])
polygon([(461, 99), (489, 99), (489, 120), (460, 120)])
polygon([(330, 97), (352, 97), (352, 119), (330, 119)])

penColor(255, 246, 214)
brushColor(255, 246, 214)
ellipse(332, 226, 347, 241, vertex_count=36)
ellipse(197, 98, 216, 114, vertex_count=36)
ellipse(467, 102, 487, 117, vertex_count=36)
ellipse(328, 91, 364, 121, vertex_count=36)

# Draw four fishing bears
bear_fishing(500, 305, 0.22, mirror_xcoord=True)
bear_fishing(330, 310, 0.28, mirror_xcoord=True)
bear_fishing(91, 435, 0.32)
bear_fishing(550, 418, 0.65, mirror_xcoord=True)

# Draw fish
fish_of_the_primitives1 = fish(405, 585, 0.35, mirror_xcoord=True, mirror_ycoord=True)
fish_of_the_primitives2 = fish(285, 585, 0.35, mirror_ycoord=True)
fish_of_the_primitives3 = fish(320, 560, 0.35)

fish_of_the_primitives4 = fish(210, 545, 0.3, mirror_xcoord=True)
fish_of_the_primitives5 = fish(230, 555, 0.3, mirror_xcoord=True)
fish_of_the_primitives6 = fish(155, 560, 0.3)
fish_of_the_primitives7 = fish(185, 540, 0.3)

fish_of_the_primitives8 = fish(235, 515, 0.2, mirror_xcoord=True, mirror_ycoord=True)
fish_of_the_primitives9 = fish(165, 518, 0.2, mirror_ycoord=True)
fish_of_the_primitives10 = fish(188, 505, 0.2)

fish_of_the_primitives11 = fish(250, 405, 0.28, mirror_xcoord=True)
fish_of_the_primitives12 = fish(270, 415, 0.28, mirror_xcoord=True)
fish_of_the_primitives13 = fish(205, 420, 0.28)
fish_of_the_primitives14 = fish(225, 400, 0.28)

fish_of_the_primitives15 = fish(270, 382, 0.15, mirror_xcoord=True, mirror_ycoord=True)
fish_of_the_primitives16 = fish(215, 380, 0.15, mirror_ycoord=True)
fish_of_the_primitives17 = fish(233, 372, 0.15)

fish_of_the_primitives18 = fish(440, 380, 0.23, mirror_xcoord=True)
fish_of_the_primitives19 = fish(460, 390, 0.23, mirror_xcoord=True)
fish_of_the_primitives20 = fish(405, 390, 0.23)
fish_of_the_primitives21 = fish(420, 375, 0.23)

fish_of_the_primitives22 = fish(455, 362, 0.12, mirror_xcoord=True, mirror_ycoord=True)
fish_of_the_primitives23 = fish(410, 362, 0.12, mirror_ycoord=True)
fish_of_the_primitives24 = fish(425, 354, 0.12)


tick = 0


def update1():
    for primitive in fish_of_the_primitives1:
        moveObjectBy(primitive, 0, 10)
    for primitive in fish_of_the_primitives2:
        moveObjectBy(primitive, 0, 10)
    for primitive in fish_of_the_primitives3:
        moveObjectBy(primitive, 0, - 10)
    for primitive in fish_of_the_primitives4:
        moveObjectBy(primitive, 0, 10)
    for primitive in fish_of_the_primitives5:
        moveObjectBy(primitive, 0, - 10)
    for primitive in fish_of_the_primitives6:
        moveObjectBy(primitive, 0, 10)
    for primitive in fish_of_the_primitives7:
        moveObjectBy(primitive, 0, - 10)
    for primitive in fish_of_the_primitives8:
        moveObjectBy(primitive, 0, - 10)
    for primitive in fish_of_the_primitives9:
        moveObjectBy(primitive, 0, - 10)
    for primitive in fish_of_the_primitives10:
        moveObjectBy(primitive, 0, 10)
    for primitive in fish_of_the_primitives11:
        moveObjectBy(primitive, 0, - 10)
    for primitive in fish_of_the_primitives12:
        moveObjectBy(primitive, 0, 10)
    for primitive in fish_of_the_primitives13:
        moveObjectBy(primitive, 0, - 10)
    for primitive in fish_of_the_primitives14:
        moveObjectBy(primitive, 0, 10)
    for primitive in fish_of_the_primitives15:
        moveObjectBy(primitive, 0, 10)
    for primitive in fish_of_the_primitives16:
        moveObjectBy(primitive, 0, 10)
    for primitive in fish_of_the_primitives17:
        moveObjectBy(primitive, 0, - 10)
    for primitive in fish_of_the_primitives18:
        moveObjectBy(primitive, 0, 10)
    for primitive in fish_of_the_primitives19:
        moveObjectBy(primitive, 0, - 10)
    for primitive in fish_of_the_primitives20:
        moveObjectBy(primitive, 0, 10)
    for primitive in fish_of_the_primitives21:
        moveObjectBy(primitive, 0, - 10)
    for primitive in fish_of_the_primitives22:
        moveObjectBy(primitive, 0, - 10)
    for primitive in fish_of_the_primitives23:
        moveObjectBy(primitive, 0, - 10)
    for primitive in fish_of_the_primitives24:
        moveObjectBy(primitive, 0, 10)


def update2():
    for primitive in fish_of_the_primitives1:
        moveObjectBy(primitive, 0, - 10)
    for primitive in fish_of_the_primitives2:
        moveObjectBy(primitive, 0, - 10)
    for primitive in fish_of_the_primitives3:
        moveObjectBy(primitive, 0, 10)
    for primitive in fish_of_the_primitives4:
        moveObjectBy(primitive, 0, - 10)
    for primitive in fish_of_the_primitives5:
        moveObjectBy(primitive, 0, 10)
    for primitive in fish_of_the_primitives6:
        moveObjectBy(primitive, 0, - 10)
    for primitive in fish_of_the_primitives7:
        moveObjectBy(primitive, 0, 10)
    for primitive in fish_of_the_primitives8:
        moveObjectBy(primitive, 0, 10)
    for primitive in fish_of_the_primitives9:
        moveObjectBy(primitive, 0, 10)
    for primitive in fish_of_the_primitives10:
        moveObjectBy(primitive, 0, - 10)
    for primitive in fish_of_the_primitives11:
        moveObjectBy(primitive, 0, 10)
    for primitive in fish_of_the_primitives12:
        moveObjectBy(primitive, 0, - 10)
    for primitive in fish_of_the_primitives13:
        moveObjectBy(primitive, 0, 10)
    for primitive in fish_of_the_primitives14:
        moveObjectBy(primitive, 0, - 10)
    for primitive in fish_of_the_primitives15:
        moveObjectBy(primitive, 0, - 10)
    for primitive in fish_of_the_primitives16:
        moveObjectBy(primitive, 0, - 10)
    for primitive in fish_of_the_primitives17:
        moveObjectBy(primitive, 0, 10)
    for primitive in fish_of_the_primitives18:
        moveObjectBy(primitive, 0, - 10)
    for primitive in fish_of_the_primitives19:
        moveObjectBy(primitive, 0, 10)
    for primitive in fish_of_the_primitives20:
        moveObjectBy(primitive, 0, - 10)
    for primitive in fish_of_the_primitives21:
        moveObjectBy(primitive, 0, 10)
    for primitive in fish_of_the_primitives22:
        moveObjectBy(primitive, 0, 10)
    for primitive in fish_of_the_primitives23:
        moveObjectBy(primitive, 0, 10)
    for primitive in fish_of_the_primitives24:
        moveObjectBy(primitive, 0, - 10)


def update_fishes():
    global tick
    if tick % 2 == 0:
        update1()
    else:
        update2()
    tick += 1


onTimer(update_fishes, 150)

run()
