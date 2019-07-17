def distance(strand_a, strand_b):
    a = list(strand_a.lower())
    b = list(strand_b.lower())
    if len(a) != len(b):
        raise ValueError("Strings not same length")
    ret = []
    for i in range(len(a)):
        if a[i] != b[i]:
            ret.append(a[i])
    return len(ret)
