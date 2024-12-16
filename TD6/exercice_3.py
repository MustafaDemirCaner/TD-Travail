def cible(liste, c):
    """Recherche si une paire d'éléments dans la liste donne une somme égale à 'c'.
    Parameters:
    - liste (list): une liste d'éléments numériques
    - c (int or float): la valeur cible pour la somme
    Returns:
    bool: True si une paire d'éléments de la liste a une somme égale à 'c', False sinon"""
    for i in range(len(liste)):
        for j in range(len(liste)):
            if liste[i] + liste[j] == c and i != j:
                return True
    return False
    
#print(cible([14, 19, 22, 28, 14, 26, 40, 44, 5, 50], 51))

def recherche_dichotomique(liste, element):
    """
    Recherche `element` dans `liste` en utilisant la méthode de recherche dichotomique.
    Parameters:
    - liste (list): une liste triée d'éléments
    - element: l'élément à rechercher
    Returns:
    int: l'indice de l'élément dans la liste, ou -1 s'il n'est pas trouvé
    """
    for i in range(len(liste)):
        if liste[i] == element:
            return i
    return -1

def cible2(liste, c):
    """Recherche si une paire d'éléments dans la liste donne une somme égale à 'c'.
    Parameters:
    - liste (list): une liste d'éléments numériques
    - c (int or float): la valeur cible pour la somme
    Returns:
    bool: True si une paire d'éléments de la liste a une somme égale à 'c', False sinon"""
    for elt in liste:
        #                         liste, 51 - elt
        if recherche_dichotomique(liste, c - elt) != -1:
            return True
    return False

print(cible2([5, 14, 19, 22, 25, 27, 29, 40, 44, 50], 50))