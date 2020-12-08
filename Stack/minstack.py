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
we are mainatining two stacks one is mainstack everytime appending the new data 
but we compare the data with the min val in minstack and append thr also if its minimum than the last value in minst.
while poping also we have to compare the latest value from both the stack ; becz we have to remove from minst also as new min will be change if its 
poped from main stack its also poped from minst.

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