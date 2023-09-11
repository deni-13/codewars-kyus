
#%%

def digitize(n):
    liste=[]
    for i in str(n): #str olarak dolasmak gereiyor,int iterable degil 
        i=int(i) #her bir sayi inte cevir
        liste.append(i) #bu int sayilari listeye ekle
    return liste[::-1]
digitize(35231)


#%% fonksiyonsuz
bos=[]
sayi =545656
for i in str(sayi):
    i=int(i)
    bos.append(i)
    
print(bos[::-1])