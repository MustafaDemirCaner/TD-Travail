def min(liste):
    """Retourne le plus petit élément de <liste>
    :param liste: (list)
    :return: (any) le plus petit élément de <liste>"""
    tmp = liste[0]
    for i in liste:
        if tmp > i:
            tmp = i
    return tmp

print(min([1,2,3,4,5]))
print(min([42,5,18,9,1]))