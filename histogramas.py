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

	genes = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

	inibicao = plt.bar(genes, relacoes[0], width = 0.5, color = 'r')
	nada = plt.bar(genes, relacoes[1], width = 0.5, color = 'b', bottom = relacoes[0])
	ativacao = plt.bar(genes, relacoes[2], width = 0.5, color = 'g', bottom = np.array(relacoes[0]) + np.array(relacoes[1]))

	plt.show()

relacoes = relacoes_entre_genes(0)
gera_histograma_gene(relacoes)