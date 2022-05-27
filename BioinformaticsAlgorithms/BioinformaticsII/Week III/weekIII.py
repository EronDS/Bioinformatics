codon_table = {"UUU":"F", "UUC":"F", "UUA":"L", "UUG":"L",
    "UCU":"S", "UCC":"S", "UCA":"S", "UCG":"S",
    "UAU":"Y", "UAC":"Y", "UAA":"STOP", "UAG":"STOP",
    "UGU":"C", "UGC":"C", "UGA":"STOP", "UGG":"W",
    "CUU":"L", "CUC":"L", "CUA":"L", "CUG":"L",
    "CCU":"P", "CCC":"P", "CCA":"P", "CCG":"P",
    "CAU":"H", "CAC":"H", "CAA":"Q", "CAG":"Q",
    "CGU":"R", "CGC":"R", "CGA":"R", "CGG":"R",
    "AUU":"I", "AUC":"I", "AUA":"I", "AUG":"M",
    "ACU":"T", "ACC":"T", "ACA":"T", "ACG":"T",
    "AAU":"N", "AAC":"N", "AAA":"K", "AAG":"K",
    "AGU":"S", "AGC":"S", "AGA":"R", "AGG":"R",
    "GUU":"V", "GUC":"V", "GUA":"V", "GUG":"V",
    "GCU":"A", "GCC":"A", "GCA":"A", "GCG":"A",
    "GAU":"D", "GAC":"D", "GAA":"E", "GAG":"E",
    "GGU":"G", "GGC":"G", "GGA":"G", "GGG":"G"}


6
count_dic = {}
for letter in 'LEADER':
    count_dic[letter] = 0

for key in codon_table.keys():
    for l in 'LEADER':
        if codon_table[key] == l:
            count_dic[l]+=1


def getcodons(dna_string):
    codons = [dna_string[i:i+3] for i in range(0, len(dna_string), 3)]
    return codons



def translate(codons):
    protein_string = ''
    for codon in codons:
        protein_string+=codon_table[codon]
    return protein_string

AminoAcidMass = {'G': 57, 'A': 71, 'S': 87, 'P': 97, 'V': 99, 'T': 101, 'C': 103, 'I': 113,
                 'L': 113, 'N': 114, 'D': 115, 'K': 128, 'Q': 128, 'E': 129, 'M': 131,
                 'H': 137, 'F': 147, 'R': 156, 'Y': 163, 'W': 186}



def getMass(peptide):
    count = 0
    for i in peptide:count+=AminoAcidMass[i]
    return count


def subpeptides(peptide):
    l = len(peptide)
    ls = []
    looped = peptide
    for start in range(0, l):
        for length in range(1, l):
            ls.append((looped[start:start + length]))
    ls.append(peptide)
    return ls



def getMassSubpeptides(subpeps):
    ts = [0] 
    for subp in subpeps:
        subp_mass = 0 
        for l in subp: 
            subp_mass+=AminoAcidMass[l]
        ts.append(subp_mass)
    return ts

subpeps = subpeptides('AQV')
print(sorted(getMassSubpeptides(subpeps)))