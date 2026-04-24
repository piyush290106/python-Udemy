def generate_diamond(n):
    """
    Function to return a diamond pattern of '*' of side n as a list of strings.
    
    Parameters:
    n (int): The number of rows for the upper part of the diamond.
    
    Returns:
    list: A list of strings where each string represents a row of the diamond.
    """
    # Your code here
    li=[]
    for i in range(1,n+1,2):
        spaces=(n-i)//2
        row=" "* spaces+ "*"*i
        li.append(row)
    for i in range(n-2,0,-2):
        spaces=(n-i)//2
        row=" "* spaces+ "*"*i
        li.append(row)
    return li
n=int(input("enter a number:"))
res=generate_diamond(n)
for row in res:
    print(row)
