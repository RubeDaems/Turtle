from turtle import *

speed(5000)
left(90)

for _ in range(3):
    for _ in range(5):
        forward(50)
        right(144)

    penup()
    forward(150)
    pendown()
    right(120)
left(90)
penup()
forward(100)
pendown()

for _ in range(360):
    forward(50)
    backward(50)
    right(1)
right(120)
forward(20)
for _ in range(360):
    color('white')
    forward(50)
    backward(50)
    right(1)