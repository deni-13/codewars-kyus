# # https://www.codewars.com/kata/54bf85e3d5b56c7a05000cf9/train/python

# Your team is writing a fancy new text editor and you've been tasked with implementing the line numbering.

# Write a function which takes a list of strings and returns each line prepended by the correct number.

# The numbering starts at 1. The format is n: string. Notice the colon and space in between.

# Examples: (Input --> Output)
#%%

lst=["a","b","c"]

l=len(lst)
liste=[]
for j in range(1,l+1):
    j=str(j)
    liste.append(j)

    
# elemanlar=""
a=[z+":"+m for z,m in list(zip(liste,lst))]
a
    # elemanlar+="".join(z,m)

    


# %%
