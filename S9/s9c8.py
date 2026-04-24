def generate_number_triangle(n):
    """
    Function to return a right-angled triangle of repeated numbers of side n as a list of strings.
    
    Parameters:
    n (int): The height of the triangle.
    
    Returns:
    list: A list of strings where each string represents a row of the triangle.
    """
    # Your code here
    li=[]
    for i in range(1,n+1):
        li.append(str(i)*i)
    return li
n=int(input("enter:"))
res=generate_number_triangle(n)
print(res)    


