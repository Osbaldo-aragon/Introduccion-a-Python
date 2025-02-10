# Ejemplo sencillo para medir el tiempo de ejecución de una función en Python
# Código en Python para usar en un cuaderno de Jupyter

import time

def funcion_ejemplo():
    """
    Función de ejemplo que realiza una operación que consume algo de tiempo.
    En este caso, simplemente hacemos una sumatoria en un bucle.
    """
    suma = 0
    for i in range(1_000_000):
        suma += i
    return suma

# Registramos el tiempo antes de llamar a la función
inicio = time.time()

# Llamamos a la función
resultado = funcion_ejemplo()

# Registramos el tiempo después de llamar a la función
fin = time.time()

# Calculamos la diferencia para obtener el tiempo total de ejecución
tiempo_ejecucion = fin - inicio

print("Resultado de la función:", resultado)
print("Tiempo de ejecución:", tiempo_ejecucion, "segundos")
