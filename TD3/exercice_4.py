def nb_occurences(element, liste):
    """
    Retourne le nombre d'occurrences de l'élément spécifié dans la liste donnée.
    Paramètres:
    - element: L'élément dont on veut compter le nombre d'occurrences
    - liste (list): La liste dans laquelle on souhaite compter les occurrences de l'élément
    Retourne:
    - int
    """
    cpt = 0
    for i in liste:
        if i == element:
            cpt += 1
    return cpt
        
print(nb_occurences(5, [1, 2, 3, 4, 5, 5, 6]))
print(nb_occurences("lucien", ["noe", "lucas", "adrien", "lucien", "serena", "laure", "nassim","antoine"]))