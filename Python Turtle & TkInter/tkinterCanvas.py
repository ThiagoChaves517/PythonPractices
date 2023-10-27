# Question 6)

# Code Libraries:
import tkinter as tk

# Function Main():
def main():
    window = tk.Tk()
    window.geometry('800x600')
    
    canvas = tk.Canvas(window, width=800, height=600)

    #First Triangle:
    canvas.create_polygon([30.004, 60.00, 45.00, 84.00, 60.00, 60.00], outline = 'black', fill = 'red')

    #Second Triangle:
    canvas.create_polygon([49.004, 84.00, 64.004, 60.00, 79.00, 84.00], outline = 'black', fill = 'green')

    #Blue Triangle:
    canvas.create_polygon([68.008, 60.00, 83.004, 84.00, 98.004, 60.00], outline = 'black', fill = 'blue')

    canvas.pack()
    window.mainloop()

main()




