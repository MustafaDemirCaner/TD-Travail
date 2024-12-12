def somme(liste):
    """Retourne la somme des éléments de <liste>
    :param liste: (list) la liste des éléments
    :return: (int) la somme des éléments de <liste>"""
    cpt = 0
    for i in liste:
        cpt += i
    return cpt

print(somme([1,2,3,4,5]))