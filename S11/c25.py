def reverse_list(lst):
    # Your code goes here
    return lst[::-1]


    pass


n=int(input("enter size of list:"))
li=[]
for i in range(n):
    val=int(input(f"enter value {i+1}:"))
    li.append(val)
print("original:",li)
res=reverse_list(li)
print("reverse:",res)

