"""
Tienes una matriz binaria m x n que representa un mapa de "1"
(tierra) y "0" (agua), retorna el numero de islas.

una isla esta redeada de agua y se forma conectando tierras
adyacentes.

Puede suponer que los cuatro bordes de la cuadricula estan
rodeados de agua.
"""

class regresiveIslands:
    def __init__(self) -> None:
        self.map = None

    def number_of_islas(self, map: list[list[str]]) -> int:
        self.map = map
        counter = 0
        for i in range(len(self.map)) :
            for j in range(len(self.map[0])) :
                self.dfs(i, j)
                counter +=1
        return counter

    def dfs(self, i, j):
        if 0 <= i < len(self.map) and 0 <= j < len(self.map[0]) and self.map[i][j] == '1' :
            self.map[i][j] = '2'
            self.dfs(i+1, j)
            self.dfs(i-1, j)
            self.dfs(i, j+1)
            self.dfs(i, j-1)

regresive = regresiveIslands()

regresive_result = regresive.number_of_islas(map = [
    ["1","1","0","0","0"],
    ["1","1","0","0","0"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"],
])

print(regresive_result)