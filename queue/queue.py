class Queue:
    def __init__(self):
        self.items=[]      
        
    def enqueue(self,item):
        self.items.insert(0,item)
        
    def dequeue(self):
        if not self.Is_empty():
            return self.items.pop()
         
    def Is_empty(self):
        return len(self.items)==0
            
    def Peek(self):
        if not self.Is_empty():
            return self.items[-1]
                    
    def __len__(self):
        return self.size()
        
    def size(self):
         return len(self.items)
         
    def printqueue(self):
        print(self.items)
         
'''         
q=Queue()
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.printqueue()
a=q.Peek()
l=q.size()

print(a)
print(l)

'''


        
