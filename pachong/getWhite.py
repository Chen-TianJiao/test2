# import cv2
# import numpy as np
# src = cv2.imread("G:/newTest/yyy/new.jpg")
# cv2.namedWindow("input", cv2.WINDOW_AUTOSIZE)
# cv2.imshow("input", src)
# """
# 提取图中的红色部分
# """
# hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)
# low_hsv = np.array([0,0,221])
# high_hsv = np.array([180,30,255])
# mask = cv2.inRange(hsv,lowerb=low_hsv,upperb=high_hsv)
# cv2.imshow("test",mask)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# coding=utf-8
import cv2
import numpy as np

img = cv2.imread("G:/newTest/yyy/new.jpg", 0)

x = cv2.Sobel(img, cv2.CV_16S, 1, 0)
y = cv2.Sobel(img, cv2.CV_16S, 0, 1)

absX = cv2.convertScaleAbs(x)  # 转回uint8
absY = cv2.convertScaleAbs(y)

dst = cv2.addWeighted(absX, 0.5, absY, 0.5, 0)

# cv2.imshow("absX", absX)
# cv2.imshow("absY", absY)

cv2.imshow("Result", dst)

cv2.waitKey(0)
cv2.destroyAllWindows()
