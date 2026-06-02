def selection(arr,n):
    for i in range(n):
        min_index=i
        for j in range(i+1,n):
            if arr[j]<arr[min_index]:
                min_index=j
        arr[i],arr[min_index]=arr[min_index],arr[i]
    return arr
n=int(input("enter a number"))
li=[]
for i in range(n):
    val=int(input(f"enter any number {i+1}:"))
    li.append(val)
print(li)
res=selection(li,n)
print(res)
