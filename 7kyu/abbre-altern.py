def abbrevName(name):
    first, last = name.upper().split(' ')  #bosluga gore iki ayri listeye bolundu (split ) 1.list : first 2.listesi : last
    return first[0] + '.' + last[0]
    