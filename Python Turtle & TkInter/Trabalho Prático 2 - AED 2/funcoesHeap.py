def minHeapify(vetor, index, size):
	left = 2 * index + 1 #Left Index of the Root
	right = 2 * index + 2 #Right Index of the Root	
	smallest = index #Right Index of the Local Heap

	if(left < len(vetor) and vetor[left] < vetor[smallest]):
		smallest = left
		
	if(right < len(vetor) and vetor[right] < vetor[smallest]):
		smallest = right
		
	if(smallest != index):
		vetor[smallest], vetor[index] = vetor[index], vetor[smallest]
		minHeapify(vetor, smallest, size)

def montarHeap(vetor):
	for i in range(len(vetor)-1, -1, -1):
		minHeapify(vetor, i, len(vetor))

def aumentarChave(heap, pos, novo):
	if(pos == len(heap)):
		heap.append(novo)
	else:
		heap[pos] = novo
	
	montarHeap(heap)
	