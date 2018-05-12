#CSCI1133 lab3
#GUANGYU YAN
import turtle

def drawsquare(length):
    turtle.forward(length)
    turtle.left(90)
    turtle.forward(length)
    turtle.left(90)
    turtle.forward(length)
    turtle.left(90)
    turtle.forward(length)
    turtle.left(90)

def main():
    turtle.speed(0)
    t = 0
    length =  int(turtle.numinput("","Enter the length of each side: "))
    times = int(turtle.numinput("", "Enter the numbr of the squares you want to draw: "))
    while t <= times:
        drawsquare(length)
        turtle.left(360/times)
        t += 1
if __name__ == "__main__":
    main()
