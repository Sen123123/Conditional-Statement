import turtle

cs = turtle.Turtle()

turtle.Screen().bgcolor("White")
turtle.Screen().setup(1000, 1000)

for a in range(4):
    cs.forward(100)
    cs.right(90)

turtle.done()