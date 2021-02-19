import numpy as np
import cv2
import random
from PIL import Image
import os
import time
import json

# 修改图片尺寸到固定（320，160）
def changePicRatio(src, size):
    img = cv2.imread(src)
    newImage = cv2.resize(img, size, interpolation=cv2.INTER_AREA)
    cv2.imwrite(src, newImage)

# 清除黑色部分
def deleteBlack(src):
    image = Image.open(src)
    imageMask = image.convert("RGBA")
    imageMask = imageMask.convert("RGBA")
    datas = imageMask.getdata()
    newData = list()
    for item in datas:
        if item[0] == 0 and item[1] == 0 and item[2] == 0:
            newData.append((0, 0, 0, 0))
        else:
            newData.append(item)

    imageMask.putdata(newData)
    imageMask.save(src, "PNG")
    return imageMask

# 创建一个图像
start = time.time()
floder = "G:/newTest/"
orignalImg = "originalPic1.png"
compoundwithoutLineImg = "1_compoundwithoutLine.png"
maskImg = "2_mask.png"
# newMaskImg = "3_newmask.png"
blockTemp1 = "4_blockTemp1.png"
blockTemp2 = "5_blockTemp2.png"
block = "6_block.png"
compoundImgName = "7_compound.png"

color_red = (47, 79, 79)
color_black = (0, 0, 0)
line_color = (255, 255, 255, 255)
# line_color = (255, 255, 255, 0)
length = 640
width = 320
sideLength = (int)(width/5)
circleR = (int)(sideLength/6)
leftPointx = random.randint((int)(length/6), (int)(length * 2 / 3))
leftPointy = random.randint((int)(width/6), (int)(width * 2 / 3))
rightPointx = leftPointx + sideLength
rightPointy = leftPointy + sideLength

orignalImg = cv2.imread(floder + orignalImg)
zeros = np.zeros((orignalImg.shape), dtype = np.uint8)

# 绘制原图加上滑块的底色图

# 绘制一个红色填充的矩形
cv2.rectangle(zeros, (leftPointx, leftPointy), (rightPointx, rightPointy), (47, 79, 79), -1)
left = random.randint(0, 1)
# left = 1
right = random.randint(0, 2)
# right = 0
high = random.randint(0, 2)
# high = 0
low = random.randint(0, 2)
# low = 2
# count = 0

# # cv2.addWeighted 将原始图片与 mask 融合
circleList = []
zeros_mask1=""
# 圆心位移的距离(320*160时是3，其他尺寸按比例缩放)
disPlacetance = 3 * (int)(length/320)
if left == 0:
    zeros_mask1 = cv2.circle(zeros, (leftPointx - disPlacetance, (int)(leftPointy + sideLength/2)), circleR, color_red, -1, cv2.LINE_AA)
    circleList.append(0)
elif left == 1:
    zeros_mask1 = cv2.circle(zeros, (leftPointx + disPlacetance, (int)(leftPointy + sideLength/2)), circleR, color_black, -1, cv2.LINE_AA)
    circleList.append(1)
else:
    circleList.append(2)

if right == 0:
    cv2.circle(zeros, (rightPointx + disPlacetance, (int)(leftPointy + sideLength/2)), circleR, color_red, -1, cv2.LINE_AA)
    circleList.append(0)
elif right == 1:
    cv2.circle(zeros, (rightPointx - disPlacetance, (int)(leftPointy + sideLength/2)), circleR, color_black, -1, cv2.LINE_AA)
    circleList.append(1)
else:
    circleList.append(2)

if high == 0:
    cv2.circle(zeros, ((int)(leftPointx + sideLength/2), leftPointy - disPlacetance), circleR, color_red, -1, cv2.LINE_AA)
    circleList.append(0)
elif high == 1:
    cv2.circle(zeros, ((int)(leftPointx + sideLength/2), leftPointy + disPlacetance), circleR, color_black, -1, cv2.LINE_AA)
    circleList.append(1)
else:
    circleList.append(2)

if low == 0:
    cv2.circle(zeros, ((int)(leftPointx + sideLength/2), rightPointy + disPlacetance), circleR, color_red, -1, cv2.LINE_AA)
    circleList.append(0)
elif low == 1:
    cv2.circle(zeros, ((int)(leftPointx + sideLength/2), rightPointy - disPlacetance), circleR, color_black, -1, cv2.LINE_AA)
    circleList.append(1)
else:
    circleList.append(2)
zeros_mask = np.array(zeros_mask1)

# 划线
# # 显示
# alpha 为第一张图片的透明度
alpha = 1
# beta 为第二张图片的透明度
beta = 0.9
gamma = 0
mask_img = cv2.addWeighted(orignalImg, alpha, zeros_mask, beta, gamma)
cv2.imwrite(floder + compoundwithoutLineImg, mask_img)
cv2.imwrite(floder + maskImg, zeros_mask)

# 给聚合图中的滑块部分添加边界线
imgmaskkk = Image.open(floder + maskImg)
imgmaskkk = imgmaskkk.convert("RGBA")

compound = Image.open(floder + compoundwithoutLineImg)
compound = compound.convert("RGBA")
compoundDatas = compound.getdata()
compoundDataList = list()

for w in range(1, imgmaskkk.size[0] - 1):
    for h in range(1, imgmaskkk.size[1] - 1):
        if imgmaskkk.getpixel((w, h)) != (0, 0, 0, 255):
            if imgmaskkk.getpixel((w + 1, h)) == (0, 0, 0, 255):
                compound.putpixel((w, h), (255, 255, 255, 0))
                compound.putpixel((w - 1, h), (255, 255, 255, 0))
            if imgmaskkk.getpixel((w - 1, h)) == (0, 0, 0, 255):
                compound.putpixel((w, h), (255, 255, 255, 0))
                compound.putpixel((w + 1, h), (255, 255, 255, 0))
            if imgmaskkk.getpixel((w, h + 1)) == (0, 0, 0, 255):
                compound.putpixel((w, h), (255, 255, 255, 0))
                compound.putpixel((w, h - 1), (255, 255, 255, 0))
            if imgmaskkk.getpixel((w, h - 1)) == (0, 0, 0, 255):
                compound.putpixel((w, h), (255, 255, 255, 0))
                compound.putpixel((w, h + 1), (255, 255, 255, 0))
            if imgmaskkk.getpixel((w - 1, h - 1)) == (0, 0, 0, 255):
                compound.putpixel((w, h), (255, 255, 255, 0))
                compound.putpixel((w + 1, h + 1), (255, 255, 255, 0))
            if imgmaskkk.getpixel((w + 1, h + 1)) == (0, 0, 0, 255):
                compound.putpixel((w, h), (255, 255, 255, 0))
                compound.putpixel((w - 1, h - 1), (255, 255, 255, 0))
            if imgmaskkk.getpixel((w + 1, h - 1)) == (0, 0, 0, 255):
                compound.putpixel((w, h), (255, 255, 255, 0))
                compound.putpixel((w - 1, h + 1), (255, 255, 255, 0))
            if imgmaskkk.getpixel((w - 1, h + 1)) == (0, 0, 0, 255):
                compound.putpixel((w, h), (255, 255, 255, 0))
                compound.putpixel((w + 1, h - 1), (255, 255, 255, 0))
compound.save(floder + compoundImgName, "PNG")

imgmaskkk = deleteBlack(floder + maskImg)

mask = cv2.imread(floder + maskImg, cv2.IMREAD_GRAYSCALE) # 将彩色mask以二值图像形式读取
masked = cv2.add(orignalImg, np.zeros(np.shape(orignalImg), dtype = np.uint8), mask = mask) #将image的相素值和mask像素值相加得到结果
cv2.imwrite(floder + blockTemp1, masked)
imgCut = cv2.imread(floder + blockTemp1)
# cropped = imgCut[(leftPointy - circleR - disPlacetance - 3) : (rightPointy + circleR + disPlacetance + 3), (leftPointx - circleR - disPlacetance - 3) : (rightPointx + circleR + disPlacetance + 3)]  # 裁剪坐标为[y0:y1, x0:x1]
cropped = imgCut[0 : width, (leftPointx - circleR - disPlacetance - 3) : (rightPointx + circleR + disPlacetance + 3)]  # 裁剪坐标为[y0:y1, x0:x1]
cv2.imwrite(floder + blockTemp2, cropped)

deleteBlack(floder + blockTemp2)

# 给滑块加阴影
cutImage = Image.open(floder + blockTemp2)
cutImage = cutImage.convert("RGBA")
cutImageDatas = cutImage.getdata()
cutImageDataList = list()
# centerRantangle = (cutImage.size[0]/2, cutImage.size[0]/2)
bigCircleR = circleR + sideLength/2
for w in range(1, cutImage.size[0] - 1):
    for h in range(1, cutImage.size[1] - 1):
        if cutImage.getpixel((w, h)) != (0, 0, 0, 0):
            if cutImage.getpixel((w + 1, h)) == (0, 0, 0, 0):
                cutImage.putpixel((w - 1, h), line_color)
                cutImage.putpixel((w - 2, h), line_color)
                cutImage.putpixel((w - 3, h), line_color)
                cutImage.putpixel((w, h), line_color)

            if cutImage.getpixel((w - 1, h)) == (0, 0, 0, 0):
                cutImage.putpixel((w + 1, h), line_color)
                cutImage.putpixel((w + 2, h), line_color)
                cutImage.putpixel((w + 3, h), line_color)
                cutImage.putpixel((w, h), line_color)

            if cutImage.getpixel((w, h + 1)) == (0, 0, 0, 0):
                cutImage.putpixel((w, h - 1), line_color)
                cutImage.putpixel((w, h - 2), line_color)
                cutImage.putpixel((w, h - 3), line_color)
                cutImage.putpixel((w, h), line_color)

            if cutImage.getpixel((w, h - 1)) == (0, 0, 0, 0):
                cutImage.putpixel((w, h + 1), line_color)
                cutImage.putpixel((w, h + 2), line_color)
                cutImage.putpixel((w, h + 3), line_color)
                cutImage.putpixel((w, h), line_color)

cutImage.save(floder + block, "PNG")
end = time.time()
cost = end - start
print(cost)
resultDic = {}
resultDic['compound'] = os.path.join(floder, compoundImgName)
resultDic['block'] = os.path.join(floder, block)
# resultDic['centerPoint'] = (leftPointx + sideLength, leftPointy + sideLength)
resultDic['offset'] = (leftPointx + sideLength)/2
print(json.dumps(resultDic))

changePicRatio(resultDic['compound'], (320, 160))
changePicRatio(resultDic['block'], (51, 160))

deleteBlack(resultDic['block'])

# os.remove(os.path.join(floder, compoundwithoutLineImg))
# os.remove(os.path.join(floder, maskImg))
# os.remove(os.path.join(floder, blockTemp1))
# os.remove(os.path.join(floder, blockTemp2))
