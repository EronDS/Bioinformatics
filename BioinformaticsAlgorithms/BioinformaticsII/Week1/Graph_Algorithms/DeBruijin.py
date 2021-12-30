## Simple ## 
genome = 'AAABBBBA'

def GetMers(genome,k):
    all_mers = [] 
    for i in range(len(genome) - k + 1):
        all_mers.append(genome[i:i+k])
    return all_mers

kmers = GetMers(genome,3)

def LRMers(kmers,k):
    k = k-1
    lrmers = []
    for mer in kmers:
        for i in range(len(mer) - k + 1):
            lrmers.append(mer[i:i+k])
    return lrmers

lrmers = LRMers(kmers,3)
lrmers

### one edge per kmer 
## one node for dinstict k-mer - 1-mer (Corresponding disntinct mers from the genome)
# follow the directions (Eulerian Walk, crossing each node exactly once) --- can pass from recurrent edges from single node

def de_brujin_ize(st,k):
    edges, nodes = [], set() # using set only add value once (unique values)
    
    for i in range(len(st) - k + 1):
        edges.append((st[i:i+k-1], st[i+1:i+k])) # suffix and prefix (Left and right k-1-mers)
        nodes.add(st[i:i+k-1])
        nodes.add(st[i+1:i+k])
    
    return nodes,edges

nodes,edges = de_brujin_ize('ACGCGTCG',3)
print(nodes)
print(edges)

