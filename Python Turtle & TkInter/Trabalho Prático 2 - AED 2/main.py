from algoritmosBusca import algoritmo_A_Estrela
from labirintos import imprimirLabirinto, geraLabirinto, gerarPontoDePartida, gerarSaidaLabirinto

def main():
    matrizLabirintoDeBools = [] # Matriz onde o labirinto será formado.
    linhas = 11
    colunas = 11
    
    corredores = [] # Carregará todos os corredores do labirinto.

    # São gerados o labirinto, o ponto de partida do COdibentinho e a saída do lugar:
    geraLabirinto(matrizLabirintoDeBools, linhas, colunas, corredores)
    p0 = gerarPontoDePartida(corredores)
    pF = gerarSaidaLabirinto(matrizLabirintoDeBools, linhas, colunas, corredores)

    # Impressão do Labirinto Completo:
    imprimirLabirinto(matrizLabirintoDeBools, linhas, colunas)
    print()

    # Impressão do Caminho do ponto p0 até o ponto pF:
    print("Caminho ate a saida:")
    print(algoritmo_A_Estrela(p0, pF, matrizLabirintoDeBools)) # Se não ouver caminho, 
                                                               # uma string será retornada da função "algoritmo_A_Estrela"...

main()