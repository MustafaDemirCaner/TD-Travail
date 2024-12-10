def substitution(phrase, lettre1, lettre2):
    """Substitue les <lettre1> par <lettre2> dans la <phrase>
    :param phrase: (str) la phrase
    :param lettre1: (str) la lettre à remplacer
    :param lettre2: (str) la lettre qui remplace
    :return: (str) La <phrase> avec les lettres substituées"""
    res = ''
    for i in phrase:
        if i == lettre1:
            res += lettre2
        else:
            res += i
    return res

print(substitution('chut', 'u', 'a'))