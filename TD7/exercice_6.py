def triangle(n):
    """Affiche un triangle de hauteur <n>
    :param n: (int) hauteur du triangle
    :return: (str) la chaîne correspondant au triangle"""
    # \n
    if n <= 0:
        return ''
    res = ''
    res = triangle(n - 1) + (n * '#') + '\n'
    return res




print(triangle(5))