import csv
from classes import BailOut

def gerador():
	for i in range (10):
		yield i * 2 #cada posicao do retorno

def init():
	# write stocks data as comma-separated values
	writer = csv.writer(open('stocks.csv', 'wb', buffering=0))
	writer.writerows([
		('GOOG', 'Google, Inc.', 505.24, 0.47, 0.09),
		('YHOO', 'Yahoo! Inc.', 27.38, 0.33, 1.22),
		('CNET', 'CNET Networks, Inc.', 8.62, -0.13, -1.49)
	])

	# read stocks data, print status messages
	stocks = csv.reader(open('stocks.csv', 'rb'))
	status_labels = {-1: 'down', 0: 'unchanged', 1: 'up'}

	for ticker, name, price, change, pct in stocks:
		
		#cmp retorna -1 se float(change) < 0.0,
		#0 se float(change) == 0.0 e
		#1 se float(change) > 0.0
		status = status_labels[cmp(float(change), 0.0)]
		print '%s is %s (%s%%)' % (name, status, pct)
		

	coiso = [1,2,3,4,5,6]
	for val1 in reversed(coiso):
		print val1
		
	val1, val2 = 1,2

	if val1 in (2,3,4):
		print 'ta la!'
	else:
		print 'nao ta la'
		
	matriz = [[1,2,3],[4,5,6],[7,8,9]]

	for tupla in matriz:
		for valor in tupla:
			#a virgula evita printar nova linha
			print str(valor) + ' ',
		print

	print range(4,8)

	#guarda valores quando precisa (?)
	ranginho = xrange(4,8)

	for valor in ranginho:
		print str(valor)

	arrayzinho = [1,2,3,4,5,6,7,8,9,10]

	print [n for n in arrayzinho if n % 2 == 0]		


	gerador = (letra for letra in 'poodle')

	print gerador.next()	

	for letra in gerador:
		print letra

if __name__ == '__main__':
	
	init()
	gera = gerador()
	print gera
	for i in gera:
		print i
		
	try:
		coiso = 1/0;
	except BailOut:
		pass
