from graph import *
windowSize(600, 600)


def color_circle(x, y, z, color):
    brushColor(color)
    circle(x, y, z)


brushColor(220, 220, 220)
rectangle(100, 100, 500, 500)

color_circle(300, 300, 120, 'yellow')

color_circle(240, 270, 25, 'red')
color_circle(360, 270, 20, 'red')
color_circle(240, 270, 11, 'black')
color_circle(360, 270, 10, 'black')

brushColor('black')
rectangle(240, 355, 360, 380)

polygon([(270, 258), (170, 206), (176, 197), (276, 249)])
polygon([(328, 258), (420, 232), (417, 222), (325, 248)])

run()
