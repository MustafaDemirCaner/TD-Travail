def est_minuscule(lettre):
    """retourne True si <lettre> est une lettre minuscule et False sinon.
    :param lettre: (str) lettre doit contenir un seul caractère.
    :return : (bool) True si <lettre> est une lettre minuscule; False sinon."""
    if lettre.islower():
        return True
    return False
#        97 <=        <= 122
#return 'a' <= lettre <= 'z'

print(est_minuscule("a"))
print(est_minuscule("A"))