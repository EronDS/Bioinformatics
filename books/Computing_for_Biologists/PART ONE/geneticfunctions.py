import random

def GCcontent(string):
    """ Fraction of GC in DNA """
    counter = 0 
    
    for i in string:
        if i == 'G' or i == 'C':
            counter += 1
    
    return counter / float(len(string)) * 100 


GCcontent('GCAAAACG')



def Transcription(dna): 
    """ Transform DNA into RNA - Simullating Transcription in Cells"""
    dna = dna.upper()
    rna = dna.replace('T', 'U')
    
    return rna 


Transcription('ACGT')


def CCAAT_boxes(DNA):
    """Finding CCAAT boxes - CCAAT is a signal sequence that sinalizes 
    the binding site for RNA transcription factor"""
    counter = 0
    
    for indexes in range(len(DNA)):
        if DNA[indexes:indexes + 5] == 'CCAAT':
            counter += 1 #
    
    return counter 

CCAAT_boxes('CCAATGCT')


def multi_CCAAT_boxes(list_DNA):
    """ Applies CCAAT_boxes function through an DNAlist"""
    DNA_dict = {} 
    for DNA in list_DNA:
       DNA_dict[DNA] = CCAAT_boxes(DNA)
    return DNA_dict 


multi_CCAAT_boxes(['CCAATGCT', 'CG', 'GCCAATGCCAAT'])

def startc_counter(DNA, start_codon = 'ATG'):
    """ return the amount of start codons present in DNA"""
    counter = 0 
    for i in range(len(DNA)):
        if DNA[i: i+3] == start_codon:
            counter += 1 
            
    return counter 

def genString(GCcontent, length):
    
    out = ''
    
    for i in range(length):
        number = random.random() # random number (0 > number < 1)
        if number < GCcontent: # reflects the probability of finding G or C in the DNA sequence
            nuc = random.choice(['G', 'C'])
        if number > GCcontent: # reflects the probability of finding A or T in the DNA sequence
            nuc = random.choice(['A' , 'T'])
        out = out + nuc
    return out


def Startcodons(GCcontent,length,trials,startcodon = 'ATG'):
    
    total = 0
    
    for iteration in range(trials):
        DNAseq = genString(GCcontent,length)
        total = total + startc_counter(DNAseq,startcodon )
    
    return float(total/ (trials * (length -2)))

def nextGen(population):
    offspring = [] 
    
    for i in range(len(population)):
        offspring.append(random.choice(population))
        
    return offspring

def Simpop(population):
    
    while population.count('a') > 0 and population.count('A') > 0:
        population = nextGen(population)
    print(population)
    

def find_motif(motif,sequence):
    indexes = [] 
    for index in range(len(sequence)):
        if sequence[index:index + len(motif)] == motif:
            indexes.append(index)
    return indexes


