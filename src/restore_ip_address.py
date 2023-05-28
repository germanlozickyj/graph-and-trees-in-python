
def restore_ip(s : str, division = 3, review_pointer = 0):
    s_lenght = len(s)
    if s_lenght > 24 :
        return []
    
    ip_list = list(s)
    ip = []

    for i in range(0, len(ip_list), division):
        groups = ''.join(ip_list[i:i+division])
        ip.append(groups)

    print(ip)



def check_ip():
    pass

restore_ip("25525511135")