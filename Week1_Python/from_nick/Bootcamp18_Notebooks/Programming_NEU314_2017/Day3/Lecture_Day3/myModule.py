"""
This initial text is overall documentation
for the module as a whole
"""


def f(x, a=2, verbose=False):
    '''
    Hmm! An amazing function that will fulfill all of your example function needs

    Computes a*x^2
    
    Parameters
    ----------
    x: numeric
        Primary input which will be squared
    a: numeric, optional, default=2
        Multiplicative factor
    verbose: bool, optional, default=False
        If True, prints additional information about the computation
        
    RETURNS:
    --------
    
    a*x^2
    '''
    x_sq = x**2
    if verbose:
        print("x_sq:", x_sq)
    return a*x_sq

pi = 3.141569

james = "tall"
