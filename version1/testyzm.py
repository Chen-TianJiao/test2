import cv2
import numpy as np
import random

img = cv2.imread("G:/pythondealPic/originalPic.jpg")
print(img.shape)
cropped = img[400:700, 300:600]
cv2.rectangle(cropped, (0, 0), (300, 300), (105,105,105), 10)
cv2.imwrite("G:/pythondealPic/cut.jpg", cropped)
