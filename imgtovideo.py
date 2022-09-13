import cv2
import numpy as np
import glob

index = 0
img_array = []
for filename in sorted(glob.glob('C:/Users/1083310/Desktop/yolov3/data/images/*.png'), key=len):
    # print(filename)
    img = cv2.imread(filename)
    height, width, layers = img.shape
    size = (width, height)
    img_array.append(img)
    if len(img_array) == 15:
        out = cv2.VideoWriter(str(index) + '.avi', cv2.VideoWriter_fourcc(*'DIVX'), 2, size)
        for i in range(len(img_array)):
            out.write(img_array[i])
        out.release()
        index += 1
        img_array = []



