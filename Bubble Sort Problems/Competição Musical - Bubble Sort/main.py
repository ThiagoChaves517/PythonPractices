# Classes do Arquivo:
class Contestant:
	# Constructor da Classe: 
	def __init__(self, nome, index, n1, n2, n3):
		self.nome = nome
		self.index = index
		if(min(n1, n2, n3) == n1):
			self.nota = n2 + n3
		elif(min(n1, n2, n3) == n2):
			self.nota = n1 + n3
		else:
			self.nota = n1 + n2
			
	# Métodos da Classe: 
	def __repr__(self):
		return self.nome + ': ' + str(self.nota)
	
	def __lt__(self, outro):
		if self.nota == outro.nota:
			return self.index > outro.index
		
		return self.nota < outro.nota
	
#-------------------------------------------------------------------------------------#

# Funções do Arquivo:
	
# Ordena uma lista de números -> Melhor Caso: O(n) / Pior Caso: O(n^2)
def bubbleSort(v):
	for i in range(len(v)-1, 0, -1):
		for j in range(0, i):
			if v[j] < v[j+1]:
				v[j], v[j+1] = v[j+1], v[j]
	return v

#-------------------------------------------------------------------------------------#

# Função Main():
num_contestants = int(input())		
placar = []

position_id = 0
for i in range(num_contestants):
	next_contestant = eval(input())  
	placar.append(Contestant(next_contestant[0], position_id, next_contestant[1], next_contestant[2], next_contestant[3]))
	position_id += 1
	
placar = bubbleSort(placar)

for i in range(num_contestants):
	print(placar[i])
			  