"""
El rompecabezas de n reinas es el problema de colocar n reinas en un tablero de ajedrez de n x n 
de manera que ninguna de ellas se ataque mutuamente.
Dado un número entero n, devuelva todas las soluciones distintas del rompecabezas de n reinas. 
Puede devolver la respuesta en cualquier orden. Cada solución contiene una configuración del tablero 
distinta de la colocación de n reinas, donde “Q” y “.” indican una reina y un espacio vacío, respectivamente.

[[[1, 3, 3, 3], [3, 3, 1, 3], [3, 3, 3, 3], [3, 0, 3, 3]]
    [1, 3, 3, 3], 
    [3, 3, 1, 3], 
    [3, 3, 3, 3], 
    [3, 0, 3, 3]]
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

class Solution:
    def __init__(self, n: int) -> None:
        board = [[0 for _ in range(n)] for _ in range(n)]
        self.n = n
        self.y = 0
        self.x = 0
        self.cache_board = copy.deepcopy(board)
        self.current_board = copy.deepcopy(board)
        self.solutions = []

    def backtrack_queens_puzzle(self):
        result = self.dfs()
        return result

    def dfs(self):        
        tmp_board = self.kill_cell(copy.deepcopy(self.current_board))
        self.current_board = copy.deepcopy(tmp_board)
        self.y += 1

        for x in range(n - 1):
            if self.current_board[self.y][x] == 0:
                self.cache_board.append(copy.deepcopy(self.current_board))
                self.x = x
                return self.dfs()
        
        #no hay espacios vacios para la reina
        last_board = copy.deepcopy(self.cache_board).pop()
        last_board[self.y - 1][self.x] = 2
        self.current_board = copy.deepcopy(last_board)
        #guardar en cache ultima casilla visitada y dada de baja
        self.cache_board.append(copy.deepcopy(self.current_board))
        self.y -= 1
        return self.dfs()
        
    def kill_cell(self, board):
        y_increment = self.y
        y_decrement = self.y
        x_increment = self.x
        x_decrement = self.x

        for movement in range(self.n) :
            board[self.y][movement] = 3
            board[movement][self.x] = 3

            if y_decrement >= self.n and x_decrement >= self.n :
                if board[y_decrement][x_decrement] == 3 or board[y_decrement][x_decrement] == 0:
                    board[y_decrement][x_decrement] = 3
                
            if y_increment < self.n and x_increment < self.n :
                if board[y_increment][x_increment] == 3 or board[y_increment][x_increment] == 0 :
                    board[y_increment][x_increment] = 3

            if y_increment < self.n and x_decrement >= 0:
                if board[y_increment][x_decrement] == 3 or board[y_increment][x_decrement] == 0:
                    board[y_increment][x_decrement] = 3
            
            if y_decrement >= self.n and x_increment >= self.n:
                if board[y_decrement][x_increment] == 3 or board[y_decrement][x_increment] == 0:
                    board[y_decrement][x_increment] = 3
            y_increment += 1
            x_increment += 1
            y_decrement -= 1
            x_decrement -= 1

        board[self.y][self.x] = 1

        return board

n = 4
result = Solution(n).backtrack_queens_puzzle()
print(result)
