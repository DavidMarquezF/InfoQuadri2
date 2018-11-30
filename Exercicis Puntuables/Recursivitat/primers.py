def esPrimer(n,r = None):
    """
    >>> esPrimer(5)
    True
    >>> esPrimer(9)
    False
    >>> esPrimer(23)
    True
    """
    if(r == None):
        r = n
    r-=1
    if r<=2:
        return True
    elif n%r==0:
        return False
    else:
        return esPrimer(n,r)
if __name__=='__main__':
    print esPrimer(5)
