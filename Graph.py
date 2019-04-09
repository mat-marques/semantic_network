# Implementar um grafo
class Graph:
    def __init__(self):
        self.list_vertices = []
        self.list_edges = []

    def search_edge(self, u, v):  # Método recebe dois objetos do tipo Vértice
        for w in self.list_edges:
            origin = w.getOrigin()
            destiny = w.getDestiny()
            if origin.getId() == u.getId() and destiny.getId() == v.getId():
                return w

    def search_vertex(self, id):  # Método recebe um int
        for i in self.list_vertices:
            if id == i.getId():
                return i
        else:
            return None

    def insert_vertex(self, id, data):
        self.list_vertices.append(Vertex(id, data))
    
    def insert_edge(self, id_origin, id_destiny, weight):
        origin_aux = self.search_vertex(id_origin)
        destiny_aux = self.search_vertex(id_destiny)
        if (origin_aux is not None) and (destiny_aux is not None):
            self.list_edges.append(Aresta(origin_aux, destiny_aux, weight))
        else:
            print("Um dos Vértices ou ambos são inválidos")

    def is_empty(self):
        if len(self.list_edges) == 0:
            return True
        else:
            return False


    def remove(self):
        
    def deepSearch(self):

    def widthSearch(self):