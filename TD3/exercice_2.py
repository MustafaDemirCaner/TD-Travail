def taille(liste):
    """Retourne la taille de <liste>
    :param liste: (list)
    :return: (int) la taille de <liste>"""
    count = 0
    for i in liste:
        count += 1
    return count

print(taille([1,2,3,4,5]))