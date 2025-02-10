## Repositorio de Ejemplos Introductorios de Python y Lógica de Programación
### En este repositorio se incluyen programas y ejercicios básicos diseñados para quienes inician en el mundo de la programación con Python. Cada ejemplo aborda conceptos fundamentales de lógica de programación, estructuras de control y manipulación de datos, con el fin de reforzar las bases necesarias para proyectos más avanzados.

## Método de Ordenamiento Burbuja

En el método de ordenamiento Burbuja, cada elemento de la lista o arreglo se compara con el siguiente (su elemento adyacente). Si el elemento actual es mayor que el siguiente (considerando un orden ascendente), se intercambian sus posiciones; de lo contrario, se mantienen como están. Una vez realizada la comparación y posible intercambio, se avanza al siguiente par de elementos, repitiendo el proceso para todos los pares de la lista.
Este procedimiento se repite varias veces (pasadas) hasta que la lista queda completamente ordenada. Con cada pasada, el elemento más grande entre los que aún no están en su posición correcta “burbujea” hacia el final de la lista, quedando en su posición definitiva.
Si el tamaño de la lista (o arreglo) es *n*:

<p align="center">
  <img src="https://codepumpkin.com/wp-content/uploads/2017/10/BubbleSort_Avg_case.gif">
</p>

- **En la primera pasada**, se necesitan $n-1$ comparaciones. Por ejemplo, si la lista tiene 9 elementos, se hacen 8 comparaciones para “empujar” el mayor de todos hacia el final.
- **En la segunda pasada**, se necesitan $n-2$ comparaciones, porque el último elemento ya está en su posición correcta. Con el ejemplo anterior, serían 7 comparaciones.
- Este patrón continúa hasta que, finalmente, en la última pasada se realizan 1 o 0 comparaciones, dependiendo de la implementación y si la lista ya está ordenada antes de llegar a esa última pasada.
Al final de estas pasadas, todos los elementos quedan ordenados, habiéndose comparado cada par el número de veces necesario para asegurar que ningún elemento fuera de orden permanezca sin intercambiar.

**Ventajas y Desventajas del Método Burbuja**
Ventajas:
- Es muy fácil de entender e implementar.
- Se puede optimizar para detectar si ya está ordenado (ej., usando un indicador o bandera que se active cuando se realice un intercambio).
**Desventajas:**
- Es ineficiente para listas grandes (su complejidad temporal promedio y peor caso es $O(n^2)$ )
- Realiza un gran número de comparaciones e intercambios incluso cuando la lista está casi ordenada (a menos que se use la optimización con bandera).
Con este método, aunque sencillo de implementar, es recomendable usarlo solo para listas pequeñas o como ejemplo didáctico, ya que existen otros métodos de ordenamiento más eficientes (como Quick Sort o Merge Sort) para listas más grandes.

