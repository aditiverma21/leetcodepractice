import os
import shutil

f=open('temp.py','w+')
f.write("This is  Temporary program")
f.close() 
print(os.getcwd())
print(os.listdir())

shutil.move('temp.py',"E:\localleetcode\leetcodepractice\study")
#[6,9,14,5,3,8,7,12,13,1]



