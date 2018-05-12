#CSCI1133
#Programming Assignment 1
#Guangyu YAN
#yanxx630
#5384684

from turtle import Turtle, Screen
import turtle
import math

def vowelCount(astring):

    alist = []
    acount = 0
    ecount = 0
    icount = 0
    ocount = 0
    ucount = 0
    for i in astring:
        if i == 'a' or i == 'A':
            acount += 1
        elif i == 'e' or i == 'E':
            ecount += 1
        elif i == 'i' or i == 'I':
             icount += 1
        elif i == 'o' or i == 'O':
            ocount += 1
        elif i == 'u' or i == 'U':
            ucount += 1
    alist.append(acount)
    alist.append(ecount)
    alist.append(icount)
    alist.append(ocount)
    alist.append(ucount)
    return(alist)


def pieChart(flist):
    COL = ['red','yellow','blue','green','purple']
    Alist = ['A','E','I','O','U']
    total = 0
    r = 300
    FONT = ("Times", 22, "bold")

    for i in range(0,5):
        total += flist[i]

    pie = Turtle()
    pie.hideturtle()
    pie.penup()
    pie.sety(-r)
    pie.pendown()
    pie.speed(0)

    if flist == [0,0,0,0,0]:
        pie.circle(r, 360)
        pie.penup()
        pie.sety(0)
        pie.pendown()
        pie.write("no vowels in the input",align = 'center',font = FONT)
        chart = Screen()
        chart.exitonclick()
        return


    for i in range(5):
        pie.fillcolor(COL[i])
        pie.begin_fill()
        pie.circle(r, flist[i] / total * 360)
        previous = pie.position()
        if flist[i] == total:
            pie.penup()
            pie.goto(0,0)
            pie.end_fill()
            pie.pendown()
        else:
            pie.goto(0,0)
            pie.end_fill()
            pie.setposition(previous)

    pie.penup()
    pie.sety(-r / 2)

    for i in range(5):
        la = Alist[i]
        frac = flist[i]
        if frac == 0:
            continue
        pie.circle(r / 2,frac * 360/total/2)
        pie.write(la,align = 'center',font = FONT)
        pie.circle(r / 2,frac * 360/total/2)

    chart = Screen()
    chart.exitonclick()


def main():
    ourstring = turtle.textinput("Input Window","Please enter a sentence")
    ourlist = vowelCount(ourstring)
    pieChart(ourlist)


if __name__ == "__main__":
    main()
