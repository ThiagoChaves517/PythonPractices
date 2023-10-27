# Question 7):

# Code Libaries:
import tkinter as tk

# Code Functions:
def circle(x1, y1, ray, color, canvas):
    x2 = x1 + 2 * ray
    y2 = y1 + 2 * ray

    canvas.create_oval(x1, y1, x2, y2, outline=color, width=10)

# Function Main():
def main():
    window = tk.Tk()
    window.geometry('800x600')
    canvas = tk.Canvas(window, width=800, height=600)

    x1, y1 = 10, 20
    ray = 120
    h = 135


    circle(x1, y1, ray, '#0885c2', canvas)
    circle(x1+h, y1+h, ray, '#fbb132', canvas)
    circle(x1+2*h, y1, ray, 'black', canvas)
    circle(x1+3*h, y1+h, ray, '#1c8b3c', canvas)
    circle(x1+4*h, y1, ray, '#ed334e', canvas)

    canvas.pack()
    tk.mainloop()

main()