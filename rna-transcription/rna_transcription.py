def to_rna(dna_strand):
    dna_strand = dna_strand.upper()
    rna_list = list(dna_strand)
    for x in range(len(rna_list)):
        if rna_list[x] == 'G':
            rna_list[x] = 'C'
        elif rna_list[x] == 'C':
            rna_list[x] = 'G'
        elif rna_list[x] == 'T':
            rna_list[x] = 'A'
        elif rna_list[x] == 'A':
            rna_list[x] = 'U'
        else:
            raise ValueError("Unsupported Character")
    rna_strand = "".join(rna_list)
    return rna_strand