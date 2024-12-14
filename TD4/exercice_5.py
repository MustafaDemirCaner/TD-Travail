def frequence(phrase):
    """Calcule et renvoie la fréquence de chaque lettre dans une phrase donnée.
    Paramètres:
    - phrase (str): La phrase dont on souhaite connaître la fréquence des lettres.
    Retourne:
    - dict: Un dictionnaire contenant chaque lettre comme clé et sa fréquence comme valeur.
    """

    res = {}
    #res["G"] = 2
    #res.update({"G": 1})
    for i in phrase:
        res[i] = phrase.count(i)
        # res.update({i, phrase.count(i)})
    return res

print(frequence("bonjour")) # {'b': 1, 'o': 2, 'n': 1, 'j': 1, 'u': 1, 'r': 1}