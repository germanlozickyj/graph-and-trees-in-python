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

class Solution:
    def backtrack_queens_puzzle(self, n):
        result = self.dfs(n)
        return result
        
    def dfs(self, n):        
        col = set() 
        positive = set()
        negative = set()
        response = []
        board = [["."] * n for i in range(n)]

        def backtrack(y) :
            if y == n:
                copy = ["".join(row) for row in board]
                response.append(copy)
            
            for c in range(n) :
                if c in col or (y + c) in positive or (y - c) in negative : 
                    continue
                
                col.add(c)
                positive.add(y + c)
                negative.add(y - c)
                board[y][c] = "Q"

                backtrack(y + 1)

                col.remove(c)
                positive.remove(y + c)
                negative.remove(y - c)
                board[y][c] = "."
        
        backtrack(0)

        return response

n = 4
result = Solution().backtrack_queens_puzzle(n)
print(result)
