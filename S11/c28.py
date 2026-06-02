def merge_two_sorted_lists(list1, list2):
    # Your code goes here
    return list1+list2


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
res=merge_two_sorted_lists(li1,li2)
print(res)

