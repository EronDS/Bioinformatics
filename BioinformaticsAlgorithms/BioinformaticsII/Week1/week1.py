from itertools import permutations, product

def Composition(string:str,k:int) -> str:
    all_mers = [] 
    for i in range(len(string) - k + 1):
        all_mers.append(string[i:i + k])
    return all_mers

file_d = 'dataset_197_3.txt'
f = open(file_d,'r')
lines = f.read().splitlines()
k = lines[0]
seq = lines[1]
k = int(k)

file = open('ans_1.txt','w')
file.write('\n'.join(Composition(seq,k)))
file.close()
f.close()

def Overlap(a:str,b:str,min_lenght = 3) -> int:
    start = 0 
    while True:
        start = a.find(b[:min_lenght], start)
        if start == -1:
            return 0
        if b.startswith(a[start: ]):
            return len(a) - start 
        start += 1

import itertools
def SCSStringReconstruction(ss) -> str:
    """
    SCS = Shortest Common Superstring (NP-complete)
    """
    shortest = None
    for ssperm in permutations(ss):
        sup = ssperm[0]
        for i in range(len(ss) - 1):
            overLen = Overlap(ssperm[i], ssperm[i+1], min_lenght = 1)
            sup += ssperm[i+1][overLen:]
        
        if shortest == None or len(shortest) > len(sup):
            shortest = sup
        return shortest
    
directory = 'dataset_198_3 (2).txt'
f = open(directory,'r')
seqs = f.read().splitlines()
file = open('ans_2.txt','w')
file.write(SCSStringReconstruction(seqs))
file.close()
f.close()

seqs = 'ATGCG GCATG CATGC AGGCA GGCAT GGCAC'.split(' ')
Overlap('CATGC', 'ATGCG')

def OverlappingGraph(seqs:list) -> set:
    k = len(seqs[0])
    adjacency_list = {}
    adj_list = set()
    for ssperm in permutations(seqs,2):
        for i  in range(len(ssperm) - 1):
            overLen = Overlap(ssperm[i], ssperm[i+1],k-1)
            if overLen == k-1:
                if ssperm[i] in adjacency_list:
                    adjacency_list[ssperm[i]] = adjacency_list[ssperm[i]] +','+ ssperm[i+1]
                else:
                    adjacency_list[ssperm[i]] = ssperm[i+1]
    for key,value in adjacency_list.items():
        adj_list.add(key + ' -> ' + value)
    return adj_list

directory = 'dataset_198_10 (2).txt'
file = open(directory,'r')
lines = file.read().splitlines()
k = len(lines[0])
write = open('ans_3.txt', 'w')
write.write('\n'.join(OverlappingGraph(lines)))
file.close()
write.close()


def DeBrujnize(string:str,k:int) -> set:
    edges = [] 
    nodes = set()
    for i in range(len(string) - k + 1):
        edges.append((string[i:i+k-1], string[i+1:i+k]))
        nodes.add(string[i:i+k-1])
        nodes.add(string[i+1:i+k])
    adjacency_list = {}
    adj_list = set()
    for i,j in edges:
        if i in adjacency_list:
            adjacency_list[i] = adjacency_list[i] + ',' + j
        else:
            adjacency_list[i] = j
    for key,value in adjacency_list.items():
        adj_list.add(key + ' -> ' + value)
    return adj_list

direct = 'dataset_199_6 (5).txt'
file = open(direct, 'r')
lines = file.read().splitlines()
k = int(lines[0])
seqs = lines[1]
file_w = open('ans_4.txt','w')
file_w.write('\n'.join(DeBrujnize(seqs,k)))

file_w.close()
file.close()

def KUniversalLinearBinaryStrings(strings,k):
    not_ = []
    occs = set()
    for string in strings:
        for i in range(len(string) - k + 1):
            if string[i:i+k] in occs:
                not_.append(string)
            occs.add(string[i:i+k])
    universal = []
    for string in strings:
        if string not in not_:
            universal.append(string)
    return universal
             
seqs = ['0101010100', '1111000111',
        '0111010001', '0011101000',
        '0100011101', '1100011011']

KUniversalLinearBinaryStrings(seqs,3)
