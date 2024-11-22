from turtle import *

speed(5)

pensize(1)
pencolor('red')
fillcolor('red')
begin_fill()
for _ in range(2):
    forward(360)
    right(90)
    forward(120)
    right(90)
end_fill()
pencolor('blue')
fillcolor('blue')
begin_fill()
for _ in range(2):
    forward(120)
    left(90)
    forward(120)
    left(90)
end_fill()
penup()
forward()
done()