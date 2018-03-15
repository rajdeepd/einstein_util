import os
import shutil
from shutil import copytree
from pathlib2 import Path
def main():
    path = '/Users/rdua/work/metamind/datasets/temp-march14'

    type_1 = path + '/Type_1'
    type_2 = path + '/Type_2'
    type_3 = path + '/Type_3'

    for i in range(1, 20):
        if i < 10:
            folder = '00' + str(i)
        else:
            folder ='0' + str(i)
        parent = path + '/' + folder
        if not Path(parent).exists():
            os.mkdir(parent)

        src_1 = type_1 + '/' + folder
        src_2 = type_2 + '/' + folder
        src_3 = type_3 + '/' + folder

        if Path(src_1).exists():
            copytree(src_1, parent + '/Type_1')
        if Path(src_2).exists():
            copytree(src_2, parent + '/Type_2')
        if Path(src_3).exists():
            copytree(src_3, parent + '/Type_3')



if __name__ == '__main__':
    main()