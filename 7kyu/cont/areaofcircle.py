# Complete the function which will return the area of a circle with the given radius.

# Returned value is expected to be accurate up to tolerance of 0.01.

# If the radius is not positive, raise ValueError.
#%%
def circle_area(r):
    pi=3.1459
    return pi*r**2 if r>0.0 else ValueError


circle_area(-1)