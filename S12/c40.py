def int_to_binary(n):
    """
    Function to convert an integer to its binary representation.
    
    Parameters:
    n (int): The integer to convert.
    
    Returns:
    str: The binary representation of the integer.
    """
    # Your code here
    binary=""
    while(n>0):
        binary=str(n%2)+binary
        n=n//2
    return binary    
n=int(input("enter any number:"))
res=int_to_binary(n)
print(res)  
