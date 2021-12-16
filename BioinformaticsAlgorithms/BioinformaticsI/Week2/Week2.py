def Skew(seq):
    """
    Finding the Skew (relation between content of Guanine
    and Cytosine), useful to find OriC (Origin of Replication)
    """
    skew = 0
    skewness = [] 
    skewness.append(skew)
    
    for nucl in seq:
        if nucl == 'C':
            skew -= 1
            skewness.append(skew)
        if nucl == 'G':
            skew += 1
            skewness.append(skew)
        if nucl == 'A' or nucl == 'T':
            skewness.append(skew)
    return skewness

def MinimumSkew(seq):
    """
    Finding the minimum location of Skew
    """
    skew = 0
    skewness = [] 
    skewness.append(skew)
    skew_dict = {}
    skew_dict[skew] = skew
    count = 0
    for nucl in seq:
        if nucl == 'C':
            skew -= 1
            count += 1
            skew_dict[count]  = skew    
        
        if nucl == 'G':
            skew += 1
            count += 1
            skew_dict[count] = skew
        
        if nucl == 'A' or nucl == 'T':
            count += 1
            skew_dict[count] = skew
    
    min_v = min(skew_dict.values())
    min_keys = []
    for key in skew_dict:
        if skew_dict[key] <= min_v:
            min_keys.append(key)
            
    
    return min_keys


def MaximumSkew(seq):
    """
    Finding the maximum location of Skew
    """
    skew = 0
    skewness = [] 
    skewness.append(skew)
    skew_dict = {}
    skew_dict[skew] = skew
    count = 0
    for nucl in seq:
        if nucl == 'C':
            skew -= 1
            count += 1
            skew_dict[count]  = skew    
        
        if nucl == 'G':
            skew += 1
            count += 1
            skew_dict[count] = skew
        
        if nucl == 'A' or nucl == 'T':
            count += 1
            skew_dict[count] = skew
    
    max_v = max(skew_dict.values())
    max_keys = []
    for key in skew_dict:
        if skew_dict[key] >= max_v:
            max_keys.append(key)
            
    
    return max_keys


def HammingDistance(p,q):
    """
    The amount of mismatches (deletions,
    insertions,or changes in nucleotides)
    between a sequence and a querry
    """
    count = 0 
    for i in range(len(p)):
        if p[i] != q[i]:
            count += 1
    return count

def AproximateMatching(seq,pat,d):
    """
    Find the indexes within the sequence (seq)
    where Hamming Distance (difference in nucleotides between
    sequence and pattern) is less than d
    
    """
    idxs = [] 
    for i in range(len(seq) - len(pat) + 1):
        hd = HammingDistance(seq[i:i+len(pat)], pat)
        if hd <= d:
            idxs.append(i)
    return idxs

def CountOccurrences(seq,pat,thresh):
    """
    Given an sequence, find the occurences of pattern (pat)
    allowing possible mismatchs, if the mismastches are less 
    than threshold (thresh)
    """
    count = 0
    for i in range(len(seq) - len(pat) + 1):
        hd = HammingDistance(seq[i:i+len(pat)], pat)
        if hd <= thresh:
            count += 1
    return count

import itertools
def FindMostFrequentKmer(string,k,d):
    """
    string = sequence of nucleotides
    k = lenght of possible mers (pattern) [used to generate every possible mer]
    d = thresholds of mismatches (Hamming Distance)
    """
    chars = ['A' , 'T' , 'C' , 'G']
    all_possible_mers = list(itertools.product(chars, repeat = k))
    keys = [''.join(c) for c in all_possible_mers]
    
    kmers_freq = {}
    for i in keys:
        kmers_freq[i] = 0
        
    for u in range(len(string) - k  + 1):
        for mer in keys:
            if HammingDistance(string[u:u+k], mer) <= d:
                kmers_freq[mer] = kmers_freq[mer] + 1
                
    max_ = max(kmers_freq.values())
    best_mers = [] 
    for mer in kmers_freq:
        if kmers_freq[mer] >= max_:
            if mer not in best_mers:
                best_mers.append(mer)
    return best_mers

def ReverseComplement(seq):
    complement = {'A' : 'T',
                  'T' : 'A',
                  'C' : 'G',
                  'G' : 'C'}
    seqR = ''
    for char in seq:
        seqR = seqR + complement[char]
    seqR = seqR[::-1]
    return seqR

def FindMostFrequentKmerAndKmerR(string,k,d):
    """
    string = sequence of nucleotides
    k = lenght of possible mers (pattern) [used to generate every possible mer]
    d = thresholds of mismatches (Hamming Distance)
    
    Finding the most frequent kmer (considering also their reverse complement)
    allowing d mismatches in Hamming Distance
    """
    
    chars = ['A' , 'T' , 'C' , 'G']
    all_possible_kmers = itertools.product(chars,repeat = k)
    kmers = [''.join(c) for c in all_possible_kmers]
    
    kmers_freq = {}
    for mer in kmers:
        kmers_freq[mer] = 0
    
    
    for u in range(len(string) - k + 1):
        for mer in kmers:
            if HammingDistance(string[u:u+k], mer) <= 1: 
                kmers_freq[mer] = kmers_freq[mer] + 1
                kmers_freq[ReverseComplement(mer)] = kmers_freq[ReverseComplement(mer)] + 1    
    
    max_ = max(kmers_freq.values())
    best_mers = [] 
    for mer in kmers_freq:
        if kmers_freq[mer] >= max_:
            if mer not in best_mers:
                best_mers.append(mer)
    return best_mers



def Neighboors(pattern,d):
    """
    Given pattern, return all possible d-neighboors
    """
    nucl = ['A' , 'T' , 'C' , 'G'] 
    possibles = itertools.product(nucl, repeat = len(pattern))   
    possibles = [''.join(c) for c in possibles]
    neighboors = [] 
    
    
    for possibility in possibles:
        if HammingDistance(possibility,pattern) <= d:
            neighboors.append(possibility)
    return neighboors



def PlotSkew(seq):
    
    import matplotlib.pyplot as plt
    import seaborn as sns
    plt.figure(figsize=(24,8))
    sns.set_theme(style='whitegrid')
    
    """
    Finding the Skew (relation between content of Guanine
    and Cytosine), useful to find OriC (Origin of Replication)
    """
    skew = 0
    skewness = [] 
    skewness.append(skew)
    
    for nucl in seq:
        if nucl == 'C':
            skew -= 1
            skewness.append(skew)
        if nucl == 'G':
            skew += 1
            skewness.append(skew)
        if nucl == 'A' or nucl == 'T':
            skewness.append(skew)
    plt.bar(range(len(skewness)),skewness)
    plt.ylabel('Relative Content of Guanine (G-C)', fontsize = 15)
    plt.xlim(0,)
    plt.show()