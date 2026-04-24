def sum_list(arr,numbers):
    # Your code goes here
    sum=0
    for i in arr:
        sum=sum+i
    return sum    


n=int(input("enter the numbers in a list:"))
li=[]
for i in range(n):
    val=int(input(f"enter value {i+1}:"))
    li.append(val)
print(li)    
res=sum_list(li,n)
print("sum is:",res)