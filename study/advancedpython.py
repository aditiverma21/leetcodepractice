import os
import shutil

f=open('temp.py','w+')
f.write("This is  Temporary program")
f.close() 
print(os.getcwd())
print(os.listdir())

shutil.move('temp.py',"E:\localleetcode\leetcodepractice\study")
shutil.move("advancedpython.py","E:\localleetcode\leetcodepractice\study")



