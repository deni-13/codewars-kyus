
#%%

#https://www.codewars.com/kata/5a19226646d843de9000007d/train/python


#%%
consonants=["a", "e", "i", "o", "u"]
text="abcdedddd"
lst=[]
lst=[i for i in text if i not in consonants ]
len(set(lst))
#%%
import string
nokt=string.punctuation
print(nokt)
def count_consonants(text):
    consonants=["a", "e", "i", "o", "u"]
    lst=[]
    t=text.lower().replace(" ","")

    lst=[i for i in t if i not in consonants]
    return len(set(lst))

count_consonants("Count my unique consonants!!")



#%% the end :)
import string

def count_consonants(text):

    nokt=string.punctuation

    consonants=["a", "e", "i", "o", "u"]
    nums=["0","1","2","3","4","5","6","7","8","9"]
    text=text.replace(" ","")
    lst=[]
    new=[]
    topl=0
    for i in text.lower():
        if i not in consonants :
            if i not in nums:
                if i not in lst: #initial
                    lst.append(i)
    print(lst)
    for j in lst:
        if j not in nokt:
            new.append(j)
            topl+=1


    return (topl)   
count_consonants('XBdurR!! JXEw?0R7ki')