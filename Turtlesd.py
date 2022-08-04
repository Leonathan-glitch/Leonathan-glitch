import turtle
import time
screen=turtle.Screen()
t=turtle.Turtle()
screen.setup(520,320)
screen.bgcolor("black")
color_set=['red','green','blue','yellow','purple']
t.pensize(4)
t.setpos(-90,30)
t.pendown()
for i in range (5):
    t.pencolor(color_set[i])
    t.forward(200)
    t.right(144)
t.penup()
t.setpos(80,-140)

    
  
