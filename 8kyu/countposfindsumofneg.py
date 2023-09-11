def count_positives_sum_negatives(arr):
    counts=0
    total=0
    for i in arr:
        if i>0:
            counts+=1
        elif i<0:
            total+=i
    return [counts,total] if len(arr)!=0 else []

#bos list durumunu da unutma


