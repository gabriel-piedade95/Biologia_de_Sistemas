import sympy as sym
import operator as op
import itertools as iter
import random as rand

## estados & matriz ##

def transforma_estados(estados):

	for i in range(0, len(estados)):

		estados[i] = sym.Matrix(estados[i])

	return estados

def cria_matriz(tam):

  mtx = []
  for i in range(0, tam):
    aux = []
    for j in range(0, tam):
      aux.append(sym.Symbol(f'A{i}{j}'))

    mtx.append(aux)

  return sym.Matrix(mtx)

## inequacoes ##

def gera_inequacoes(estados):

  resultados = []
  inequacoes = []

  for i in range(0, len(estados) - 1):
    res = cria_matriz(len(estados[i]))*estados[i]
    resultados.append(res) 


  for i in range(0, len(resultados)):
    for j in range(0, len(resultados[i])):
      inequacoes.append(seleciona_inequacao(resultados[i][j], estados[i][j], estados[i + 1][j]))

  return inequacoes

def gera_restricoes(estados):

  ineqs = gera_inequacoes(estados)
  restricoes = {}

  for i in range(0, len(estados[0])):
    aux = []
    for j in range(0, len(estados) - 1):
      aux.append(ineqs[(len(estados[i]) * j) + i])

    restricoes[i] = aux

  return restricoes


def seleciona_inequacao(ineq, est1, est2):

  if est1 == 1:
    if est2 == 0:
      return op.lt(ineq, 0)
    elif est2 == 1:
      return  op.ge(ineq, 0)

  elif est1 == 0:
    if est2 == 0:
      return op.le(ineq, 0)
    elif est2 == 1:
      return  op.gt(ineq, 0)


## estados ##

def gera_estados(dom):

  aux = [dom[x] for x in dom]

  for possibilidade in list(iter.product(*aux)):
    
    yield possibilidade

## Resolve CSP ##

def testa_resticao(rest, dom, estados):

  ineqs = list.copy(rest)
  for i in range(0, len(ineqs)):
    x = 0
    for var in dom:
      ineqs[i] = ineqs[i].subs(var, estados[x])
      x += 1
    if ineqs[i] == False:
      break

  return ineqs

def resolve_CSP(rest, dom):

  resultados = []
  estados = gera_estados(dom)
  while True:
    try:
      estado = next(estados)
      teste = testa_resticao(rest, dom, estado)
      if all(teste):
        resultados.append(estado)
      
    except StopIteration:
      break
  return resultados

def gera_linhas_possiveis(estados):

  estados =  transforma_estados(estados)
  mat = cria_matriz(len(estados[0]))
  restricoes = gera_restricoes(estados)
  for i in range(0, mat.shape[0]):
    var = mat.row(i)
    rest = restricoes[i]
    dom = {} 
    for k in var:
      dom[k] = (-1, 0, 1)

    with open(f'gene{i}.txt','w', encoding='utf-8') as f:
      for solucao in resolve_CSP(rest, dom):
        for est in solucao:
          f.write(str(est) + '  ')
        f.write('\n')