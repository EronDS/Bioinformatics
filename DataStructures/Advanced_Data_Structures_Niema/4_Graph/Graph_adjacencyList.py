from collections import deque

class Graph:
    def __init__(self):
        self.graph = {}
        self.nodes = self.graph.keys()
        self.node_count = 0
    
    def add_node(self,v):
        if v in self.nodes:
            print('Node already present')
            return
        self.node_count+=1
        self.graph[v] = []
    def add_undirected_edge(self,a,b):
        if a not in self.nodes or b not in self.nodes:
            print('a or b not in nodes')
            return
        self.graph[a].append(b)
        self.graph[b].append(a)
    def add_weighted_undirected_edge(self,a,b,weight):
        if a not in self.nodes or b not in self.nodes:
            print('a or b not in nodes')
            return
        self.graph[a].append([b,weight])
        self.graph[b].append([a,weight])
    def add_directed_edge(self,a,b):
        if a not in self.nodes or b not in self.nodes:
            print('a or b not in nodes')
            return
        self.graph[a].append(b)
    def add_weighted_directed_edge(self,a,b,weight):
        if a not in self.nodes or b not in self.nodes:
            print('a or b not in nodes')
            return
        self.graph[a].append([b,weight])
    def delete(self,x):
        if x not in self.nodes:
            print("Delete Operation can't be proceed\
                {} not found in nodes").format(x)
            return
        for i in self.graph:
            for u in self.graph[i]:
                if u[0] == x:
                    self.graph[i].remove(u)
        self.graph.pop(x)

graph = Graph()
graph.add_node('A')
graph.add_node('B')
graph.add_node('C')
graph.add_weighted_undirected_edge('A','B',10)
graph.graph
graph.add_weighted_directed_edge('C','B',15)
graph.delete('A')
