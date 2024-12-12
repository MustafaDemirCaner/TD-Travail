def chiffrer_cesar(msg, decalage):
    """Chiffre le message <msg> en utilisant le chiffrement de César avec le décalage spécifié.
    :param msg: (str) Le message à chiffrer. Seules les lettres de l'alphabet latin non accentuées
    ,→ seront chiffrées.
    :param decalage: (int) Le décalage à appliquer pour le chiffrement. Si le décalage est positif, les
    lettres seront décalées vers la droite. Si le décalage est négatif, elles seront décalées vers la
    gauche.
    ,→
    ,→
    :return: (str) Le message chiffré.
    Remarque:
    Cette fonction suppose que toutes les lettres du message sont en majuscule et ne contiennent pas de
    ,→ carac"""
    res = ""
    decalage = decalage % 26
    for i in msg:
        # A
        #       88    + 8        > 90
        if chr(ord(i) + decalage) > "Z":
            res += chr((ord(i) + decalage) - 90 + ord("A"))
        else: 
            res += chr(ord(i) + decalage)
    return res

def vigenere(msg, cle):
    """Chiffre le texte selon le chiffrement de Vigénère avec la clé donnée.
    :param texte: (str) le texte à chiffrer
    :param cle: (str) la clé de chiffrement
    :return: (str) le texte chiffré"""
    l = 0
    res = ""
    print(ord("O") - ord("A"))
    for i in range(len(msg)):
        if l >= len(cle):
            l = 0
        res += chr(((ord(cle[l]) - 65) - (ord(msg[i]) - 65) + 26) % 26)
        #res += chiffrer_cesar(cle[l], ord(msg[i]) - 65)
        l += 1
    return res

print(vigenere("MONMESSAGESECRET", "MYSTERE"))
