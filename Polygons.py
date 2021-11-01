from turtle import *

import numpy as np

speed(500)
pencolor('blue')


def polygon(side_len, sides, angle):
    for i in range(sides):
        forward(side_len)
        left(angle)
    if side_len > 0:
        left(2)
        forward(8)
        polygon(side_len - 1, sides, angle)


side_len = 110
sides = 8
angle = 360 / sides

polygon(side_len, sides, angle)
