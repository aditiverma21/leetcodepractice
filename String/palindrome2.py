def palindrome(inp):
    i=0
    j=len(inp)-1
    while(j>i):
        while not inp[i].isalnum() and j>i:
            i+=1
        while not inp[j].isalnum() and j>i:
            j-=1
            
        if inp[i].lower()!=inp[j].lower():
            return False
        i+=1
        j-=1    
    return True

        
result=palindrome('Was it a cat I saw?')
print(result)
	