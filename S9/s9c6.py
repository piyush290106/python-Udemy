def generate_pyramid(n):
    """
    Function to return a pyramid pattern of '*' of side n as a list of strings.
    
    Parameters:
    n (int): The number of rows in the pyramid.
    
    Returns:
    list: A list of strings where each string represents a row of the pyramid.
    """
    # Your code here
    li=[]
    for i in range(1,n+1,1):
        li.append("*" *i)
    return li 
n=int(input("enter:"))
res=generate_pyramid(n)
print(res)   
