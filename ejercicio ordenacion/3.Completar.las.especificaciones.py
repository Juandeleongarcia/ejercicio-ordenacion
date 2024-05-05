from typing import TypeVar, List

T = TypeVar('T', int, float, str)  # Tipo de datos de la tabla

def está_explorado(t: List[T], inicio: int, fin: int) -> bool:
    """
    Determina si la parte de la tabla t desde el índice inicio hasta el índice fin
    contiene segmentos explorados según la definición dada.
    Args:
    t: La tabla de componentes.
    inicio: El índice de inicio del rango en la tabla.
    fin: El índice de fin del rango en la tabla.
    Returns:
    True si todos los segmentos en el rango están explorados, False en caso contrario.
    """
    # Verificar si hay al menos un segmento
    if inicio > fin:
        return False
    
    segmentos = []  # Lista para almacenar los segmentos en el rango dado
    
    # Encontrar los segmentos en el rango dado
    i = inicio
    while i <= fin:
        max_segmento = t[i]  # Valor máximo del segmento
        j = i + 1
        while j <= fin and t[j] >= max_segmento:
            max_segmento = t[j]
            j += 1
        segmentos.append((i, j - 1))
        i = j
    
    # Verificar las condiciones de los segmentos
    for inicio_segmento, fin_segmento in segmentos:
        if t[inicio_segmento] != max(t[inicio_segmento: fin_segmento + 1]):
            return False
        if fin_segmento < fin and max(t[inicio_segmento: fin_segmento + 1]) >= t[fin_segmento + 1]:
            return False
    
    return True

# Ejemplo de uso
tabla = [7, 8, 10, 18, 17, 14, 15, 16, 18, 20, 21, 19]
inicio = 5
fin = 10
if está_explorado(tabla, inicio, fin):
    print("El rango dado contiene segmentos explorados.")
else:
    print("El rango dado no contiene segmentos explorados.")
