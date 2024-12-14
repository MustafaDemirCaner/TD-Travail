def points_scrabble(mot):
    """Calcule et renvoie le score d'un mot donné selon les règles du Scrabble.
    Paramètres:
    - mot (str): Le mot dont on souhaite connaître le score. Le mot doit être en majuscules et sans
    ,→ accents.
    Retourne:
    - int: Le score total du mot selon les règles du Scrabble.
    """
    score_lettre={"A":1,"B":3,"C":3,"D":2,"E":1,"F":4,"G":2,"H":4,"I":1,"J":8,"K":10,"L":1,"M":2,"N":1,"O":1,"P":3}
    
    cpt = 0
    for i in mot:
        cpt += score_lettre[i]
    return cpt
        
print(points_scrabble("ABC"))