def Count(t,q):
    count = 0
    for i in range(len(t)):
        if t[i:i+len(q)] == q:
            count += 1
    return count

def Frequent(t,k=3): #propably not well optimized (in terms of processing time) 
    seqs = [] 
    freq = {}
    maxes = []
    
    for i in range(len(t) - 2):
        seqs.append(t[i:i+k])
        
    for seq in seqs:
        if seq not in freq:
            freq[seq] = seqs.count(seq)
    if len(freq) > 0:
        max_ = max(freq.values())
        
        for key in freq.keys():
            if freq[key] >= max_:
                maxes.append(key)
            else:
                pass

    return maxes


def ReverseComplement(seq):
    seqT = ''
    complement = {'A' : 'T', 
                  'T' : 'A',
                  'C' : 'G',
                  'G' : 'C'}
    
    for char in seq:
        seqT += complement[char]
    
    return seqT[::-1]


def PatternMatching(t,q):
    idxs = [] 
    for i in range(len(t)):
        if t[i:i+len(q)]  == q:
            idxs.append(i)
    return idxs



def PattenMatchingWDoubleStrand(t,q):
    idxs = []
    qT = ReverseComplement(q) 
    for i in range(len(t)):
        if t[i:i+len(q)] == q:
            idxs.append(i)
        if t[i:i+len(q)] == qT:
            idxs.append(i)
    
    idxs = sorted(idxs)
    return idxs


def FrequencyFC(t,k=3): # same as Frequency but return an dictionary with keys and values
    seqs = [] 
    freq = {}
    
    for i in range(len(t) - 2):
        seqs.append(t[i:i+k])
        
    for seq in seqs:
        if seq not in freq:
            freq[seq] = seqs.count(seq)
    return freq


def FindingClumps(seq,k,l,t):
    clumps = [] 
    for i in range(len(seq)):
        subpart = seq[i:i+l] # sliding window of size L through genome
        freq = FrequencyFC(subpart,k)
        for key in freq:
            if freq[key] >= t:
                if key not in clumps:
                    clumps.append(key)
    return clumps
