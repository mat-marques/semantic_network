# Implementar um grafo
from Edge import *
from Vertex import *

class Graph:
    def __init__(self):
        self.list_vertices = []
        self.list_edges = []
        self.time = 0

    def search_edge(self, u, v):  # Método recebe dois objetos do tipo Vértice
        for w in self.list_edges:
            origin = w.getOrigin()
            destiny = w.getDestiny()
            if origin.getId() == u.getId() and destiny.getId() == v.getId():
                return w
        return None

    def search_vertex(self, id):  # Método recebe um int
        for i in self.list_vertices:
            if id == i.getId():
                return i
        else:
            return None

    def search_vertex_by_data(self, id_name):  # Método recebe um int
        for i in self.list_vertices:
            if id_name == i.getData():
                return i
        else:
            return None

    def insert_vertex(self, data):
        verify = self.search_vertex_by_data(data)
        if verify is None:
            self.list_vertices.append(Vertex(data))
    
    def insert_edge(self, id_origin, id_destiny, weight, data):
        origin_aux = self.search_vertex_by_data(id_origin)
        destiny_aux = self.search_vertex_by_data(id_destiny)
        if (origin_aux is not None) and (destiny_aux is not None):
            self.list_edges.append(Edge(origin_aux, destiny_aux, weight, data))
        else:
            print("Um dos Vértices ou ambos são inválidos")

    def is_empty(self):
        if len(self.list_edges) == 0:
            return True
        else:
            return False
        
    def search_adjacent(self, u):  # Método recebe um vertice
        for i in range(len(self.list_edges)):
            origin = self.list_edges[i].getOrigin()
            destiny = self.list_edges[i].getDestiny()
            if (u.getData() == origin.getData()) and (destiny.getVisited() == False):
                destiny.setVisited(True)  # Para que não retorn o mesmo vertice seguidas veses
                return (destiny, self.list_edges[i].getData())
        else:
            return None

    def search_graph(self, u, relation, v):
        for i in self.list_vertices:
            i.setVisited(False)
        u_id = self.search_vertex_by_data(u)
        v_id = self.search_vertex_by_data(v)
        if u_id is None or v_id is None:
            return False
        path = []
        for i in range(len(self.list_edges)):
            origin = self.list_edges[i].getOrigin()
            destiny = self.list_edges[i].getDestiny()
            if u_id.getData() == origin.getData():
                path.append(self.list_edges[i].getData())
                if self.visity(destiny, relation, v_id, path):
                    return True
            path.clear()
        else:
            return False

    def visity(self, u, relation, v, path):
        if u.getData() == v.getData():
            if self.inference(path, relation):
                return True
            else:
                return False
        for i in range(len(self.list_edges)):
            origin = self.list_edges[i].getOrigin()
            destiny = self.list_edges[i].getDestiny()
            if u.getData() == origin.getData():
                path.append(self.list_edges[i].getData())
                if self.visity(destiny, relation, v, path):
                    return True
                path.pop()
        else:
            return False

    def inference(self, path, relation):
        r = 0
        cont = 0
        for element in path:
            if relation == "e_um" and element == "e_um":
                r = r + 1
            elif relation == "tem" and (element == "e_um" or element == "tem"):
                if element == "tem":
                    r = r + 1
                cont = cont + 1
            elif relation == element or element == "e_um":
                if element == relation:
                    r = r + 1 
                cont = cont + 1 
        
        if relation == "e_um" and r == len(path):
            return True
        elif relation == "tem" and r > 0 and cont == len(path):
            return True
        else:
            if r == 1 and cont == len(path):
                return True
            return False