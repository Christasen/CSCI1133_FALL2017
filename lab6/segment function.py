import turtle
#def pieChart(flist):
    COL = ['red','yellow','blue','green','purple']
    total = 0
    flist = [1,4,5,6,7]
    for i in range(0,5):
        total += flist[i]
    print(total)
    r = 200

    pie = turtle()
    pie.penup()
    pie.sety(-r)
    pie.pendown()
    for i in range(0,5):
        for frac in flist:
            pie.fillcolor(COL[i])
            pie.begin_fill()
            pie.circle(r, frac * 360 /total)
            pos = pie.position()
            pie.goto(0,0)
            pie.end_fill()
            pie.setposition(position)

pie.hideturtle()
