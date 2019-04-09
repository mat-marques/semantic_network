from Graph import *
def main(fileName):
    # file = open(fileName, "r")
    graph = Graph()
    graph.insert_vertex(1, "Neymar")
    graph.insert_vertex(2, "Atacante")
    graph.insert_vertex(3, "Atleta")
    graph.insert_vertex(4, "Pessoa")
    graph.insert_vertex(5, "Chuteira")

    graph.insert_edge(1, 2, 0, "e_um")
    graph.insert_edge(2, 3, 0, "e_um")
    graph.insert_edge(3, 4, 0, "e_um")
    graph.insert_edge(2, 5, 0, "tem")

    graph.print_Graph_first_level(1, 2)
    graph.print_Graph_first_level(2, 3)

    #print(graph.search_vertex(4))

    # file.close()

if __name__ == "__main__":
    main("")