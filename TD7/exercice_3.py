def fibonacci(n):
    """Retourne la valeur du <n>-ième de la suite de Fibonacci
    :param n: (int) Le rang de la suite
    :return: (int) Le <n>-ième terme de Fibonacci"""
    # 0 1 2 3 4 5
    # 0 1 1 2 3 5
    if n < 2:
        return n 
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(5))