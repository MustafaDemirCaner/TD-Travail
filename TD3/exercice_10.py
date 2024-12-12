def suppression(element, liste):
    """Supprime la première occurrence de l'élément spécifié dans la liste donnée et retourne une
    ,→ nouvelle liste.
    Cette fonction ne modifie pas la liste originale, mais crée plutôt une nouvelle liste avec la
    ,→ première occurrence de l'élément supprimé.
    Paramètres:
    - element: L'élément à supprimer
    - liste (list): La liste dans laquelle on souhaite supprimer l'élément
    Retourne:
    - list: Une nouvelle liste avec la première occurrence de l'élément supprimé. Si l'élément n'est
    ,→ pas dans la liste, retourne la liste originale."""
    # liste.remove(element)
    res = []
    for i in liste:
        if i == element:
            element = None
        else:
            res.append(i)
    return res

print(suppression(5, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 5]))
