def max_consecutive_difference(lst):
    max=0
    # Your code goes here
    for i in range(len(lst)-1):
        diff=abs(lst[i]-lst[i+1])
        if diff>max:
            max=diff
    return max
n=int(input("enter size of list:"))
li=[]
for i in range(n):
    val=int(input(f"enter value {i+1}:"))
    li.append(val)
print("original:",li)
res=max_consecutive_difference(li)
print(f"consecutive difference between {i} and {i+1} element is:{res}")    




