import turtle

turtle.Screen().bgcolor("white")
turtle.Screen().setup(1000,1000)

w = turtle.Turtle()

w.right(120)
w.forward(100)
w.right(120)
w.forward(100)
w.right(120)
w.forward(100)

w.end_poly()
w.pendown()

w.forward(6)

turtle.done()