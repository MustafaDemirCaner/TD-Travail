# demir
# d r 
# e i
# rimed
def miroir(mot):
    """Retourne le miroir de <mot>
    :param mot: (str) un mot
    :return: (str) le miroir du mot"""
    res = ''
    for lettre in mot:
        res = lettre + res
        # print(res)
    return res 

print(miroir("demir"))