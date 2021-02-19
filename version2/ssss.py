import numpy as np
import cv2
import random
from PIL import Image
import scipy.misc
import pandas as pd
import matplotlib.pyplot as plt

def transparent_back(img):
    img = img.convert('RGBA')
    L, H = img.size
    color_0 = img.getpixel((0,0))
    for h in range(H):
        for l in range(L):
            dot = (l,h)
            color_1 = img.getpixel(dot)
            if color_1 == color_0:
                color_1 = color_1[:-1] + (0,)
                img.putpixel(dot,color_1)
    return img

if __name__ == '__main__':
    img=Image.open('G:/pythondealPic/cut.png')
    img=transparent_back(img)
    img.save('G:/pythondealPic/cut.png')