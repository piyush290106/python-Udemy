def is_perfect_square(num):
    """
    Function to check if a number is a perfect square.
    
    Parameters:
    num (int): The number to check.
    
    Returns:
    bool: True if num is a perfect square, False otherwise.
    """
    # Your code here
    for i in range(0,num+1):
        if i*i==num:
            return True
        
    return False
n = int(input("Enter a number: "))
print(is_perfect_square(n))

    
