import turtle
chart_title = 'Tourism GDP by States/Territories in Australia'
segment_labels = ['QLD', 'VIC', 'NSW', 'SA', 'WA', 'TAS', 'NT', 'ACT']
percentages = [0.24, 0.22, 0.328, 0.06, 0.082, 0.03, 0.02, 0.02]

from turtle import *

radius = 200


penup()
forward(radius)
left(90)
pendown()
color('palegreen')
begin_fill()
circle(radius)
end_fill()
home()
right(90)
color('black')

def segment(percentages):
    rollingPercent = 0
    radius=200
    for percent in percentages:
        segment = percent * 360
        rollingPercent += segment
        setheading(rollingPercent)
        pendown()
        forward(radius)
        penup()
        home()

segment(percentages)
hideturtle()
Screen()
screen.exitonclick()
