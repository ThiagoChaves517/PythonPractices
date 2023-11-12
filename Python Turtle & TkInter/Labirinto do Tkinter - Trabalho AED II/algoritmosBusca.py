# Biblioteca que utiliza as propriedades de uma heap.
from funcoesHeap import aumentarChave

# Esta função localiza os corredores mais próximos e acessíveis (os pontos que estão sinzalizados com 0):
def criarTransicoes(estadoInicial, matrizLabirinto):
    estadosEscolhidos = []

    # Devo ir pro Norte?
    if(estadoInicial[0] > 0 and matrizLabirinto[estadoInicial[0]-1][estadoInicial[1]] == 0):
        estadosEscolhidos.append((estadoInicial[0]-1, estadoInicial[1]))

    # Devo ir pro Leste?
    if(estadoInicial[1] < len(matrizLabirinto[0])-1 and matrizLabirinto[estadoInicial[0]][estadoInicial[1]+1] == 0):
        estadosEscolhidos.append((estadoInicial[0], estadoInicial[1]+1))

    # Devo ir pro Oeste?
    if(estadoInicial[1]  > 0 and matrizLabirinto[estadoInicial[0]][estadoInicial[1]-1] == 0):
        estadosEscolhidos.append((estadoInicial[0], estadoInicial[1]-1))
    
    # Devo ir pro Sul?
    if(estadoInicial[0] < len(matrizLabirinto)-1 and matrizLabirinto[estadoInicial[0]+1][estadoInicial[1]] == 0):
        estadosEscolhidos.append((estadoInicial[0]+1, estadoInicial[1]))
        
    return estadosEscolhidos


# Esta é uma função heurística simples que calcula a distância de Manhattan até o estado final,
# ou seja, a distância entre os pontos do estado atual e do estado final.
def calcularCusto(estado, estadoFinal):
    return abs(estado[0] - estadoFinal[0]) + abs(estado[1] - estadoFinal[1])


# Este algoritmo busca o caminho mais curto até a saída do labirinto:
def algoritmo_A_Estrela(estadoInicial, estadoFinal, matrizLabirintoDeBools): # Sendo estadoInicial e estadoFinal tuplas.
    agendaDePrioridades = []
    estadosPassados = set()
    predecessores = {}  # Dicionário para rastrear o caminho.
    g = {estadoInicial: 0}  # Custos acumulados para chegar a cada estado.

    agendaDePrioridades.append((-1, -1))
    aumentarChave(agendaDePrioridades, 0, (calcularCusto(estadoInicial, estadoFinal), estadoInicial))
    estadosPassados.add(estadoInicial)

    while (len(agendaDePrioridades) > 0):
        lixeira, estado = agendaDePrioridades.pop(0)  # Ignora o primeiro elemento da tupla, que é o custo total da caminhada até o momento.

        if (estado == estadoFinal):
            caminho = []
            while estado is not None:
                caminho.append(estado)
                estado = predecessores.get(estado)  # Volta ao predecessor deste estado.
            caminho.reverse()  # Inverte o caminho para começar do início.
            return caminho  # Retorna o caminho completo.

        transicoesDoEstado = criarTransicoes(estado, matrizLabirintoDeBools)

        for transicao in transicoesDoEstado:
            proximoEstado = transicao
            novoCusto = g[estado] + 1  # Supõe-se que o custo para mover-se entre quaisquer dois estados adjacentes seja 1.

            if ( (proximoEstado not in estadosPassados) or (novoCusto < g.get(proximoEstado, float('inf'))) ): #get() retorna g[proximoEstado] no caso dele já existir em g. 
                                                                                                         #Se não estiver, retorna infinito, pois "proximoEstado" ainda não foi explorado.
                g[proximoEstado] = novoCusto
                f = novoCusto + calcularCusto(proximoEstado, estadoFinal) # f = g + h
                agendaDePrioridades.append((-1, -1))
                aumentarChave(agendaDePrioridades, len(agendaDePrioridades)-1, (f, proximoEstado))
                predecessores[proximoEstado] = estado
                estadosPassados.add(proximoEstado)

    return (0,0)