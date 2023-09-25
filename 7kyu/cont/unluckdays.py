#%%
import datetime

yil=2015
tarih=[]
for i in range(1,13):
    dates=(datetime.datetime(yil,i,13)) #date time objesi olarak dates degiskenine yazdim
    tarih.append(dates) #append islemi

print(tarih)
say=""
for j in tarih:
    say+="".join(str(j.weekday()))  
if "4" in say:
    print(say.count("4"))





        
    



# %%



#%% queries?
# import datetime

# x = datetime.datetime.now()
# type(x)

#https://www.w3schools.com/python/python_datetime.asp  python dates
#how to add day detail
#https://stackoverflow.com/questions/9847213/how-do-i-get-the-day-of-week-given-a-date