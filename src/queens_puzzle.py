"""
El rompecabezas de n reinas es el problema de colocar n reinas en un tablero de ajedrez de n x n 
de manera que ninguna de ellas se ataque mutuamente.
Dado un número entero n, devuelva todas las soluciones distintas del rompecabezas de n reinas. 
Puede devolver la respuesta en cualquier orden. Cada solución contiene una configuración del tablero 
distinta de la colocación de n reinas, donde “Q” y “.” indican una reina y un espacio vacío, respectivamente.
"""

"""
Entrada: n = 4
Salida: [[
    ".Q…",
    "…Q",
    “Q…”,
    "…Q."],
    ["…Q.",
    “Q…”,
    "…Q",
    ".Q…"
    ]]
Explicación: Existen dos soluciones distintas al rompecabezas de las 4 reinas como se muestra arriba
"""
def backtrack_queens_puzzle(n : int):
    #board = [[0 for _ in range(n)] for _ in range(n)]
    result = dfs(n)
    return result

def dfs(n, y = 0, x = 0, collection_cache = {}, current_collection = {}, solutions = []):
    dict_kill_cell = kill_cell(n, 2, y)
    collection_cache[str(y) + str(x)] = dict_kill_cell


def kill_cell(n, x, y):    
    hash = {}
    y_increment = y
    y_decrement = y
    x_increment = x
    x_decrement = x
    
    for movement in range(n - 2) :
        if y_decrement >= movement and x_decrement >= movement :
            hash[str(y_decrement) + str(x_decrement)] = 3

        if y_increment >= movement and x_increment >= movement :
            hash[str(y_increment) + str(x_increment)] = 3
        
        if y_increment >= movement and x_decrement >= movement :
            hash[str(y_increment) + str(x_decrement)] = 3
        
        if y_decrement >= movement and x_increment >= movement :
            hash[str(y_decrement) + str(x_increment)] = 3
        y_increment += 1
        x_increment += 1
        y_decrement -= 1
        x_decrement -= 1
    return hash

n = 4
result = backtrack_queens_puzzle(n)
