def remove_duplicates(lst):
    # Your code goes here
    li=set(lst)
    lii=list[li]
    return lii




n=int(input("enter the size of list:"))
li=[]
for i in range(n):
    val=int(input(f"enter val {i+1}:"))
    li.append(val)
print(li)
res=remove_duplicates(li)
print(res)
