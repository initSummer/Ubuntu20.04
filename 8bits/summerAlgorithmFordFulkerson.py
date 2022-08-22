from summerClassEdge import *
from summerClassNetwork import *
from queue import Queue
print("Class FordFulkerson is Imported")

class FordFulkerson():
    '''
    使用方法：
    1.创建一个对象FordFulkerson ffks；
    2.ffks即是该算法的抽象对象
    3.将一个网络传递给ffks：ffks.get(NetWork)
    4.启动算法ffks.start()
    5.得到最大流网络
        可以将该网络输出G=ffks.return_network()
        或者将该网络打印ffks.display()
    '''
    def __init__(self):
        self.G = None
        self.max_flow = 0 #如果传入的网络中流不是0，还能正确计算吗？
                            #如果网络流合法，那么可以
        self.X = None
        self.Y = None
        self.forword_cut_edge = [] 
        self.reverse_cut_edge = [] 

    def get_network(self, G:Network):
        self.G = G

    def return_network(self):
        return self.G

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
        ''' 用queue实现广度优先搜索
            找到残存网中的一条增广路径
            通过visited_node记录访问过的节点
            确保最简路径 '''
        path = None # declare a path 
        visited_node = set() # declare visited node and it is a empty set
        visited_node.add(self.G.s) # put s into visited node
        q = Queue() # declare a queue
        q.put(self.Node(self.G.s, None, -1)) # put 
        while not q.empty():
            # 只要正在访问的节点有没有被访问过的相邻节点，那么q就不会空，寻找就会继续进行
            node_v = q.get()
            v = node_v.w

            #1. 找到所有连接v的边
            #2. 分别获得点对v,w
            #3. 如果v是from_node，那么返回flow
            #4. 如果v是to_node，那么返回cap-flow
            #5. 评判标准，首先没有被访问过，其次剩余容量大于零
            #6. 将这个节点标记为已访问
            #7. 以这个节点定义一个Node
            #8. 将这个节点put到q，以供while循环
            #9. 当这个节点是t时，break while，找到了一条增广路径

            for e in self.G.get_edges(v):    # traverse all edge linked v
                w = e.other_node(v)    #other node of the edge, and the edge is from v to w

                # v2w have remainingCap and w has not been Accessed
                # 为什么rct>0？
                # 如果是from_node，那么只要有剩余网络就可以
                # 如果是to_node，那么只要有流量就可以
                # !!!!!!!!!!!!!!!!!!!!!!!!!!!!
                if e.residual_cap_to(w) > 0 and w not in visited_node:#!!!!!!!!!!!
                    visited_node.add(w) # 如果这条路走不通，其他路还能访问这个节点吗？
                                        # 不能，但是无所谓
                                        # 这条路走不通，说明这个节点没有后续节点可以走？？？
                                        # 不对，需要重新想
                                        # 某个节点被标记了，那么同时这个节点一定会经过队列中
                                        # 那么这个节点一定会被遍历所有连接的节点
                                        # 所以不会影响结果
                                        # 之前的思路也是对的，如果这个节点被标记了
                                        # 那么他一定是没有to_node的，所以他不需要在被检查一遍
                    node_w = self.Node(w, e, node_v)
                    q.put(node_w)
                    if w == self.G.t: # arrive t
                        path = node_w # path是个什么东西？
                                        # 是一个链表，Node是一种链表，Node.parent记录了其from_node
                        break
        return path

    def start(self):
        for e in self.G.E:
            e.flow = 0
        while True:
            ''' LOOP until cant find a agmtPath '''

            ''' Step 1. Find a augmenting path '''
            path = self.get_augmenting_path() # find an augmenting path
            if path is None:
                break

            ''' Step 2. calculate how much to modify as Bottle '''
            bottle = 100000
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
                e.moddify_flow(w,bottle) # 会不会造成flow>cap?
                                            # 不会，flow+residualCap = Cap
                                            # 所以，计算完成后一定会有边flow=Cap
                                            # （除非Cap极大，大于设置的初始bottle）
                                            # 而其他边flow<Cap

                node = node.parent

            # now, flow_of_net is plused by Bottle
            self.max_flow += bottle

    def min_st_cut(self):
        self.X = [self.G.s]
        queue = Queue()
        queue.put(self.G.s)
        while not queue.empty():
            node = queue.get() # 为什么上面用queue，这里用stack？可以用queue（stack）吗？
                                # 随便
            for e in self.G.get_from_edges(node):
                if e.w != self.G.t and e.w not in self.X and e.residual_cap_to(e.w) > 0:
                    self.X.append(e.w)
                    queue.put(e.w)
            for e in self.G.get_to_edges(node):
                if e.v not in self.X and e.residual_cap_to(node) > 0:
                    self.X.append(e.v)
                    queue.put(e.v)
        self.Y = list(set(self.G.V)-set(self.X))
        self.X.sort()
        self.Y.sort()

        self.forword_cut_edge = [e for e in self.G.E if e.v in self.X and e.w in self.Y]
        self.reverse_cut_edge = [e for e in self.G.E if e.v in self.Y and e.w in self.X]
        return self.X, self.Y, self.forword_cut_edge, self.reverse_cut_edge

    def display_max_flow(self):

        print("MaxFlowNetwork = ", self.max_flow)
        print('%-10s%-10s%-8s' % ("edge", "cap", "flow"))
        for e in self.G.E:
            print('%-10s%-10d%-8s' %
                    (e, e.cap, e.flow if e.flow<e.cap else str(e.flow)+"*"))

    def display_st_cut(self):
        print('X={0}, !X={1}'.format(self.X, self.Y))
        print ('forword cut edge ={}'.format([str(e) for e in self.forword_cut_edge]))
        print ('reverse cut edge ={}'.format([str(e) for e in self.reverse_cut_edge]))

    def plot(self):
        start = []
        to = []
        flow = []
        for e in self.G.E:
            if e.flow != 0:
                start.append(e.v)
                to.append(e.w)
                flow.append(e.flow)
        g_plot = nx.DiGraph()
        for i in range(0, len(start)):
            g_plot.add_weighted_edges_from([(start[i], to[i], flow[i])])
        nx.draw(g_plot,
                with_labels=True, 
                pos=nx.spring_layout(g_plot),
                width=[float(v['weight']) for (r,c,v) in g_plot.edges(data=True)])
        ax = matplotlib.pyplot.gca()
        ax.set_axis_off()
        matplotlib.pyplot.show()
