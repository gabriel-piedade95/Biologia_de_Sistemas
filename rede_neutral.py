import dados
import BioSist as bios 
import convergencia_redes as cR
import math 
import random as rand


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

### Algoritmo Genetico ###


# Cria Populacao #

def varia_gene(mtz, gene):

	var = []

	linhas_gene = bios.abre_arquivo(f'gene{gene}.txt')

	for i in range(0, len(linhas_gene)):

		if distanciaHamming(mtz[i], linhas_gene[j]):

			nova_matriz = mtz.copy()
			nova_matriz[i] = linhas_gene[j]
			var.append(nova_matriz)

	return var

def cria_populacao(mtz):
	
	pop = []

	for i in range(0, 11):

		
		pop.append(varia_gene(mtz, i))


	return pop

# Selecao #

def evento_selecao(mtz, pop, limiar):

	h, w = calculos_matriz(mtz)
	selecionados = [0] * 11

	for i in range(0, 11):

		pop_gene = pop[i]
		aux = []
		for j in range(0, len(pop_gene)):
			h_j, w_j = calculos_matriz(pop_gene[j])
			
			if limiar >= dist_Q(h, w, h_j, w_j):
				aux.append(pop_gene[j])

		selecionados[i] = aux

	return selecionados
		
# Reproducao #

def recombinacao(mtz_1, mtz_2):

	corte = rand.randint(0, 11)
	return mtz_1[:corte] + mtz_2[corte:]


def sorteia_reprodutores(pop):

	gene_1, gene_2 = rand.sample(range(0, 11), 2)
	tam_1 = len(pop[gene_1])
	tam_2 = len(pop[gene_2])
	rep_1 = pop[gene_1][rand.randint(0, tam_1)]
	rep_2 = pop[gene_2][rand.randint(0, tam_2)]

	return rep_1, rep_2

# Mutacao #

def sorteia_individuos(pop, parcela):

	tam = 0
	for i in range(0, 11):
		tam += len(pop[i])

	n_parcela = int(tam*parcela)
	individuos = []




# Geracoes #


def roda_geracoes(n, mtz):

	pop = cria_populacao(mtz)

	pass
