def moyenne(liste):
    """Retourne la moyenne des éléments de <liste>
    :param liste: (list)
    :return: (float) la moyenne des éléments de <liste>"""
    cpt = 0
    for i in liste:
        cpt += i
    return cpt / len(liste)