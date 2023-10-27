# Question 2)

# Code Libraries:
import turtle as t

# Function Main():
def main():
    # Turtle Screen:
    window = t.Screen()

    # 10:1 Proportion:
    width = 300
    height = width/10

    # Making the rectangles:
    t.penup()
    t.backward(width/2)
    t.pendown()

    # - Green Rectangle:
    t.fillcolor('#74C365')

    t.begin_fill()
    t.forward(width)
    t.left(90)
    t.forward(height)
    t.left(90)
    t.forward(width)
    t.left(90)
    t.forward(height)
    t.end_fill()

    # - Blue Rectangle:
    t.left(180)
    t.penup()
    t.forward(2*height)
    t.right(90)
    t.pendown()

    t.fillcolor('#4169E1')

    t.begin_fill()
    t.forward(width)
    t.left(90)
    t.forward(height)
    t.left(90)
    t.forward(width)
    t.left(90)
    t.forward(height)
    t.end_fill()

    window.exitonclick()

main()    