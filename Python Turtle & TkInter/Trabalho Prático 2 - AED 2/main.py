import tkinter as tk
from algoritmosBusca import algoritmo_A_Estrela
from labirintos import imprimirLabirinto, inicializarLabirinto

def main():
    matrizLabirintoDeBools = []
    linhas = 10
    colunas = 10

    p0 = (1,1) # Ponto Incial (Modifique para criar um novo ponto de partida)
    pF = (1,9) # Saída do Labirinto. (Modifique para criar uma nova saída do labirinto)

    # Pontos que sinalizam os corredores do labirinto
    listaDePontos = [p0, (2,1), (3,1), (4,1), (4,2), (4,3), (3,3), (2,3), (1,3), (1,4), (1,5), (1,6), (1,7), (1,8), pF]
    listaDePontos2 = [(4,4), (4,5), (3,5), (3,6), (3,7), (3,8), (4,8), (5,8), (5,7), (6,8), (6,7), (6,6), (6,5), (6,4), (7,4), (8,4), (8,3), (8,2), (8,1), (7,1), (6,1), (6,2)]

    inicializarLabirinto(matrizLabirintoDeBools, linhas, colunas)

    # Criando os corredores do labirinto:
    for ponto in listaDePontos:
        matrizLabirintoDeBools[ponto[0]][ponto[1]] = 0

    for ponto in listaDePontos2:
        matrizLabirintoDeBools[ponto[0]][ponto[1]] = 0


    # Impressão do Labirinto Completo:
    imprimirLabirinto(matrizLabirintoDeBools, linhas, colunas)
    print()

    # Impressão do Caminho do ponto p0 até o ponto pF:
    print(algoritmo_A_Estrela(p0, pF, matrizLabirintoDeBools))


main()