#%%
def last(*args):
    if isinstance(args[-1], (list, str, tuple)):
        return args[-1][-1]
    return args[-1]
last(1, "b", 3, "d", 5) 









