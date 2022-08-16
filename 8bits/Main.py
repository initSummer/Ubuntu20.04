# how to graphical

from summerNetwork_h import *
def main():
    V = [1, 2, 3, 4, 5, 6]
    E = [Edge(1, 2, 2, 1), Edge(1, 3, 3, 1), 
        Edge(2, 4, 3, 1), Edge(2, 5, 1, 1),
        Edge(3, 4, 1, 1), Edge(3, 5, 1, 1), 
        Edge(4, 6, 2, 1), Edge(5, 6, 3, 1)]
    s, t = 1, 6
    G = Network(V, E, s, t)
    G.display()
    ford_fulkerson = FordFulkerson()
    ford_fulkerson.get_network(G)
    ford_fulkerson.start()
    ford_fulkerson.display()
    G = ford_fulkerson.return_network()
    G.display()


if __name__ == "__main__":
    main()
