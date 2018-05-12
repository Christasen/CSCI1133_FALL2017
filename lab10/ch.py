import urllib
import turtle
# web1 = "https://www.google.com/fiance/historical?output=csv&q="
# var2 = "etsy"
# web3 = web1 + var2
# page1 = urllib.request.urlopen(web3)
turtle.hideturtle()
turtle.setworldcoordinates(0,0,500,500) #####this is significant!!!!
filename = open('all_day.csv','r')
list1 = filename.readlines()
close = []
date = []
i = 1;
while i < len(list1):
    a = list1[i]
    alist = a.split(",")
    close.append(alist[4])
    date.append(alist[0])
    i = i + 1

i = len(close)
pointOneX = 0
pointOneY = 0;

while i >= 0:
    pointOneX = pointOneX + 10
    pointOneY = 10*(float(close[i-1]))
    turtle.goto(pointOneX, pointOneY)
    turtle.dot(2)
    i = i -1

turtle.exitonclick()
