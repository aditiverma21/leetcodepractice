
class Node:
    def __init__(self,data:int):
        self.data=data
        self.left=None
        self.right=None
         
    def add_left(self,node):
        self.left=node

    def add_right(self,node):
        self.right=node

root=Node(1)
print(root.data)
ldata=Node(2)
rdata=Node(3)
root.add_left(ldata)
root.add_right(rdata)
lldata=Node(4)
lrdata=Node(5)
rldata=Node(6)
rrdata=Node(7)

ldata.add_left(lldata)
ldata.add_right(lrdata)
rdata.add_left(rldata)
rdata.add_right(rrdata)

def bfs(root:Node):
    qu=[]
    
    qu.append(root)
    
    while qu!=[]:
        node=qu.pop(0)
        if node.left!=None:
            qu.append(node.left)
        if node.right!=None:
            qu.append(node.right)
        print(node.data) 
    
bfs(root)


    
    
        