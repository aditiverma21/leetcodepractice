# time complexity in slection sort is O(n*2) as each time it traverse along the arr by decreasing one position 

def Selction_Sort(arr):
    print(__name__)
    for i in range(len(arr)):
        s=arr.index(min(arr[i:len(arr)]))
        temp=arr[i]
        arr[i]=arr[s]
        arr[s]=temp
    return arr
    
'''    
f=open('heapsort.py','w+')
f.write("This is  Heapsort program")
f.close() 
'''  
arr=[64,25,12,22,11]
out=Selction_Sort(arr)
print(out)
print(__name__)


        
        