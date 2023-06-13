"""
goals:
    Dada una cuadrícula m x n y una cadena palabra,
    devuelve true si esta existe en la cuadrícula.
    La palabra puede construirse a partir de letras de celdas secuencialmente adyacentes, 
    donde las celdas adyacentes son vecinas horizontal o verticalmente.
    Una misma celda de letra no pude ser utilizada más de una vez.

- crear una funcion dfs
- queue en donde se almacena las palabras que se van buscando dentro de dfs
- marcar con 0 las letras usadas
"""
def word_search(board : dict, word : str):
    word_index = 0
    queue = [[0, 0, word[0]]]

    while queue:
        y, x, letter = queue.pop() 
        for y in range(len(board) - y) :
          for x in range(len(board[0]) - x) :
            if board[y][x] == letter:
                board[y][x] = 0
                word_index += 1
                queue.push([
                   y, x, word_index
                ])




board = [
  ["A", "B", "C", "E"],
  ["S", "F", "C", "S"],
  ["A", "D", "E", "E"],
]

word = "ABCCED"

print(word_search(board, word))