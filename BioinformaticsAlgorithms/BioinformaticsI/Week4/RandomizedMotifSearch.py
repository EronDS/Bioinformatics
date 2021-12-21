from typing import Generic
from Bio.Seq import Seq
from Bio import motifs
import random
from itertools import product
from collections import Counter
from numpy.lib.npyio import savez_compressed
random.seed(0)
from Bio.motifs import matrix
import numpy as np
import itertools

### Randomized Motif Search ###

def GetRandomMers(dna,k,t):
    random_mers = []
    for string in dna:
        mers_string = [] 
        for i in range(len(string) - k + 1):
            mers_string.append(string[i:i + k])
        random_mers.append(random.choice(mers_string))
    return random_mers

def Profile(mers):
    mers_bp = [] 
    for mer in mers:
        mers_bp.append(Seq(mer))
    m = motifs.create(mers_bp)
    wm = m.counts.normalize(pseudocounts = 1)
    return wm


def GetBest(dna,k,profile):
    mers = [] 
    ent = [] 
    for string in dna:
        string_mer = []
        string_ent = [] 
        for i in range(len(string)- k + 1):
            mer = string[i:i + k]
            entropy = 1 
            idx = 0
            for u in mer:
                entropy = entropy * profile[u][idx]
                if idx < len(string):
                    idx += 1
            string_mer.append(mer)
            string_ent.append(entropy)
        max_entropy = max(string_ent)
        for i in range(len(string_ent)):
            if string_ent[i] >= max_entropy:
                mers.append(string_mer[i])
    return mers


def Consensus(motifs_):
    motifs_bp = [] 
    for motif_ in motifs_:
        motifs_bp.append(Seq(motif_))
    m = motifs.create(motifs_bp)
    return m.consensus

def HammingDistance(p,q):
    distance = 0
    for i in range(len(p)):
        if p[i] != q[i]:
            distance += 1
    return distance

def Score(motifs_):
    consensus = str(Consensus(motifs_))
    score = 0
    for motif_ in motifs_:
        score += HammingDistance(motif_,consensus)
    return score


def RandomizedMotifSearch(dna,k,t):
    Motifs = GetRandomMers(dna,k,t)
    BestMotifs = Motifs
    running = True
    while running == True:
        profile = Profile(Motifs)
        Motifs = GetBest(dna,k,profile)
        if Score(Motifs) < Score(BestMotifs):
            BestMotifs = Motifs
        else:
            running = False
    return BestMotifs, Score(BestMotifs)


def Algorithm(dna,k,t):
    global_best, global_best_score = RandomizedMotifSearch(dna,k,t)
    for i in range(1000):
        random.seed()
        best,best_score = RandomizedMotifSearch(dna,k,t)
        if best_score < global_best_score:
            global_best_score = best_score
            global_best = best
    return global_best, global_best_score


### SAMPLE TEST ###

dna = 'CGCCCCTCTCGGGGGTGTTCAGTAAACGGCCA GGGCGAGGTATGTGTAAGTGCCAAGGTGCCAG TAGTACCGAGACCGAAAGAAGTATACAGGCGT TAGATCAAGTTTCAGGTGCACGTCGGTGAACC AATCCACCAGCTCCACGTGCAATGTTGGCCTA'
k,t = 8,5
ans = Algorithm(dna.split(' '),k,t)

### DATASET ###

f = open('dataset_161_5.txt', 'r')
lines = f.read().splitlines()
k = int(lines[0][0:2])
t = int(lines[0][2:])
dna = lines[1]
print(*Algorithm(dna.split(' '),k,t))


motifs_ = ['TGA', 'GTT' , 'GAA' , 'TGT']
dna = 'TGACGTTC TAAGAGTT GGACGAAA CTGTTCGC'
dna.split(' ')
dna
profile = Profile(motifs_)
profile
print(*GetBest(dna.split(' '), 3, profile))
