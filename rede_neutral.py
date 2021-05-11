import itertools as iter 
import dados
import BioSist as bios 


mtz = dados.matriz_wildtype

dic_poss = {-1: [-1], 0: [0], 1: [1], -2: [-1, 0], 2: [0, 1], 3: [-1, 1], 5: [-1, 0, 1]}
l = [5, 5, 5, 5, 5]


def distribuicao_distancia_Hamming(mtz, n):

  dic_poss = {-1: [-1], 0: [0], 1: [1], -2: [-1, 0], 2: [0, 1], 3: [-1, 1], 5: [-1, 0, 1]}
  tam = len(mtz)
  mtz_linha = np.matrix(mtz).reshape(1, tam**2)
  soma = 0
  for combinacao in iter.combinations(mtz_linha.tolist()[0], n):
    prod = 1
    for i in range(0, len(combinacao)):

      prod *= (len(dic_poss[combinacao[i]]) - 1)
    
    soma += prod

  return soma
