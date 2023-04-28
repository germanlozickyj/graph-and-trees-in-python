"""
Tienes una matriz binaria m x n que representa un mapa de "1"
(tierra) y "0" (agua), retorna el numero de islas.

una isla esta redeada de agua y se forma conectando tierras
adyacentes.

Puede suponer que los cuatro bordes de la cuadricula estan
rodeados de agua.
"""

def search_island_number(matriz):
    current_pointer = 0
    hash_island_found = {}
    counter = 0
    for matriz_binary in matriz :
        for binary in matriz_binary:
            if binary == "1" :
                result = dfs(matriz_binary, current_pointer)
                current_pointer += 1
    
def dfs(matriz, pointer):
    pass

search_island_number([
    ["1","1","0","0","0"],
    ["1","1","0","0","0"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"],
])