from Graph import *

def main(fileName):
    # file = open(fileName, "r")
    graph = Graph()
    graph.insert_vertex(1, "Neymar")
    graph.insert_vertex(2, "Atacante")
    graph.insert_vertex(3, "Atleta")
    graph.insert_vertex(4, "Pessoa")
    graph.insert_vertex(5, "Chuteira")
    graph.insert_vertex(6, "Tênis")
    graph.insert_vertex(7, "Cadarço")
    graph.insert_vertex(8, "Atividade Física")
    graph.insert_vertex(9, "Hábito Saudavel")
    graph.insert_vertex(10, "Sour")

    graph.insert_edge(1, 2, 0, "e_um")
    graph.insert_edge(2, 3, 0, "e_um")
    graph.insert_edge(3, 4, 0, "e_um")
    graph.insert_edge(2, 5, 0, "tem")
    graph.insert_edge(5, 6, 0, "e_um")
    graph.insert_edge(6, 7, 0, "tem")
    graph.insert_edge(3, 8, 0, "pratica")
    graph.insert_edge(8, 9, 0, "e_um")
    graph.insert_edge(8, 10, 0, "tem")

    while True:
        inp = input("Digite a entrada (vértice relacionamente destino) ou q para sair: ")
        if inp == "q":
            break
        method = input("Digite o método de busca (dfs ou bfs): ")

        inp2 = inp.split(" ")
        if method == "bfs":
            path = graph.breadth_first_search(inp2[0], inp2[1], inp2[2])

            if len(path) == 0:
                print(path)
                print(inp +" => Inferência é falsa")
            else:
                print(path)
                print(inp +" => Inferência é verdadeira")

    # file.close()

if __name__ == "__main__":
    main("")