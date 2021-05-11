import matplotlib.pyplot as plt
import BioSist as bios 
import numpy as np 
import dados
import espaco_neutral as eN
import convergencia_redes as cR 

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

def gera_histograma_gene(gene):

	relacoes = relacoes_entre_genes(gene)
	from dados import ordem_genes as genes

	total = relacoes[0][0] + relacoes[1][0] + relacoes[2][0]
	inib = [x/total for x in relacoes[0]]
	nd = [x/total for x in relacoes[1]]
	atv = [x/total for x in relacoes[2]] 

	inibicao = plt.bar(genes, inib, width = 0.5, color = 'r')
	nada = plt.bar(genes, nd, width = 0.5, color = 'b', bottom = inib)
	ativacao = plt.bar(genes, atv, width = 0.5, color = 'g', bottom = np.array(inib) + np.array(nd))
	plt.title(f'{genes[gene]}')
	plt.show()


#distribuicao das entropias

def distribuicao_entropias():

	entropias = eN.entropia_bacias(eN.linhas)
	plt.hist(entropias)
	plt.title('Distribuição das Entropias das bacias (d = 1)')
	plt.show()


#distribuicao dos W


def W_possiveis(linhas_possiveis):

	trns = bios.gera_transicoes(dados.matriz_wildtype)
	lista_WT = dados.lista_adj_WT
	W = [cR.cal_W_total(lista_WT)]

	for i in range(0, 11):

		for linha in linhas_possiveis[i]:

			n_trns = bios.altera_transicoes(dados.matriz_wildtype, linha, i, trns)
			n_lista = bios.lista_adjacencia(n_trns)
			W.append(cR.cal_W_total(n_lista))

	return W

def distribuicao_W():

	W = W_possiveis(eN.linhas)
	plt.hist(W)
	plt.title("Distribuição dos W (d = 1)")
	plt.show()


distribuicao_entropias()
distribuicao_W()

