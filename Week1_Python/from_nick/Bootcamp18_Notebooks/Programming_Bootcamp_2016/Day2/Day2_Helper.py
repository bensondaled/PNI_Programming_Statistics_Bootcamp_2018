import numpy as np

def myrand():
    '''
    myrand receives no inputs and returns a single float
    randomly sampled from the uniform distribution between 0 and 1
    '''
    return np.random.rand()

def unique(s):
    '''
    unique receives a string s as input and returns a string
    of the unique characters in s, sorted alphabetically
    '''
    temp = list(set(s))   # Reduces s to a set, to get unique elements, then casts result back to list
    temp.sort()           # Sorts the unqiue values
    return "".join(temp)  # Returns the sorted unique values as a string