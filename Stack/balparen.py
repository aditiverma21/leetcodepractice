from stack import Stack

def is_match(p1,p2):
    if p1=='(' and p2==')':
        return True
    elif p1=='{' and p2=='}':
        return True
    elif p1=='[' and p2==']':
        return True
    else:
        return False




def bal_parathesis(strvalue):
    s=Stack()
    Isbalanced=True
    index=0
    
    while (len(strvalue)>index) and Isbalanced:
        paren=strvalue[index]
        if paren in '({[':
            s.push(paren)
            
        else:
            if s.isempty():
                Isbalanced=False
                
            else:
                top=s.pop()
                if not is_match(top,paren):
                    Isbalanced=False
                    
        index+=1
        
        
    if s.isempty() and Isbalanced:
        return True
    else:
        return False
        
        
print("String : (((({})))) Balanced or not?")
print(bal_parathesis("(((({}))))"))

print("String : [][]]] Balanced or not?")
print(bal_parathesis("[][]]]"))


