# In this little assignment you are given a string of space separated numbers, and have to return the highest and lowest number.

# Examples
# high_and_low("1 2 3 4 5")  # return "5 1"
# high_and_low("1 2 -3 4 5") # return "5 -3"
# high_and_low("1 9 3 4 -5") # return "9 -5"

#%%
numbers= "1 2 3 4 5".split(" ")

print(numbers)
integer=[]
for i in numbers:
    integer.append(int(i))  #elementler integer'e cevrilip 
for  j in range(len(integer)+1):
    mini=integer[0]
    if j < mini:
        mini=j
    maxi=integer[0]
    if j>maxi:
        maxi=j
print(mini,maxi)





