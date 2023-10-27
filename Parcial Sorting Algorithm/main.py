#def selectionSort(v):
#	for i in range(len(v)):
#		menor = i
#		for j in range(i, len(v)-1, 1):
#			if(v[menor] > v[j+1]):
#				menor = j+1
#		v[menor], v[i] = v[i], v[menor]
		
#def insertionSort(v):
#	for i in range(len(v)):
#		j = i
#		while (j > 0 and v[j] < v[j-1]):
#			v[j], v[j-1] = v[j-1], v[j]
#			j = j-1

# Funções do Arquivo:

# Ordena uma lista até a posição k-1, mantendo a ordem relativa dos números restantes como a mesma -> Melhor Caso: O(n2) / Pior Caso: O(n^2)
def parcialSort(v,k): 
	try:
		listaCopia = []
		for i in range(len(v)):
			listaCopia.append(v[i])

		listaDosMenores = []
		for i in range(k):
			menor = i
			for j in range(i, len(v)-1, 1):
				if(v[menor] > v[j+1]):
					menor = j+1
			listaDosMenores.append(v[menor])
			v[menor], v[i] = v[i], v[menor]

		for i in range(len(listaCopia)):
			if(listaCopia[i] not in listaDosMenores):
				listaDosMenores.append(listaCopia[i])

		return listaDosMenores
	except IndexError:
		print('Erro: Lista acessada fora do intervalo proposto!')
	
#-------------------------------------------------------------------------------------#
		
# Função Main():

tamanhoLista = int(input())
tamanhoDaOrdenacao = int(input())
lista = eval(input())

lista = parcialSort(lista, tamanhoDaOrdenacao)

print(lista)

