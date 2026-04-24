def generate_inverted_triangle(n):
    """
    Function to return an inverted right-angled triangle of '*' of side n as a list of strings.
    
    Parameters:
    n (int): The height and base of the triangle.
    
    Returns:
    list: A list of strings where each string represents a row of the triangle.
    """
    # Your code here
    li=[]
    for i in range(n ,0,-1):
        li.append("*"*i)
    return li    
n=int(input("enter:"))
res=generate_inverted_triangle(n)
print(res)