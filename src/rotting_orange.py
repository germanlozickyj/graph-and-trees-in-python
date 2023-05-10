"""
Vas a recibir una cuadrícula m x n en la que cada celda puede tener uno de los tres valores siguientes:

0: representa una celda vacía
1: representa una naranja fresca
2: representa una naranja podrida
Cada día cualquier naranja 4-direccionalmente adyacente a una naranja podrida también se vuelve podrida.

Debes retornar el número mínimo de días que deben transcurrir hasta que ninguna celda tenga una naranja fresca. Si esto es imposible, retorna -1.

Por ejemplo:

// Input
const cultivo = [
  [2,1,1],
  [1,1,0],
  [0,1,1],
];

orangesRotting(cultivo);

// Output
4
"""

def oranges_rotting(crop):
    days = 0
    for y in range(len(crop)):
          for x in range(len(crop[0])):
            if crop[y][x] == 2:
              rotted = 0
              crop[y][x] = 3
              if y + 1 < len(crop) and crop[y + 1][x] == 1 : 
                rotted += 1
                crop[y+1][x] = 2 
              if x + 1 < len(crop[0]) and crop[y][x + 1] == 1:
                rotted += 1
                crop[y][x + 1] = 2
              if not rotted == 0:
                days+=1
    return days

print(oranges_rotting([
  [2,1,1],
  [1,1,0],
  [0,1,1],
]))