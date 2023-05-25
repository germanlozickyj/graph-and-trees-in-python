

#Letter Combinations of a Phone Number

def backtrack(numbers):
    keyboard = {
        '2': "abc",
        '3': "def",
        '4': "ghi",
        '5': "jkl",
        '6': "mno",
        '7': "pqrs",
        '8': "tuv",
        '9': "wxyz"
    }
    cache = []
    str_combination = []

    for number in numbers:
        if not number in keyboard : continue
        if not cache : 
            cache.append(number)
            continue
        for cache_number in cache:
            str_temp = concat_numbers(keyboard[cache_number], keyboard[number])
            str_combination.extend(str_temp)
        cache.append(number)

    return str_combination

def concat_numbers(hash_str, hash_str_two):
    str_concated = []
    for x in range(len(hash_str_two)):
        for str in hash_str :
            str_concated.append(f"{str}{hash_str_two[x]}") 
            
    return str_concated

str_combination = backtrack("23")
print(str_combination)

