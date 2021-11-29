def reading_fasta(filename):
    seq = ''
    f = open(filename, 'r')
    
    for line in f:
        line = line.rstrip()
        
        if line.startswith('>'):
            pass
        else:
            seq = seq + line
    
    f.close()
    return seq

file_dir = 'fasta_files\X73525.txt'
reading_fasta(file_dir)