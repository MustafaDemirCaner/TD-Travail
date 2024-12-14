def creer_etudiant(numero_agora, nom, prenom, formation):
    """Créer un dictionnaire représentant un étudiant.
    :param numero_agora: (int) le numéro agora
    :param nom: (str) le nom
    :param prenom: (str) le prenom
    :param formation: (str) la formation
    :return: (dict) un dictionnaire d'étudiant"""
    return {'numero_agora': numero_agora,
            'nom':  nom, 
            'prenom': prenom, 
            'formation': formation}

print(creer_etudiant(10815589, "Stark", "Tony", "SdN"))
    