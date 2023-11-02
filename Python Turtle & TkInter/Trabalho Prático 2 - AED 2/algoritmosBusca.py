from funcoesHeap import aumentarChave as heapPush

def gerarEstadoInicial(x, y):
    tupla = (x, y)
    
    return tupla

def criarTransicoes(estadoInicial, matrizLabirinto):
    estadosEscolhidos = []

    if(estadoInicial[0] > 0 and matrizLabirinto[estadoInicial[0]-1][estadoInicial[1]] == False): # Is there sea in North?
        estadosEscolhidos.append((estadoInicial[0]-1, estadoInicial[1]))

    if(estadoInicial[1] < len(matrizLabirinto[0])-1 and matrizLabirinto[estadoInicial[0]][estadoInicial[1]+1] == False): # Is there sea in East?
        estadosEscolhidos.append((estadoInicial[0], estadoInicial[1]+1))

    if(estadoInicial[1]  > 0 and matrizLabirinto[estadoInicial[0]][estadoInicial[1]-1] == False): # Is there sea in West?
        estadosEscolhidos.append((estadoInicial[0], estadoInicial[1]-1))
    
    if(estadoInicial[0] < len(matrizLabirinto)-1 and matrizLabirinto[estadoInicial[0]+1][estadoInicial[1]] == False): # Is there sea in South?
        estadosEscolhidos.append((estadoInicial[0]+1, estadoInicial[1]))

    matrizLabirinto[estadoInicial[0]][estadoInicial[1]] = True

    return estadosEscolhidos

def calcularCusto(estado, estadoFinal):
    # Esta é uma função heurística simples que calcula a distância de Manhattan até o estado final
    return abs(estado[0] - estadoFinal[0]) + abs(estado[1] - estadoFinal[1])

def algoritmo_A_Estrela(estadoInicial, estadoFinal, matrizLabirintoDeBools): # Sendo estadoInicial e estadoFinal tuplas.
    agendaDePrioridades = []
    estadosPassados = set()
    predecessores = {}  # Dicionário para rastrear o caminho
    g = {estadoInicial: 0}  # Custos acumulados para chegar a cada estado

    heapPush(agendaDePrioridades, 0, (calcularCusto(estadoInicial, estadoFinal), estadoInicial))
    estadosPassados.add(estadoInicial)

    while (len(agendaDePrioridades) > 0):
        lixeira, estado = agendaDePrioridades.pop(0)  # Ignora o primeiro elemento da tupla, que é o custo total da caminhada até o momento

        if (estado == estadoFinal):
            caminho = []
            while estado is not None:
                caminho.append(estado)
                estado = predecessores.get(estado)  # Volta ao predecessor deste estado
            caminho.reverse()  # Inverte o caminho para começar do início
            return caminho  # Retorna o caminho completo

        transicoesDoEstado = criarTransicoes(estado, matrizLabirintoDeBools)

        for transicao in transicoesDoEstado:
            proximoEstado = transicao
            novoCusto = g[estado] + 1  # Supõe-se que o custo para mover-se entre quaisquer dois estados adjacentes seja 1

            if ( (proximoEstado not in estadosPassados) or (novoCusto < g.get(proximoEstado, float('inf'))) ): #get() retorna g[proximoEstado] no caso dele já existir em g. 
                                                                                                         #Se não estiver, retorna infinito, pois "proximoEstado" ainda não foi explorado.
                g[proximoEstado] = novoCusto
                f = novoCusto + calcularCusto(proximoEstado, estadoFinal)
                heapPush(agendaDePrioridades, 0, (f, proximoEstado))
                predecessores[proximoEstado] = estado
                estadosPassados.add(proximoEstado)

    return None

#----------------------------------------------------------------------------------------------------

'''

Versão #2

def algoritmo_A_Estrela(estadoInicial, estadoFinal, matrizLabirintoDeBools):
    agendaDePrioridades = []
    estadosPassados = set()
    predecessores = {}  # Dicionário para rastrear o caminho
    
    aumentarChave(agendaDePrioridades, 0, estadoInicial)
    estadosPassados.add(estadoInicial)

    while len(agendaDePrioridades) > 0:
        
        estado = agendaDePrioridades.pop(0)  
        
        if (estado == estadoFinal):
            caminho = []
            while estado is not None:
                caminho.append(estado)
                estado = predecessores.get(estado)  # Volta ao predecessor deste estado
            caminho.reverse()  # Inverte o caminho para começar do início
            return caminho  # Retorna o caminho completo
        
        transicoesDoEstado = criarTransicoes(estado, matrizLabirintoDeBools)
        
        for transicao in transicoesDoEstado:     
            proximoEstado = transicao 
            if proximoEstado not in estadosPassados:
                predecessores[proximoEstado] = estado  # Define o estado atual como predecessor do próximo estado
                aumentarChave(agendaDePrioridades, 0, proximoEstado) 
                estadosPassados.add(proximoEstado) 
    
    return None

'''
    

'''

Versão #1

def algoritmo_A_Estrela(estadoInicial, estadoFinal, matrizLabirintoDeBools):
    agendaDePrioridades = []
    estadosPassados = set()
    caminhoParaSaida = []
    
    aumentarChave(agendaDePrioridades, 0, estadoInicial)
    estadosPassados.add(estadoInicial)

    while len(agendaDePrioridades) > 0:
        
        estado = agendaDePrioridades.pop(0)  #agenda.retiraPrimeiro()
        
        if (estado == estadoFinal):
            return estado
        
        transicoesDoEstado = criarTransicoes(estado, matrizLabirintoDeBools)
        
        for transicao in transicoesDoEstado:     #para cada transição válida a partir de estado, faça
            proximoEstado = transicao #estado gerado a partir dessa transição
            if proximoEstado not in estadosPassados:
                aumentarChave(agendaDePrioridades, 0, proximoEstado) #agenda.insere(próximo)
                estadosPassados.add(proximoEstado) #estadosPassados.insere(próximo)
    
    return None
'''