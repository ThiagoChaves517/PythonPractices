# Funções do Arquivo:

# Ordena uma lista de números -> Melhor Caso: O(n) / Pior Caso: O(n^2)
def bubbleSort(v):
	for i in range(len(v)-1, 0, -1):
		for j in range(i):
			if v[j] > v[j+1]:
				v[j], v[j+1] = v[j+1], v[j]
				
	return v

# Coleta item que está no meio de uma lista de inteiros -> Complexidade: O(1)
def middleIndex_List(v):
	if len(v) == 1: 
		return v[0]
	
	return len(v)//2

#-------------------------------------------------------------------------------------#

# Função Main():
lista = []
lista = eval(input())

while lista != []:
	somaDasDistancias = 0
	if len(lista) > 1:
		lista = bubbleSort(lista)

		casaDoMeioIndex = middleIndex_List(lista)

		for i in range(len(lista)):
			if lista[i] != lista[casaDoMeioIndex]:
				somaDasDistancias = somaDasDistancias + abs(lista[casaDoMeioIndex] - lista[i])
			
	print(somaDasDistancias)
	lista = eval(input())
	
	
	
	