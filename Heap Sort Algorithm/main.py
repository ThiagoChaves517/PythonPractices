# Code Functions:

def max_heapify(vetor, index, size): # This function transforms a small tree into a max heap,
	left = 2 * index + 1             # determing the sorting order as ascending
	right = 2 * index + 2
	greatest = index
	
	if(left < size and vetor[left] > vetor[greatest]):
		greatest = left
		
	if(right < size and vetor[right] > vetor[greatest]):
		greatest = right
	
	if(greatest != index):
		vetor[greatest], vetor[index] = vetor[index], vetor[greatest]
		max_heapify(vetor, greatest, size)

def montar_heap(vetor): # This function transform all the sub trees in heaps, making the vector a complete heap.
	for i in range(len(vetor)-1, -1, -1):
		max_heapify(vetor, i, len(vetor))

def heap_sort(vetor):       # This function depends on the type of heapify the function montar_heap uses... 
	montar_heap(vetor)      # (which is max_heapify in that case).
	                        # It gradually transforms the heap made into a sorted array.
	vectorSize = len(vetor)
	while(vectorSize > 1):
		#Step 1:
		vetor[0], vetor[vectorSize-1] = vetor[vectorSize-1], vetor[0]
		
		#Step 2:
		vectorSize -= 1
		
		#Step 3:
		max_heapify(vetor, 0, vectorSize)
		

# Function Main:
def main():
	vetor = eval(input())
	while(vetor != []):
		heap_sort(vetor)
		print(vetor)
		vetor = eval(input())
	
main()