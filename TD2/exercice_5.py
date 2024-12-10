def est_garemaman(mot1, mot2):
    """Retourne True si <mot1> est anagramme de <mot2>, False sinon
    :param mot1: (str) le premier mot
    :param mot2: (str) le second mot
    :return: (str) True si <mot1> est anagramme de <mot2>, False sinon"""

    return sorted(mot1) == sorted(mot2)

    # for i in mot1:
    #     if nb_occurences(mot1, i) != nb_occurences(mot2, i):
    #         return False
    # return True

    # if len(mot1) != len(mot2):
    #     return False

    # char_count = {}
    # for char in mot1:
    #     char_count[char] = char_count.get(char, 0) + 1

    # for char in mot2:
    #     if char not in char_count:
    #         return False
    #     char_count[char] -= 1
    #     if char_count[char] < 0:
    #         return False
    # return True

print(est_garemaman("anagramme", "garemaman"))