#CSCI1133
import turtle
from stretch1 import identity
from WP1 import matrix



def showMatrix(turtle_object, m):
    screen = turtle.getscreen()
    screen.setworldcoordinates()
    screen.tracer(0)

    for i in range(len(m)):
        if m[i][i] == 1:
            screen.dot()
        else:

    screen.update()


def main():
        x = identity(100)
