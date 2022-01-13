## Hamiltonian = Visit every node once
## Eulerian = Visit every edge once
class OverlapGraph:
    def __init__(self):
        self.genomepath = {}
        self.composition = [] 
    def Composition(self,string,k,dna=False):
        if dna:
            for seq in string:
                for i in range(len(seq) - k + 1):
                    self.composition.append(seq[i:i+k])
        else:
            for i in range(len(string) - k + 1):
                self.composition.append(string[i:i+k])
        f = open("stringrec.txt",'w')
        rec = '\n'.join(sorted(self.composition))
        f.write(rec)
        f.close()
        return 
    def Composition_fromtxt(self,txt):
        file = open(txt,'r')
        lines = file.read().splitlines()
        return self.Composition(lines[1],int(lines[0]))
    def Composition_to_graph(self,composition,k):
        for u in composition:
            self.genomepath[u] = []
        for x in composition:
            for y in composition:
                if x[k - (k-1):] == y[:k-1]:
                    self.genomepath[x].append(y)
        self.genomepath = {k:v for k,v in self.genomepath.items() if len(v) != 0}
        file = open('OverlapGraph.txt','w')
        file.write("\n".join([f"{k} -> {','.join(v)}" for k,v in self.genomepath.items()]))
        file.close()
        return
    def Composition_to_OverlapGraph_from_txt(self,file):
        f = open(file,'r')
        lines = f.read().splitlines()
        k = int(len(lines[0]))
        f.close()
        return self.Composition_to_graph(lines,k)
    

graph = OverlapGraph()
graph.Composition('CAATCCAAC',5)
composition= 'ATGCG GCATG CATGC AGGCA GGCAT GGCAC'.split(' ')
composition
graph.Composition_to_graph(composition,5)
graph.Composition_to_graph_from_txt('dataset_198_10 (4).txt')
graph.f.close()