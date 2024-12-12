def est_base(symbole):
    """Retourne True si la <symbole> est soit un A, un C, un T ou un G ; False sinon.
    :param symbole: (str)
    :return : (bool) True si <symbole> est soit un A, un C, un T ou un G ; False sinon."""
    if symbole == 'A' or symbole == 'C' or symbole == 'G' or symbole == 'T':
        return True
    return False


def est_code_genetique(sequence):
    """Retourne True si la chaine <sequence> est uniquement composée des lettres A, C, T et G ;
    False sinon.
    :param symbole: (str)
    :return : (bool)"""
    #ACGT N
    for i in sequence:
        # if not est_base(i):
        if est_base(i) == False:
            return False
    return True

print(est_code_genetique("ADN"))
print(est_code_genetique("ACGT"))