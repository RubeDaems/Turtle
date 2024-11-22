from turtle import *

speed(1)
bgcolor('black')

pencolor('')
fillcolor('yellow')
begin_fill()

for _ in range(4):
    forward(100)
    right(90)
end_fill()
teleport(-200, 0)
pencolor('black')
fillcolor('yellow')
begin_fill()

for _ in range(4):
    forward(100)
    right(90)
end_fill()
teleport(0, 200)
fillcolor('yellow')
begin_fill()

for _ in range(4):
    forward(100)
    right(90)
end_fill()
teleport(-200, 200)
penup()
fillcolor('yellow')
begin_fill()

for _ in range(4):
    forward(100)
    right(90)
end_fill()
done()