def tete_a_toto(n):
    """Returne la chaîne de caractère de la tête de toto
    :param n: (int) le niveau de reflet
    :return: (str) la tête et le reflet de ses yeux"""
# n+1 ((0 + 0))
# 2
# (((0 + 0) + (0 + 0)) + ((0 + 0) + (0 + 0)))
    if n <= 0:
        return '(0 + 0)'
    else:
        return '(' + tete_a_toto(n - 1) + " + " + tete_a_toto(n - 1) + ')'
    

print(tete_a_toto(1))