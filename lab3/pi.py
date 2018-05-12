#CSCI1133 LAB3
#GUANGYU YAN

import random
import turtle
import math

def spot(x,y):
    turtle.penup()
    turtle.goto(x,y)
    turtle.dot(5)
    turtle.pendown()

def main():
    darts = 0
    times = 1000
    while times > 0:
        x = random.uniform(-1,1)
        y = random.uniform(-1,1)
        x = 150*x
        y = 150*y
        if x**2 + y**2 <= 22500:
            turtle.color("green")
            spot(x,y)
            darts += 1
        else:
            turtle.color("red")
            spot(x,y)
        times -= 1
    pi = 4 * darts / 1000
    turtle.write(pi)
if __name__ == "__main__":
    main()
