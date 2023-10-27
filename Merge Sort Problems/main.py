#Code Functions:

def merge(esquerda, direita):
	vetorFinal = []
	i = 0
	j = 0
	while(i < len(esquerda) and j < len(direita)):
		if(esquerda[i] < direita[j]):
			vetorFinal.append(esquerda[i])
			i += 1
		else:
			vetorFinal.append(direita[j])
			j += 1
		
	while(i < len(esquerda)):
		vetorFinal.append(esquerda[i])
		i += 1	
	while(j < len(direita)):
		vetorFinal.append(direita[j])
		j += 1
			
	return vetorFinal


def mergeSort(vetor): 
	if(len(vetor) > 1):
		meio = len(vetor)//2
		esquerda = mergeSort(vetor[:meio])
		direita = mergeSort(vetor[meio:])
		vetor = merge(esquerda, direita)
	return vetor
	

# Code Classes:
class ponto:
	def __init__(self, x, y):
		self.x = x
		self.y = y
	
	def __repr__(self):
		return str(self.x) + ' ' + str(self.y)

	def __lt__(self, outro):
		if(((self.x**2 + self.y**2)**(1/2)) == ((outro.x**2 + outro.y**2)**(1/2))):
			if(self.x == outro.x):
				return self.y < outro.y
			else:
				return self.x < outro.x
			
		return (self.x**2 + self.y**2)**(1/2) < (outro.x**2 + outro.y**2)**(1/2)
	
# Code Main:
def main():
    entrada = eval(input())

    pontos = []
    for item in entrada:
        pontos.append(ponto(item[0], item[1]))
        
    pontosOrdenados = mergeSort(pontos)
    for i in pontosOrdenados:
        print(i)
        
main()
	
	
					  