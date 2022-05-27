
AminoAcidMass = {'G': 57, 'A': 71, 'S': 87, 'P': 97, 'V': 99, 'T': 101, 'C': 103, 'I': 113,
                 'L': 113, 'N': 114, 'D': 115, 'K': 128, 'Q': 128, 'E': 129, 'M': 131,
                 'H': 137, 'F': 147, 'R': 156, 'Y': 163, 'W': 186}


def cyclepeptide(peptide):
    l = len(peptide)
    ls = []
    looped = peptide + peptide
    for start in range(0, l):
        for length in range(1, l):
            ls.append((looped[start:start + length]))
    ls.append(peptide)
    return ls


def linear_spectrum(peptide):
	prefix_mass = [0 for x in range(len(peptide) + 1)]
	for i in range(1,len(peptide)+1):
		prefix_mass[i] = prefix_mass[i-1] + int(AminoAcidMass[str(peptide[i-1])])
	linear = []
	for i in range(len(peptide)):
		for j in range(i+1,len(peptide)+1):
			linear.append(prefix_mass[j] - prefix_mass[i])
	linear.append(0)	
	return sorted(linear)


def getMassSubpeptides(subpeps):
    ts = [0] 
    for subp in subpeps:
        subp_mass = 0 
        for l in subp: 
            subp_mass+=AminoAcidMass[l]
        ts.append(subp_mass)
    return ts

def Score(ts,rs):
    #ts = theoretical spectrum
    #rs = real (experimental) spectrum | noisy 
    score = 0 
    for i in rs:
        if i in ts:
            score += 1
            ts.remove(i)
    return score


def Convoluted(spectral):
    dic = {}
    ls = [] 
    sorted(spectral)
    for i in spectral:
        for u in spectral:
            if u > i:
                if str(u-i) not in dic.keys(): dic[str(u-i)] = 1
                else:dic[str(u-i)] += 1
    for key in dic.keys():
        for i in range(dic[key]):ls.append(int(key))
    return ls

def ScoredConvolutedAAs(spectral,m):
    dic = {}
    ls = [] 
    sorted(spectral)
    for i in spectral:
        for u in spectral:
            if u > i and (u-i) > 57 and (u-i) < 200:
                if str(u-i) not in dic.keys(): dic[str(u-i)] = 1
                else:dic[str(u-i)] += 1
    dic = dict(sorted(dic.items(), key = lambda x: x[1], reverse = True))
    dic = {k:dic[k] for k in list(dic.keys())[:m]}
    list_dic = [int(i) for i in dic.keys()]
    return list_dic



ls = linear_spectrum('PEEP')
rs = [int(i) for i in '0 97 97 97 100 129 194 226 226 226 258 323 323 355 393 452'.split()]
print(Score(ls,rs))

