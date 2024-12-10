def nb_occurences(mot, lettre):
    """Retourne le nombre d'occurences de <lettre> dans le <mot>
    :param mot: (str) Le mot
    :param lettre: (str) La lettre à compter
    :return: (int) le nombre d'occurences de <lettre> dans le <mot>"""
    nb = 0
    for i in mot:
        if i == lettre:
            nb += 1
    return nb

print(nb_occurences("kamehameha", "a"))