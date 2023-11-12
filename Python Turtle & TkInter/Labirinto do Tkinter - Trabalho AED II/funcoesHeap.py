# Localiza o noh pai de uma chave filha, sendo "pos" o indíce em que o filho se encontra.
def nohPaiIndex(pos):
    return (pos - 1) // 2

# Substitui uma chave atual por uma nova chave, e coloca esta no lugar certo da heap no final.
def aumentarChave(heap, pos, novaChave):    
    heap[pos] = novaChave
    
    while pos > 0 and heap[nohPaiIndex(pos)] > heap[pos]:
        heap[pos], heap[nohPaiIndex(pos)] = heap[nohPaiIndex(pos)], heap[pos]
        pos = nohPaiIndex(pos)

