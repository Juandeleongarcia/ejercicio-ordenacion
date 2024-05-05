def ordenacion_insercion_dicotomica(t):
    """
    Procedimiento que ordena la lista t utilizando el método de inserción dicotómica.
    Args:
    t: lista de elementos comparables.
    Precondición:
    - t no está vacío y sus elementos son comparables.
    Postcondición:
    - Los elementos de t están ordenados en su lugar en orden creciente.
    """
    def busqueda_dicotomica(t, elemento, inicio, fin):
        """
        Función que realiza una búsqueda dicotómica para encontrar la posición de inserción de un elemento en una lista ordenada.
        Args:
        t: lista ordenada de elementos comparables.
        elemento: elemento a insertar en la lista.
        inicio: índice inicial de búsqueda.
        fin: índice final de búsqueda.
        Returns:
        La posición de inserción del elemento en la lista.
        """
        if inicio > fin:
            return inicio
        else:
            medio = (inicio + fin) // 2
            if elemento <= t[medio]:
                return busqueda_dicotomica(t, elemento, inicio, medio - 1)
            else:
                return busqueda_dicotomica(t, elemento, medio + 1, fin)

    # Algoritmo principal de ordenación por inserción dicotómica
    for i in range(1, len(t)):
        elemento_actual = t[i]
        posicion = busqueda_dicotomica(t, elemento_actual, 0, i - 1)
        for j in range(i, posicion, -1):
            t[j] = t[j - 1]
        t[posicion] = elemento_actual

# Ejemplo de uso
lista = [5, 3, 2, 4, 6, 8, 1, 7, 6, 5, 4]
print("Lista original:", lista)
ordenacion_insercion_dicotomica(lista)
print("Lista ordenada:", lista)
