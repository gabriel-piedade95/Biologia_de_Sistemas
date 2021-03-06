from dados import matriz_wildtype as mtz 
from dados import estados
import BioSist as bios 
import matplotlib.pyplot as plt
import Inferencia_Redes as iR 
import numpy as np
import networkx as nx


#gera as bacias WT e cria uma lista das entropias

def linhas_uma_diferenca(mtz):

	linhas_possiveis = {}
	d = [-1, 0, 1]

	for linha in range(0, 11):

		linha_aux = mtz[linha].copy()
		aux = []
		for coluna in range(0, 11):

			for i in d:
				if i != linha_aux[coluna]:

					nova_linha = linha_aux.copy()
					nova_linha[coluna] = i
					aux.append(nova_linha)

		linhas_possiveis[linha] = aux

	return linhas_possiveis

def seleciona_linhas_uma_diferenca(estados, linhas):

	ineqs = iR.inequacoes(estados)
	resultados = {}

	for i in range(0, len(ineqs)):
	    restricoes = ineqs[i]
	    resultados[i] = []
	    for linha in linhas[i]:
	      aux = [False] * len(restricoes)
	      for r in range(0, len(restricoes)):
	        prod = np.array(linha.copy()) * np.array(estados[r])  
	        if restricoes[r](sum(prod), 0):
	          aux[r] = True
	        else:
	          break
	      if all(aux):
	        resultados[i].append(linha)
  
	return resultados


def entropia_bacias(linhas_possiveis):
	
	trns = bios.gera_transicoes(mtz)
	lista_trns = bios.lista_adjacencia(trns)
	bacias_WT = bios.bacias(lista_trns)
	H_wt = bios.entropia(bacias_WT)
	H = [H_wt]
	for i in range(0, 11):

		for linha_possivel in linhas_possiveis[i]:
			n_trns = bios.altera_transicoes(mtz, linha_possivel, i, trns)
			n_lista = bios.lista_adjacencia(n_trns)
			n_bacias = bios.bacias(n_lista)
			H.append(bios.entropia(n_bacias))

	return H


def diferencas_entropia(entropias, limiar):
	
	return [(x, entropias[0]) for x in entropias if abs(entropias[0] - x) <= limiar]


def imprime_grafo(transicoes):


	G = nx.DiGraph()
	G.add_edges_from(transicoes)
	pos = nx.spring_layout(G)
	plt.figure(3, figsize = (14, 10))
	nx.draw_networkx_nodes(G, pos, node_size = 100)
	nx.draw_networkx_edges(G, pos, arrows = True)
	plt.show()


l = linhas_uma_diferenca(mtz)
linhas = seleciona_linhas_uma_diferenca(estados, l)








