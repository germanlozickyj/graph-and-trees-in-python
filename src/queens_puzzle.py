"""
El rompecabezas de n reinas es el problema de colocar n reinas en un tablero de ajedrez de n x n 
de manera que ninguna de ellas se ataque mutuamente.
Dado un número entero n, devuelva todas las soluciones distintas del rompecabezas de n reinas. 
Puede devolver la respuesta en cualquier orden. Cada solución contiene una configuración del tablero 
distinta de la colocación de n reinas, donde “Q” y “.” indican una reina y un espacio vacío, respectivamente.
[
    [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]], 
    [
        [1, 3, 3, 3], 
        [3, 3, 0, 0], 
        [3, 0, 3, 0], 
        [3, 0, 0, 3]]
]
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
import copy

def backtrack_queens_puzzle(n: int):
    board = [[0 for _ in range(n)] for _ in range(n)]
    cache_board = [copy.deepcopy(board)]
    result = dfs(n, current_board=board, cache_board=cache_board)
    return result


def dfs(n, y=0, x=0, cache_board=[], current_board={}, solutions=[]):
    tmp_collect = kill_cell(n, y, x, current_board)

    for cell in range(n):
        if tmp_collect[y + 1][cell] == 0:
            current_board[y][x] = 1
            cache_board.append(copy.deepcopy(current_board))
            current_board = copy.deepcopy(tmp_collect)

            return dfs(n, y + 1, cell, cache_board, current_board, solutions)

    current_board = copy.deepcopy(cache_board.pop())
    current_board[y][x] = 2

    return dfs(n, y, x + 1, cache_board, current_board, solutions)    


def kill_cell(n, y, x, board):
    y_increment = y
    y_decrement = y
    x_increment = x
    x_decrement = x

    for movement in range(n) :
        board[y][movement] = 3
        board[movement][x] = 3
        if y_decrement >= n and x_decrement >= n and board[y_decrement][x_decrement] != 1:
            board[y_decrement][x_decrement] = 3

        if y_increment < n and x_increment < n and board[y_increment][x_increment] != 1:
            board[y_increment][x_increment] = 3
        
        if y_increment <= n and x_decrement >= 0 and board[y_increment][x_decrement] != 1:
            board[y_increment][x_decrement] = 3
        
        if y_decrement >= n and x_increment >= n and board[y_decrement][x_increment] != 1:
            board[y_decrement][x_increment] = 3
        y_increment += 1
        x_increment += 1
        y_decrement -= 1
        x_decrement -= 1

    return board

n = 4
result = backtrack_queens_puzzle(n)
print(result)
