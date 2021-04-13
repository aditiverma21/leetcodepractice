def reformat_phoneno(number):
    '''
    if the string after removing spaces and - have no.of elements multiple of 3 then our for loop will give the proper result but 
    no.of elements like 4,7,10,13....res get '-' in second last position. SO we are modifying the main result accordingly.
    if 8 and 11 elements are present last two element comes after '-' that not a problm.
    '''
    l=[x for x in numbers if x.isdigit()]
    s=''.join(l)
    length=len(s)-1
    res=''
    for i in range(length):
        if i!=0 and i%3==0:
            res =res+"-"+s[i]
        else:
            res=res+s[i]
    mainres=''
    if res[len(res)-2]=='-':
        mainres=res[:len(res)-3]+'-'+s[length-2:]
        return mainres
    else:
        return res
            
            
