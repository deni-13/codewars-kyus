# Simple, given a string of words, return the length of the shortest word(s).

# String will never be empty and you do not need to account for different data types.

def find_short(s):
    s=s.split(" ") #listeye cevirdik
    shortest=s[0] #initializing value
    for i in s:
        if len(i)<len(shortest): # i elemani < shortest
            shortest=i
            

        l=len(shortest)
    return l # l: shortest word length


find_short("bitcoin take over the world maybe who knows perhaps" )

#%%

lst= "bitcoin take over the world maybe who knows perhaps".split(" ")
shortest=lst[0]
for i in lst:
    if len(i)<len(shortest):
        shortest=i
print(shortest)
