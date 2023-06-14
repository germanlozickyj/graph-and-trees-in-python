"""
goals:
    Dada una cuadrícula m x n y una cadena palabra,
    devuelve true si esta existe en la cuadrícula.
    La palabra puede construirse a partir de letras de celdas secuencialmente adyacentes, 
    donde las celdas adyacentes son vecinas horizontal o verticalmente.
    Una misma celda de letra no pude ser utilizada más de una vez.
"""
def word_search(board, word):
    queue = []
    
    for y in range(len(board)):
      for x in range(len(board[0])):
          if board[y][x] == word[0]:
              board[y][x] = 0
              queue.append([y, x, 1])
    
    if not queue:
        return False
    
    while queue:
        y, x, word_index = queue.pop() 

        if word_index == len(word):
            return True
        
        movements = [
            [y, x + 1], 
            [y, x - 1], 
            [y + 1, x], 
            [y - 1, x]
          ]
        
        for movement_y, movement_x in movements:
            if str(y) + str(x) == str(movement_y) + str(movement_x) : continue
            if movement_y < 0 or movement_x < 0 : continue
            if movement_y > len(board) - 1 or movement_x > len(board[0]) - 1 or word_index > len(word) - 1: continue

            if board[movement_y][movement_x] == word[word_index]:
                word_index+=1
                queue.append([
                    movement_y, movement_x, word_index
                ])
    return False

# Input
board = [
  ["A", "B", "C", "E"],
  ["S", "F", "C", "S"],
  ["Z", "D", "E", "E"],
]

word = "ABCCED"

print(word_search(board, word))
#Output
#true

# Input
board = [
  ["A", "M", "C", "E"],
  ["A", "M", "C", "E"],
  ["A", "M", "C", "E"],
]

word = "AMA"
print(word_search(board, word));

#Output
#false