'''
Create min stack using stack
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
i/p:
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]
o/p:
[null,null,null,null,-3,null,0,-2]

expanation
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2


'''

class MinStack:
    
    def __init__(self):
        self.st=[]
        self.minst=[]
        
    def push(self, x):
        if self.minst==[] or self.minst[-1]>=x:
            self.minst.append(x)
        self.st.append(x)
        
    def pop(self):
        if self.st[-1]==self.minst[-1]:
            self.minst.pop()
        self.st.pop()
        
    def top(self):
        return self.st[-1]
        
    def getMin(self):
        return self.minst[-1]
        
        

# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(-2)
obj.push(0)
obj.push(-3)
param_1 = obj.getMin()
obj.pop()
param_3 = obj.top()
param_4 = obj.getMin()
print(param_1,param_3,param_4)