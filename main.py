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

        inp = input("Digite a entrada (vértice relacionamento destino) ou q para sair: ")
        if inp == "q":
            break

        inp2 = inp.split(" ")
        if graph.search_graph(inp2[0], inp2[1], inp2[2]):
            print(inp +" => é verdadeira")
        else:
            print(inp +" => é falsa")
        print()


if __name__ == "__main__":
    main()