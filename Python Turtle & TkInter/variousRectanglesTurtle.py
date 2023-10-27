# Question 3):

# Code Library:
import turtle as t
import random as rand

# Code Functions:
def makeOneRectangle(width):
    # 10:1 Proportion:
    height = width/10

    # Making for the rectangle:
    t.fillcolor(rand.randint(0, 255)/255, rand.randint(0, 255)/255, rand.randint(0, 255)/255)

    t.begin_fill()
    t.forward(width)
    t.left(90)
    t.forward(height)
    t.left(90)
    t.forward(width)
    t.left(90)
    t.forward(height)
    t.end_fill()

    # Preparing for a new one:
    t.left(180)
    t.penup()
    t.forward(2*height)
    t.right(90)
    t.pendown()


# Function Main():
def main():
    window = t.Screen()
    numDrawings = int(input())
    width = 300

    # Preparing for the rectangle:
    t.penup()
    t.right(90)
    t.forward(5*(300/10))
    t.left(90)  
    t.backward(width/2)  
    t.pendown()

    for i in range(numDrawings):
        makeOneRectangle(width)

    window.exitonclick()   

main()