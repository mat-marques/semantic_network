import sys
from Graph import *

def main():

    file = open(sys.argv[1])
    graph = Graph()
    for lines in file:
        line = lines.split("\n")
        words = line[0].split()
        graph.insert_vertex(words[0])
        graph.insert_vertex(words[2])
        graph.insert_edge(words[0], words[2], 0, words[1])

    while True:

        inp = input("Digite a entrada (vértice relacionamente destino) ou q para sair: ")
        if inp == "q":
            break
        method = input("Digite o método de busca (dfs ou bfs): ")

        inp2 = inp.split(" ")
        if method == "bfs":
            path = graph.breadth_first_search(inp2[0], inp2[1], inp2[2])

            if not path[0]:
                print(inp +" => é falsa")
            else:
                print(inp +" => é verdadeira")
                
            print("")

        else:
            graph.depth_first_search(inp2[0], inp2[1], inp2[2])

    # file.close()

if __name__ == "__main__":
    main()