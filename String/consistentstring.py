#allowed = "ab", words = ["ad","bd","aaab","baa","badab"]

def countConsistentStrings(allowed, words):
    #return sum(all(ch in allowed for ch in word)for word in words)
    
    count=0
    maincount=0
    for element in words:
        for ch in element:
            if ch not in allowed:
                count=0
                break
            else:
                count+=1
        if count>=1:
            maincount+=1
            
    return maincount

a="ab"
w= ["ad","bd","aaab","baa","badab"]  
out=countConsistentStrings(a,w)
print(out)