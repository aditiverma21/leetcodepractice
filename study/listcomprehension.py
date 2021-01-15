list_a = [1, 2, 3, 4]
list_b = [2, 3, 4, 5]

res=[]
for a in list_a:
    for b in list_b:
        if a==b:
            res.append(a)
            
            
print(res)

#using list comprehension
print([a for a in list_a for b in list_b if a==b])

#Return numbers from the list which are not equal as a tuple:
list_aa = [1, 2, 3]
list_bb = [2, 7]

output=[(a,b) for a in list_aa for b in list_bb if a!=b]
print(output)
 
 
#converts each of the string from list_a to a smaller case.
name_list = ["Hello", "World", "In", "Python"]
print([ele.lower() for ele in name_list])

