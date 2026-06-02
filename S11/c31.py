def merge_three_dictionaries(dict1, dict2, dict3):
    # Your code goes here
    d = {}
    for i in range(len(dict1)):
        d[dict1[i]] = dict2[i] +dict3[i]   # or tuple(li2[i], li3[i])
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
li3=[]

for i in range(n):
    val=int(input(f"enter value {i+1}:"))
    li3.append(val)     

print("original:",li1)
print("original:",li2)
res=merge_three_dictionaries(li1,li2,li3)
print(res)
