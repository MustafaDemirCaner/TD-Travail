def est_monotone_croissante(liste):
    """Test si <liste> est une suite monotone croissante
    :param liste: (list)
    :return: (bool) True si <liste> est une suite monotone croissante, False sinon"""
    for i in range(len(liste) - 1):
        if liste[i] > liste[i+1]:
            return False
    return True
        
print(est_monotone_croissante([1,2,3,4,5,6]))

def est_monotone(liste):
    """Test si <liste> est une suite monotone
    :param liste: (list)
    :return: (bool) True si <liste> est une suite monotone, False sinon"""
    if est_monotone_croissante(liste):
        return True
    else:
        for i in range(len(liste) - 1):
            if liste[i] < liste[i+1]:
                return False
    return True

print(est_monotone([6,5,4,3,2,1]))
print(est_monotone([1,2,3,4,5,6]))
print(est_monotone([1,2,3,4,3,5,6]))