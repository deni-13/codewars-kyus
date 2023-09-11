#%%
l=["3:1","2:0"]

elemanlar=list()
for  i in l :
    print(i)    #out : ['3:1'  '2:0']
    elemanlar.append(i.split(":"))  
print(elemanlar)  #[['3', '1'], ['2', '0']]
for j in range(len(elemanlar)):   #  0 .index [["3","1"], 1.index: ["2","0"]]
    for k in range(len(elemanlar[j])):  #index ici elemanlar  3 1  2 0
        elemanlar[j][k]=int(elemanlar[j][k])  #string olan her eleman int
liste=elemanlar
print(liste) #[[3, 1], [2, 0]]
for i in range(len(liste)):  #0  #1
    for j  in range(len(liste[i])-1):
        if liste[i][j]< liste[i][j+1]:
            print("loss")
        elif liste[i][j]> liste[i][j+1]:
            print("win")
        else:
            print("tie")
#%%

def points(games):
    elements=list()
    for  i in games :
        print(i)    #out : ['3:1'  '2:0']
        elements.append(i.split(":"))  
    for j in range(len(elements)):   #  0 .index [["3","1"], 1.index: ["2","0"]]
        for k in range(len(elements[j])):  #index ici elemanlar  3 1  2 0
            elements[j][k]=int(elements[j][k])  #string olan her eleman int
    liste=elements
#print(liste) #[[3, 1], [2, 0]]
    point=0
    for i in range(len(liste)):  #0  #1
        for j  in range(len(liste[i])-1):
            if liste[i][j]< liste[i][j+1]:
                point+=0
            elif liste[i][j]> liste[i][j+1]:
                point+=3
            else:
                point+=1                
    return point



l=['1:0','2:0','3:0','4:4','2:2','3:3','1:4','2:3','2:4','3:4']
points(l)


    



# %%
