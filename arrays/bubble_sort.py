def bubble(arr,n):
    max=0
    for i in range(0,n):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr            

               
n=int(input("enter a number:"))

li=[]
for i in range(n):
    val=int(input(f"enter value{i+1}:"))
    li.append(val)
print(li)    

res=bubble(li,n)
print(res)