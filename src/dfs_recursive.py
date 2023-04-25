
def dfs_recursive(root, value):

    if (root.value == value) :
        return root
    
    right = dfs_recursive(root.right, value)
    left = dfs_recursive(root.left, value)
    
    if right != None:
        return right

    if left != None:
        return left
    
    return None

def dfs_loop(root):
   stack = []
   visited = set()
   stack.append(root)
 
   while stack: 
       currentNode = stack.pop()
       if currentNode not in visited: 
           visited.add(currentNode)
       for nodo in currentNode.next:
           if nodo not in visited:
               stack.append(nodo)
               
