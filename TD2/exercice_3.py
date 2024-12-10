def tisser(phrase, symbole):
    """Retourne la version tissée par le <symbole> de <phrase>
    :param phrase: (str) la phrase à tisser
    :param symbole: (str) le symbole de l"""
    res = ''
    for i in phrase:
        if i == ' ':
            res += symbole
        else:
            res += i
    return res

print(tisser("Une phrase tirée par les cheveux", "-"))
            
