from summerClassEdge import *
from summerClassNetwork import *
from queue import Queue
print("Class FordFulkerson Imported")

class FordFulkerson():
    def __init__(self, G:Network):
        self.G = G
        self.max_flow = 0
        self.BOTTLE = 10000

    class Node:
        ''' used to marking paths '''
        def __init__(self, w, e:Edge, parent):
            '''
            :param w:顶点
            :param e: edge from previous node to w
            :param parent: the previous node of w
            '''
            self.w, self.e, self.parent = w, e, parent

    def get_augmenting_path(self):
        ''' get an augmenting path '''
        path = None
        visited_node = set()
        visited_node.add(self.G.s)
        q = Queue()
        q.put(self.Node(self.G.s, None, -1))
        while not q.empty():
            node_v = q.get()
            v = node_v.w
            for e in self.G.get_edges(v):    # traverse all edge linked v
                w = e.other_node(v)    #other node of the edge, and the edge is from v to w
                # v2w have remainingCap and w has not been Accessed
                if e.residual_cap_to(w) > 0 and w not in visited_node:
                    visited_node.add(w)
                    node_w = self.Node(w, e, node_v)
                    q.put(node_w)
                    if w == self.G.t: # arrive t
                        path = node_w
                        break
        return path

    def start(self):
        while True:
            path = self.get_augmenting_path() # find an augmenting path
            if path is None:
                break
            node = path
            while node.parent != -1:
                w, e = node.w, node.e
                self.BOTTLE = min(self.BOTTLE, e.residual_cap_to(w))
                node = node.parent
            node = path
            while node.parent != -1:
                w, e = node.w, node.e
                e.moddify_flow(w,self.BOTTLE)
                node = node.parent
            self.max_flow += self.BOTTLE

    def display(self):
        print("最大网络流 = ", self.max_flow)
        print('%-10s%-10s%-8s' % ("edges", "cap", "flow"))
        for e in self.G.E:
            print('%-10s%-10d%-8s' %
                    (e, e.cap, e.flow if e.flow<e.cap else str(e.flow)+"*"))
