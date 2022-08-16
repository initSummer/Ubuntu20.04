print("class Network is Imported")
class Network():
    ''' st-net '''
    def __init__(self, V:list, E:list, s:int, t:int):
        '''
        :param V
        :param E
        :param s
        :param t
        :return:
        '''
        self.V = V
        self.E = E
        self.s = s
        self.t = t

    def get_from_edges(self, v):
        '''
        获得从 v 节点 流出的边
        '''
        '''
        get the from_edge of a node
        '''
        return [edge for edge in self.E if edge.is_from(v)]

    def get_to_edges(self, v):
        '''
        get the to_edge of node v
        '''
        return [edge for edge in self.E if edge.is_to(v)]

    def get_edges(self, v):
        ''' get all edge linked node_v '''
        return self.get_from_edges(v) + self.get_to_edges(v)


    def flows_from(self, v):
        ''' 获得deg+(v) '''
        ''' deg+(v) '''
        edges = self.get_from_edges(v)
        return sum([e.flow for e in edges])

    def flows_to(self, v):
        ''' deg-(v) '''
        edges = self.get_to_edges(v)
        return sum([e.flow for e in edges])

    def self_check(self, s, t):
        ''' 网络中s的流出是否等于t的流入
        :return s流出=t流入 返回true
        注意，自检只检查了s的流出和t的流入，没有检查s和t的流入流出，
        没有检查其他节点的流入流出是否守恒
        没有检查每条边的cap是否为正
        没有检查每条边的flow是否为正，是否过载
        '''
        return int(self.flows_to(s)) == int(self.flows_from(t))

    def display(self):
        if not self.self_check(self.s,self.t):
            print("error! This network doesnot obdy thelaw of flow_conservation")
            return
        print('%-10s%-10s%-8s' % ('edge', 'cap', 'flow'))
        for e in self.E:
            print('%-10s%-10s%-8s' % 
                    (e, e.cap, e.flow if e.flow < e.cap else str(e.flow)+"*"))

