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

def jouer_manche(appariements):
    """La fonction doit retourner le symbole du gagnant de chaque duel pour une manche d'un tournoi à
    ,→ élimination directe.
    :param appariements: (str) appariements pour le tournoi, chaque paire de symboles represente un
    ,→ duel.
    :return: (str) symboles du gagnant de chaque duel.
    """
    res = ""
    for i in range(0, len(appariements) - 1, 2):
        res += duel(appariements[i], appariements[i + 1])
    return res

print(jouer_manche("PRRRSSSR"))

def jouer_tournoi(appariements):
    """La fonction doit retourner le symbole du gagnant d'un tournoi à élimination directe.
    :param appariements: (str) appariements initiaux pour le tournoi, chaque paire de symboles
    ,→ représente un duel.
    :return: (str) symbole du gagnant du tournoi.
    """
    res = appariements
    while (len(res) != 1):
        res = jouer_manche(res)
    return res

print(jouer_tournoi("PRRRSSSR"))

def jouer_tournoi2(appariements):
    """La fonction doit retourner le symbole du gagnant d'un tournoi à élimination directe.
    :param appariements: (str) appariements initiaux pour le tournoi, chaque paire de symboles
    ,→ représente un duel.
    :return: (str) symbole du gagnant du tournoi.
    """
    rules = {
        "R" : ["S", "L"],
        "P" : ["R", "Y"],
        "S" : ["L", "P"],
        "L" : ["P", "Y"],
        "Y" : ["S", "R"],
    }
    while (len(appariements) != 1):
        res = ""
        for i in range(0, len(appariements) - 1, 2):
            if appariements[i] == appariements[i + 1]:
                res += appariements[i]
            elif appariements[i + 1] in rules[appariements[i]]:
                res += appariements[i]
            else:
                res += appariements[i + 1]
        appariements = res
    return appariements
    #appariements = 'aaaaaa'
                                    
    



print(jouer_tournoi2("PPSSYPPYRYRRRRPR"))
