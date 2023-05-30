
def restore_ip(s : str):
    s_lenght = len(s)
    if s_lenght > 24 :
        return []
    
    ip_list = list(s)
    ip = []
    max_range = 3

    for i in range(0, len(ip_list), 3):
        groups = ''.join(ip_list[i:i+3])
        ip.append(groups)
        if max_range > len(groups):
            max_range = len(groups)

    ips = check_ip(ip, max_range=max_range)

def check_ip(ip, review_pointer = 0, max_range = 0):
    extracted = ip[review_pointer][review_pointer:review_pointer+max_range]
    ip[review_pointer] = ip[review_pointer][review_pointer].replace(extracted, "")
    print(ip)
    
    
restore_ip("25525511135")