def is_multiple(dividend, divisor):
    '''
        The function check if the dividend is a multiple of the divisor number
        dividend: number to be divided
        divisor : numberby which the dividend is divided
        
        return True is the divisor is a multiple of the dividend
        return False otherwise
    '''
    if dividend % divisor == 0:
        return True
    return False
    
    
def multiple():
    '''
    Print number from 1 to 100
    for multiple of 4, print "oi" instead of the number
    for multiple of 5, print "ay" instead of the number
    for multiple of 4 and 5, print "oi ay" instead of the number
    '''

    for x in range(1,101):
        if is_multiple(x,4) == True and is_multiple(x,5) == True:
            print "oi ay"   
        elif is_multiple(x,4) == True:            
            print "oi"
        elif is_multiple(x,5) == True:
            print "ay"
        else:
            print x