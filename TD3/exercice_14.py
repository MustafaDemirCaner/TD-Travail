def element_unique(liste):
    """ Trouve et renvoie l'élément de la liste qui apparaît une seule fois.
    Paramètres:
    - liste (list): La liste d'éléments à analyser.
    Retourne:
    - L'élément qui apparaît une seule fois dans la liste.
    """
    for i in liste:
        if liste.count(i) == 1:
            return i
    return -1

print(element_unique([1,2,3,4,3,2,1]))