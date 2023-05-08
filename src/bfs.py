def bfs(root):
    if not root : return []
    response = [root]
    queue = [root]
    counter = 1
    while queue:
        for _ in range(len(queue)):
            currentNode = queue.pop(0)
            response.append(currentNode)
            for child in currentNode.children:
                queue.append(child)
        counter+=1
    return response

"""
En un tablero de ajedrez infinito tienes un caballo en la casilla [origenX, origenY].

Un caballo tiene 8 posibles movimientos para hacer.

Debes devolver el número mínimo necesario de movimientos para llevar al caballo a la casilla [objetivoX, objetivoY]. 

Se garantiza que la respuesta sí existe.

Ejemplo:

# Input
origenX = 0
origenY = 0
objetivoX = 5
objetivoY = 5
minKnightMoves(origenX, origenY, objetivoX, objetivoY)

# Output
4
"""
def moveHorsesInChess(origen_x : int, origen_y : int, objetivo_x : int, objetivo_y : int):
    if origen_x == objetivo_x and origen_y == objetivo_y:
        return 0
    
    movements = [
        [1,2],[1,-2],[-1,2],[-1,-2],
        [2,1],[2,-1],[-2,1],[-2,-2]
    ]
    queue = [[origen_x,origen_y]]   
    cache = [[origen_x,origen_y]]
    counter = 0

    while queue :
        for _ in range(len(queue)):
            current_position = queue.pop(0)
            if cache[0] == current_position[0] and cache[1] == current_position[1]: continue
            if current_position[0] == objetivo_x and current_position[1] == objetivo_y :
                return counter
            cache.append([
                    current_position[0],
                    current_position[1]
                ])
            for movement in movements:
                x = current_position[0] + movement[0]
                y = current_position[1] + movement[1]
                if not abs(x - objetivo_x) < 8 and not abs(y - objetivo_x) < 8: continue
                queue.append([
                    current_position[0] + movement[0], 
                    current_position[1] + movement[1]
                ])
        counter+=1
    return counter
                

print(moveHorsesInChess(0, 0, 5, 5))
