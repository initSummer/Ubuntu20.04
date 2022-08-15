print("class Edge is Imported")
class Edge():
    ''' edge in flownet '''
    def  __init__(self, v:int, w:int, cap:int, flow = 0):
        '''
        define a edge from node_v to node_w
        :param v: 
        :param w: 
        :param cap: capicity
        :param flow: flow of edge(v,w)
        '''
        self.v, self.w = v, w
        self.cap, self.flow = cap, flow

    def is_from(self, v):
        ''' 是否是v顶点的流入边 '''
        return self.v == v

    def is_to(self, v):
        ''' 是否是v顶点的流出边 '''
        return self.w == v

    def other_node(self, p):
        ''' return the other node 1 of two node of edge '''
        return self.v if p == self.w else self.w

    def residual_cap_to(self, p):
        '''
        calculate the remaningCap of edge
        :return: remaningCap of v_to_w if p = w
        :return: remaningCap of w_to_v if p = v
        '''
        return self.cap - self.flow if p == self.w else self.flow

    def moddify_flow(self, p, x):
        ''' 
        moddify flow x 
        flow of v2w add x if p = w
        flow of v2w reduce x if p = v
        '''
        if p == self.w:
            self.flow += x
        else:
            self.flow -= x

    def __str__(self):
        return str(self.v) + ' -> ' + str(self.w)

