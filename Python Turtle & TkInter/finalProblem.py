# Question 9):

# Code Libaries:
import tkinter as tk

# Code Functions:
def circle(x1, y1, ray, outcolor, fillcolor, canvas):
    x2 = x1 + 2*ray
    y2 = y1 + 2*ray 

    canvas.create_oval(x1, y1, x2, y2, outline=outcolor, fill=fillcolor, width=1)

def print_coords(event):
    # Outputting x and y coords to console
    print(event.x, event.y)


# Function Main():
def main():
    window = tk.Tk()
    window.geometry('800x600')
    window.bind("<Button-1>", print_coords)

    canvas = tk.Canvas(window, width=800, height=600)

    T = 150
    canvas.create_line(400 - T, 300, 400 + T, 300)
    canvas.create_line(400, 300 - T, 400, 300 + T) 
    
    centroX = 400
    centroY = 300

    circle(centroX - T/1.05, centroY + T/23, 0.45*T, 'red', '#db7093', canvas)
    canvas.create_rectangle([centroX + T/16 - centroX/100, centroY + T/23, centroX + T/16 - centroX/100 + T*0.9, centroY + T/23 + T*0.9], outline='blue', fill='#4169E1')
    #canvas.create_line([200, centroY + T/23 + T*0.9, 700, centroY + T/23 + T*0.9])
    canvas.create_polygon([centroX + T/16 - centroX/100, centroY + T/23 - centroY/25, centroX + T/16 - centroX/100 + T*0.9, centroY + T/23 - centroY/25, centroX + T/16 - centroX/100 + T*0.9/2, (centroY + T/23 - centroY/25) - (0.9 * pow(3, 1/2) * T)/2], outline='green', fill='#90EE90')
    canvas.pack()
    tk.mainloop()

main()