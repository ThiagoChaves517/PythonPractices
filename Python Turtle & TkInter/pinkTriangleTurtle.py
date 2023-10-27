# Question 1)

# Code Libraries:
import turtle

# Function Main():
def main():
    t = turtle.Turtle()
    window = turtle.Screen()
    x = 100

    t.fillcolor('pink') #To choose the triangle's color.

    t.backward(x/2) #To center the triangle.

    t.begin_fill() #Start of the painting.
    t.forward(x) #Start of the drawing.
    t.left(120)
    t.forward(x)
    t.left(120)
    t.forward(x) #End of the drawing.
    t.end_fill() #End of the painting.

    window.exitonclick() #With this, the window will exit just when clicking it!

main()
