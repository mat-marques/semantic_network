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
            if (u.getData() == origin.getData()) and (destiny.getVisited() == False):
                destiny.setVisited(True)  # Para que não retorn o mesmo vertice seguidas veses
                return (destiny, self.list_edges[i].getData())
        else:
            return None

    def init_resource(self, resource):  # Função usado no BFS e Dijkstra Método recebe um Objeto
        for v in self.list_vertices:
            v.setEstimate(99999)
            v.setVisited(False)
        resource.setVisited(True)
        resource.setEstimate(0)

    def breadth_first_search(self, u, relation, v):
        r = 0
        path = []
        u_id = 0
        v_id = 0
        if isinstance(u, str) and isinstance(v, str):
            u_id = self.search_vertex_by_data(u)
            v_id = self.search_vertex_by_data(v)
        else:
            u_id = u
            v_id = v

        resource = self.search_vertex(u_id)
        if resource is None:
            return "Vértice Nulo"
        self.init_resource(resource)
        l = [resource]
        while 0 != len(l):
            u = l[0]
            v = self.search_adjacent(u)  # retorna adjacente não visitado
            if v is None:
                l.pop(0)  # retiro o vertice sem adjacentes

            else:
                if relation == "e_um" and v[1] == "e_um":
                    path.append((u.getData(), "e_um", v[0].getData()))
                    v[0].setVisited(True)
                    l.append(v[0])
                    if v_id == v[0].getId():
                        return path

                elif relation == "tem" and (v[1] == "e_um" or v[1] == "tem"):
                    path.append((u.getData(), v[1], v[0].getData()))
                    v[0].setVisited(True)
                    l.append(v[0])
                    if v[1] == "tem":
                        r = r + 1
                    if v_id == v[0].getId() and r > 0:
                        return path

                elif v[1] == "e_um" or v[1] == relation:
                    path.append((u.getData(), v[1], v[0].getData()))
                    v[0].setVisited(True)
                    l.append(v[0])
                    if v[1] == relation:
                        r = r + 1
                    if v_id == v[0].getId() and r == 1:
                        return path

            u.setVisited(True)
        path.clear()
        return path

    def depth_first_search(self, u, relation, v):
        for i in self.list_vertices:
            i.setVisited(False)
        u_id = self.search_vertex_by_data(u)
        v_id = self.search_vertex_by_data(v)
        lista = []
        self.visita(u_id, relation, v_id, lista)

    def visita(self, vertex, relation, v, lista):
        print("Visitando o vértice %s"% vertex.getData())
        vertex.setVisited(True)
        vertexAux = self.search_adjacent(vertex)
        while vertexAux is not None:
            lista.append(vertexAux[1])
            print(lista)
            if v == vertexAux[0]:
                print("ACHEI VÉRTICE")
                break
            self.visita(vertexAux[0], relation, v, lista)
            lista.pop()
            vertexAux = self.search_adjacent(vertex)


    def print_graph_with_destiny(self, origin, destiny):
        destiny_Aux = self.search_vertex(destiny)
        if len(destiny_Aux.predecessor) == 0:
            print("Não ha caminho")
        else:
            print(destiny)
            self.print_graph(origin, destiny)

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

