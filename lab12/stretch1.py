                                                                                                                                                           import turtle
import random
import math


def mouseInput(x,y):
    print(x,',',y)

class Shape:
    def __init__(self,x=0, y=0, fil="",bol = False):
        self.xloc = x
        self.yloc = y
        self.fil = fil
        self.bol = bol

    def setFillcolor(self,fil1):
        self.fil = fil1

    def setFilled(self,bol1):
        self.bol = bol1

    def isFilled(self):
        a = self.bol
        return a
class Circle(Shape):
    #The way to define the new class
    def __init__(self,x=0,y=0,fil="",bol =False, r = 1):
        super().__init__(x,y,fil,bol) #this one is really essential
        self.r = r
    def draw(self,turtle):
        if seld.bol == True:
            turtle.penup()
            turtle.goto(self.x,self.y)
            turtle.fillcolor(self.fil)
            turtle.begin_fill()
            turtle.circle(self.r)
            turtle.end_fill()
            turtle.pendown()

        else:
            turtle.penup()
            turtle.goto(self.x,self.y)
            turtle.circle(self.r)
            turtle.pendown()
    def isIN(self,x,y):
        d1 = math.pow(x-(self.x + self.r),2)
        d2 = math.pow(y-(self.y + self.r),2)
        r1 = sqrt(d1 + d2)
        if r1 <= self.r:
            return True

class Display:
    def __init__(self):
        self.t = turtle.Turtle()
        self.scr = self.t.getscreen() #or turtle.getscreen()
        self.ele = []
        self.t.speed(0)
        self.t.hideturtle() #must be self.t since t does not exist
        #on click event should be included here
        self.scr.onclick(self.mouseEvent)
        self.scr.listen()
    def mouseEvent(self,x,y):
        drawShape = True
        for i in self.ele:
            if i.isIN(x,y) == True:
                self.remove(i)
                drawShape = False
        if drawShape == True:
            r = random.randint(1,100)
            clist = ["red","blue,","green","yellow","black","purple"]
            i = random.randint(0,len(self.ele)-1)
            color = clist[i]
            c = Circle(x,y,color,True,r)
            self.add(c)

        #add(c) #self.add?

        #we can use the class we defined anywhere in our porgram
    def add(self,shape1):
        self.ele.append(shape1)
        shape1.draw(self.t)
    def remove(self,shape1):
        self.ele.remove(shape1)
        self.scr.clear() #clearscreen()
        for i in self.ele:
            i.draw(self,t)


class Rectangles(Shape):
    def __init__(self,x=0,y=0,fil="",bol =False, w=1, h=1):
        super().__init__(x,y,fil,bol) #this one is really essential
        self.w = w
        self.h = h
    def draw(self,turtle):
        if seld.bol == True:
            turtle.penup()
            turtle.goto(self.x,self.y)
            turtle.fillcolor(self.fil)
            turtle.begin_fill()
            for i in range(2):
                turtle.forward(self.w)
                turtle.right(90)
                turtle.forward(self.h)
                turtle.right(90)
            turtle.end_fill()
            turtle.pendown()

        else:
            turtle.penup()
            turtle.goto(self.x,self.y)
            turtle.circle(self.r)
            turtle.pendown()
    def isIN(self,x,y):
        x1 = self.x + self.w
        y1 = self.y + self.h
        if x <= x1 and y <= y1 and x>= self.x and y >= self.y:
            return True

        #t.penup()
        #t.goto(x,y)
        #t.fillcolor(color)
        #t.circle(r)
        #t.endfill()
        #t.pendown()
