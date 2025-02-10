# Ejemplo sencillo de ordenamiento por el método burbuja (Bubble Sort)
import time
def bubble_sort(lista):
    """
    Función que implementa el método de ordenamiento burbuja.
    Recorre la lista repetidamente y en cada pasada compara 
    pares de elementos adyacentes, intercambiándolos si están 
    en el orden equivocado.
    """
    # Recorremos la lista tantas veces como elementos tenga
    for i in range(len(lista)):
        # En cada pasada, comparamos e intercambiamos elementos adyacentes
        for j in range(0, len(lista) - i - 1):
            # Si el elemento actual es mayor que el siguiente, los intercambiamos
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                time.sleep(2)
    
    return lista

# Ejemplo de uso
lista_ejemplo = [64, 34, 25, 12, 22, 11, 90]
print("Lista original:", lista_ejemplo)

lista_ordenada = bubble_sort(lista_ejemplo)
print("Lista ordenada:", lista_ordenada)
