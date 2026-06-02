def merge_lists_to_dictionary(keys, values):
    # Your code goes here
    d=dict(zip(keys,values))
    return d

n=int(input("enter size of list:"))
li1=[]
for i in range(n):
    val=int(input(f"enter value {i+1}:"))
    li1.append(val)
li2=[]
for i in range(n):
    val=int(input(f"enter value {i+1}:"))
    li2.append(val)    

print("original:",li1)
print("original:",li2)
res=merge_lists_to_dictionary(li1,li2)
print(res)
