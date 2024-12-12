def est_monotone_croissante(liste):
    """Test si <liste> est une suite monotone croissante
    :param liste: (list)
    :return: (bool) True si <liste> est une suite monotone croissante, False sinon"""
    for i in range(len(liste) - 1):
        if liste[i] > liste[i+1]:
            return False
    return True
        
print(est_monotone_croissante([1,2,3,4,5,6]))