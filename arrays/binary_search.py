def binary(arr,target,n):
    start=0
    end=n-1
    while start<=end:
        mid=(start+end)//2
    

        if arr[mid]==target:
            return True
        elif arr[mid]<target:
            start=mid+1
        elif arr[mid]>target:
            end=mid-1
    return False            

n=int(input("enter size of array:" ))
li=[]
for i in range(n):
    val=int(input(f"enter  elemnt {i+1}:"))
    li.append(val)
li.sort()
print(li)      
target=int(input("enter target value:"))
res=binary(li,target,n)
print(res)

