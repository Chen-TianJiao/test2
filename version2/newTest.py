import numpy as np
import cv2
import random
from PIL import Image
import scipy.misc
import pandas as pd
import matplotlib.pyplot as plt

# 创建一个图像
# img = np.zeros((2160, 3840, 3), np.uint8)
img = cv2.imread("G:/pythondealPic/originalPic1.png")
color_red = (47, 79, 79)
color_black = (0,0,0)
zeros = np.zeros((img.shape), dtype = np.uint8)

# 绘制一个红色填充的矩形
cv2.rectangle(zeros, (300, 400), (600, 700), (47, 79, 79), -1)
left = random.randint(0, 1)
right = random.randint(0, 2)
high = random.randint(0, 2)
low = random.randint(0, 2)
count = 0
zeros_mask1=""
zeros_mask2=""
zeros_mask3=""
zeros_mask4=""

# # 显示
# alpha 为第一张图片的透明度
alpha = 1
# beta 为第二张图片的透明度
beta = 1
gamma = 0
# # cv2.addWeighted 将原始图片与 mask 融合
# mask_img = cv.addWeighted(img, alpha, zeros_mask, beta, gamma)
mask_img = "";

# circleCenter = [(300, 550), (600, 550), (450, 400), (450, 700)]
# color = [(47, 79, 79), (0, 0, 0)]
# for i in range(0, 4):
#     randomNum = random.randint(0, 2)
#     if randomNum != 2:
#         count += 1
#         zero_mask_single = cv2.circle(zeros, circleCenter[i], 75, color[randomNum], -1)
#         zeros_mask += np.array(zero_mask_single)
#
#
circleList = []

if left == 0:
    zeros_mask1 = cv2.circle(zeros, (300, 550), 75, color_red, -1)
    circleList.append(0)
elif left == 1:
    zeros_mask1 = cv2.circle(zeros, (300, 550), 75, color_black, -1)
    circleList.append(1)
else:
    circleList.append(2)

if right == 0:
    zeros_mask2 = cv2.circle(zeros, (600, 550), 75, color_red, -1)
    circleList.append(0)
elif right == 1:
    zeros_mask2 = cv2.circle(zeros, (600, 550), 75, color_black, -1)
    circleList.append(1)
else:
    circleList.append(2)

if high == 0:
    zeros_mask3 = cv2.circle(zeros, (450, 400), 75, color_red, -1)
    circleList.append(0)
elif high == 1:
    zeros_mask3 = cv2.circle(zeros, (450, 400), 75, color_black, -1)
    circleList.append(1)
else:
    circleList.append(2)

if low == 0:
    zeros_mask4 = cv2.circle(zeros, (450, 700), 75, color_red, -1)
    circleList.append(0)
elif low == 1:
    zeros_mask4 = cv2.circle(zeros, (450, 700), 75, color_black, -1)
    circleList.append(1)
else:
    circleList.append(2)

zeros_mask = np.array(zeros_mask1)

# 划线
# cv2.rectangle(zeros_mask, (bbox[0] + border_width, bbox[1] + border_width),
#                   (bbox[2] - border_width, bbox[3] - border_width), (169, 169, 169), border_width)
mask_img = cv2.addWeighted(img, alpha, zeros_mask, beta, gamma)

cv2.imwrite("G:/pythondealPic/testas.png", mask_img)
cv2.imwrite("G:/pythondealPic/mask.png", zeros_mask)

imgmaskkk = Image.open("G:/pythondealPic/mask.png")
imgmaskkk = imgmaskkk.convert("RGBA")
datas = imgmaskkk.getdata()
newData = list()
for item in datas:
    if item[0] == 0 and item[1] == 0 and item[2] == 0:
        newData.append((0, 0, 0, 0))
    else:
        newData.append(item)

imgmaskkk.putdata(newData)
imgmaskkk.save("G:/pythondealPic/newmask.png", "PNG")

# imgx = Image.open('G:/pythondealPic/originalPic1.png').convert('RGBA')
# maskx = Image.open('G:/pythondealPic/newmask.png').convert('RGBA')
# #生成掩膜图
# label = Image.blend(imgx, maskx, 0.5)
# label.save('G:/pythondealPic/3_predicted.png')
mask = cv2.imread("G:/pythondealPic/newmask.png", cv2.IMREAD_GRAYSCALE) # 将彩色mask以二值图像形式读取
masked = cv2.add(img, np.zeros(np.shape(img), dtype = np.uint8), mask = mask) #将image的相素值和mask像素值相加得到结果
cv2.imwrite("G:/pythondealPic/cut.png", masked)

imgCut = cv2.imread("G:/pythondealPic/cut.png")
cropped = imgCut[325:775, 225:675]  # 裁剪坐标为[y0:y1, x0:x1]
cv2.imwrite("G:/pythondealPic/cut.png", cropped)
# imgCut = cv2.imread("G:/pythondealPic/cut.png")

tt = Image.open("G:/pythondealPic/cut.png")
tt_array = tt.load()
width = tt.size[0]  # 获取宽度
height = tt.size[1]  # 获取长度

def circlexy(x, y, r, heartx, hearty):
    if pow((heartx - x), 2) + pow((hearty - y), 2) <= pow((r), 2):
        return True;
    else:
        return False;

print(circleList)
for x in range(width):
    for y in range(height):
        if (x <= 150 or x >= 300) and y < 75:
            tt.putpixel((x, y), (255, 255, 255, 0))
        if y >= 75 and y <= 150 and (x <= 75 or x >= 375):
            tt.putpixel((x, y), (255, 255, 255, 0))
        if y >= 300 and y <= 375 and (x <= 75 or x >= 375):
            tt.putpixel((x, y), (255, 255, 255, 0))
        if y >= 375 and (x <= 150 or x >= 300):
            tt.putpixel((x, y), (255, 255, 255, 0))
        if x >= 150 and x <= 300 and y < 75:
            if circlexy(x, y, 75, 225, 75) == False:
                tt.putpixel((x, y), (255, 255, 255, 0))
        if x >= 150 and x <= 300 and y > 375:
            if circlexy(x, y, 75, 225, 375) == False:
                tt.putpixel((x, y), (255, 255, 255, 0))
        if y >= 150 and y <= 300 and x < 75:
            if circlexy(x, y, 75, 75, 225) == False:
                tt.putpixel((x, y), (255, 255, 255, 0))
        if y >= 150 and y <= 300 and x > 375:
            if circlexy(x, y, 75, 375, 225) == False:
                tt.putpixel((x, y), (255, 255, 255, 0))

        if circleList[0] == 1:
            if y >= 150 and y <= 300 and x <= 150:
                if circlexy(x, y, 75, 75, 225):
                    tt.putpixel((x, y), (255, 255, 255, 0))
        if circleList[1] == 1:
            if y >= 150 and y <= 300 and x >= 300:
                if circlexy(x, y, 75, 375, 225):
                    tt.putpixel((x, y), (255, 255, 255, 0))
        if circleList[2] == 1:
            if x >= 150 and x <= 300 and y <=150:
                if circlexy(x, y, 75, 225, 75):
                    tt.putpixel((x, y), (255, 255, 255, 0))
        if circleList[3] == 1:
            if x >= 150 and x <= 300 and y >=300:
                if circlexy(x, y, 75, 225, 375):
                    tt.putpixel((x, y), (255, 255, 255, 0))

        if circleList[0] == 2:
            if y >= 150 and y <= 300 and x <= 75:
                if circlexy(x, y, 75, 75, 225):
                    tt.putpixel((x, y), (255, 255, 255, 0))
        if circleList[1] == 2:
            if y >= 150 and y <= 300 and x >= 375:
                if circlexy(x, y, 75, 375, 225):
                    tt.putpixel((x, y), (255, 255, 255, 0))
        if circleList[2] == 2:
            if x >= 150 and x <= 300 and y <=75:
                if circlexy(x, y, 75, 225, 75):
                    tt.putpixel((x, y), (255, 255, 255, 0))
        if circleList[3] == 2:
            if x >= 150 and x <= 300 and y >=375:
                if circlexy(x, y, 75, 225, 375):
                    tt.putpixel((x, y), (255, 255, 255, 0))


tt = tt.convert('RGB')
tt.save("G:/pythondealPic/cutnew.png")
# x = 0;
# y = 0;
# for x in range(0, 75):
#     if y <= 150 or y > 300:



# imgmask = Image.open('G:/pythondealPic/cut.jpg')
# e, g = imgmask.size
# img1 = imgmask.convert('L')
# img1 = np.array(img1, dtype='float32')
# arr = 255 - img1
# arr1 = arr.sum(axis=0)  # 每一列求和
# arr2 = arr.sum(axis=1)  # 每一行求和
# df = pd.DataFrame(arr)  # 把像素点转化为dataframe
# df.insert(len(df.columns), len(df.columns), arr2)  # 最后一列插入每一行的和
# df1 = pd.concat([df, (pd.DataFrame(df.sum()).T)])  # 最后一行插入每一列的和
# df2 = df1[df1[e] > 0]  # 根据最后一列把大于0的行筛选出来
#
# # 根据最后一行，把等于0的列删除掉
# for c in df2.columns:
#     if df2[c].sum() == 0:
#         df2.drop(columns=[c], inplace=True)
#
# df2.drop(columns=[e], inplace=True)  # 删除最后一列
# df3 = df2.head((df2.shape[0]) - 1)  # 删除最后一行
# a = 255 - df3
# scipy.misc.toimage(df3.values).save('G:/pythondealPic/touming.jpg')  # 保存图像

cv2.imshow('Rectangle', img)

cv2.waitKey(20000)
