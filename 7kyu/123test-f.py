#%%
def number(lines):
    l=len(lines)
    if l==0:
        return []
    else:
        liste=[]
        for j in range(1,l+1):
            j=str(j) #once stringe cevirip listeye ekle
            liste.append(j)
    # ["1","2","3"]
    a=[z+":"+m for z,m in list(zip(liste,lines))]
    e=[]
    for i in a:
        i=i.strip(" ")
        e.append(i)
        
        
    return e


    

lst=["a","b","c"]
#lst2=[]
number(lst)

