class ClasseFeliz (object):
	
	#variaveis da classe sao definidas no construtor
	def __init__(self,valor_inicial=0):
		self.valor = valor_inicial
		
	def aumenta(self,qtd):
		self.valor += qtd
	
	def diminui(self,qtd):
		self.valor -= qtd
		
	def negativo(self):
		return self.valor < 0
		
