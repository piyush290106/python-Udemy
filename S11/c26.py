def count_even_odd(lst,n):
    c_even=0
    c_odd=0
    for i in range(n):
        if lst[i]%2==0:
            c_even+=1
        else:
            c_odd+=1
    return c_even,c_odd


    # Your code goes here
    pass



n=int(input("enter size of list:"))
li=[]
for i in range(n):
    val=int(input(f"enter value {i+1}:"))
    li.append(val)
print("original:",li)
even,odd=count_even_odd(li,n)
print("even count is:",even)
print("odd count is:",odd)

