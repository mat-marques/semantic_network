class Vertex:
    def __init__(self, data):
        self.id = 0
        self.data = data
        self.predecessor = []
        self.visited = False
        self.estimate = 999999
        self.time = 0

    def setVisited(self, valor):
        self.visited = valor

    def getVisited(self):
        return self.visited

    def setEstimate(self, estimate):
        self.estimate = estimate

    def getEstimate(self):
        return self.estimate
    
    def setTime(self, time):
        self.time = time

    def getTime(self):
        return self.time

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