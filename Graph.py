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

    def insert_vertex(self, id, data):
        self.list_vertices.append(Vertex(id, data))
    
    def insert_edge(self, id_origin, id_destiny, weight, data):
        origin_aux = self.search_vertex(id_origin)
        destiny_aux = self.search_vertex(id_destiny)
        if (origin_aux is not None) and (destiny_aux is not None):
            self.list_edges.append(Edge(origin_aux, destiny_aux, weight, data))
        else:
            print("Um dos Vértices ou ambos são inválidos")

    def is_empty(self):
        if len(self.list_edges) == 0:
            return True
        else:
            return False

    def print_Graph_first_level(self, origin, destiny):
        origin_aux = self.search_vertex(origin)
        destiny_aux = self.search_vertex(destiny)

        edge_aux = self.search_edge(origin_aux, destiny_aux)
        if edge_aux is not None:
            print(origin_aux.getData() + " " + edge_aux.getData()  + " " + destiny_aux.getData())
        else:
            print("Não há caminho!")
        
    # def deepSearch(self):

    def search_adjacent(self, u):  # Método recebe um vertice
        for i in range(len(self.list_edges)):
            origin = self.list_edges[i].getOrigin()
            destiny = self.list_edges[i].getDestiny()
            if (u.getId() == origin.getId()) and (destiny.getVisited() == False):
                destiny.setVisited(True)  # Para que não retorn o mesmo vertice seguidas veses
                return destiny
        else:
            return None

    def init_resource(self, resource):  # Função usado no BFS e Dijkstra Método recebe um Objeto
        for v in self.lista_Vertices:
            v.setEstimate(99999)
            v.setVisited(False)
        resource.setVisited(True)
        resource.setEstimate(0)

    def breadth_first_search(self, id):
        resource = self.search_vertex(id)
        if resource is None:
            return "Vértce Nulo"
        self.init_resource(resource)
        l = [resource]
        while 0 != len(l):
            u = l[0]
            v = self.search_adjacent(u)  # retorna adjacente não visitado
            if v is None:
                l.pop(0)  # retiro o vertice sem adjacentes

            else:
                self.time += 1
                v.setTime(self.tempo)
                v.predecessor.append(u.getId())
                v.setVisited(True)
                l.append(v)

            u.setVisited(True)

    def print_graph_with_destiny(self, origin, destiny):
        destiny_Aux = self.search_vertex(destiny)
        if len(destiny_Aux.predecessor) == 0:
            print("Não ha caminho")
        else:
            print(destiny)
            self.imprime_Grafo(origin, destiny)

    def print_graph(self, origin, destiny):
        if origin == destiny:
            print("Fim")
        else:
            destiny_Aux = self.search_vertex(destiny)
            if len(destiny_Aux.predecessor) == 0:
                print("Não ha caminho")
            else:
                print(destiny_Aux.predecessor[0])
                self.print_graph(origin, destiny_Aux.predecessor[0])