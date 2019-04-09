class Edge:
	def __init__(self, origin, destiny, weight = 0):
		self.origin = origin
		self.destiny = destiny
		self.weight = weight

	def getOrigin(self):
		return self.origin
		
	def getDestiny(self):
		return self.destiny
	
	def setweight(self, weight):
		self.weight = weight
		
	def	getWeight(self):
		return self.weight
		
	def setOrigin(self, vertex):
		self.origin = vertex
		
	def setDestiny(self, vertex):
		self.destiny = vertex