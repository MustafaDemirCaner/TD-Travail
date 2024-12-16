def somme_entiers_rec_term(n, acc=0):
    """Somme des entiers de 1 à n
    :param n: (int) un entier
    :param acc: (int) l'accumulateur
    :return: (int) la somme des entiers de 1 à n"""
    if n == 0:
        return acc    
    else: 
        acc = n + somme_entiers_rec_term(n - 1)
    return acc

print(somme_entiers_rec_term(4))