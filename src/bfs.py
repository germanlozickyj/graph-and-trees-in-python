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

def moveHorsesInChess(origen_x : int, origen_y : int, objetivo_x : int, objetivo_y : int):
    movements = [[1,2],[1,-2],[-1,2],[-1,-2],[2,1],[2,-1],[-2, 1], [-2, -2]]
    queue = movements
    hash_cache = {}
    while queue :
        for _ in range(len(queue)):
            currentNode = queue.pop(0)
            if hash_cache.get(f"{currentNode[0]},{currentNode[1]}") == True: continue
        

moveHorsesInChess(0, 0, 5, 5)
