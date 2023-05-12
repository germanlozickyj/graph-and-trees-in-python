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
  def __init__(self) -> None:
    self.map = None
    
  def shortestBridge(self, map):
      self.map = map
      bridges = 0
      for y in range(len(map)):
        for x in range(len(self.map[0])):
            self.dfs(x, y)
            bridges += 1
         
      return bridges
  def dfs(self, y, x):
      if 0 <= y < len(self.map) and 0 <= x < len(self.map[0]) and self.map[y][x] == 1 :
          self.map[y][x] = 2
          self.dfs(y+1, x)
          self.dfs(y-1, x)
          self.dfs(y, x+1)
          self.dfs(y, x-1)
"""
mapa = [
  [1,1,1,1,1],
  [1,0,0,0,1],
  [1,0,1,0,1],
  [1,0,0,0,1],
  [1,1,1,1,1],
]
response = Bridge().shortestBridge(mapa)
print(response)
"""

mapa = [
  [1,1,0,0,1],
  [1,1,0,0,1],
  [1,0,0,0,1],
  [1,0,0,0,1],
  [1,0,0,1,1],
]
response = Bridge().shortestBridge(mapa)
print(response)