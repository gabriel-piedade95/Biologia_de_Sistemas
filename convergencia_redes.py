

def _cal_T_estados(lista, est_ant):

	if est_ant == lista[est_ant]:
		return 0

	if est_ant not in lista:
		return 1

	anteriores = []
	for k in range(0,  len(lista)):
		if lista[k] == est_ant and k != est_ant:
			anteriores.append(k)

	n = 1
	for i in range(0, len(anteriores)):
		n += _cal_T_estados(lista, anteriores[i])

	return n

def cal_T(lista):

	T = [0] * len(lista)
	for i in range(0, len(lista)):
		T[i] = _cal_T_estados(lista, i)

	return T

def _cal_L_estados(lista, est_ant):

	prox_est = lista[est_ant]
	if est_ant == prox_est:

		return 0

	if lista[prox_est] == prox_est:

		return 1

	return 1 + _cal_L_estados(lista, prox_est)


def cal_L(lista):

	L = [0] * len(lista)
	for i in range(0, len(lista)):
		L[i] = _cal_L_estados(lista, i)

	return L 


def _caminho_atrator(lista, est_ant):

	prox_est = lista[est_ant]
	if est_ant == prox_est:
		return 

	if lista[prox_est] == prox_est:
		return [est_ant]

	return [est_ant] + _caminho_atrator(lista, prox_est)


def cal_w(lista):

	w = [0] * len(lista)
	L = cal_L(lista)
	T = cal_T(lista)

	for i in range(0, len(lista)):

		somatorio_w = 0
		caminho = _caminho_atrator(lista, i)
		if L[i] != 0 and caminho != None:
			
			for estado in caminho:
				somatorio_w += T[estado]

			w[i] = somatorio_w/L[i]


	return w


def cal_W_total(lista):

	return sum(cal_w(lista))/len(lista)


