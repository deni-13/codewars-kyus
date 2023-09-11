def remove_exclamation_marks(s):
    s=s.replace("!","")
    return s


print(remove_exclamation_marks("hello!"))


#%%  lambda 

remove_exclamation_marks= lambda s: s.replace("!","")

