import os
path = '/home/laksh/Desktop/dataset/withoutball'
files = os.listdir(path)
i = 1
for file in files:
    os.rename(os.path.join(path, file), os.path.join(path, "abcde" + str(i)+'.jpg'))
    i = i+1
