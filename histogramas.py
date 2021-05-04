import matplotlib.pyplot as plt
import BioSist as bios 
import numpy as np 

def relacoes_entre_genes(gene):

	linhas = bios.abre_arquivo(f'gene{gene}.txt')
	inibicao = [0] * 11
	nada = [0] * 11
	ativacao = [0] * 11
	
	for i in range(0, len(linhas)):

		for j in range(0, len(linhas[i])):

			if linhas[i][j] == -1:
				inibicao[j] += 1

			if linhas[i][j] == 0:
				nada[j] += 1

			if linhas[i][j] == 1:
				ativacao[j] += 1

	return (inibicao, nada, ativacao)

def gera_histograma_gene(relacoes):

	from dados import ordem_genes as genes
	total = relacoes[0][0] + relacoes[1][0] + relacoes[2][0]
	inib = [x/total for x in relacoes[0]]
	nd = [x/total for x in relacoes[1]]
	atv = [x/total for x in relacoes[2]] 

	inibicao = plt.bar(genes, inib, width = 0.5, color = 'r')
	nada = plt.bar(genes, nd, width = 0.5, color = 'b', bottom = inib)
	ativacao = plt.bar(genes, atv, width = 0.5, color = 'g', bottom = np.array(inib) + np.array(nd))

	plt.show()

relacoes = relacoes_entre_genes(0)
gera_histograma_gene(relacoes)