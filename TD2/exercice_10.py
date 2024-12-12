def est_base(symbole):
    """Retourne True si la <symbole> est soit un A, un C, un T ou un G ; False sinon.
    :param symbole: (str)
    :return : (bool) True si <symbole> est soit un A, un C, un T ou un G ; False sinon."""
    if symbole == 'A' or symbole == 'C' or symbole == 'G' or symbole == 'T':
        return True
    return False

print(est_base("A"))