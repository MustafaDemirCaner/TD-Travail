def recherche_formation(formation, etudiants):
    """Retourne les étudiants de <formation> dans <liste_etudiants>
    :param formation: (str) le nom de la formation
    :param liste_etudiants: (list) liste d'étudiants
    :return: (list) La liste d'étudiants de <formation>"""
    res = []
    for i in etudiants:
        if i['formation'] == 'SdN':
            res.append(i)
            # res += i
    return res

etudiants = [
{"numero_agora" : 69377571, "nom" : "Snow", "prenom" : "Jon", "formation" : "SdN"},
{"numero_agora" : 38301789, "nom" : "Uzumaki", "prenom" : "Naruto", "formation" : "M&N"},
{"numero_agora" : 10815589, "nom" : "Stark", "prenom" : "Tony", "formation" : "SdN"},
{"numero_agora" : 71001288, "nom" : "Cooper", "prenom" : "Sheldon", "formation" : "SdN"},
]

print(recherche_formation("SdN", etudiants))