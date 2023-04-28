
def sum_root(root):
    left_pointer = root['left']
    left_number = root['value']
    right_pointer = root['right']
    right_number = root['value']
    while(True):
        if left_pointer :
            left_number = str(left_number) + str(left_pointer['value'])
            if not 'next' in left_pointer or left_pointer['next'] == None: break
            left_pointer = left_pointer['next']
    while(True):
        if right_pointer :
            right_number = str(right_number) + str(right_pointer['value'])
            if not 'next' in right_pointer or right_pointer['next'] == None: break
            right_pointer = right_pointer['next']
    return int(left_number) + int(right_number)


def sum_root_regresive(root):
    left = sum_function(root, 'left')
    right = sum_function(root, 'right')
    return left + right

def sum_function(root, direction, str_queue = ''):
    if root.get(direction) == None:
        return int(str_queue + str(root['value']))
    
    return sum_function(root[direction], direction, str_queue + str(root['value']))


tree = {
    'value' : 1,
    'left' : {
        'value': 2,
        'right': None,
        'left' : {
            'value' : 5,
            'left' : None,
            'right' : None,
        },
    },
    'right' : {
        'value': 3,
        'left' : None,
        'right' : {
            'value': 3,
            'left' : None,
            'right' : None
        }
    }
}

sum_regresive = sum_root_regresive(tree)
sum_by_bucle = sum_root(tree)
