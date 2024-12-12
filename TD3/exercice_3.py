def indice(element, liste):
    """Retourne l'indice de la première occurence de <element> dans <liste>
    :param element: (any) un élément
    :param liste: (list) une liste
    :return: (int) l'indice de la première occurence de <element> dans <liste>"""
    for i in range(len(liste)):
        if element == liste[i]:
            return i
    return -1
        
print(indice(3, [1, 2, 3, 4, 5]))