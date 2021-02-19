import numpy as np
import cv2
import random
from PIL import Image
from PIL import ImageGrab
import scipy.misc
import pandas as pd
import matplotlib.pyplot as plt
import os
import time
import json

# 修改图片尺寸到固定（320，160）
def changePicRatio(src, size):
    img = cv2.imread(src)
    newImage = cv2.resize(img, size, interpolation=cv2.INTER_AREA)
    cv2.imwrite(src, newImage)

# 创建一个图像
start = time.time()
floder = "G:/newTest/"
# floder = "G:/pythondealPic/"
orignalImgName = "originalPic.png"
compoundImgName = "compoundPic.png"
orignalImg = cv2.imread(floder + orignalImgName)
color_red = (47, 79, 79)
color_black = (0, 0, 0)
zeros = np.zeros((orignalImg.shape), dtype = np.uint8)

# length = 3840
# width = 2160
# sideLength = 300
length = 960
width = 480
sideLength = (int)(width/5)
circleR = (int)(sideLength/6)
leftPointx = random.randint((int)(length/6), (int)(length * 2 / 3))
leftPointy = random.randint((int)(width/6), (int)(width * 2 / 3))
rightPointx = leftPointx + sideLength
rightPointy = leftPointy + sideLength

# 绘制一个红色填充的矩形
cv2.rectangle(zeros, (leftPointx, leftPointy), (rightPointx, rightPointy), (47, 79, 79), -1)
left = random.randint(0, 1)
left = 1
right = random.randint(0, 2)
right = 0
high = random.randint(0, 2)
high = 0
low = random.randint(0, 2)
low = 2
count = 0
zeros_mask1=""

# # 显示
# alpha 为第一张图片的透明度
alpha = 1
# beta 为第二张图片的透明度
beta = 0.9
gamma = 0
# # cv2.addWeighted 将原始图片与 mask 融合
mask_img = "";

circleList = []
if left == 0:
    zeros_mask1 = cv2.circle(zeros, (leftPointx - 9, (int)(leftPointy + sideLength/2)), circleR, color_red, -1, cv2.LINE_AA)
    circleList.append(0)
elif left == 1:
    zeros_mask1 = cv2.circle(zeros, (leftPointx + 9, (int)(leftPointy + sideLength/2)), circleR, color_black, -1, cv2.LINE_AA)
    circleList.append(1)
else:
    circleList.append(2)

if right == 0:
    cv2.circle(zeros, (rightPointx + 9, (int)(leftPointy + sideLength/2)), circleR, color_red, -1, cv2.LINE_AA)
    circleList.append(0)
elif right == 1:
    cv2.circle(zeros, (rightPointx - 9, (int)(leftPointy + sideLength/2)), circleR, color_black, -1, cv2.LINE_AA)
    circleList.append(1)
else:
    circleList.append(2)

if high == 0:
    cv2.circle(zeros, ((int)(leftPointx + sideLength/2), leftPointy - 9), circleR, color_red, -1, cv2.LINE_AA)
    circleList.append(0)
elif high == 1:
    cv2.circle(zeros, ((int)(leftPointx + sideLength/2), leftPointy + 9), circleR, color_black, -1, cv2.LINE_AA)
    circleList.append(1)
else:
    circleList.append(2)

if low == 0:
    cv2.circle(zeros, ((int)(leftPointx + sideLength/2), rightPointy + 9), circleR, color_red, -1, cv2.LINE_AA)
    circleList.append(0)
elif low == 1:
    cv2.circle(zeros, ((int)(leftPointx + sideLength/2), rightPointy - 9), circleR, color_black, -1, cv2.LINE_AA)
    circleList.append(1)
else:
    circleList.append(2)

zeros_mask = np.array(zeros_mask1)

# 划线
mask_img = cv2.addWeighted(orignalImg, alpha, zeros_mask, beta, gamma)

cv2.imwrite(floder + compoundImgName, mask_img)
cv2.imwrite(floder + "mask.png", zeros_mask)

# imgmaskkk = Image.open(floder + "mask.png")
imgmaskkk = Image.open(floder + "mask.png")
imgmaskkk = imgmaskkk.convert("RGBA")
datas = imgmaskkk.getdata()
newData = list()

compound = Image.open(floder + compoundImgName)
compound = compound.convert("RGBA")
compoundDatas = compound.getdata()
compoundDataList = list()

for w in range(1, imgmaskkk.size[0] - 1):
    for h in range(1, imgmaskkk.size[1] - 1):
        if imgmaskkk.getpixel((w, h)) != (0, 0, 0, 255):
            if imgmaskkk.getpixel((w + 1, h)) == (0, 0, 0, 255) or imgmaskkk.getpixel((w, h + 1)) == (0, 0, 0, 255):
                compound.putpixel((w, h), (255, 255, 255, 0))
            if imgmaskkk.getpixel((w, h - 1)) == (0, 0, 0, 255) or imgmaskkk.getpixel((w - 1, h)) == (0, 0, 0, 255):
                compound.putpixel((w, h), (255, 255, 255, 0))
            if imgmaskkk.getpixel((w - 1, h - 1)) == (0, 0, 0, 255) or imgmaskkk.getpixel((w - 1, h + 1)) == (0, 0, 0, 255):
                compound.putpixel((w, h), (255, 255, 255, 0))
            if imgmaskkk.getpixel((w + 1, h - 1)) == (0, 0, 0, 255) or imgmaskkk.getpixel((w + 1, h - 1)) == (0, 0, 0, 255):
                compound.putpixel((w, h), (255, 255, 255, 0))
        # if (imgmaskkk.getpixel((w, h)) != imgmaskkk.getpixel((w + 1, h))) or (imgmaskkk.getpixel((w, h)) != imgmaskkk.getpixel((w, h + 1))) or (imgmaskkk.getpixel((w, h)) != imgmaskkk.getpixel((w - 1, h))) or (imgmaskkk.getpixel((w, h)) != imgmaskkk.getpixel((w, h - 1))):
        #     compound.putpixel((w, h), (255, 255, 255, 0))

for item in datas:
    if item[0] == 0 and item[1] == 0 and item[2] == 0:
        newData.append((0, 0, 0, 0))
    else:
        newData.append(item)

# compound.putdata(compoundDataList)
compound.save(floder + "compound.png", "PNG")
imgmaskkk.putdata(newData)
imgmaskkk.save(floder + "newmask.png", "PNG")

mask = cv2.imread(floder + "newmask.png", cv2.IMREAD_GRAYSCALE) # 将彩色mask以二值图像形式读取
masked = cv2.add(orignalImg, np.zeros(np.shape(orignalImg), dtype = np.uint8), mask = mask) #将image的相素值和mask像素值相加得到结果
cv2.imwrite(floder + "cutTemp.png", masked)

imgCut = cv2.imread(floder + "cutTemp.png")
cropped = imgCut[(leftPointy - circleR - 9 - 3) : (rightPointy + circleR + 9 + 3), (leftPointx - circleR - 9 - 3) : (rightPointx + circleR + 9 + 3)]  # 裁剪坐标为[y0:y1, x0:x1]
cv2.imwrite(floder + "cutTemp.png", cropped)

changePicRatio(floder + "cutTemp.png", (51, 51))
tt = Image.open(floder + "cutTemp.png")
tt_array = tt.load()
width = tt.size[0]  # 获取宽度
height = tt.size[1]  # 获取长度

ttMask = tt.convert("RGBA")
ttMask = ttMask.convert("RGBA")
datas = ttMask.getdata()
newData = list()
for item in datas:
    if item[0] == 0 and item[1] == 0 and item[2] == 0:
        newData.append((0, 0, 0, 0))
    else:
        newData.append(item)

ttMask.putdata(newData)
ttMask.save(floder + "cut.png", "PNG")
# 给滑块加阴影
cutImage = Image.open(floder + "cut.png")
cutImage = cutImage.convert("RGBA")
cutImageDatas = cutImage.getdata()
cutImageDataList = list()
centerRantangle = (cutImage.size[0]/2, cutImage.size[0]/2)
bigCircleR = circleR + sideLength/2
for w in range(1, cutImage.size[0] - 1):
    for h in range(1, cutImage.size[1] - 1):
        # if cutImage.getpixel((w, h)) != (0, 0, 0, 0):
        #     if pow((w - centerRantangle[0]), 2) + pow((h - centerRantangle[1]), 2) > pow(bigCircleR, 2):
        #     # print(pow((w - centerRantangle[0]), 2) + pow((h - centerRantangle[1]), 2))
        #         cutImage.putpixel((w, h), (192, 192, 192, 255))
        # else :
        # # print(w, h)
        if cutImage.getpixel((w, h)) != (0, 0, 0, 0):

            if cutImage.getpixel((w + 1, h)) == (0, 0, 0, 0):
                cutImage.putpixel((w - 1, h), (	192,192,192, 255))
                cutImage.putpixel((w, h), (	192,192,192, 255))
                # cutImage.putpixel((w - 2, h), (240, 230, 140, 255))
                # cutImage.putpixel((w, h), (0, 0, 0, 255))
            if cutImage.getpixel((w - 1, h)) == (0, 0, 0, 0):
                cutImage.putpixel((w + 1, h), (	192,192,192, 255))
                cutImage.putpixel((w, h), (	192,192,192, 255))
                # cutImage.putpixel((w + 2, h), (240, 230, 140, 255))
                # cutImage.putpixel((w, h), (0, 0, 0, 255))
            if cutImage.getpixel((w, h + 1)) == (0, 0, 0, 0):
                cutImage.putpixel((w, h - 1), (	192,192,192, 255))
                cutImage.putpixel((w, h), (	192,192,192, 255))
                # cutImage.putpixel((w, h - 2), (240, 230, 140, 255))
                # cutImage.putpixel((w, h), (0, 0, 0, 255))
            if cutImage.getpixel((w, h - 1)) == (0, 0, 0, 0):
                cutImage.putpixel((w, h + 1), (	192,192,192, 255))
                cutImage.putpixel((w, h), (	192,192,192, 255))
                # cutImage.putpixel((w, h + 2), (240, 230, 140, 255))
                # cutImage.putpixel((w, h), (0, 0, 0, 255))
cutImage.save(floder + "newCut.png", "PNG")
end = time.time()
cost = end - start
print(cost)
resultDic = {}
resultDic['compound'] = os.path.join(floder, "compound.png")
resultDic['block'] = os.path.join(floder, "newcut.png")
resultDic['centerPoint'] = (leftPointx + sideLength, leftPointy + sideLength)
print(json.dumps(resultDic))

changePicRatio(resultDic['compound'], (320, 160))
# changePicRatio(resultDic['block'], (51, 51))

# os.remove(os.path.join(floder, "cut.png"))
# os.remove(os.path.join(floder, "compoundPic.png"))
# os.remove(os.path.join(floder, "mask.png"))
# os.remove(os.path.join(floder, "newmask.png"))
# os.remove(os.path.join(floder, "cutTemp.png"))
