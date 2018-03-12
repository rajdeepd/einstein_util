import cv2 as cv
import numpy as np
path = r"C:\Users\Public\Pictures\Sample Pictures\Hydrangeas.jpg"
img = cv.imread(path)
normalizedImg = np.zeros((800, 800))
normalizedImg = cv.normalize(img,  normalizedImg, 0, 255, cv.NORM_MINMAX)
cv.imshow('dst_rt', normalizedImg)
cv.waitKey(0)
cv.destroyAllWindows()