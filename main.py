import turtle

screen = turtle.Screen()
screen.screensize(500,500)
screen.bgcolor('yellow')

t = turtle.Turtle()

t.setheading(135)

t.begin_fill()
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.fillcolor('cyan')
t.end_fill()

#to move turtle to new place
t.penup()
t.goto(0,0)
t.pendown()

t.setheading(45)
t.begin_fill()
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.fillcolor('brown')
t.end_fill()

t.hideturtle()

#This is the last line of code
turtle.done()


