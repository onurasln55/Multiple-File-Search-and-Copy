import os
import shutil
list_dirs=[]
index_dirs=0
path=input("Dosyaların aranacagı dizini girin:")
path=path.replace("\\","/")
for root, dirs, files in os.walk(path, topdown=False):
   for name in dirs:
      i=os.path.join(root, name)
      i=i.replace("\\","/")
      list_dirs.insert(index_dirs,i)
      index_dirs=index_dirs+1
dest=input("Hedef:")
dest=dest.replace("\\","/")
print(dest)
ara=input("Alınacak dosya adı:")
kopya_list=[]
index=0
for i in list_dirs:
   if ara in i:
      print(i)
      temp=i.replace(path,dest)
      print(temp)
      shutil.copytree(i, temp)
