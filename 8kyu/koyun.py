def count_sheep(n):
    if n==0:
        return ''
    str1=''.join([f"{i} sheep..." for i in range(1,n+1)])  #dongu sayisi kadar join yapiyor .. f"{i} sheep..." f string kullandik
    #her dongu sonu str'ye ekleme yapiyor
    return str1

        
count_sheep(2)
    



