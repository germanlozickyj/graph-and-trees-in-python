"""
Reemplazar un Color en una Sección de la Imagen
Una imagen está representada por una cuadrícula de enteros m x n donde image[i][j] representa el valor de los píxeles de la imagen.
También se le dan tres enteros sr, sc y color. Debe realizar un relleno en la imagen comenzando por el píxel image[sr][sc].

Para realizar un relleno, considere el píxel inicial, 
más cualquier píxel conectado en 4 direcciones al píxel 
inicial del mismo color que el píxel inicial, más cualquier 
píxel conectado en 4 direcciones a esos píxeles (también con el mismo color), 
y así sucesivamente. Reemplazar el color de todos los píxeles mencionados por el color.

Devuelve la imagen modificada después de realizar el relleno.

Ejemplo 1:
Entrada: imagen = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2
Salida: [[2,2,2],[2,2,0],[2,0,1]]
Explicación: Desde el centro de la imagen con posición (sr, sc) = (1, 1) (es decir, el píxel rojo), todos los píxeles conectados por un camino del mismo color que el píxel inicial (es decir, los píxeles azules) se colorean con el nuevo color.
Observe que la esquina inferior no se colorea con el color 2, porque no está conectada en 4 direcciones al píxel inicial.

Ejemplo 2:
Entrada: imagen = [[0,0,0],[0,0,0]], sr = 0, sc = 0, color = 0
Salida: [[0,0,0],[0,0,0]]
Explicación: El píxel inicial ya tiene el color 0, por lo que no se realizan cambios en la imagen.

"""
class issueOne():

    def __init__(self, image) -> None:
        self.image = image

    def remplazeColor(self, sr, sc, color) -> list:
        for i in range(len(self.image)) :
            for j in range(len(self.image[0])):
                self.dfs(i, j, sr, sc, color)
        return self.image
    
    def dfs(self, i, j, sr, sc, color):
        if 0 <= i < len(self.image) and 0 <= j < len(self.image[0]) and self.image[i][j] == sr:
            if j == 0 :
                self.image[i][j] = color
            else:
                if self.image[i][j - 1] == color :
                    self.image[i][j] = color
            self.dfs(i, j + 1, sr, sc, color)
            self.dfs(i, j + 2, sr, sc, color)

#issueOne = issueOne([[1,1,1],[1,1,0],[1,0,1]])
#print(issueOne.remplazeColor(sr = 1, sc = 1, color = 2))


"""

Construir una cadena a partir de un árbol binario
Dada la raíz de un árbol binario, construya una cadena 
formada por paréntesis y enteros a partir de un árbol binario 
con el modo de recorrido de preorden, y devuélvala. 
Omita todos los pares de paréntesis vacíos que no afecten a la relación de mapeo 
uno a uno entre la cadena y el árbol binario original.

Ejemplo 1
Entrada: raíz = [1,2,3,4]
Salida: "1(2(4))(3)"
Explicación: Originalmente, tiene que ser “1(2(4)())(3()())”, 
pero hay que omitir todos los pares de paréntesis vacíos innecesarios. Y será “1(2(4))(3)”

Ejemplo 2:
Entrada: raíz = [1,2,3,null,4]
Salida: "1(2()(4))(3)"
Explicación: Casi lo mismo que el primer ejemplo, excepto que no podemos omitir el primer 
par de paréntesis para romper la relación de mapeo uno a uno entre la entrada y la salida.
"""
class Node :
    def __init__(self, value) -> None:
        self.value = value
        self.right = None
        self.left = None

    def get(self, pointer):
        if pointer == 'left':
            return self.left
        return self.right

class issueTwo:
    def __init__(self, root) -> None:
        self.root = root
    
    def resolve(self):
        self.root = self.make_tree()
        right = self.dfs('right')
        left = self.dfs('left')
        return str(self.root.value) + right + left
    
    def make_tree(self):
        rootNode = Node(self.root[0])
        rootNode.right = []
        rootNode.left = []

        for value in self.root[1:] :
            if value is not None:
                if value % 2 == 0:
                    rootNode.right.append(value)
                else:
                    rootNode.left.append(value)
        return rootNode
    
    def dfs(self, pointer, str = ''):
        if len(self.root.get(pointer)) == 0:
            return str
        else:
            str = f"({self.root.get(pointer)[0]})"
        if len(self.root.get(pointer)) > 1 :
            str = str[0:len(str)-1] + f"({self.root.get(pointer)[1]}))"
            self.root.get(pointer).pop(1)
        self.root.get(pointer).pop(0)

        return self.dfs(pointer, str)

#- tests
        
#issueTwo = issueTwo([1,2,3,4])
#print(issueTwo.resolve())

#issueTwo = issueTwo([1,2,3,None,4])
#print(issueTwo.resolve())


"""
Batalla Naval - Contar Barcos
Dado un tablero de m x n donde cada celda es un acorazado ‘X’ o un vacío ‘.’, devuelva el número de los barcos en el tablero. Los barcos sólo pueden colocarse horizontal o verticalmente en el tablero. En otras palabras, sólo pueden tener la forma 1 x k (1 fila, k columnas) o k x 1 (k filas, 1 columna), donde k puede ser de cualquier tamaño. Al menos una celda horizontal o vertical separa dos barcos (es decir, no hay barcos adyacentes).

Ejemplo 1:
Entrada: tablero = [[“X”,".",".", “X”],[".",".", “X”],[".",".", “X”]
Salida: 2

Ejemplo 2:
Entrada: tablero = [["."]]
Salida: 0

Número de Islas Cerradas
Dada una cuadrícula 2D formada por 0s (tierra) y 1s (agua). Una isla es un grupo máximo de 0s conectado en 4 direcciones y una isla cerrada es una isla totalmente (toda a la izquierda, arriba, derecha, abajo) rodeada de 1s. Devuelve el número de islas cerradas.

Ejemplo 1:
Input: grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]
Salida: 2
Explicación: Las islas en gris están cerradas porque están completamente rodeadas de agua (grupo de 1s)
"""