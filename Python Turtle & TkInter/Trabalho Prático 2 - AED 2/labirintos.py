from mathSolutions import oddInt
import random as r

def inicializarLabirinto(linhas, colunas): #Gera um labirinto vazio
    matriz = []

    for i in range(linhas):
        for j in range(colunas):
            matriz.append(1) # Sendo "True" as paredes do labirinto.

    return matriz

def geraLabirinto(colunas, linhas):
    labirinto = inicializarLabirinto(linhas, colunas)
    lista = [] # uma lista vazia

    # Gera o primeiro ponto
    y0 = oddInt(r.randint(3, linhas-2))
    x0 = oddInt(r.randint(3, colunas-2))

    # Insere os quatro primeiros corredores em L
    lista.append((y0 - 1, x0, y0 - 2, x0)) # para cima
    lista.append((y0, x0 - 1, y0, x0 - 2)) # para a esquerda
    lista.append((y0 + 1, x0, y0 + 2, x0)) # para baixo
    lista.append((y0, x0 + 1, y0, x0 + 2)) # para a direita

    while (len(lista) > 0):
        lista.pop(r.randrange(len(lista)))

        # se for uma coordenada válida (parede), então
        # cria um novo corredor

        

        if (labirinto[y2][x2] == 0):
            Labirinto[ ][ ] = 1
            Labirinto[ ][ ] = 1
        para cada coordenada alcançável a partir de (y2, x2):
            insira a coordenada alcançavel em L se o destino estiver dentro dos limites do
            labirinto e for uma parede
