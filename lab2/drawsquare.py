import turtle

def drawsquare(length):
    turtle.forward(length)
    turtle.left(90)
    turtle.forward(length)
    turtle.left(90)
    turtle.forward(length)
    turtle.left(90)
    turtle.forward(length)

length =  int(input("Enter the length of each side: "))
drawsquare(length)
turtle.left(30)
drawsquare(length)
turtle.left(30)
drawsquare(length)
