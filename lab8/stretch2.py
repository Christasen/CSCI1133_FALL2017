import turtle
import random

def tree(t, trunkLength):

    if trunkLength < 5:
         return
    else:

        t.forward(trunkLength)
        a = random.randint(15,45)
        l = random.randint(12,18)
        t.right(a)
        tree(t, trunkLength-l)
        c = random.randint(15,45)
        d = random.randint(12,18)
        t.left(a+c)
        tree(t, trunkLength-d)
        t.right(c)
        t.backward(trunkLength)


def main():
    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(0,-200)
    t.pendown()
    t.left(90)
    tree(t,100)


if __name__ == "__main__":
    main()
