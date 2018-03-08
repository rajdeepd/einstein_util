import os
from voc_2005_parser.voc_2005_parser import generate_annotations

path = '/Users/rdua/work/metamind/datasets/VOC2005_1'
cal_tech = path + '/Annotations/Caltech_cars'


def main():
    folder = cal_tech
    generate_annotations(folder)


if __name__ == '__main__':
    main()