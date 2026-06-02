def is_prime(n):
    """
    Function to check if a number is prime.
    
    Parameters:
    n (int): The number to check.
    
    Returns:
    bool: True if n is prime, False otherwise.
    """
    # Your code here
    for i in range(2,n+1):
        if n%i==0:
            return False
        else:
            return True
n=int(input("enter any number:"))
res=is_prime(n)
print(res)        

