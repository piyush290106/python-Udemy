def merge_dicts_with_overlapping_keys(dicts):
    # Your code goes here

    res={}
    for d in dicts:
        for key,value in d.items():
            if key in res:
                res[key]+=value
            else:
                res[key]=value
    return res

n = int(input("Enter number of dictionaries: "))

dicts = []

for i in range(n):
    d = eval(input(f"Enter dictionary {i+1}: "))
    dicts.append(d)

print(merge_dicts_with_overlapping_keys(dicts))

    
    
