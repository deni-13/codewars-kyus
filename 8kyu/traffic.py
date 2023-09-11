# You're writing code to control your town's traffic lights. 
# You need a function to handle each change from green, to yellow, to red, and then to green again.

# Complete the function that takes a string as 
# an argument representing the current state of the light and returns 
# a string representing the state the light should change to.

# For example, when the input is green, output should be yellow

def update_light(current):
    lst=["green","yellow","red"]    
    ind=lst.index(current)
    bas=(ind+1) %len(lst)  #ind boyuta bolumunden kalan cevircek -- modunu almamiz gerekiyor
    return  lst[bas]
update_light("yellow")
        
# 0 1  1  2  2 0  --- len(lst) = 3
#%% for ile 
def update_(current):
    lst=["green","yellow","red"]    
    for i in range(len(lst)):   
        current=lst[i]
        nexti=(i+1 )%len(lst)
    return lst[nexti]
update_light("red")
        