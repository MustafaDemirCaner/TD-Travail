def calcul_cout(legumes, quantites):
    """Retourne le coût d'une liste de courses
    :param legumes: (list) le coût de chaque légume
    :param quantites: (list) la quantité de chaque légume
    :return: (int ou float) le coût total de la liste de course"""
    toplam = 0
    for i in range(len(legumes)):
        toplam += legumes[i]*quantites[i]
    return toplam 

print(calcul_cout([9, 5, 12], [2, 1, 1]))
    


    # return (legumes[0]*quantites[0]) + (legumes[1]*quantites[1]) + (legumes[2]*quantites[2])