from collections import defaultdict

def ordenacion_topologica(restricciones):
    """
    Calcula una ordenación topológica de las tareas cumpliendo las restricciones.
    
    Args:
    restricciones: lista de pares (i, j) donde i precede a j.
    
    Returns:
    Una lista con la ordenación topológica de las tareas, o None si no es posible cumplir todas las restricciones.
    """
    # Construir el grafo dirigido a partir de las restricciones
    grafo = defaultdict(list)
    for precedente, siguiente in restricciones:
        grafo[precedente].append(siguiente)
    
    # Función DFS para realizar el recorrido y obtener la ordenación topológica
    def dfs(v, visitados, en_proceso, orden):
        if v in en_proceso:
            return False  # Se ha detectado un ciclo
        if v in visitados:
            return True   # Ya se ha visitado este nodo
        
        en_proceso.add(v)
        for vecino in grafo[v]:
            if vecino in visitados:
                continue
            if vecino in en_proceso or not dfs(vecino, visitados, en_proceso, orden):
                return False
        
        en_proceso.remove(v)
        visitados.add(v)
        orden.append(v)
        return True
    
    visitados = set()
    orden = []
    
    # Realizar el recorrido DFS para obtener la ordenación topológica
    for tarea in list(grafo.keys()):  # Copia de las claves
        if tarea not in visitados:
            en_proceso = set()
            if not dfs(tarea, visitados, en_proceso, orden):
                return None  # No es posible cumplir todas las restricciones
    
    return list(reversed(orden))  # Devolver la ordenación topológica invertida

# Ejemplo de uso
restricciones = [(1, 2), (1, 3), (2, 4), (3, 4), (4, 5)]
orden = ordenacion_topologica(restricciones)
if orden is None:
    print("No es posible cumplir todas las restricciones.")
else:
    print("Ordenación topológica:", orden)
