"""
Combinación de Sumas
Dada una matriz de enteros distintos candidatos y un entero objetivo, 
devuelve una lista de todas las combinaciones únicas de candidatos 
en las que los números elegidos suman el objetivo. 
Puede devolver las combinaciones en cualquier orden. 
El mismo número puede ser elegido entre los candidatos 
un número ilimitado de veces. Dos combinaciones son únicas 
si la frecuencia de al menos uno de los números elegidos es diferente. 
Los casos de prueba se generan de forma que el número de combinaciones 
únicas que suman el objetivo sea inferior a 150 combinaciones para la entrada dada.

Ejemplo 1:
Entrada: candidatos = [2,3,6,7], objetivo = 7
Salida: [[2,2,3],[7]]
Explicación: 2 y 3 son candidatos, y 2 + 2 + 3 = 7. Nótese que 2 puede usarse varias veces. 7 es un candidato, y 7 = 7. 
Estas son las dos únicas combinaciones.
"""
def combitation_of_sums(candidates, number):

    def dfs(goal, queue, combinations):
        if not goal :
            combinations.append(queue)
            return
        
        for number in candidates:
            if number > goal:
                return
            if not queue or queue[-1] <= number :
                dfs(goal - number, queue + [number], combinations)

    response = []
    candidates.sort()

    dfs(number, [], response)
    return response

#result = combitation_of_sums([2,3,6,7], 7)
#print(result)


"""
Permutaciones
Dado un array nums de enteros distintos, devuelve todas las permutaciones posibles. 
Puede devolver la respuesta en cualquier orden.

Ejemplo 1:
Entrada: nums = [1,2,3]
Salida: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
[[1, 2, 3], [3,1,2], [2,3,1], [1,3,2], [2,1,3], [3,2,1]]
Ejemplo 2:
Entrada: nums = [0,1]
Salida: [[0,1],[1,0]]

"""
def permutations(input):
    response = []

    def dfs(last, permutations):
        if len(input) == 2 :
            permutations.append([last[1], last[0]])
            return

        current_permutation = []

        if len(permutations) == len(input) + len(input):
            return 
        if len(permutations) == len(input):
            copy = input.copy()
            copy.reverse()
        else :
            copy = last.copy()
        
        pop = copy.pop()
        current_permutation.append(pop)

        for number in copy:
            current_permutation.append(number)
        
        permutations.append(current_permutation)

        dfs(current_permutation, permutations)
    
    response.append(input)
    dfs(input, response)

    return response



#print(permutations([1,2,3]))
#print(permutations([0,1]))

"""
Combinaciones de Letras
Dada una cadena s, se puede transformar cada letra individualmente 
para que sea minúscula o mayúscula para crear otra cadena. 
Devuelve una lista de todas las posibles cadenas que podríamos crear. 
Devuelve la salida en cualquier orden.

Ejemplo 1:
Entrada: s = "a1b2"
Salida: [
            “a1b2”,
            “a1B2”,
            “A1b2”,
            “A1B2”
        ]

Ejemplo 2:
Entrada: s = "3z4"
Salida: [“3z4”, “3Z4”]
"""
def combination_of_letters(string : str):
    response = []

    def dfs(pointer, response):
        if len(response) == len(string):
            return response

        if string[pointer].isalpha():
            response.append(string.replace(string[pointer], string[pointer].lower()))
            response.append(string.replace(string[pointer], string[pointer].upper()))
            return dfs(pointer+1, response)
        else:
            return dfs(pointer+1, response)
            
    return dfs(0, response)

response = combination_of_letters("a1b2")
print(response)


