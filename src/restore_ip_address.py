import copy
"""
tests

// Input
restoreIpAddresses("25525511135")

// Output
[
  "255.255.111.35",
  "255.255.11.135",
]
"""
def restore_ip(s: str):
    s_length = len(s)
    if s_length > 24:
        return []

    ip_list = list(s)
    ip = []
    max_range = 3

    for i in range(0, len(ip_list), 3):
        groups = ''.join(ip_list[i:i+3])
        ip.append(groups)
        if max_range > len(groups):
            max_range = len(groups)
        
    ips = check_ip(copy.copy(ip), max_range=max_range)

    if check(ip):
        ips.append(ip)

    return ips

def check_ip(ip, review_pointer=0, index=0, max_range=0, ips_valid=[]):
    str = copy.copy(ip)

    if review_pointer == 3 and index <= max_range:
        return ips_valid

    extracted = str[review_pointer][index:index+max_range]
    str[review_pointer] = str[review_pointer][index - max_range].replace(extracted, "")
    new_ip = []

    for i in range(0, len(''.join(str)), 3):
        groups = ''.join(''.join(str)[i:i+3])
        new_ip.append(groups)
        if max_range > len(groups):
            max_range = len(groups)
    
    new_ip.insert(review_pointer, extracted)

    if check(new_ip):
        ips_valid.append(new_ip)
    
    if index <= max_range:
        index = 0

    review_pointer += 1

    return check_ip(ip, review_pointer, index, max_range, ips_valid)

def check(ip):
    for value in ip:
        if int(value) > 255:
            return False
    return True

result = restore_ip("25525511135")
print(result)