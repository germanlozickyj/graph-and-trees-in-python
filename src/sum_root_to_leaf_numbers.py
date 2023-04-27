
def sum_root(root):
    left_pointer = root['left']
    left_number = root['value']
    while(True):
        if left_pointer :
            left_number = str(left_number) + str(left_pointer['value'])
            if not 'next' in left_pointer or left_pointer['next'] == None: break
            left_pointer = left_pointer['next']

    print(left_number)



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