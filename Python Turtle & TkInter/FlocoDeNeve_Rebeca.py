import turtle as t
import tkinter as tk
from tkinter import simpledialog

#essa função é chamava para decompor cada lado do triangulo equilatero
def floco_de_neve(lado, nivel):
    # Condição de parada: quando o nível se iguala a zero, movemos a tartaruga para o início.
    if nivel == 0:
        t.forward(lado)
    else:
        # Dividimos o lado em três partes.
        lado /= 3
        # Decrementados os níveis
        nivel -= 1
        # Primeira chamada recursiva que desenha o primeiro segmento  do floco.
        floco_de_neve(lado, nivel)
        t.left(60)
        # Segunda chamada recursiva para desenhar outro segmento do floco.
        floco_de_neve(lado, nivel)
        t.right(120)
        # Terceira chamada recursiva para desenhar o último segmento do floco.
        floco_de_neve(lado, nivel)
        t.left(60)
        # Quarta chamada recursiva para completar o desenho do floco.
        floco_de_neve(lado, nivel)

def main():
    window = tk.Tk()
    window.withdraw() 
    lado = simpledialog.askinteger("Tamanho do lado", "Informe o tamanho do lado do triângulo:")
    
    n = simpledialog.askinteger("Níveis", "Digite quantos níveis deseja:")

    window.destroy() 

    window = t.Screen()
    t.speed(0)
    t.penup()
    t.pendown()
    t.shape("turtle")
    t.color("blue")

    for _ in range(3):
        # Desenha o floco de neve para cada um dos três lados de um triângulo equilátero.
        floco_de_neve(lado, n)
        t.right(120)

    window.exitonclick()

main()