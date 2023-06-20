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
    board = [[0 for _ in range(n)] for _ in range(n)]
    result = dfs(n, current_collection=board)
    return result

def dfs(n, pointer = 0, collection_cache = [], current_collection = [], solutions = []):
    collection_cache[pointer] = current_collection
    current_collection[0][pointer] = 1
    tmp_board = write_kill_cell(n, pointer, current_collection)

def write_kill_cell(n, x, board, y = 0):    
    if n == x and n == y :
        return board


n = 4
result = backtrack_queens_puzzle(n)
