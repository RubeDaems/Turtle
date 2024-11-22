from turtle import *

speed(1)
left(90)

for _ in range(4):
    for _ in range(5):
        forward(50)
        right(144)

    penup()
    forward(150)
    pendown()
    right(90)

mainloop()