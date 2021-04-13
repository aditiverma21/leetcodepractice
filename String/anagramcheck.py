
st1="aditiiii"
st2="dtiia"
#An anagram of a string is another string that contains the same characters, only the order of characters can be different. For example, “abcd” and “dabc” are an anagram of

from collections import Counter
def anagram_check(str1,str2):
    dict_1=Counter(str1)
    count=0
    print(dict_1)
    for ch in str2:
        if ch in dict_1:
            # we are decrementing in dic1 so for every occurence of ch in st2 we are marking in dict1 by decrementing 1
            dict_1[ch]=dict_1[ch]-1
            if dict_1[ch]==0:
                count+=1
        else:    
            return False
    if len(dict_1)==count:        
        return True
    else:
        return False

result=anagram_check('adbs','dbas')
print(result)
        
'''
def Anagramcheck(st1,st2):
    dd={}
    
    if len(st1)!=len(st2):
        return False
    
    for k in st1:
        if k not in dd.keys():
            dd[k]=1
        else:
            dd[k]+=1
    print(dd) 
    
    count=0    
    for ch in st2:    
        if ch in dd.keys():
            dd[ch]=dd[ch]-1
            if dd[ch]==0:
                count+=1
        else:
            return("Strings are not anagram")
    print(dd)
    print(count)
    if len(dd)==count:
        return ("Strings are Anagram")
    else:
        return("Strings are not anagram")
            

def demo(st1,st2):
    for i in st1:
        print(i)
        if i in st2:
            st2=st2.replace(i,"",1)
            print(st2)
        else:
            return("string is not Anagram")   
        
    return("Strings are Anagram")
    
   
out=Anagramcheck(st1,st2)
print(out)
'''      
        