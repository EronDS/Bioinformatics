class Graph:
    def __init__(self):
        self.graph = [] 
        self.nodes = [] 
        self.node_count = 0 
    def add_nodes(self,v):
        if v in self.nodes:
            print('{v} already in graph'.format(v=v))
            return
        self.node_count += 1
        self.nodes.append(v)
        if self.graph == []:
            self.graph.append([0])
            return
        for n in self.graph:
            n.append(0)
        temp_list = []
        for i in range(self.node_count):
            temp_list.append(0)
        self.graph.append(temp_list)
    def traverse_graph(self):
        for i in range(self.node_count):
            for j in range(self.node_count):
                print(self.graph[i][j], end = ' ')
            print('')
    def add_undirected_edge(self,a,b):
        if a not in self.nodes or b not in self.nodes:
             print("Node(s) not found")
             return
        index_a = self.nodes.index(a)
        index_b = self.nodes.index(b)
        self.graph[index_a][index_b] = 1
        self.graph[index_b][index_a] = 1
    def add_weighted_undirected_edge(self,a,b,weight):
        if a not in self.nodes or b not in self.nodes:
            print('Node(s) not found')
            return
        index_a,index_b = self.nodes.index(a),self.nodes.index(b)
        self.graph[index_a][index_b] = weight
        self.graph[index_b][index_a] = weight
    
    def add_directed_edge(self,a,b):
        if a not in self.nodes or b not in self.nodes:
            print('Node(s) not found')
            return
        index_a,index_b = self.nodes.index(a),self.nodes.index(b)
        self.graph[index_a][index_b] = 1
    
    def add_weighted_directed_edge(self,a,b,weight):
        if a not in self.nodes or b not in self.nodes:
            print('Node(s) not found')
            return
        index_a,index_b = self.nodes.index(a),self.nodes.index(b)
        self.graph[index_a][index_b] = weight
        
graph = Graph()
graph.add_nodes('1')
graph.add_nodes('2')
graph.add_nodes('3')
graph.node_count
graph.graph
graph.nodes
graph.node_count
graph.traverse_graph()
graph.add_undirected_edge('1','2')
graph.add_weighted_undirected_edge('1','2',3)
graph.add_directed_edge('1','2')
graph.add_weighted_directed_edge('1','3',3)