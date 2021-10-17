import os 
import sys
import bisect


def naive_algorithm(p,T):
    matchs = [] 
    for i in range(len(T) - len(p) + 1):
        match = True
        for j in range(len(p)):
            if T[i+j] != p[j]:
                match = False
                break
        if match == True:
            matchs.append(i)
    
    print('p:{}'.format(p))
    print('T:{}'.format(T[:30] + '...'))
    print('Exact Matching Index(es):{}'.format(list(matchs)))
    for u in list(matchs):
        print('Best Match: ')
        print(T[u:u+len(p)])
    
    return matchs



class Index(object):
    def __init__(self,t,k):
        self.k = k
        self.index = []

        for i in range(len(t) - k + 1):
            self.index.append((t[i:i+k], i))
        
        self.index.sort()

    
    def query(self,p):
        kmer = p[:self.k]

        i = bisect.bisect_left(self.index, (kmer,-1))
        hits = [] 
        while  i < len(self.index):
            if self.index[i][0] != kmer:
                break 

            hits.append(self.index[i][1])
            i+=1
        return hits 


def Verification(p,t,index):
    k = index.k 
    offsets = [] 

    for i in index.query(p):
        if p[k:] == t[i+k:i+len(p)]:
            offsets.append(i)

    return offsets