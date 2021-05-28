import BioSist as bios
import rede_neutral as rN




### Algoritmo Genetico ###


# Cria Populacao #

def varia_gene(mtz, gene):

	var = []

	linhas_gene = bios.abre_arquivo(f'gene{gene}.txt')

	for i in range(0, len(linhas_gene)):

		if rN.distanciaHamming(mtz[i], linhas_gene[j]):

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

	h, w = rN.calculos_matriz(mtz)
	selecionados = [0] * 11

	for i in range(0, 11):

		pop_gene = pop[i]
		aux = []
		for j in range(0, len(pop_gene)):
			h_j, w_j = rN.calculos_matriz(pop_gene[j])
			
			if limiar >= rN.dist_Q(h, w, h_j, w_j):
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

def sorteia_individuo(pop):

	gene = rand.randint(0, 11)
	t = rand.randtint(0, len(pop[gene]))
	ind = pop[gene][t]

	return ind


	

# Geracoes #


def roda_geracoes(n, mtz):

	pop = cria_populacao(mtz)