from mathSolutions import oddInt
import random as r

def imprimirLabirinto(matriz, linhas, colunas):
    for i in range(linhas):
        for j in range(colunas):
            print(matriz[i][j], end=' ')
        print()

def inicializarLabirinto(matrizLabirinto, linhas, colunas): #Gera um labirinto vazio
    for i in range(linhas):
        linhaMatriz = [] # Represenda cada uma das linhas da matriz "matrizLabirintoDeBools"  
        for j in range(colunas):
            linhaMatriz.append(1)

        matrizLabirinto.append(linhaMatriz) # Sendo "1" as paredes do labirinto e "0" os corredores.

    return matrizLabirinto

'''
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
'''