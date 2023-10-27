# Question 4):

# Code Library:
import turtle as t
import math as m

# Function Main():
def main():
    window = t.Screen()

    numTriangles = int(input())

    if(numTriangles > 0):
        lineWidth = 200
        regionWidth = lineWidth/(numTriangles + 1) + lineWidth/60
        triangleSide = lineWidth/10

        t.penup()
        t.forward(lineWidth/2)
        t.pendown()

        #First Triangle:
        t.forward((regionWidth - triangleSide)/2)
        t.left(60)
        t.forward(triangleSide)
        t.right(120)
        t.forward(triangleSide)
        t.left(60)

        if(numTriangles > 1):
            for i in range(1, m.floor(numTriangles/2)):
                #Right triangles:
                t.forward(regionWidth - triangleSide)
                t.left(60)
                t.forward(triangleSide)
                t.right(120)
                t.forward(triangleSide)
                t.left(60)

        #Last Line Right:
        t.forward((regionWidth - triangleSide))
        print(t.position())

        #New Start:
        t.penup()
        t.home()
        t.forward(lineWidth/2)
        t.left(180)
        t.pendown()

        if(numTriangles > 1):
            t.forward((regionWidth - triangleSide)/2)

            #Left triangles:
            for i in range(0, m.ceil(numTriangles/2)):
                if(i > 0):
                    t.forward(regionWidth - triangleSide)
                    
                #Left triangles:
                t.right(60)
                t.forward(triangleSide)
                t.left(120)
                t.forward(triangleSide)
                t.right(60)
        
            
        #Last Line Left:
        if(numTriangles == 1):
            t.forward((regionWidth - triangleSide)/2)
            t.hideturtle()
            print(t.position())
        else:
            t.forward((regionWidth - triangleSide))
            print(t.position())
            t.hideturtle()

    window.exitonclick()   

main()


