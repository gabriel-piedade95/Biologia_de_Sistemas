import operator as op
import itertools as iter
import numpy as np

def seleciona_inequacao(est1, est2):

  if est1 == 1:
    if est2 == 0:
      return op.lt
    elif est2 == 1:
      return  op.ge

  elif est1 == 0:
    if est2 == 0:
      return op.le
    elif est2 == 1:
      return  op.gt

def inequacoes(estados):
  
  ineqs = {}
  for i in range(0, 11):
    
    aux = []
    for j in range(0, len(estados) -1):
      aux.append(seleciona_inequacao(estados[j][i], estados[j + 1][i]))
  
    ineqs[i] = aux

  return ineqs

def resolve_CSP(estados, linhas = None):
  
  if linhas == None:
    linhas_possiveis = list(iter.product([-1, 0, 1], repeat=11))
  else:
    linhas_possiveis = linhas
    
  ineqs = inequacoes(estados)
  resultados = {}
  for i in range(0, len(ineqs)):
    restricoes = ineqs[i]
    resultados[i] = []
    for linha in linhas_possiveis:
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


def imprime_solucoes(solucoes):

  for gene in range(0, len(solucoes)):
    s = solucoes[gene]
    with open(f'gene{gene}.txt', 'w', encoding= 'utf-8') as f:
      for linha in range(0, len(s)):
        l = s[linha]
        for j in range(0, len(l)):
          f.write(str(l[j]) + ' ')
        f.write('\n')