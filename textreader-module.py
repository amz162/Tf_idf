import glob
import os

    
myDict = []
flag=0
path = 'sample/'

for filename in glob.glob(os.path.join(path, '*.txt')):
    content = open(os.path.join(filename), 'r')
    contents =content.read()
    if flag==0:
        myDict= [contents]
        flag=1
    else:
        myDict.append(contents)     
#print(myDict)

for i in myDict:
    print(i+" ----//------ ")





