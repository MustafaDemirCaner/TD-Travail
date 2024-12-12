def hamming_distance(adn_1, adn_2):
    """Retourne la distance de Hamming entre <adn_1> et <adn_2>.
    :param adn_1: (str) une séquence d'ADN
    :parma adn_2: (str) une séquence d'ADN
    :return: (int) la distance de Hamming entre <adn_1> et <adn_2>"""
    res = 0
    # ACGT s1
    # GTCA s2
    for i in range(len(adn_1)):
        if adn_1[i] != adn_2[i]:
            res += 1
    return res

print(hamming_distance("GAGCCTACTAACGGGAT", "CATCGTAATGACGGCCT"))
        
