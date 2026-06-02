def is_subset(lst1, lst2):
    # Your code goes here
    for i in lst1:
        if i not in lst2:
            return False
        else:
            return True

    
n=int(input("enter any number:"))
li1=[]
for i in range(0,n):
    val1=int(input(f"enter value {i+1}:"))
    li1.append(val1)
n=int(input("enter any number:"))

li2=[]
for i in range(0,n):
    val2=int(input(f"enter value {i+1}:"))
    li2.append(val2)
res=is_subset(li1,li2)
print(res)
