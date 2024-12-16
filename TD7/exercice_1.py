def somme_entiers_rec(n):
    """Somme des entiers de 1 à n
    :param n: (int) un entier
    :return: (int) la somme des entiers de 1 à n"""
    while (n > 0):
        return n + somme_entiers_rec(n - 1)
    return 0
    
print(somme_entiers_rec(3))

