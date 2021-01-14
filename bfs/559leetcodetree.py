class Node:
    def __init__(self,data:int):
        self.data=data
        self.children=None
    
    def add_children(self,li:list):
        self.children=li
        
        
root=Node(1)
print(root.data)
two=Node(2)
three=Node(3)
four=Node(4)
l1=[two,three,four]
root.add_children(l1)
five=Node(5)
six=Node(6)
l2=[five,six]
two.add_children(l2)
seven=Node(7)
eight=Node(8)
nine=Node(9)
l3=[seven,eight,nine]
four.add_children(l3)
'''
              1
            / | \
           2  3  4
          /\    /|\
         5 6   7 8 9
'''
def bfs(root:Node):
    q=[]
    q.append(root)
    while q:
        node=q.pop(0)
        if node.children:
            for n in node.children:
                q.append(n)
        print(node.data)
        
bfs(root)