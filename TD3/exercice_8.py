def insertion(liste, element, position):
    """
    Insère un élément dans une liste à une position spécifiée et retourne une nouvelle liste.
    Paramètres:
    - liste (list): La liste dans laquelle on souhaite insérer l'élément
    - element: L'élément à insérer
    - position (int): La position à laquelle insérer l'élément
    Retourne:
    - list: Une nouvelle liste avec l'élément inséré
    """
    res = []
    for i in range(len(liste)):
        if i == position:
            res.append(element)
        res.append(liste[i])
    return res


print(insertion([1, 2, 3, 4], 5, 2))