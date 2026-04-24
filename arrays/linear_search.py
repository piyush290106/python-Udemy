# li=[1,2,3,4,5]
# target=2
# for i in li:
#     if li[i]==target:
#         print (True)
#         break
#     else:
#        print( False)

# ------------------------------------------------------
# def linear_search(arr,target):
#     size=len(arr)
#     for i in range(0,size):
#         if arr[i]==target:
#             return i
#     return -1

# li=[1,2,3,4,5,6]
# target=3
# res=linear_search(li,target)
# print(res)
        

# def linear_search(arr, target):
#     for i in range(len(arr)):
#         if arr[i] == target:
#             return i
#     return -1

# # Taking list input
# li = list(map(int, input("Enter elements separated by space: ").split()))

# # Taking target input
# target = int(input("Enter target value: "))

# # Function call
# res = linear_search(li, target)

# # Output
# if res != -1:
#     print("Element found at index:", res)
# else:
#     print("Element not found")

# --user input---
n=int(input("enter the number of elements:"))
li=[]
for i in range(n):
    val = int(input(f"Enter element {i+1}: "))  
    li.append(val)
print(li)    

