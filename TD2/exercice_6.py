def est_palindrome(mot):
    """Retourne True si <mot> est un palindrome, False sinon
    :param mot: (str) un mot
    :return: (bool) True si <mot> est un palindrome, False sinon"""
    if mot[::-1] == mot:
        return True
    return False

print(est_palindrome("bob"))
print(est_palindrome("Hello"))