## Eulerian Cycle <- Cycle where each node is visited once
from collections import deque
import random
import networkx as nx
import matplotlib.pyplot as plt

class Graph:
    def __init__(self):
        self.graph = {}
        self.nodes = self.graph.keys()
        self.edges = 0
        self.visited = []
        self.started = [] 

    def read_graph(self,file):
        with open(file, 'r') as file:
            graph = dict((line.strip().split(' -> ') for line in file))
        for key in graph:
            if key not in self.nodes:
                self.graph[key] = []
            if len(graph[key].split(',')) > 1:
                for i in graph[key].split(','):
                    self.edges += 1
                    self.graph[key].append(i)
            else:
                for i in graph[key].split(','):
                    self.edges += 1
                    self.graph[key].append(i)
    
    def eulerian_walks(self, node = None):
        if node == None:
            node  = random.choice(list(self.graph.keys()))
            if node in self.started:
                while node in self.started:
                    node  = random.choice(list(self.graph.keys())) 
            self.started.append(node)
        
        while len(self.visited) < self.edges:
            if len(node) > 1:
                v = random.choice(self.graph[node])[0]
                if (node,v) not in self.visited:
                    self.visited.append((node,v))
                    return self.eulerian_walks(node= v)
                if (node,v) in self.visited: return 
            else:
                v = self.graph[node][0]
                if (node,v) not in self.visited:
                    self.visited.append((node,v))
                    return self.eulerian_walks(node=v)
                if (node,v) in self.visited: return
    def find_eulerian_path(self,node=None):
        self.eulerian_walks()
        ans = len(self.visited)
        while ans < self.edges - 2:
            self.visited = [] 
            self.eulerian_walks()
            ans = len(self.visited)
        for node in self.graph.keys():
            if self.visited[0][0] in self.graph[node] and node in self.graph[self.visited[-1][1]]:
                self.visited.insert(0,((node)))
                self.visited.append((node))
                return 
