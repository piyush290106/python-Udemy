def generate_hollow_right_angled_triangle(n):
    """
    Function to return a hollow right-angled triangle of '*' of side n as a list of strings.
    
    Parameters:
    n (int): The height of the triangle.
    
    Returns:
    list: A list of strings where each string represents a row of the triangle.
    """
    # Your code here
    li=[]
    for i in range(1,n+1):
        space=(n-i)//2
        row=" "*space +" "+"*"*i
        li.append(row)
    return li
n=int(input("enter any number"))
res=generate_hollow_right_angled_triangle(n)

for row in res:
    print(row)
