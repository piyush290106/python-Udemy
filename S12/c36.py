def sum_of_even_numbers(n):
    """
    Function to return the sum of the first n even natural numbers.
    
    Parameters:
    n (int): The number of even numbers to sum.
    
    Returns:
    int: The sum of the first n even natural numbers.
    """
    # Your code here
    n=int(input("enter any number:"))
    sum=0
    for i in range(1,n+1):
        sum = sum + (2 * i)
    return sum
   
n = int(input("enter any number:"))
res=sum_of_even_numbers(n)
print(res)
