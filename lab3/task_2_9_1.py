from graph import *
from math import sin, cos, pi
window = mainWindow()
window.geometry('600x600+350+70')
canvasSize(600, 600)


def ellipse(x1, y1, x2, y2, vertex_count = 36):
    (x1, x2) = (min(x1, x2), max(x1, x2))
    (y1, y2) = (min(y1, y2), max(y1, y2))
    a = (x2 - x1) / 2
    b = (y2 - y1) / 2
    VERTEX = [(a * cos(i * 2 * pi / vertex_count) + (x1 + x2) / 2,\
                b * sin(i * 2 * pi / vertex_count) + (y1 + y2) / 2)\
                    for i in range(vertex_count)]
    mypol = polygon(VERTEX)
    return mypol


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

# Draw a hole
penColor('black')
brushColor(76, 76, 76)
ellipse(335, 430, 490, 480, vertex_count = 36)
brushColor(15, 79, 66)
ellipse(350, 445, 475, 480, vertex_count = 36)

# Draw a fishing rod
penColor('black')
penSize(2)
line(235, 382, 246, 336)
line(246, 336, 425, 165)
penSize(1)
line(425, 165, 425, 465)

# Draw a bear:
# a head
penColor('black')
brushColor(231, 231, 231)
ellipse(160, 236, 252, 283, vertex_count = 36)
circle(173, 246, 8)
brushColor('black')
circle(200, 250, 2.6)
circle(252, 256, 2.6)
line(195, 271, 225, 271)
line(225, 271, 248, 269)

# a torso
brushColor(231, 231, 231)
ellipse(91, 270, 231, 520, vertex_count = 36)
ellipse(165, 450, 270, 530, vertex_count = 36)
ellipse(230, 510, 310, 538, vertex_count = 36)
ellipse(207, 324, 264, 350, vertex_count = 36)

# Draw a fish:
# a torso
brushColor(193, 204, 202)
polygon([(380, 540),
         (390, 530),
         (400, 523),
         (410, 519),
         (420, 516),
         (430, 516),
         (440, 517),
         (450, 519),
         (460, 522),
         (450, 531),
         (440, 537),
         (430, 540),
         (420, 542),
         (410, 543),
         (400, 543),
         (390, 542),
         (380, 540)])

# a tail
polygon([(360, 565),
         (350, 545),
         (360, 545),
         (370, 544),
         (380, 540)])

# a fins
brushColor(222, 167, 167)
polygon([(410, 519),
         (405, 516),
         (400, 513),
         (390, 510),
         (430, 506),
         (433, 511),
         (430, 516),
         (420, 516)])

polygon([(439, 538),
         (444, 542),
         (449, 542),
         (437, 550),
         (434, 548),
         (432, 545),
         (430, 540)])

polygon([(400, 543),
         (399, 546),
         (396, 551),
         (392, 553),
         (409, 553),
         (411, 549),
         (409, 543)])

# an eye
brushColor(121, 121, 243)
circle(442, 526, 5)
brushColor(127, 133, 141)
circle(443, 527, 2)
penColor(219, 219, 36)
penSize(2)
line(439, 525, 441, 527)

run()