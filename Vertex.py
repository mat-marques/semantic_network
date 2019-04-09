class Vertex:
    def __init__(self, id, data):
        self.id = id
        self.data = data
        self.predecessor = []

    def setId(self, id):
        self.id = id

    def getId(self):
        return self.id

    def setData(self, data):
        self.data = data

    def getData(self):
        return self.data