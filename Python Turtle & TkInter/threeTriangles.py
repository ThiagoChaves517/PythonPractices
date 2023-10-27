# Question 5)

# Code Libraries:
import turtle as t

# Code Functions:
def triangleMosaic(n, window):
    t.fillcolor('red')
    t.penup()
    t.goto(-300, 300) 
    t.pendown()
    
    counter = 0
    for i in range(n):
        print('Triangle ' + str(counter+1))
        if(i % 2 == 0):
            print(' - p1 = ', t.position())
            t.begin_fill()
            t.forward(150)
            t.backward(75)
            t.right(90)
            t.penup()
            t.forward(120) 
            t.pendown()
            t.right(148)
            t.forward(15 * pow(89, 1/2))
            t.left(180)
            t.forward(15 * pow(89, 1/2))
            t.end_fill()
            print(' - p3 = ', t.position())
            

            t.begin_fill()
            t.left(116)
            t.forward(15 * pow(89, 1/2) - 0.01)
            print(' - p2 = ', t.position())
            t.left(122)
            t.forward(149.98)
            t.end_fill()

            t.penup()
            t.left(180)
            t.forward(150 + 30)
            t.pendown()
        else:
            print(' - p1 = ', t.position())
            t.begin_fill() #Start of the painting.
            t.right(58)
            t.forward(15 * pow(89, 1/2) - 0.01)
            print(' - p2 = ', t.position())
            t.right(122)
            t.forward(150) #End of the drawing.
            print(' - p3 = ', t.position())
            t.right(122)
            t.forward(15 * pow(89, 1/2) - 0.01)
            t.end_fill() #End of the painting.
            
            t.penup()
            t.right(58)
            t.forward(30)
            t.pendown()

        if(counter == 0):
            t.fillcolor('green')
            counter += 1
        elif(counter == 1):
            t.fillcolor('blue')
            counter += 1
        elif(counter == 2):
            t.fillcolor('red')
            counter = 0

# Função Main():
def main():
    window = t.Screen()
    window.screensize(canvheight= 3000, canvwidth= 3000)

    #triangleMosaic(3, window)

    # Preparing for the first triangle:
    t.penup()
    t.goto(-300, 300) 
    t.pendown()

    # First Triangle:
    t.fillcolor('red')
    t.begin_fill()
    print(' - p1 = ', t.position())
    t.goto(-150.02, 300.00)
    print(' - p2 = ', t.position())
    t.goto(-225.00, 180.00)
    print(' - p3 = ', t.position())
    t.goto(-300.00, 300.00)
    t.end_fill()

    t.penup()
    t.forward(150 + 30)
    t.pendown()    

    # Second Triangle:
    t.fillcolor('green')
    t.begin_fill()
    print(' - p1 = ', t.position())
    t.goto(-120.00, 300.00)
    print(' - p2 = ', t.position())
    t.goto(-45.01, 180.00)
    print(' - p3 = ', t.position())
    t.goto(-195.01, 180.00)
    t.end_fill()
    t.goto(-120.00, 300.00)

    t.penup()
    t.forward(30)
    t.pendown()    

    # Third Triangle:

    t.fillcolor('blue')
    t.begin_fill()
    print(' - p1 = ', t.position())
    t.goto(-90.02, 300.00)    
    print(' - p2 = ', t.position())
    t.goto(59.95, 300.00)
    print(' - p3 = ', t.position())
    t.goto(-15.03, 180.00)
    
    t.end_fill()

    t.penup()
    t.forward(30)
    t.pendown()  

    window.exitonclick()

main()
    
