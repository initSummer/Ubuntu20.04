print("class Network Imported")
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
        ''' deg+(v) '''
        edges = self.get_from_edges(v)
        return sum([e.flow for e in edges])

    def flows_to(self, v):
        ''' deg-(v) '''
        edges = self.get_from_edges(v)
        return sum([e.flow for e in edges])

    def check(self, s, t):
        ''' 网络中s的流出是否等于t的流入
        :return s流出=t流入 返回true
        '''
        return self.flows_to(s) == self.flows_from(t)

    def display(self):
        if not self.check():
            print("error! This network doesnot obdy thelaw of flow_conservation")
            return
        print(' %-10s%-10s%-8s' % ('边', '容量', '流'))
        for e in self.E:
            print(' %-10s%-10s%-8s' % 
                    (e, e.cap, e.flow if e.flow < e.cap else str(e.flow)+"*"))

