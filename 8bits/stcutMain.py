# how to graphical
from summerNetwork_h import *
def main():
    V = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    E = [Edge(0, 1, 15), Edge(0,2,15), Edge(0,3,15), 
            Edge(1,4,2), Edge(2,4,3), Edge(2,5,2), 
            Edge(3,5,4), Edge(4,5,2), Edge(4,6,2),
            Edge(5,6,4), Edge(4,7,3), Edge(6,8,15),
            Edge(7,8,15)]
    s, t = 0, 8
    G = Network(V, E, s, t)
    ffks = FordFulkerson()
    ffks.get_network(G)
    ffks.start()
    ffks.display()



if __name__ == "__main__":
    main()
