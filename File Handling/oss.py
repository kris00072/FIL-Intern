import os
path="C:\\fl";
print(os.listdir(path))
for dirpath,dir,file in os.walk(path):

    #print(dirpath,dir,file)
    for i in file:
        if(i.endswith(".py")):
            print(i)