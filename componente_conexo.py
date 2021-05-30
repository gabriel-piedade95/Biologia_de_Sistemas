import rede_neutral as rN 
import BioSist as bios
import dados


def encontra_conexoes(mtz, lista):

	wt = [int(x) for x in rN.stringfica_rede(mtz).split('-')]
	dist = {}

	for i in range(0, len(lista)):

		nova_rede = [int(x) for x in lista[i].split('-')]
		d = 0

		for j in range(0, len(nova_rede)):

			nova_linha = bios.abre_arquivo(f'gene{j}.txt')[nova_rede[j]]

			for k in range(0, len(nova_linha)):

				if nova_linha[k] != mtz[j][k]:

					d += 1

		try:
			dist[d].append(lista[i])

		except KeyError:

			dist[d] = [lista[i]]

	return dist

mtz = dados.matriz_wildtype
caminho = rN.le_arquivo('heap_1')
dist = encontra_conexoes(mtz, caminho[:100])
for d in dist:
	print(d, len(dist[d]))