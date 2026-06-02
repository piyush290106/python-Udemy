
def check_unique(lst):
    return len(lst) == len(set(lst))
    # Your code goes here

n=int(input("enter the size of list:"))
li=[]
for i in range(n):
    val=int(input(f"enter val {i+1}:"))
    li.append(val)
print(li)
res=check_unique(li)
print(res)


