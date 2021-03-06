## Eulerian Walks - one edge (kmer) exactly once

class DeBruijn:
    def __init__(self,):
        self.kmers = [] 
        self.nodes = set()
        self.edges = {}
    def Graph(self,string,k):
        for i in range(len(string) - k + 1):
            ''' k-1 mers overlap '''
            l = string[i:i+k-1]
            r = string[i+1:i+k]
            self.nodes.add(l)
            self.nodes.add(r)
            if l not in self.edges.keys():
                self.edges[l] = [] 
            self.edges[l].append(r)
        file = open('DeBruijn.txt','w')
        file.write('\n'.join([f"{k} -> {','.join(v)}" for k,v in self.edges.items()]))
        file.close()
    def Graph_fromfile(self,file):
        file = open(file,'r')
        lines = file.read().splitlines()
        k = int(lines[0])
        seq = lines[1]
        return self.Graph(seq,k)
    def Graph_fromkmers(self,kmers):
        self.kmers = kmers
        k = len(self.kmers[0])
        for mer in self.kmers:
            l = mer[:-1]
            r = mer[1:]
            if l[1:] == r[:-1]:
                if l not in self.edges.keys():
                    self.edges[l] = [] 
            self.nodes.add(l)
            self.nodes.add(r)
            self.edges[l].append(r)
        file = open('DeBruijnFromKmers.txt','w')
        file.write('\n'.join([f"{k} -> {','.join(v)}" for k,v in self.edges.items()]))
        file.close()           
    def Graph_fromkmers_file(self,file):
        f = open(file,'r')
        lines = f.read().splitlines()
        return self.Graph_fromkmers(lines)
graph = DeBruijn()
graph.Graph('AAGATTCTCTAAGA',4)
graph.Graph_fromfile('dataset_199_6 (7).txt')
graph.Graph_fromkmers()

sample = open('sample.txt','r')
mers = sample.read().splitlines()
sample.close()
graph.Graph_fromkmers(mers)
graph.edges
graph.Graph_fromkmers_file('dataset_200_8.txt')