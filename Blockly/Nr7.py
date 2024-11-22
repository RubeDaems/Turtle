from turtle import *

speed(9)
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

for _ in range(4):
    forward(50)
    backward(50)
    right(45)

mainloop()