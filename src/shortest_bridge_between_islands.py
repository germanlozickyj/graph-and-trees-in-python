"""
Dada una matriz binaria n x m en la que 1 representa tierra y 0 agua, asumiendo que hay dos islas en el mapa,
retorna el tamaño del puente más corto para conectar ambas islas.

Recuerda que una isla está rodeada de agua y se forma conectando celdas con tierra adyacentes. 
Puedes suponer que los cuatro bordes de la cuadrícula están rodados de agua.

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
    self.bridge_lenght = None
    
  def shortestBridge(self, map):
      self.map = map
      self.bridge_lenght = len(map[0])
      for y in range(len(map)):
        for x in range(len(self.map[0])):
          if self.map[y][x] == 1:
            result = self.dfs(x, y)
            if result < self.bridge_lenght :
               self.bridge_lenght = result
      return self.bridge_lenght 
  
  def dfs(self, y, x):
      long = len(self.map[y])
      if x < len(self.map[0]):
        water_cell = 0
        for x in range(len(self.map[0])):
           if self.map[y][x] == 0:
              water_cell += 1
              if (x + 1) < long and self.map[y][x + 1] == 1:
                return water_cell 
      return long
            
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