#%%
def password(string):
    invalid_ch="!@#$%^&*()-_+={}[]|\:;?/>.<,"
    if len(string) <8 or string==invalid_ch or string.isupper() or string.islower() :
        return False
    else:
        return True


password('!ReLF)H$N')

#%%
import re
def password(string):
    
    return bool(re.match("^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,}$",string))

password('!ReLF)H$N')

#%% alt

password= lambda x: len(x) > 7 and all(any(f(c) for c in x) for f in (str.islower, str.isupper, str.isdigit))

#%% en begendigim sol
def password(string):
    #your code here
    if any(letter.isdigit() for letter in string) and any(letter.isupper() for letter in string) and any(letter.islower() for letter in string) and len(string) >= 8:
        return True
    else:
        return False