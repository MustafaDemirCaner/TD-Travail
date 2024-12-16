tableau = [
[0,0,0,0,0],
[0,1,2,3,4],
[0,2,4,6,8],
[0,3,6,9,12],
[0,4,8,12,16]]

tableau2 = [
[1,2,3,4,5],
[6,7,8,9,10],
[11,12,13,14,15],
[16,17,18,19,20],
[21,22,23,24,25]
]

def somme_ligne(position_ligne, tableau):
    """Calcul la somme des éléments de la ligne à <position_ligne> du <tableau>
    :param position_ligne: (int) la position d'une ligne du tableau
    :param tableau: (list) un tableau
    :return: (int) la somme des éléments de la ligne à <position_ligne> du <tableau>"""
    res = 0
    tmp = tableau[2]
    for i in tmp:
        res += i
    return res

print(somme_ligne(2, tableau))

def somme_colonne(position_colonne, tableau):
    """Calcul la somme des éléments de la colonne à <position_colonne> du <tableau>
    :param position_colonne: (int) la position d'une colonne du tableau
    :param tableau: (list) un tableau
    :return: (int) la somme des éléments de la colonne à <position_colonne> du <tableau>"""
    res = 0
    for i in tableau:
        res += i[position_colonne]
    return res

print(somme_colonne(1, tableau))

def somme_diagonale(diagonale, tableau):
    """Calcul de la somme des éléments sur la <diagonale>.
    Si <diagonale>=0 c'est la diagonale partant du coin supérieur gauche au coin inférieur droit,
    Si <diagonale>=1 c'est du coin inférieur gauche au coin supérieur droit.
    :param diagonale: (int) l'identifiant de la diagonale
    :param tableau: (list) un tableau
    :return: (int) la somme des éléments de la <diagonale> du <tableau>"""
    res = 0
    for i in range(len(tableau)):
        if diagonale == 0:
            res += tableau[i][i]
        else:
            res += tableau[len(tableau) - i - 1][i]
    return res

print(somme_diagonale(0, tableau))

def possede_elements_1_a_N(tableau):
    """Test si tous les éléments de 1 à N sont présent dans le <tableau> où N est le nombre de cases du
    <tableau>↪→
    :param grille: (list)
    :return: (bool) si tous les éléments de 1 à N sont présent dans le tableau"""
    # res= []
    # for i in tableau:
    #     for j in i:
    #         res.append(j)
    # for i in range(len(res) - 1):
    #     if res[i] != res[i + 1] - 1:
    #         return False
    # return True

    n = len(tableau)**2
    l = [ 0 for i in range(n)]
    for i in range(len(tableau)):
        for j in range(len(tableau[i])):
            if l[tableau[i][j]-1] == 0:
                l[tableau[i][j]-1]=1
            else:
                return False
    return sum(l) == len(l)


print(possede_elements_1_a_N(tableau2))