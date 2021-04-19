class Noh:

	def __init__(self, conteudo):
		self.conteudo = conteudo
		self.prox = None
		self.ant = []

	def __repr__(self):
		return str(self.conteudo)

	def imprime_arvore(self, nivel = 0):
		print(f'{" " * nivel}- {self.conteudo}')
		if len(self.ant) !=0 :
			for i in self.ant:
				i.imprime_arvore(nivel + 1)


class Grafo:

	def __init__(self):
		self.raizes = []
		self.nohs = []


	def encontra_noh(self, conteudo):

		cont_nohs = [n.conteudo for n in self.nohs]
		if conteudo in cont_nohs:
			return self.nohs[cont_nohs.index(conteudo)]

		else:
			return False

	def adiciona_aresta(self, ant, prox):

		if not self.encontra_noh(ant):
			self.nohs.append(Noh(ant))

		if not self.encontra_noh(prox):
			self.nohs.append(Noh(prox))

		if ant != prox:
			
			noh_ant = self.encontra_noh(ant)
			prox_noh = self.encontra_noh(prox)

			noh_ant.prox = prox_noh
			prox_noh.ant.append(noh_ant)

		else:
			noh = self.encontra_noh(prox)
			noh.prox = None
			self.raizes.append(noh)

	def monta_grafo(self, lista):

		for i in range(0, len(lista)):

			self.adiciona_aresta(i, lista[i])

	def imprime_grafo(self):

		for arvore in self.raizes:
			arvore.imprime_arvore()
