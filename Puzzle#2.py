def is_palindrome(string):
    '''
        string: a string
        return: True is string is a palindrome
                False otherwise
    '''    
    #set all characters in the string in lowercase
    string = string.lower()
    
    #join all alpha characters together 
    string = ''.join(char for char in string if char.isalpha())
    
    #check if the string is a palindrome
    return string == string[::-1]
    