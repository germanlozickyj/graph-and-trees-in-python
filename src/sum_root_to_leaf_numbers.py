
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

tree = {
    'value' : 1,
    'left' : {
        'value': 2,
        'right': None,
        'next' : {
            'value' : 5,
            'left' : None,
            'right' : None,
            'next': None
        },
    },
    'right' : {
        'value': 3,
        'next' : None
    }
}
sum = sum_root(tree)
print(sum)