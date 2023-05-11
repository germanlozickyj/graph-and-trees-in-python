"""
Dada una matriz binaria n x m en la que 1 representa tierra y 0 agua, asumiendo que hay dos islas en el mapa, retorna el tamaño del puente más corto para conectar ambas islas.

Recuerda que una isla está rodeada de agua y se forma conectando celdas con tierra adyacentes. Puedes suponer que los cuatro bordes de la cuadrícula están rodados de agua.

Ejemplo 1:

# Input
mapa = [
  [1,1,1,1,1],
  [1,0,0,0,1],
  [1,0,1,0,1],
  [1,0,0,0,1],
  [1,1,1,1,1],
]
Bridge().shortestBridge(mapa)

# Output
1

Ejemplo 2:

# Input
mapa = [
  [1,1,0,0,1],
  [1,1,0,0,1],
  [1,0,0,0,1],
  [1,0,0,0,1],
  [1,0,0,1,1],
]
Bridge().shortestBridge(mapa)

# Output
2
"""


class Bridge:
  def shortestBridge(self, A):
    # Tu código aquí 👇
    return len(A)

mapa = [
  [1,1,1,1,1],
  [1,0,0,0,1],
  [1,0,1,0,1],
  [1,0,0,0,1],
  [1,1,1,1,1],
]
response = Bridge().shortestBridge(mapa)
print(response)

mapa = [
  [1,1,0,0,1],
  [1,1,0,0,1],
  [1,0,0,0,1],
  [1,0,0,0,1],
  [1,0,0,1,1],
]
response = Bridge().shortestBridge(mapa)
print(response)