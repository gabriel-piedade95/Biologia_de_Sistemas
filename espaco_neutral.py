from dados import matriz_wildtype as mtz 
import BioSist as bios 

linhas = bios.seleciona_linhas(mtz)
trns = bios.gera_transicoes(mtz)
lista = bios.lista_adjacencia(trns)
bacias_WT = bios.bacias(lista)
H = [bios.entropia(bacias_WT)]

for i in range(0, 11):

	for linha_possivel in linhas[i]:
		n_trns = bios.altera_transicoes(mtz, linha_possivel, i, trns)
		n_lista = bios.lista_adjacencia(n_trns)
		n_bacias = bios.bacias(n_lista)
		H.append(bios.entropia(n_bacias))

print(H)
