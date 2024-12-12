def nom_mois(num):
    """Retourne le nom du mois numéro <num>
    :param num: (int) Numéro entre 1 et 12
    :return: (str) Le nom du mois"""
    les_mois= [
        'Janvier',
        "Février",
        "Mars",
        "Avril",
        "Mai",
        "Juin",
        "Juillet",
        "Aout",
        "Septembre",
        'Octobre',
        'Novembre',
        'Décembre'
    ]
    
    if 13 > num > 0:    
        return les_mois[num - 1] 
    else:
        return "n'existe pas"
    
print(nom_mois(42))
print(nom_mois(5))
