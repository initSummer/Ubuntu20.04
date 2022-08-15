from summerClassEdge import *
from summerClassNetwork import *
from queue import Queue
print("Class FordFulkerson is Imported")

class FordFulkerson():
    def __init__(self, G:Network):
        self.G = G
        self.max_flow = 0

    class Node:
        ''' used to marking paths '''
        def __init__(self, w, e:Edge, parent):
            '''
            :param w:顶点
            :param e: edge from previous node to w
            :param parent: the previous node of w, -1 if thereis nothing
            '''
            self.w, self.e, self.parent = w, e, parent

    def get_augmenting_path(self):

        ''' get an augmenting path '''
        ''' 用queue实现广度优先搜索，找到残存网中的一条增广路径，通过visited_node记录访问过的节点，确保最简路径 '''
        path = None # declare a path 
        visited_node = set() # declare visited node and it is a empty set
        visited_node.add(self.G.s) # put s into visited node
        q = Queue() # declare a queue
        q.put(self.Node(self.G.s, None, -1)) # put 
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
            ''' LOOP until cant find a agmtPath '''

            ''' Step 1. Find a augmenting path '''
            path = self.get_augmenting_path() # find an augmenting path

            if path is None:
                break

            ''' Step 2. calculate how much to modify as Bottle '''
            bottle = 10000
            node = path
            while node.parent != -1:
                w, e = node.w, node.e
                bottle = min(bottle, e.residual_cap_to(w))
                node = node.parent

            ''' Step 3. Add every edge_flow by bottle 
            and add MaxFlow by bottle '''
            # modify node which in this path
            node = path
            while node.parent != -1:
                w, e = node.w, node.e
                e.moddify_flow(w,bottle)
                node = node.parent

            # now, flow_of_net is plused by Bottle
            self.max_flow += bottle

    def display(self):
        print("最大网络流 = ", self.max_flow)
        print('%-10s%-10s%-8s' % ("edge", "cap", "flow"))
        for e in self.G.E:
            print('%-10s%-10d%-8s' %
                    (e, e.cap, e.flow if e.flow<e.cap else str(e.flow)+"*"))
