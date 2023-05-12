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
    self.bridge = 0
    
  def shortestBridge(self, map):
      self.map = map
      for y in range(len(map)):
        for x in range(len(self.map[0])):
          if self.map[y][x] == 1 and x + 1 < len(self.map[0]) and self.map[y][x + 1] == 1:
            self.dfs(x, y)
      return self.bridge
  
  def dfs(self, y, x):
      if y < len(self.map) and x < len(self.map[0]):
        for x in range(len(self.map[0]) - x):
            if self.map[y][x] == 0 and x + 1 < len(self.map[0]) and self.map[y][x + 1] == 1:
              self.bridge += 1
        for y in range(len(self.map) - y):
            if self.map[y][x] == 0 and y + 1 < len(self.map) and self.map[y + 1][x] == 1:
              self.bridge += 1
      return 
            
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