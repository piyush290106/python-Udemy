def insertion(arr,n):
    n=len(arr)

    for i in range(1,n):
        key=arr[i]
        j=i-1
        while j>=0 and arr[j]>key:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key    
            
    return arr
n=int(input("enter a number"))
li=[]
for i in range(n):
    val=int(input(f"enter any number {i+1}:"))
    li.append(val)
print(li)
res=insertion(li,n)
print(res)
        

