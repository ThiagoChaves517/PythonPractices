# Função de Rotação da Direita para a Esquerda:
def rotacaoLL(arv):
	if(arv is not None and arv['esq']):
		arvNova = arv['esq']
		arvTemp = arvNova['dir']
		
		arvNova['dir'] = arv
		arv['esq'] = arvTemp
			
		return arvNova
	
	else:
		return arv

# Função de Rotação da Esquerda para a Direita:
def rotacaoRR(arv):
	if(arv is not None):
		arvNova = arv['dir']
		arvTemp = arvNova['esq']
		
		arvNova['esq'] = arv
		arv['dir'] = arvTemp
			
		return arvNova
	
	else:
		return arv


# Calcula a altura de um nodo da árvore:
def alturaArvore(arv):
	if(arv is not None):
		alturaArvoreEsq = alturaArvore(arv['esq'])
		alturaArvoreDir = alturaArvore(arv['dir'])
		
		return 1 + max(alturaArvoreEsq, alturaArvoreDir) 
	
	else:
		return 0
	
# Calcula o fator de balanceamento de um nodo da arvore:
def fator_B_Arvore(arv):
	if(arv is not None):
		alturaArvoreEsq = alturaArvore(arv['esq'])
		alturaArvoreDir = alturaArvore(arv['dir'])
		
		if(alturaArvoreEsq > alturaArvoreDir):
			return alturaArvoreDir-alturaArvoreEsq
		if(alturaArvoreEsq < alturaArvoreDir):
			return alturaArvoreDir-alturaArvoreEsq

	return 0

# Função que insere em um novo nodo na árvore:
def inserirArvore(arv, num):
	if(arv is None):
		return {'valor': num, 'esq': None, 'dir': None, 'h': 1}
	else:
		if(arv['valor'] < num):
			arv['dir'] = inserirArvore(arv['dir'], num)
			
		else:
			arv['esq'] = inserirArvore(arv['esq'], num)
	
	fatorB = alturaArvore(arv['esq']) - alturaArvore(arv['dir'])
	while(fatorB < -1 or fatorB > 1):
		#Rotações Duplas:
		if(fatorB < -1 and alturaArvore(arv['dir']['esq']) - alturaArvore(arv['dir']['dir']) > 0):
			arv['dir'] = rotacaoLL(arv['dir'])
			arv = rotacaoRR(arv)
			
		if(fatorB > 1 and alturaArvore(arv['esq']['dir']) - alturaArvore(arv['esq']['esq']) > 0):
			arv['esq'] = rotacaoRR(arv['esq'])
			arv = rotacaoLL(arv)
		
		#Rotações Simples:
		if(fatorB < -1):
			arv = rotacaoRR(arv)
		if(fatorB > 1):
			arv = rotacaoLL(arv)
		
		fatorB = alturaArvore(arv['esq']) - alturaArvore(arv['dir'])
		
	arv['h'] = alturaArvore(arv)
		
	return arv

# Função que reavalia a altura de cada nodo da árvore:
def reverAlturaArvore(arv):
	if(arv is not None):
		arv['h'] = alturaArvore(arv)
		reverAlturaArvore(arv['esq'])
		reverAlturaArvore(arv['dir'])

# Função que imprime a árvore em Pre-Ordem:
def imprimirArvore_PreOrdem(arv):
	if(arv is not None):
		print(arv['valor'], end=' ')
		imprimirArvore_PreOrdem(arv['esq'])
		imprimirArvore_PreOrdem(arv['dir'])
		
# Função que imprime a árvore em Pos-Ordem:
def imprimirArvore_PosOrdem(arv):
	if(arv is not None):
		imprimirArvore_PosOrdem(arv['esq'])
		imprimirArvore_PosOrdem(arv['dir'])
		print(arv['valor'], end=' ')

# Main do Código:
def main():
	arvore = None
	vetor = eval(input())
	counter = 1
	altura = 0
	fatorB = 0
	
	while(vetor != []):
		for i in vetor:
			arvore = inserirArvore(arvore, i)
			
		reverAlturaArvore(arvore)
		altura = alturaArvore(arvore) # Opcional
		fatorB = fator_B_Arvore(arvore) # Opcional
		
		print('Arvore ' + str(counter))
		print('pre: ', end=' ')
		imprimirArvore_PreOrdem(arvore)
		print()
		print('pos: ', end=' ')
		imprimirArvore_PosOrdem(arvore)
		print()
		
		arvore = None
		vetor = eval(input())
		counter += 1
		print()
	
main()