#given a list of ints, return True if any two nums in list sum to 0


def add_to_zero(somelist):
    """ 

    >>> add_to_zero([1,2,3,4,5])
    False

    >>> add_to_zero([1,2,3,4,5,-1])
    True
    
    >>> add_to_zero([1,2,3,4,5,-1,0])
    True

    >>> add_to_zero([])
    False


    """
    #if the list is empty, return False
    if len(somelist)==0:
            return False
    #loop over numbers in list 
    for num in somelist:
        #if a negative of this num exists in the list, return True 
        if -num in somelist:
            return True
        
    #if negative version of number does not exist, return False
    return False 




#####################################################################

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print