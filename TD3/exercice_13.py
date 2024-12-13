def minusculer(mot):
    """Retourne <mot> avec sa première lettre passée en minuscule
    :param mot: (str) le mot
    :return: (str) le mot avec la première lettre en minuscule"""
    mot1 = ''
    mot1 += mot[0].lower()
    for i in range(1, len(mot)):
        mot1 += mot[i]
    return mot1

print(minusculer("doiS")) 
print(minusculer("Tu"))

def decouper_avant(phrase, separateur):
    """Retourne le premier morceau de <phrase> selon le <separateur>
    :param phrase: (str) la phrase
    :param separateur: (str) le séparateur des morceaux d"""
    # res = ''
    # for i in phrase:
    #     if i == separateur:
    #         break
    #     res += i
    # return res
    if separateur in phrase:
        return phrase[:phrase.index(separateur)]
    else:
        return phrase

print(decouper_avant("Tu dois parler comme Yoda", " "))


def decouper_apres(phrase, separateur):
    """Retourne le morceau de <phrase> situé après la première occurence du <separateur>
    :param phrase: (str) la phrase
    :param separateur: (str) le séparateur des morceaux de la phrase
    :return: (str) le morceau de la phrase situé après la première occurence du <separateur>"""
    # res = ''
    # seen_sep = False
    # for i in phrase:
    #     if i == separateur:
    #         seen_sep = True
    #         separateur = None
    #         continue
    #     if seen_sep == True:
    #         res += i
    # return res
    if separateur in phrase:
        return phrase[phrase.index(separateur)+1:]
    else:
        return ""

print(decouper_apres("Tu dois parler comme Yoda", " "))

def decouper_tout(phrase, separateur):
    """Retourne la liste des morceaux de <phrase> selon le <separateur>
    :param phrase: (str) la phrase
    :param separateur: (str) le séparateur des morceaux de la phrase
    :return: (list) les morceaux de la phrase selon le <separateur>"""
    return phrase.split(separateur)

print(decouper_tout("Tu dois parler comme Yoda", " "))

def supprimer_indice(liste, indice):
    """Retourne <liste> l'élément à la position <indice>
    :param liste: (list)
    :param indice: (int) la position de l'élément à supprimer
    :return: (list) la liste sans l'élément à la position <indice>"""
    return liste[:indice] + liste[indice + 1:]

print(supprimer_indice(["Tu", "dois", "parler", "comme", "Yoda"], 2))

def reinserer(liste, indice_source, indice_destination):
    """Resinsere l'element de la position <indice_source> à la position <indice_destination>
    :param liste: (list)
    :param indice_source: (int) position de départ
    :param indice_destination: (int) position d'arrivée
    :return: (list) retourne la liste avec le mot à sa nouvelle position
    """
    tmp = supprimer_indice(liste,indice_source)
    # tmp = ["dois", "parler", "comme", "Yoda"]
    if indice_destination < len(tmp):
        #       ["dois", "parler"              "Tu"                     "comme", "Yoda"]
        # reinserer(["Tu", "dois", "parler", "comme", "Yoda"], 0, 2)
        return tmp[:indice_destination] + [liste[indice_source]] + tmp[indice_destination:]
    else:
        # ["dois", "parler", "comme", "Yoda"]  "Tu" 
        # reinserer(["Tu", "dois", "parler", "comme", "Yoda"], 0, 4)
        return tmp + [liste[indice_source]]
    
print(reinserer(["Tu", "dois", "parler", "comme", "Yoda"], 0, 4))
    
def joindre(liste, jointure):
    """Retourne la chaîne de caractères composé des éléments de <liste> et liés par la <jointure>
	:param liste: (list) 
	:param jointure: (str) le symbole de liaison
	:return: (str) la chaîne liée par la jointure"""
    return jointure.join(liste)

print(joindre(["Tu", "dois", "parler", "comme", "Yoda"], " "))

def anastropher(phrase):
    """Retourne l'anastrophe de la <phrase>
    :param phrase: (str)
    :return: (str) la phrase anastrophée"""
    liste = decouper_tout(phrase,' ')
    # ["Tu", "dois", "parler", "comme", "Yoda"]

    liste[0] = minusculer(liste[0])
    # ["tu", "dois", "parler", "comme", "Yoda"]

    liste = reinserer(liste,0,len(liste))
    # ["dois", "parler", "comme", "Yoda", "tu"]

    liste = reinserer(liste,0,len(liste))
    # ["parler", "comme", "Yoda", "tu", "dois"]


    liste[0] = liste[0][0].upper() + liste[0][1:]
    #          p -> P                arler

    return joindre(liste,' ')

print(anastropher("Tu dois parler comme Yoda"))
