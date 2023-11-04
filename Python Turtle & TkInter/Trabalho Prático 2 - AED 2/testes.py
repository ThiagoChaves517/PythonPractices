#      |         Este arquivo serviu para o teste de diversas questões.               | 
#      |   As funções dos arquivos "funcoesHeap.py" e "algoritmosBusca.py", porém,    |
#      |                       não foram testadas aqui.                               |

import random as r
from termcolor import cprint

def imprimirLabirinto(matriz, linhas, colunas):
    for i in range(linhas):
        for j in range(colunas):
            if(matriz[i][j] != 0):
                cprint(matriz[i][j], "blue", end=' ')
            else:
                print(matriz[i][j], end=' ')
        print()

def inicializarLabirinto(matrizLabirinto, linhas, colunas): #Gera um labirinto vazio
    for i in range(linhas):
        linhaMatriz = [] # Represenda cada uma das linhas da matriz "matrizLabirintoDeBools"  
        for j in range(colunas):
            linhaMatriz.append(1)

        matrizLabirinto.append(linhaMatriz) # Sendo "1" as paredes do labirinto e "0" os corredores.

    return matrizLabirinto

def oddInt(n):
    if(n == 0):
        return 1

    if(n % 2 == 0):
        return n - 1
    
    return n


def validarCorredor(matrizLabirinto, linhas, colunas, corredorTupla):
    x1, y1 = corredorTupla[0], corredorTupla[1]
    x2, y2 = corredorTupla[2], corredorTupla[3]

    if((x2 > 0 and x2 < linhas-1) and (y2 > 0 and y2 < colunas-1) and matrizLabirinto[x2][y2] == 1):
        return True
    
    return False 


# Lembrando que "1" é parede e que "0" é corredor.
def geraLabirinto(matrizLabirinto, linhas, colunas):
    labirinto = inicializarLabirinto(matrizLabirinto, linhas, colunas)
    lista = [] # Uma lista vazia.

    # Gera o primeiro ponto:
    x0 = oddInt(r.randint(3, linhas-2))
    y0 = oddInt(r.randint(3, colunas-2))
    labirinto[x0][y0] = 0

    # Insere os quatro primeiros corredores em L:
    lista.append((x0-1, y0, x0-2, y0)) # Corredor de dois quadrados para cima.
    lista.append((x0, y0+1, x0, y0+2)) # Corredor de dois quadrados para a direita.
    lista.append((x0, y0-1, x0, y0-2)) # Corredor de dois quadrados para a esquerda.
    lista.append((x0+1, y0, x0+2, y0)) # Corredor de dois quadrados para baixo.

    while(len(lista) > 0):
        pontos = lista.pop(r.randrange(len(lista)))

        if(validarCorredor(matrizLabirinto, linhas, colunas, pontos) == True):
            labirinto[pontos[0]][pontos[1]] = 0
            labirinto[pontos[2]][pontos[3]] = 0
            
            x2 = pontos[2]
            y2 = pontos[3] 

            lista.append((x2-1, y2, x2-2, y2)) # Corredor de dois quadrados para cima.
            lista.append((x2, y2+1, x2, y2+2)) # Corredor de dois quadrados para a direita.
            lista.append((x2, y2-1, x2, y2-2)) # Corredor de dois quadrados para a esquerda.
            lista.append((x2+1, y2, x2+2, y2)) # Corredor de dois quadrados para baixo.

def test():
    matrizLabirintoDeBools = []
    linhas = 11
    colunas = 11

    geraLabirinto(matrizLabirintoDeBools, linhas, colunas)

    imprimirLabirinto(matrizLabirintoDeBools, linhas, colunas)

test()