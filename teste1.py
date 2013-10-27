import re #regular expressions
import sys #tratamento de excecao
import glob #arquivos no linux

from time import localtime
from classes import ClasseFeliz
from itertools import groupby


def init():
	print 'hello world'
	
	name0 = 'poodle'
	#name1 = raw_input('Entre com um valor: \n')
	
	print 'Eu gosto muito do %s' % name0
	#print 'Eu gosto muito do %s' % name1
	
	friends = ['Igor', 'Jorge', 'Nina']
	
	""" iterador primeiro, string depois """
	for i, name in enumerate(friends):
		print 'iteration {iteration} is {name}'.format(iteration=i, name=name)

	coiso1, coiso2 = ('coiso1',3)
	
	print "coiso1: %s, coiso2: %d" % (coiso1, coiso2)
	
	print 'valor1: {0}, valor2: {1}'.format(coiso1,coiso2)
	
	for test_string in ['555-1212','ILL-EGAL']:
		if re.match(r'^\d{3}-\d{4}$',test_string):
			print test_string, 'eh um telefone valido'
		else:
			print test_string, 'nao eh um telefone valido'
	
	
	precos = {'maca':0.40, 'banana':0.50}
	minha_compra = {
		'maca':1,
		'banana':6
	}
	
	fatura_mercearia = sum(precos[fruta] * minha_compra[fruta]
							for fruta in minha_compra)
							
	print 'O gasto foi de R$ %g' % fatura_mercearia
	
	try:
		total = 1/1;
	except ValueError:
		print 'erro' #nao chega aqui
	
	
	""" lendo arquivo texto """
	files = glob.glob('*.txt') #todos arquivos .txt
	for file_name in sorted(files):
		
		print '		---' + file_name
		"""
		with open(file_name) as f:
			for line in f:
				print '\t' + line.rstrip()
			f.close()
		print
		"""
		
	time_now = localtime()
	hour = time_now.tm_hour
	
	print 'Hora atual: {0}'.format(hour)
	
	feliz = ClasseFeliz(30)
	feliz.aumenta(20)
	feliz.diminui(60)
	
	print "valor da classe feliz: " + str(feliz.valor)
	print "valor da classe eh negativo? {0}".format(feliz.negativo())
	
	lines = '''
This is the
first paragraph.

This is the second.'''.splitlines()
	
	for has_chars, frags in groupby(lines, bool):
		if has_chars:
			print ' '.join(frags)
			
	arrayzinho = [1,2,3,4,5,6]
	
	print arrayzinho[1:]
		
if __name__ == '__main__':
	init()
