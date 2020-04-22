from graph import *
from math import sin, cos, pi
window = mainWindow()
window.geometry('600x600+350+70')
canvasSize(600, 600)


def ellipse(x1, y1, x2, y2, vertex_count = 36):
    """
    This function draw an ellipse.
    It is necessary because the 'graph' module does not have the function to draw an ellipse.
    """
    (x1, x2) = (min(x1, x2), max(x1, x2))
    (y1, y2) = (min(y1, y2), max(y1, y2))
    a = (x2 - x1) / 2
    b = (y2 - y1) / 2
    VERTEX = [(a * cos(i * 2 * pi / vertex_count) + (x1 + x2) / 2,\
                b * sin(i * 2 * pi / vertex_count) + (y1 + y2) / 2)\
                    for i in range(vertex_count)]
    mypol = polygon(VERTEX)
    return mypol


def fish(x0, y0):
    # Draw a fish:
    # a torso
    brushColor(193, 204, 202)
    polygon([(x0 + 30, y0 + 34),
             (x0 + 40, y0 + 24),
             (x0 + 50, y0 + 17),
             (x0 + 60, y0 + 13),
             (x0 + 70, y0 + 10),
             (x0 + 80, y0 + 10),
             (x0 + 90, y0 + 11),
             (x0 + 100, y0 + 13),
             (x0 + 110, y0 + 16),
             (x0 + 100, y0 + 25),
             (x0 + 90, y0 + 31),
             (x0 + 80, y0 + 34),
             (x0 + 70, y0 + 36),
             (x0 + 60, y0 + 37),
             (x0 + 50, y0 + 37),
             (x0 + 40, y0 + 36),
             (x0 + 30, y0 + 34)])

    # a tail
    polygon([(x0+10, y0 + 59),
             (x0 + 0, y0 + 39),
             (x0 + 10, y0 + 39),
             (x0 + 20, y0 + 38),
             (x0 + 30, y0 + 34)])

    # a fins
    brushColor(222, 167, 167)
    polygon([(x0 + 60, y0 + 13),
             (x0 + 55, y0 + 10),
             (x0 + 50, y0 + 7),
             (x0 + 40, y0 + 4),
             (x0 + 80, y0 + 0),
             (x0 + 83, y0 + 5),
             (x0 + 80, y0 + 10),
             (x0 + 70, y0 + 10)])

    polygon([(x0 + 89, y0 + 32),
             (x0 + 94, y0 + 36),
             (x0 + 99, y0 + 36),
             (x0 + 87, y0 + 44),
             (x0 + 84, y0 + 42),
             (x0 + 82, y0 + 39),
             (x0 + 80, y0 + 34)])

    polygon([(x0 + 50, y0 + 37),
             (x0 + 49, y0 + 40),
             (x0 + 46, y0 + 45),
             (x0 + 42, y0 + 47),
             (x0 + 59, y0 + 47),
             (x0 + 61, y0 + 43),
             (x0 + 59, y0 + 37)])

    # an eye
    brushColor(121, 121, 243)
    circle(x0 + 92, y0 + 20, 5)
    brushColor(127, 133, 141)
    circle(x0 + 93, y0 + 21, 2)
    penColor(219, 219, 36)
    penSize(2)
    line(x0 + 89, y0 + 19, x0 + 91, y0 + 21)
    penColor('black')
    penSize(1)


def bear_fishing(x0, y0):
    # Draw a bear fishing:
    # Draw a hole
    penColor('black')
    brushColor(76, 76, 76)
    ellipse(x0 + 244, y0 + 265, x0 + 399, y0 + 315, vertex_count=36)
    brushColor(15, 79, 66)
    ellipse(x0 + 259, y0 + 280, x0 + 384, y0 + 315, vertex_count=36)

    # Draw a fishing rod
    penColor('black')
    penSize(2)
    line(x0 + 144, y0 + 217, x0 + 155, y0 + 171)
    line(x0 + 155, y0 + 171, x0 + 334, y0 + 0)
    penSize(1)
    line(x0 + 334, y0 + 0, x0 + 334, y0 + 300)

    # Draw a bear:
    # a head
    penColor('black')
    brushColor(231, 231, 231)
    ellipse(x0 + 69, y0 + 71, x0 + 161, y0 + 118, vertex_count=36)
    circle(x0 + 82, y0 + 81, 8)
    brushColor('black')
    circle(x0 + 109, y0 + 85, 2.6)
    circle(x0 + 161, y0 + 91, 2.6)
    line(x0 + 104, y0 + 106, x0 + 134, y0 + 106)
    line(x0 + 134, y0 + 106, x0 + 157, y0+ 104)

    # a torso
    brushColor(231, 231, 231)
    ellipse(x0 + 0, y0 + 105, x0 + 140, y0 + 355, vertex_count=36)
    ellipse(x0 + 74, y0 + 285, x0 + 179, y0 + 365, vertex_count=36)
    ellipse(x0 + 139, y0 + 345, x0 + 219, y0 + 373, vertex_count=36)
    ellipse(x0 + 116, y0 + 159, x0 + 173, y0 + 185, vertex_count=36)


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
ellipse(196, - 33, 489, 243, vertex_count = 36)

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
ellipse(332, 226, 347, 241, vertex_count = 36)
ellipse(197, 98, 216, 114, vertex_count = 36)
ellipse(467, 102, 487, 117, vertex_count = 36)
ellipse(328, 91, 364, 121, vertex_count = 36)

# Draw two fishing bears
bear_fishing(91, 165)
bear_fishing(201, 165)

# Draw two fish
fish(350, 506)
fish(300, 406)


run()