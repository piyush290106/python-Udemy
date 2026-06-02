def rotate_list(lst, k):
    # Your code goes here
    n=len(lst)
    k=k%n
    return lst[-k:]+lst[:-k]
           
            
n=int(input("enter size of list:"))
li=[]
for i in range(n):
    val=int(input(f"enter value {i+1}:"))
    li.append(val)
k = int(input("enter rotation value k:"))

print("original:",li)
res = rotate_list(li, k)

print("rotated list:", res)
            
            
            
            
    
