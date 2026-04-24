def generate_sandglass(n):
    """
    Function to return a sandglass pattern of '*' of side n as a list of strings.
    
    Parameters:
    n (int): The height of the sandglass.
    
    Returns:
    list: A list of strings where each string represents a row of the sandglass pattern.
    """
    # Your code here
    li=[]
    for i in range(n, 0, -2):
        spaces = (n - i) // 2
        row = " " * spaces + "*" * i
        li.append(row)

    # Lower part (increasing stars)
    for i in range(3, n + 1, 2):
        spaces = (n - i) // 2
        row = " " * spaces + "*" * i
        li.append(row)

    return li
n=int(input("enter a number:"))
res=generate_sandglass(n)
for row in res:
    print(row)    
