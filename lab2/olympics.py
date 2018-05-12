import turtle

turtle.pensize(10)
def drawcircle(radius):
    turtle.circle(radius)

radius1 = int(input("Enter the radius of the circle: "))

turtle.color("black")
drawcircle(radius1)

turtle.color("red")
turtle.penup()
turtle.forward(128)
turtle.pendown()
drawcircle(radius1)

turtle.color("blue")
turtle.penup()
turtle.backward(256)
turtle.pendown()
drawcircle(radius1)

turtle.color("green")
turtle.penup()
turtle.forward(150)
turtle.right(90)
turtle.pendown()
drawcircle(radius1)

turtle.color("yellow")
turtle.penup()
turtle.left(120)
turtle.backward(87)
turtle.pendown()
drawcircle(radius1)
