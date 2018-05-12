#CSCI1133 lab3
#GUANGYU YAN
import turtle
import random
import math
def walk():
    alist = [0,90,180,270]
    i = random.randint(0,3)
    turtle.left(alist[i])
    turtle.forward(20)

def main():
    steps = 0
    while (turtle.xcor() <= turtle.window_width()/2 ) or (turtle.ycor() <= turtle.window_height()/2):
        walk()
        steps += 20
    return steps

if __name__ == "__main__":
    main()
