from turtle import Turtle, Screen
def pieChart(flist):
    COL = ['red','yellow','blue','green','purple']
    Alist = ['A','E','I','O','U']
    total = 0
    r = 200
    R = r * 0.5
    FONTSIZE = 20
    FONT = ("Ariel", FONTSIZE, "bold")

    for i in range(0,5):
        total += flist[i]

    pie = Turtle()
    pie.penup()
    pie.sety(-r)
    pie.pendown()

    j = 0
    k = 0
    while j <= 4:
        while k <= 4:
            pie.fillcolor(COL[j])
            pie.begin_fill()
            frac = flist[k]
            pie.circle(r, frac* 360 /total)
            pos = pie.position()
            pie.goto(0,0)
            pie.end_fill()
            pie.setposition(pos)
            j += 1
            k += 1
    pie.penup()
    pie.sety(-R)
    
    l = 0
    m = 0
    while m <= 4:
        while l <= 4:
            la = Alist[m]
            frac = flist[l]
            pie.circle(R,frac * 360/total/2)
            pie.write(la,align = 'center',font = FONT)
            pie.circle(R,frac * 360/total/2)
            l += 1
            m += 1

    pie.hideturtle()
    #pie.Screen().exitonclick()
