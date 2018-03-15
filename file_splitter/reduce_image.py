from PIL import Image
import numpy as np
import os
import scipy
from scipy import misc
from scipy.misc import imsave
def load_image( infilename ) :
    img = Image.open( infilename )
    img.load()
    data = np.asarray( img, dtype="int32" )
    return data
train_data = []
base = "/Users/rdua/work/metamind/datasets/cervical-orginial-train"
base_red = "/Users/rdua/work/metamind/datasets/cervical-train-reduced-20%"
base_path = base + "/Type_3/"
base_red_path = base_red + "/Type_3/"


list_files = os.listdir(base_path)
for l in list_files:
    p = base_path + l
    try:
        arr = load_image(p)
        arr_resized = misc.imresize(arr, [1000,1000])
        print(l)
        imsave(base_red_path + l, arr_resized)
    except IOError as err:
        print("IO error: {0}".format(err))
