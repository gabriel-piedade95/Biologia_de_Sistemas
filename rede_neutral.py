import itertools as iter 
import dados
import BioSist as bios 
import histogramas as hist 
import convergencia_redes as cR
import math 


global h_WT, w_WT, mtz_WT
mtz_WT = dados.matriz_wildtype
h_WT, w_WT = calculos_matriz(mtz_WT)


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

def Q(limiar, H, W):

	dif_H = abs(H - h_WT)
	dif_W = abs(W - w_WT)
	D = math.sqrt((dif_W**2) + (dif_H**2))
	return D == limiar


mtz = dados.matriz_wildtype
linhas_possiveis = [0] * 11

for i in range(0, 11):
	
	linhas_genes = bios.abre_arquivo(f'gene{i}.txt')
	aux = []

	for j in range(0, len(linhas_genes)):

		if distanciaHamming(linhas_genes[j], mtz[i]):
			aux.append(linhas_genes[j])

	linhas_possiveis[i] = aux


Hs = []
Ws = []

for i in range(0, 11):

	for linha in linhas_possiveis[i]:

		nova_matriz = mtz_WT.copy()
		nova_matriz[i] = linha
		h, w = calculos_matriz(nova_matriz)
		Hs.append(h)
		Ws.append(w)


import matplotlib.pyplot as plt


plt.scatter(Hs, Ws, color = 'green')
plt.title('Gráfico Entropia(H) por Convergência(W)')
plt.xlabel('Entropia(H)')
plt.ylabel('Convergência(W)')
plt.scatter(h_WT, w_WT, color = 'red')
plt.show()




