class Edge:
	def __init__(self, origin, destiny, weight = 0, data):
		self.origin = origin
		self.destiny = destiny
		self.weight = weight
		self.data = data

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

	def setData(self, data):
		self.data = data

	def getData(self):
		return self.data

	def __str__(self):
		return "E(%s----%s---->%s)" % (self.origin.getId(),self.data,self.destiny.getId())