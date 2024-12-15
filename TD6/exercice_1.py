def recherche_sequentielle(liste, valeur):
    """
    Effectue une recherche séquentielle d'une valeur dans une liste.
    Paramètres :
    - liste (list): La liste dans laquelle effectuer la recherche.
    - valeur (any): La valeur à rechercher dans la liste.
    Retourne :
    int: l'indice de l'élément dans la liste, ou -1 s'il n'est pas trouvé
    """
    for i in range(len(liste)):
        if liste[i] == valeur:
            return i
    return -1



print(recherche_sequentielle([1, 2, 3, 4, 5], 3))