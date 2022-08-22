# how to graphical
from summerNetwork_h import *
import numpy
import time
T1 = time.time()
def StrctNode(a):
    return numpy.linspace(0,a-1,a,dtype=int)

def main():
    # V = [0, 1, 2, 3, 4, 5, 6, 7, 8, ]
    V1 = StrctNode(20)
    E1 = [Edge(0,1,100),Edge(0,2,100),Edge(0,3,100),
            Edge(0,4,100),Edge(0,5,100),Edge(1,6,1),Edge(2,7,1),
            Edge(3,8,1), Edge(4,9,1),Edge(5,10,1),Edge(6,11,10),
            Edge(7,11,100),Edge(7,12,100),Edge(8,12,100),
            Edge(9,13,100),Edge(10,13,100),Edge(11,14,1),
            Edge(12,15,1),Edge(13,16,1),Edge(14,17,100),
            Edge(15,17,100),Edge(17,18,1),Edge(14,19,100),
            Edge(15,19,100),Edge(16,19,100),Edge(18,19,100)]
    s1, t1 = V1[0], V1[-1]
    G1 = Network(V1, E1, s1, t1)

    V2 = StrctNode(6)
    E2 = [Edge(0,1,2),Edge(0,2,3),Edge(1,3,3),Edge(1,4,1),
            Edge(2,3,1),Edge(2,4,1),Edge(3,5,2),Edge(4,5,3)]
    s2, t2 = 0, 5
    G2 = Network(V2,E2,s2,t2) 

    G = G2
    G.display()
    ffks = FordFulkerson()
    ffks.get_network(G)
    ffks.start()
    ffks.display_max_flow()
    ffks.min_st_cut()
    ffks.display_st_cut()
   # ffks.plot()

if __name__== '__main__':
    main()
    T2 = time.time()
    print(' 程序运行时间：%.6s毫秒 ' % ((T2 - T1)*1000))
