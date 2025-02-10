# Ejemplo sencillo de ordenamiento por el método Quick Sort
# Código en Python para usar en un cuaderno de Jupyter

def quick_sort(lista):
    """
    Función que implementa el método de ordenamiento Quick Sort.
    Se selecciona un elemento "pivote" y se divide la lista en dos sublistas:
    - elementos menores que el pivote
    - elementos mayores o iguales al pivote
    Luego se aplica recursividad para ordenar estas sublistas.
    """
    
    # Caso base: listas con 0 o 1 elementos ya están ordenadas
    if len(lista) < 2:
        return lista
    else:
        # Elegimos el primer elemento como pivote (podríamos elegir otro)
        pivote = lista[0]
        
        # Sublista de elementos menores que el pivote
        menores = [x for x in lista[1:] if x < pivote]
        
        # Sublista de elementos mayores o iguales al pivote
        mayores = [x for x in lista[1:] if x >= pivote]
        
        # Llamamos recursivamente a quick_sort en las sublistas
        return quick_sort(menores) + [pivote] + quick_sort(mayores)

# Ejemplo de uso
lista_ejemplo = [64, 34, 25, 12, 22, 11, 90]
print("Lista original:", lista_ejemplo)

lista_ordenada = quick_sort(lista_ejemplo)
print("Lista ordenada:", lista_ordenada)
