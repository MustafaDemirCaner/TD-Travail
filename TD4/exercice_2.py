def recherche_etudiant(numero_agora, etudiants):
    """Retourne le dictionnaire d'un étudiant si <numero_agora> est dans <liste_etudiants>
    :param numero_agora: (int) le numéro agora de l'étudiant
    :param liste_etudiants: (list) liste d'étudiants
    :return: (dict) le dictionnaire de l'étudiant <numero_agora>"""
    for i in etudiants:
        if i["numero_agora"] == numero_agora:
            return i

etudiants = [
    {"numero_agora" : 69377571, "nom" : "Snow", "prenom" : "Jon", "formation" : "SdN"},
    {"numero_agora" : 38301789, "nom" : "Uzumaki", "prenom" : "Naruto", "formation" : "M&N"},
    {"numero_agora" : 10815589, "nom" : "Stark", "prenom" : "Tony", "formation" : "SdN"},
    {"numero_agora" : 71001288, "nom" : "Cooper", "prenom" : "Sheldon", "formation" : "SdN"}
]

print(recherche_etudiant(10815589, etudiants))