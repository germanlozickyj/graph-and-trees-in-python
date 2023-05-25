

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
    str_combination = ""

    for number in numbers:
        if not number in keyboard : continue
        if not cache : 
            cache.append(number)
            continue
        for cache_number in cache:
            current_str = concat_numbers(keyboard[cache_number], keyboard[number])
            str_combination = f"{str_combination}{current_str}"
        cache.append(number)

    return str_combination

def concat_numbers(hash_str, hash_str_two):
    str_concated = ""
    for x in range(len(hash_str_two)):
        for str in hash_str :
            str_concated = f"{str_concated}{str}{hash_str_two[x]}"  
            
    return str_concated

str_combination = backtrack(['2','7', '8'])
print(str_combination)