def inicializarLabirinto(linhas, colunas): #Gera um labirinto vazio
    for i in range(linhas):
        for j in range(colunas):
            matrizLabirintoDeBools.append(-1) # Sendo "True" as paredes do labirinto.

def geraLabirinto(linhas, colunas)
    Labirinto = inicializarLabirinto(linhas, colunas)
    lista = [] # uma lista vazia

    # Gera o primeiro ponto
Linha← coordenada ímpar entre 3 e 
← coordenada ímpar entre 3 e 
p1 = (1, 7)
(−1, 7)
(1, 5) (1, 6, 1, 5) L
(3, 7)
(1, 9) (1, 8, 1, 9) L
L = [(3, 6, 3, 5), (2, 7, 1, 7), (3, 8, 3, 9), (4, 7, 5, 7), (1, 6, 1, 5), (1, 8, 1, 9)]
L
L
M N
M N
y0 M − 2
x0 N − 2
# Insere os quatro primeiros corredores em L
L.insere( ) # para cima
L.insere( ) # para a esquerda
L.insere( ) # para baixo
L.insere( ) # para a direita
enquanto L não estiver vazia
← remova um elemento aleatorio de L
# se for uma coordenada válida (parede), então
# cria um novo corredor
se Labirinto[ ][ ] == 0, então
Labirinto[ ][ ] = 1
Labirinto[ ][ ] = 1
para cada coordenada alcançável a partir de , faça
insira a coordenada alcançavel em L se o destino estiver dentro dos limites do
labirinto e for uma parede
(y0 − 1, , x0 y0 − 2, ) x0
( , y0 x0 − 1, , y0 x0 − 2)
( + 1, , + 2, ) y0 x0 y0 x0
( , + 1, , + 2) y0 x0 y0 x0
( , , , ) y1 x1 y2 x2
( , ) y2 x2
y2 x2
y1 x1
y2 x2
