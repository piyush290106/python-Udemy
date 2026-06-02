def find_largest(arr,n):
    max=0
    for i in range(0,n):
        if arr[i]>max:
            max=arr[i]
    return max       




n=int(input("enter the size of list:"))
li=[]
for i in range(n):
    val=int(input(f"enter val {i+1}:"))
    li.append(val)
print(li)
res=find_largest(li,n)
print(res)