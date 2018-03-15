# -*- coding: utf-8 -*-
# @author: Rajdeep Dua

import argparse
import os
import shutil
from shutil import copyfile
import numpy as np
from zip_file import make_zipfile

def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(l), n):
        yield l[i:i + n]

def create_sub_folders(path, list):
    for l in list:
        file_name = os.path.basename(l)
        if not file_name.startswith('.'):
            new_ = path + '/' + file_name
            if not os.path.exists(new_):
                os.mkdir(new_)


def move_files(abs_dirname, dest_dir, zip_location):
    """Move files into subdirectories."""
    labels_split = {}
    files = [os.path.join(abs_dirname, f) for f in os.listdir(abs_dirname)]

    for f in files:
        print(f)
        f_basename = os.path.basename(f)
        if os.path.isdir(f):
            list_ = os.listdir(f)
            list_withdir = []
            for l in list_:
                print(f + '/' + l)
                list_withdir.append(f + '/' + l)
            list_split_ = list(chunks(list_withdir, 10))
            print(list_split_)
            labels_split[f_basename] = list_split_

    no_of_files = []
    total_split = 10


    # First create split folders

    for i in range(1, total_split):
        subdir_name = os.path.join(dest_dir, '{0:03d}'.format(i))
        if not os.path.exists(subdir_name):
            os.mkdir(subdir_name)

        else:
            print(subdir_name + ' already exists')
        create_sub_folders(subdir_name, files)
        for f in files:
            file_name = os.path.basename(f)

            if os.path.isdir(f):
                print(file_name)
                split = labels_split[file_name]
                print(i)
                print(len(split))
                if len(split) > 0:
                    split_specific = split[i - 1]
                    print(str(i) + ':' + file_name)
                    print(split_specific)
                    for s_ in split_specific:
                        s_base_file = os.path.basename(s_)
                        shutil.copyfile(s_, subdir_name + '/' + file_name + '/' + s_base_file)
                else:
                    print(file_name + ':split is empty')
        #shutil.make_archive(os.path.basename(subdir_name), 'zip',root_dir=None, base_dir=subdir_name  )
        make_zipfile(zip_location + '/' + os.path.basename(subdir_name) + '.zip', subdir_name)

def parse_args():
    """Parse command line arguments passed to script invocation."""
    parser = argparse.ArgumentParser(
        description='Split files into multiple subfolders.')

    parser.add_argument('src_dir', help='source directory')

    return parser.parse_args()


def main():
    """Module's main entry point (zopectl.command)."""
    src_dir ='/Users/rdua/work/metamind/datasets/temp-march14/cervical-train-reduced-20%'
    dest_dir ='/Users/rdua/work/metamind/datasets/temp-march14/' + 'destination'
    zip_location = '/Users/rdua/work/metamind/datasets/temp-march14/' + 'zipped'

    if not os.path.exists(src_dir):
        raise Exception('Directory does not exist ({0}).'.format(src_dir))

    move_files(src_dir, dest_dir, zip_location)


if __name__ == '__main__':
    main()