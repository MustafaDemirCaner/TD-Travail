def duel(symbole_1, symbole_2):
    """Affrontement entre deux joueurs au jeu Pierre-Papier-Ciseaux.
    La fonction doit retourner le symbole du gagnant. En cas d'égalité, la fonction retourne le
    ,→ symbole_1.
    :param symbole_1: Symbole choisi par le premier joueur.
    :param symbole_2: Symbole choisi par le second joueur.
    :return: Symbole du gagnant.
    Les symboles possibles sont 'R' (Rock - Pierre), 'P' (Paper - Feuille) et 'S' (Scissors - Ciseaux).
    """
    rules = {
        "R" : "S",
        "P" : "R",
        "S" : "P",
    }
    
    # DRAW
    if symbole_1 == symbole_2:
        return symbole_1
    
    # BATTLE
    if rules[symbole_1] == symbole_2:
        return symbole_1
    else:
        return symbole_2
    
print(duel("S", "R"))