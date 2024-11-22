from turtle import *

speed(10)

pensize(3)
pencolor('black')
fillcolor('black')
begin_fill()
for _ in range(1):
    circle(100)
end_fill()
teleport(5, 5)
pencolor('white')
fillcolor('white')
begin_fill()
for _ in range(1):
    circle(85)
end_fill()

#eerste oog
pencolor('black')
fillcolor('black')
begin_fill()
teleport(-45, 50)
for _ in range(1):
    circle(35)
end_fill()
pencolor('white')
fillcolor('white')
begin_fill()
teleport(-40, 55)
for _ in range(1):
    circle(28)
end_fill()
pencolor('black')
fillcolor('black')
begin_fill()
teleport(-25, 75)
for _ in range(1):
    circle(10)
end_fill()

#tweede oog
begin_fill()
teleport(55, 50)
for _ in range(1):
    circle(35)
end_fill()
pencolor('white')
fillcolor('white')
begin_fill()
teleport(60, 55)
for _ in range(1):
    circle(28)
end_fill()
pencolor('black')
fillcolor('black')
begin_fill()
teleport(75, 75)
for _ in range(1):
    circle(10)
end_fill()

# mond
begin_fill()
teleport(0, 30)
for _ in range(2):
    forward(30)
    left(10)
    for _ in range(1):
        forward(10)
end_fill()
begin_fill()
teleport(0, 30)
for _ in range(1):
    left(150)
    forward(30)
    right(10)
    forward(45)
end_fill()
#tanden
pensize(5)
begin_fill()
teleport(0, 30)
left(100)
for _ in range(2):
    forward(26)
    penup()
    backward(28)
    right(90)
    forward(40)
    left(90)
    pendown()
end_fill()

begin_fill()
teleport(0, 30)
right(265)
for _ in range(2):

    pendown()
end_fill()
done()

