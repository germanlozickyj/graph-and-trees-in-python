"""
Tienes una matriz binaria m x n que representa un mapa de "1"
(tierra) y "0" (agua), retorna el numero de islas.

una isla esta redeada de agua y se forma conectando tierras
adyacentes.

Puede suponer que los cuatro bordes de la cuadricula estan
rodeados de agua.
"""
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None

class DoublyLinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
        self.lenght = 0

    def add(self, value):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.previous = self.tail
            self.tail.next = newNode
            self.tail = newNode
        self.lenght += 1

        return self
        
        
def search_island_number(matrices):
    linkedList = DoublyLinkedList()
    for matriz in matrices :
        linkedList.add(matriz)

    result = dfs(linkedList)

def dfs(linkedList):
    for linked

search_island_number([
    ["1","1","0","0","0"],
    ["1","1","0","0","0"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"],
])