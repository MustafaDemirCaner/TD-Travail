def complement(sequence):
    """Retourne le complément de la <sequence>
    :param sequence: (str) Une séquence d'ADN
    :return: (str) Le complément de la <sequence>"""
    res = ''
    for i in sequence:
        if i == 'A':
            res += 'T'
        elif i == 'T':
            res += 'A'
        elif i == 'C':
            res += 'G'
        elif i == 'G':
            res += 'C'
        else:
            res += i
    return res

print(complement("AAAACCCGGT"))
