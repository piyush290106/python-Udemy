def is_palindromic_tuple(tup):
    return tup==tup[::-1]
    
n=int(input("enter size of list:"))
li=[]
for i in range(n):
    val=int(input(f"enter value{i+1}:"))
    li.append(val)
tu=tuple(li) 
res=is_palindromic_tuple(tu)
print(res)           

  
