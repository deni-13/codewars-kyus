#%%
#Abbreviate a Two Word Name
def abbrev_name(name):
    for  i in range(len(name)): 
        if name[i]==" ":
            return name[0].upper()+"."+name[i+1].upper()
abbrev_name("jon lenon")
