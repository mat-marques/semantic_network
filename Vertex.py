class Vertex:
    def __init__(self, data):
        self.id = 0
        self.data = data
        self.predecessor = []
        self.visited = False
        self.currentAdjacent = 0
        self.adjacent = 0

    def setVisited(self, valor):
        self.visited = valor

    def getVisited(self):
        return self.visited

    def setCurrentAdjacent(self, currentAdjacent):
        self.currentAdjacent = currentAdjacent

    def getCurrentAdjacent(self):
        return self.currentAdjacent
    
    def setAdjacent(self, adjacent):
        self.adjacent = adjacent

    def getAdjacent(self):
        return self.adjacent

    def setId(self, id):
        self.id = id

    def getId(self):
        return self.id

    def setData(self, data):
        self.data = data

    def getData(self):
        return self.data

    def __str__(self):
        return ("Vertice: %s Valor: %s" % (
            self.id, self.data))