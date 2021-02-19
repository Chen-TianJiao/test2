import cv2
import numpy as np
import random

img = cv2.imread("G:/pythondealPic/originalPic.jpg")
# cv2.imshow('image', img)
print(img.shape)
cropped = img[400:700, 300:600]  # 裁剪坐标为[y0:y1, x0:x1]
cv2.rectangle(cropped, (0, 0), (300, 300), (105,105,105), 10)
# cv2.rectangle(cropped, (310, 410), (590, 690), (105,105,105), 10)
cv2.imwrite("G:/pythondealPic/cut.jpg", cropped)

# rectangle = np.zeros((img.shape),dtype="uint8")
# cv2.rectangle(rectangle,(300, 400),(600, 700),(255,240,245),5)
# # cv2.imshow("Rectangle",rectangle)

# cicleHeart = [(300, 550),(350, 400),(600, 550),(350,700)]
# cicleHeart = [(300, 550)]
# for x in cicleHeart:
#     randomNum = random.randint(0,2)
#     randomNum = 1
#     print(randomNum)
#     if randomNum != 2:
#         circle = np.zeros((img.shape), dtype="uint8")
#         cv2.circle(circle, x, 50, (255,240,245), 5)
#         if randomNum == 0:
#             bitwise_or = cv2.bitwise_or(rectangle,circle)
#             cv2.imshow("Circle", bitwise_or)
#         elif randomNum == 1:
#             bitwiseXor = cv2.bitwise_xor(rectangle, circle)
#             cv2.imshow("XOR", bitwiseXor)
# circle = np.zeros((300,300),dtype="uint8")
# cv2.circle(circle,(150,150),150,255,-1)
# cv2.imshow("Circle",circle)
#
# bitwiseAnd = cv2.bitwise_and(rectangle,circle)
# cv2.imshow("And",bitwiseAnd)
#
# bitwiseOr = cv2.bitwise_or(rectangle,circle)
# cv2.imshow("OR",bitwiseOr)
#
# bitwiseXor = cv2.bitwise_xor(rectangle,circle)
# cv2.imshow("XOR",bitwiseXor)
#
# bitwiseNot = cv2.bitwise_not(rectangle)
# # cv2.imshow("Not",bitwiseNot)
# cv2.waitKey(0)
#
#
# cv2.fillPoly(img, [area1, area2], (255, 255, 255))
