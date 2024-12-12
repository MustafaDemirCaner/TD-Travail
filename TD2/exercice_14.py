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

def complement_inverse(sequence):
    """Retourne le complément inverse de la <sequence>
    :param sequence: (str) Une séquence d'ADN
    :return: (str) Le complément inverse de la <sequence>"""
    res = ''
    for i in sequence:
        res = i + res
    return complement(res)

print(complement_inverse("ATGCGCTAGCTCATTT"))