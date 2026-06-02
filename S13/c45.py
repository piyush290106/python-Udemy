def are_equal_strings(s, t):
    """
    Function to check if two strings are equal without using built-in functions.
    
    Parameters:
    s (str): The first string.
    t (str): The second string.
    
    Returns:
    bool: True if the strings are equal, False otherwise.
    """
    # Your code here
    if str(s)==str(t):
        return True
    else:
        return False
    
n=input("enter:")
m=input("enter:")
res=are_equal_strings(n,m)
print(res)

