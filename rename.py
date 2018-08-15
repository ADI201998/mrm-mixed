import os
path = '/home/laksh/deep_learning/non-ball/test-set'
files = os.listdir(path)
i = 1
for file in files:
    os.rename(os.path.join(path, file), os.path.join(path,"non-ball-test-set"+str(i)+'.jpg'))
    i = i+1
