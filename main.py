import os
import shutil
list_dirs=[]
index_dirs=0
path="C:/Users/Adeo/Downloads"
for root, dirs, files in os.walk(path, topdown=False):
   for name in dirs:
      i=os.path.join(root, name)
      i=i.replace("\\","/")
      list_dirs.insert(index_dirs,i)
      index_dirs=index_dirs+1
dest="C:/Users/Adeo/OneDrive - ADEO/Desktop/kopyala"
ara=input("Alınacak dosya adı:")
#print(list_dirs)
kopya_list=[]
index=0
for i in list_dirs:
   if ara in i:
      print(i)
      temp=i.replace(path,dest)
      print(temp)
      shutil.copytree(i, temp)
