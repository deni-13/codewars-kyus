# #sentence smash
# ['hello', 'world', 'this', 'is', 'great']  =>  'hello world this is great'
# #
arr=[]
str1=['hello', 'world', 'this', 'is', 'great']
i=0 
while i <len(str1):
    print(str1[i])
    arr.append(str1[i])
    i+=1
    
print("elemanlar arrayde",arr)

j=" ".join(arr) #join cikisi

print(j)





#%%
# #
def smash(words):
    arr=[]
    i=0 
    while i <len(words):
        print(words[i])
        arr.append(words[i])
        i+=1

    j=" ".join(arr)

    return j

str1=['hello', 'world', 'this', 'is', 'great']


smash(str1)
