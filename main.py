import random
import turtle

colores = [(245, 243, 238), (246, 242, 244), (202, 164, 110), (240, 245, 241), (236, 239, 243),
           (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20),
           (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149),
           (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171),
           (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102),
           (107, 127, 153), (176, 192, 208), (168, 99, 102)]

t = turtle.Turtle()
turtle.colormode(255)
t.speed("fastest")
turtle.bgcolor("black")
t.color("blue")
t.hideturtle()

t.penup()
posx = -300
posy = -260
t.setx(posx)
t.sety(posy)
filas = 10
columnas = 10

for _ in range(filas):
    for _ in range(columnas):
        t.pendown()
        t.begin_fill()
        t.circle(10)
        t.end_fill()
        t.penup()
        t.forward(50)
        t.color(random.choice(colores))
    posy += 50
    t.setx(posx)
    t.sety(posy)

screen = turtle.Screen()
screen.exitonclick()
