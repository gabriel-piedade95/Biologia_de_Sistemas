import itertools as iter 
import dados
import BioSist as bios 


mtz = dados.matriz_wildtype

dic_poss = {-1: [-1], 0: [0], 1: [1], -2: [-1, 0], 2: [0, 1], 3: [-1, 1], 5: [-1, 0, 1]}
l = [5, 5, 5, 5, 5]


def linhas_com_distancia_n(linhas_possiveis, distancia):

	soma = 0
	for i in iter.combinations(linhas_possiveis, distancia):
		prod = 1
		for j in range(0, len(i)):
			prod *= (len(dic_poss[i[j]]) -1)
		soma += prod

	return soma

