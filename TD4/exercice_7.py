def conversion_romain_entier(nombre_romain):
    """Convertit un nombre romain en un nombre entier.
    Paramètres:
    - nombre_romain (str): Le nombre romain à convertir.
    Retourne:
    - int: La valeur entière correspondant au nombre romain.
    """
    valeurs_romaines = {'I': 1,'V': 5,'X': 10,'L': 50,'C': 100,'D': 500,'M': 1000 }
    total = 0
    prev_value = 0

    for key in reversed(nombre_romain):
        current_value = valeurs_romaines[key]
        if current_value < prev_value:
            total -= current_value
        else:
            total += current_value
        prev_value = current_value
    return total

print(conversion_romain_entier('XIV'))