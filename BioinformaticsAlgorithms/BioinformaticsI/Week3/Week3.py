
from Bio import motifs
from Bio.Seq import Seq
import math
import itertools
from itertools import product


def ExpectedMerOccurence(k,nb_strings,lenght):
    """ Expected occurence of specific mer through probability"""
    chars = .25 
    prob = chars**k
    
    total_prob = (nb_strings * (lenght-k+1)) * prob
    return total_prob


def HammingDistance(p,q):
    """ Mismatch error between pattern and querry"""
    count = 0 
    for i in range(len(p)):
        if p[i] != q[i]:
            count += 1
    return count




def SlideWindow(string,k):
    """ Assistant function to slide window in Motif Enumeratin"""
    for i in range(len(string) - k + 1):
        yield string[i:i+k]
        
def MotifEnumeration(dna,k,d):
    """ Find motif given Hamming Distance """
    nucl = ['A' , 'T' , 'C' , 'G']
    mers = [''.join(c) for c in product(nucl,repeat=k)]
    pattern = []
    
    for mer in mers:
        if all(any(HammingDistance(pat,mer) <= d for pat in SlideWindow(string,k)) for string in dna):
            pattern.append(mer)
    
    return pattern


def Consensus(Motifs):
    """ Find consesus string """
    Motifs_seq = [] 
    for motif in Motifs:
        Motifs_seq.append(Seq(motif))
    
    motif = motifs.create(Motifs_seq)
    return motif.degenerate_consensus


def MotifCounts(Motifs):
    """ Couting motifs """
    Motifs_seq = [] 
    for motif in Motifs:
        Motifs_seq.append(Seq(motif))
    
    motif = motifs.create(Motifs_seq)
    return motif.counts


def Flatten(t):
    """ Assistant function to Entropy Calculation """
    return [item for sublist in t for item in sublist]


def OccurenceToProb(values,lenght = 10):
    """ Occurence to probability """
    prob = [] 
    for value in values:
        prob.append(value / lenght)
    return prob
        
def Entropy(Motifs,lenght):
    """ Finding Entropy (Variation) at each position given motifs"""
    dict_ = dict(MotifCounts(Motifs))
    values = dict_.values()
    values_ = Flatten(values)
    prob = OccurenceToProb(values_,lenght)
    
    return sum([-x*math.log2(x) for x in prob if x>0])

 
def MotifLogo(Motifs):
    """ Visualization of the most frequent nucleotide at each position (Consensus Motif)"""
    Motifs_seq = [] 
    
    for motif in Motifs:
        Motifs_seq.append(Seq(motif))
    
    motif = motifs.create(Motifs_seq)
    return motif.weblogo('MotifLogo.pdf', format = 'pdf')




def HammingDistance(p,q):
    count = 0 
    for i in range(len(p)):
        if p[i] != q[i]:
            count+=1
    return count

def GetMers(dna,k, set= True):
    if set == True:
        all_mers = [] 
        for string in dna:
            for i in range(len(string) - k +1):
                if string[i:i+k] not in all_mers:
                    all_mers.append(string[i:i+k])
    if set == False:
        all_mers = []
        for i in range(len(dna) - k + 1):
            if dna[i:i+k] not in all_mers:
                all_mers.append(dna[i:i+k])
    return all_mers


def DistanceBetweenPatternNstrings(pattern, DNA):
    k = len(pattern)
    distance = 0
    for sequence in DNA:
        Hamming_distance = float('inf')
        for i in range(len(sequence)-k+1):
            if Hamming_distance > HammingDistance(pattern, sequence[i:i+k]):
                Hamming_distance = HammingDistance(pattern, sequence[i:i+k])
        distance += Hamming_distance

    return distance



def MedianString(dna,k):
    distance = float('inf')
    patterns = GetMers(dna,k)
    for i in range(len(patterns)):
        pat = patterns[i]
        if distance > DistanceBetweenPatternNstrings(pat,dna):
            distance = DistanceBetweenPatternNstrings(pat,dna)
            Median = pat
    return Median

def Profile(seq,k,entropy_matrix):
    A  = entropy_matrix[0]
    C = entropy_matrix[1]
    G = entropy_matrix[2]
    T = entropy_matrix[3]
    
    mers = GetMers(seq,k,False)
    chosen = ''
    for i in range(len(seq)):
        max_prob = 0
        for mer in mers:
            prob = 1
            for i in range(k):
                if mer[i] == 'A':
                    prob = prob * A[i]
                if mer[i] == 'C':
                    prob = prob * C[i]
                if mer[i] == 'T':
                    prob = prob * T[i]
                if mer[i] == 'G':
                    prob = prob *G[i]
            if prob > max_prob:
                max_prob = prob
                chosen = mer
    return chosen



def GreedyScore(motif,matrix,t):
    score = 1
    for i in range(len(motif)):
        if motif[i] == 'A':
            score = score * (matrix[0][i] / t)
        if motif[i] == 'C':
            score = score * (matrix[1][i] / t)
        if motif[i] == 'G': 
            score = score * (matrix[2][i] / t)
        if motif[i] == 'T':
            score = score * (matrix[3][i] / t)
        
    return score
        
def GreedyMotifSearch(motifs,k,t):
    
    first_mers = []
    for string in motifs:
        first_mers.append(string[:k])
        
    matrix = MotifCounts(first_mers)
    best_mers = [] 
    for string in motifs:
        score_str = 0
        bestmer_str = '' 
        for i in range(len(string) - k + 1):
            score_ = GreedyScore(string[i:i+k],matrix,t)
            if score_ > score_str:
                score_str = score_
                bestmer_str = string[i:i+k]
                
        best_mers.append(bestmer_str)
    return best_mers