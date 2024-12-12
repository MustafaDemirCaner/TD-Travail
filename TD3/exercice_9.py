def filtre_pairs(liste):
    """Retourne une nouvelle liste contenant uniquement les éléments pairs de la liste donnée.
    Paramètres:
    - liste (list): La liste d'entiers à filtrer
    Retourne:
    - list: Une nouvelle liste contenant uniquement les éléments pairs de la liste originale"""
    res = []
    for i in liste:
        if i % 2 == 0:
            res.append(i)
    return res

print(filtre_pairs([1,2,3,4,5,6,7,8,9,10]))