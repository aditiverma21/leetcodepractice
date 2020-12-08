#Create Target Array in the Given Order
'''
Input: nums = [0,1,2,3,4], index = [0,1,2,2,1]
Output: [0,4,1,3,2]
Explanation:
nums       index     target
0            0        [0]
1            1        [0,1]
2            2        [0,1,2]
3            2        [0,1,3,2]
4            1        [0,4,1,3,2]
End
''''''
'''

def createTargetArray(nums, index):
    target=[]
    for x,y in zip(nums,index):
        target.insert(y,x)
    return target
    
    '''
    array=[]
    l=len(index)
    for i in range(l):
        array.insert(index[i],nums[i])
    return array
    '''
            
            
        