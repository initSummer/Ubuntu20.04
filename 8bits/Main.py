# how to graphical

from summerNetwork_h import *
if __name__ == "__main__":
    V = [1, 2, 3, 4, 5, 6]
    E = [Edge(1, 2, 2), Edge(1, 3, 3), Edge(2, 4, 3), Edge(2, 5, 1),
        Edge(3, 4, 1), Edge(3, 5, 1), Edge(4, 6, 2), Edge(5, 6, 3)]
    s, t = 1, 6
    G = Network(V, E, s, t)
    ford_fulkerson = FordFulkerson(G)
    ford_fulkerson.start()
    ford_fulkerson.display()
   
