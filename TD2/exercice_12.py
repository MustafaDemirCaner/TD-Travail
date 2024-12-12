def ADN_en_ARNm(sequence):
    """Retourne l'ARNm à partir de la <sequence>
    :param sequence: (str) une séquence d'ADN
    :return: (str) l'ARNm obtenue à partir de la <sequence>"""
    res = ''
    for i in sequence:
        if i == 'T':
            res += 'U'
        else:
            res += i
    return res

print(ADN_en_ARNm("GATGGAACTTGACTACGTAAATT"))