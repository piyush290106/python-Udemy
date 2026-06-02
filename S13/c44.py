def count_vowels(s):
    """
    Function to count the number of vowels in the input string.
    
    Parameters:
    s (str): The input string to check for vowels.
    
    Returns:
    int: The count of vowels in the input string.
    """
    # Your code here
    count=0
    for i in s:
        if i=='a'or i=='A' or i=='e' or i=='E' or i=='i' or i=='I' or i=='o' or i=='O' or i=='u' or i=='U':
            count+=1
    return count
s=input("enter any string:")
res=count_vowels(s)
print(res)        