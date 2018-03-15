import os
import shutil

dir_src = "/Users/rdua/Downloads/train-2/Type_3/"
dir_dst = "/Users/rdua/Downloads/test-2/Type_3"
count = 0

list = os.listdir(dir_src)
for filename in os.listdir(dir_src):
    if count < 150:
      if filename.endswith('.png'):
          shutil.copy( dir_src + filename, dir_dst)
      print(str(count) + ':' + filename + ' copied')
      count += 1
    else:
      exit