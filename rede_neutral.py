import dados
import BioSist as bios 
import convergencia_redes as cR
import math 
import random as rand
import networkx as nx
import matplotlib.pyplot as plt

### Calculos ###

def distanciaHamming(linha_matriz, linha_possivel):

	a = 0
	for i in range(0, len(linha_matriz)):

		if linha_matriz[i] != linha_possivel[i]:
			a += 1

	return a == 1


def calculos_matriz(mtz):

	trns = bios.gera_transicoes(mtz)
	lista_transicoes = bios.lista_adjacencia(trns)
	bacias = bios.bacias(lista_transicoes)

	H = bios.entropia(bacias)
	W = cR.cal_W_total(lista_transicoes)

	return H, W

def dist_Q(h1, w1, h2, w2):

	h = abs(h1 - h2)
	w = abs(w1 - w2)
	Q = math.sqrt((h**2) + (w**2))


	return Q 



### Stringfica ###

def stringfica_rede(mtz):

	aux = []
	for i in range(0, len(mtz)):

		linhas_possiveis = bios.abre_arquivo(f'gene{i}.txt')

		for j in range(0, len(linhas_possiveis)):

			if linhas_possiveis[j] == mtz[i]:
				aux.append(j)
				break

	return '-'.join(str(x) for x in aux)

def matriz_da_string(string):

	aux = [int(x) for x in string.split('-')]
	matriz = []
	for i in range(0, 11):
		linhas = bios.abre_arquivo(f'gene{i}.txt')
		linha = linhas[aux[i]]
		matriz.append(linha)

	return matriz

### Random Walks ###

def randomwalk_grafo(mtz, passos):
	
	posicao = stringfica_rede(mtz)
	caminho = [posicao]
	rede = mtz.copy()

	i = 0

	while i < passos:
	
		gene = rand.randint(0, 10)
		linhas = bios.abre_arquivo(f'gene{gene}.txt')
		aux = []

		for j in range(0, len(linhas)):

			if distanciaHamming(rede[gene], linhas[j]):
				aux.append(linhas[j])

		n = rand.randint(0, len(aux) - 1)
		nova_rede = rede.copy()
		nova_rede[gene] = aux[n]

		nova_posicao = stringfica_rede(nova_rede)

		if nova_posicao not in caminho:

			caminho.append(nova_posicao)
			rede = nova_rede
			i += 1

	return caminho


def imprime_randomwalk(caminho, n):

	with open(f'randomwalk_{n}.txt', 'w', encoding = 'utf-8') as f:

		for i in range(0, len(caminho)):

			for j in range(0, len(caminho[i])):

				f.write(caminho[i][j])
			f.write('\n')

### Imprime Grafo Neutral ###


def le_arquivo_rdn_wlk(n):

	caminho = []
	with open(f'randomwalk_{n}.txt', 'r', encoding = 'utf-8') as f:
		for linha in f:
			caminho.append(linha[:-1])

	return caminho

def gera_grafo(caminho):

	trns = []
	for i in range(0, len(caminho) - 1):

		trns.append((caminho[i + 1], caminho[i]))

	return trns 

def imprime_grafo(transicoes):

	G = nx.DiGraph()
	G.add_edges_from(transicoes)
	pos = nx.spring_layout(G)
	plt.figure(3, figsize = (14, 10))
	nx.draw_networkx_nodes(G, pos, node_size = 100)
	nx.draw_networkx_edges(G, pos, arrows = True)
	plt.show()


caminho = le_arquivo_rdn_wlk(2)
trns = gera_grafo(caminho) 
imprime_grafo(trns)














