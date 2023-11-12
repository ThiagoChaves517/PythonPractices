from mathSolutions import oddInt
import random as r

# Obs.: A função abaixo depende firmimente da função "geraLabirinto()" e da lista "corredores", a qual contém os corredores disponíveis do labirinto!
# Esta função fornece o ponto de partida no qual Codibentinho irá começar sua aventura no labirinto.
def gerarPontoDePartida(corredores):
    index = r.randrange(len(corredores))
    x, y = corredores[index]

    return (x, y)

# Obs.: A função abaixo depende firmimente da função "geraLabirinto()" e da lista "corredores", a qual contém os corredores disponíveis do labirinto!
# Esta função fornece a saída do labirinto em que Codibentinho.
def gerarSaidaLabirinto(matrizLabirinto, linhas, colunas, corredores):
    while(True):
        index = r.randrange(len(corredores))
        x, y = corredores[index]

        if(x - 1 == 0): # Saída ao Norte
            matrizLabirinto[x-1][y] = 0
            return (x - 1, y)
        
        if(x + 1 == linhas-1): # Saída ao Sul
            matrizLabirinto[x+1][y] = 0
            return (x + 1, y)
        
        if(y + 1 == colunas-1): # Saída ao Leste
            matrizLabirinto[x][y+1] = 0
            return (x, y + 1)
        
        if(y - 1 == 0): # Saída ao Oeste
            matrizLabirinto[x][y-1] = 0
            return (x, y - 1)

# Esta função imprime a matriz labirinto, apesar de tbm poder imprimir qualquer tipo primitivo de matriz 2D.
def imprimirLabirinto(matriz, linhas, colunas):
    for i in range(linhas):
        for j in range(colunas):
            print(matriz[i][j], end=' ')
        print()

# Gera uma sala cheia de paredes, ou seja: formada apenas de "1"s.
# Não é necessário usá-la em "main.py", pois ela já está inserida em "geraLabirinto()".
def inicializarLabirinto(matrizLabirinto, linhas, colunas): 
    for i in range(linhas):
        linhaMatriz = [] # Represenda cada uma das linhas da matriz "matrizLabirintoDeBools".
        for j in range(colunas):
            linhaMatriz.append(1)

        matrizLabirinto.append(linhaMatriz) # Sendo "1" as paredes do labirinto e "0" os corredores.

    return matrizLabirinto

# Valida se dois pontos - partindo de um - são paredes e se estão dentro dos limites da matriz.
def validarCorredor(matrizLabirinto, linhas, colunas, corredorTupla):
    x1, y1 = corredorTupla[0], corredorTupla[1]
    x2, y2 = corredorTupla[2], corredorTupla[3]

    if((x2 > 0 and x2 < linhas-1) and (y2 > 0 and y2 < colunas-1) and matrizLabirinto[x2][y2] == 1):
        return True
    
    return False 


# Esta função gera um labirinto de booleanos de forma aleatória, dependo apenas das proporções da matriz.
# Ela também recebe uma lista chamada "corredores", a qual deverá receber os corredores "0" criados.
# Obs.: Recomendasse que geraLabirinto() receba apenas matrizes de proporções ímpares.
# Obs.: Lembrando que "1" é parede e que "0" é corredor.
def geraLabirinto(matrizLabirinto, linhas, colunas, corredores):
    labirinto = inicializarLabirinto(matrizLabirinto, linhas, colunas)
    lista = [] # Uma lista vazia.

    # Gera o primeiro ponto:
    x0 = oddInt(r.randint(3, linhas-2))
    y0 = oddInt(r.randint(3, colunas-2))
    labirinto[x0][y0] = 0
    corredores.append((x0,y0))

    # Insere os quatro primeiros corredores em L:
    lista.append((x0-1, y0, x0-2, y0)) # Corredor de dois quadrados para cima.
    lista.append((x0, y0+1, x0, y0+2)) # Corredor de dois quadrados para a direita.
    lista.append((x0, y0-1, x0, y0-2)) # Corredor de dois quadrados para a esquerda.
    lista.append((x0+1, y0, x0+2, y0)) # Corredor de dois quadrados para baixo.

    # Gera os diversos caminhos do labirinto:
    while(len(lista) > 0):
        pontos = lista.pop(r.randrange(len(lista)))

        if(validarCorredor(matrizLabirinto, linhas, colunas, pontos) == True):
            labirinto[pontos[0]][pontos[1]] = 0
            labirinto[pontos[2]][pontos[3]] = 0
            corredores.append((pontos[0], pontos[1]))
            corredores.append((pontos[2], pontos[3]))
            
            x2 = pontos[2]
            y2 = pontos[3] 

            lista.append((x2-1, y2, x2-2, y2)) # Corredor de dois quadrados para cima.
            lista.append((x2, y2+1, x2, y2+2)) # Corredor de dois quadrados para a direita.
            lista.append((x2, y2-1, x2, y2-2)) # Corredor de dois quadrados para a esquerda.
            lista.append((x2+1, y2, x2+2, y2)) # Corredor de dois quadrados para baixo.