def correction_QCM(reponses_etudiant, reponses_valides):
    """
    Calcule et renvoie le score d'un étudiant pour un QCM en fonction de ses réponses et des réponses
    ,→ valides.
    Paramètres:
    - reponses_etudiant (dict): Dictionnaire contenant les réponses fournies par l'étudiant.
    - reponses_valides (dict): Dictionnaire contenant les bonnes réponses pour le QCM.
    Retourne:
    - int: Le score total de l'étudiant pour le QCM.
    Règles de notation :
    - 3 points pour chaque bonne réponse.
    - -1 point pour chaque mauvaise réponse.
    - 0 point pour une question non répondue.
    """
    score = 0
    for i in reponses_valides:
        tmp = reponses_etudiant.get(i)
        if reponses_valides[i] == tmp:
            score += 3
        elif tmp == None:
            score += 0
        else:
            score -= 1
    return score






reponses_valides = {"mot_cle_boucle_pour":"for", "mot_cle_retour":"return", "langage_fondamentaux_prog":"python", "mot_cle_fonction":"def"}
reponses_etudiant = {"mot_cle_boucle_pour":"for", "langage_fondamentaux_prog":"java", "mot_cle_fonction":"def"}

print(correction_QCM(reponses_etudiant, reponses_valides))